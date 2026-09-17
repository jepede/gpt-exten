#include "NativeBackdrop.h"
#include "Protocol.h"
#include <android/api-level.h>
#include <android/hardware_buffer.h>
#include <EGL/egl.h>
#include <EGL/eglext.h>
#include <GLES3/gl3.h>
#include <GLES2/gl2ext.h>
#include <algorithm>
#include <atomic>
#include <chrono>
#include <condition_variable>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <fcntl.h>
#include <limits.h>
#include <mutex>
#include <signal.h>
#include <spawn.h>
#include <string>
#include <sys/socket.h>
#include <sys/wait.h>
#include <thread>
#include <unistd.h>
#include <vector>

extern char** environ;
namespace screenbackdrop {
namespace {
struct Pending { AHardwareBuffer* buffer=nullptr; wire::Response meta{}; };
struct Imported { AHardwareBuffer* buffer=nullptr; EGLImageKHR image=EGL_NO_IMAGE_KHR; GLuint texture=0; GLsync fence=nullptr; };
struct State {
    std::mutex mutex;
    std::condition_variable wake;
    std::thread thread;
    std::atomic<bool> stop{true},live{false};
    int socket=-1; pid_t child=-1;
    int maxEdge=1280,fps=24;
    Pending pending;
    uint64_t captured=0;
    std::string status="Real screen capture is OFF";
    EGLDisplay display=EGL_NO_DISPLAY;
    EGLContext context=EGL_NO_CONTEXT;
    PFNEGLGETNATIVECLIENTBUFFERANDROIDPROC clientBuffer=nullptr;
    PFNEGLCREATEIMAGEKHRPROC createImage=nullptr;
    PFNEGLDESTROYIMAGEKHRPROC destroyImage=nullptr;
    PFNGLEGLIMAGETARGETTEXTURE2DOESPROC imageTarget=nullptr;
    GLuint program=0,vao=0,texture=0,fbo=0;
    int width=0,height=0;
    wire::Response current{};
    std::deque<Imported> retired;
} s;
void Status(const std::string& text) { std::lock_guard<std::mutex> lock(s.mutex); s.status=text; }
std::string ErrorText(const char* prefix,int code=errno) { return std::string(prefix)+": "+std::strerror(code); }
void ReleasePending(Pending& p) { if(p.buffer)AHardwareBuffer_release(p.buffer);p={}; }
void Retire(Imported& p,bool contextLost=false) {
    if(!contextLost) { if(p.fence)glDeleteSync(p.fence); if(p.texture)glDeleteTextures(1,&p.texture); }
    if(p.image!=EGL_NO_IMAGE_KHR && s.destroyImage && s.display!=EGL_NO_DISPLAY)
        s.destroyImage(s.display,p.image);
    if(p.buffer)AHardwareBuffer_release(p.buffer);
    p={};
}
void DropGL(bool lost) {
    if(!lost && (!s.retired.empty() || s.texture)) glFinish();
    for(auto& p:s.retired)Retire(p,lost); s.retired.clear();
    if(!lost) {
        if(s.texture)glDeleteTextures(1,&s.texture);
        if(s.fbo)glDeleteFramebuffers(1,&s.fbo);
        if(s.vao)glDeleteVertexArrays(1,&s.vao);
        if(s.program)glDeleteProgram(s.program);
    }
    s.texture=s.fbo=s.vao=s.program=0;s.width=s.height=0;s.current={};
    s.context=EGL_NO_CONTEXT;s.display=EGL_NO_DISPLAY;
}
// The import/copy must not leak GL state into the host ImGui renderer.
struct GLState {
    GLint program,vao,active,tex,sampler,readFbo,drawFbo,unpack,viewport[4],scissor[4];
    GLboolean blend,cull,depth,stencil,scissorOn,discard,coverage,alphaCoverage,mask[4];
    GLState() {
        glGetIntegerv(GL_CURRENT_PROGRAM,&program);glGetIntegerv(GL_VERTEX_ARRAY_BINDING,&vao);
        glGetIntegerv(GL_ACTIVE_TEXTURE,&active);glActiveTexture(GL_TEXTURE0);
        glGetIntegerv(GL_TEXTURE_BINDING_2D,&tex);glGetIntegerv(GL_SAMPLER_BINDING,&sampler);
        glGetIntegerv(GL_READ_FRAMEBUFFER_BINDING,&readFbo);glGetIntegerv(GL_DRAW_FRAMEBUFFER_BINDING,&drawFbo);
        glGetIntegerv(GL_PIXEL_UNPACK_BUFFER_BINDING,&unpack);
        glGetIntegerv(GL_VIEWPORT,viewport);glGetIntegerv(GL_SCISSOR_BOX,scissor);
        blend=glIsEnabled(GL_BLEND);cull=glIsEnabled(GL_CULL_FACE);depth=glIsEnabled(GL_DEPTH_TEST);
        stencil=glIsEnabled(GL_STENCIL_TEST);scissorOn=glIsEnabled(GL_SCISSOR_TEST);
        discard=glIsEnabled(GL_RASTERIZER_DISCARD);coverage=glIsEnabled(GL_SAMPLE_COVERAGE);
        alphaCoverage=glIsEnabled(GL_SAMPLE_ALPHA_TO_COVERAGE);glGetBooleanv(GL_COLOR_WRITEMASK,mask);
    }
    static void Set(GLenum x,GLboolean v) { if(v)glEnable(x);else glDisable(x); }
    ~GLState() {
        glUseProgram(program);glBindVertexArray(vao);glActiveTexture(GL_TEXTURE0);
        glBindTexture(GL_TEXTURE_2D,tex);glBindSampler(0,sampler);glActiveTexture(active);
        glBindBuffer(GL_PIXEL_UNPACK_BUFFER,unpack);
        glBindFramebuffer(GL_READ_FRAMEBUFFER,readFbo);glBindFramebuffer(GL_DRAW_FRAMEBUFFER,drawFbo);
        glViewport(viewport[0],viewport[1],viewport[2],viewport[3]);glScissor(scissor[0],scissor[1],scissor[2],scissor[3]);
        Set(GL_BLEND,blend);Set(GL_CULL_FACE,cull);Set(GL_DEPTH_TEST,depth);Set(GL_STENCIL_TEST,stencil);
        Set(GL_SCISSOR_TEST,scissorOn);Set(GL_RASTERIZER_DISCARD,discard);Set(GL_SAMPLE_COVERAGE,coverage);
        Set(GL_SAMPLE_ALPHA_TO_COVERAGE,alphaCoverage);glColorMask(mask[0],mask[1],mask[2],mask[3]);
    }
};
const char* vertex=R"GLSL(#version 300 es
precision highp float;
out vec2 uv;
void main(){uv=vec2(gl_VertexID==1?2.0:0.0,gl_VertexID==2?2.0:0.0);gl_Position=vec4(uv*2.0-1.0,0,1);}
)GLSL";
const char* fragment=R"GLSL(#version 300 es
precision highp float;
in vec2 uv;
out vec4 result;
uniform sampler2D image;
uniform int displayP3;
vec3 linearize(vec3 c){return mix(pow((c+0.055)/1.055,vec3(2.4)),c/12.92,lessThanEqual(c,vec3(0.04045)));}
vec3 encode(vec3 c){c=clamp(c,0.0,1.0);return mix(1.055*pow(c,vec3(1.0/2.4))-0.055,c*12.92,lessThanEqual(c,vec3(0.0031308)));}
void main(){
    vec4 c=texture(image,uv);
    if(displayP3!=0){
        vec3 rgb=linearize(clamp(c.rgb/max(c.a,0.00001),0.0,1.0));
        // D65 linear Display-P3 -> linear sRGB; out-of-gamut values are clipped.
        rgb=mat3(1.224940176,-0.042056955,-0.019637555,
                 -0.224940176,1.042056955,-0.078636046,
                 0.0,0.0,1.098273601)*rgb;
        c.rgb=encode(rgb)*c.a;
    }
    result=c;
}
)GLSL";
GLuint Shader(GLenum kind,const char* source) {
    GLuint shader=glCreateShader(kind);glShaderSource(shader,1,&source,nullptr);glCompileShader(shader);
    GLint ok=0;glGetShaderiv(shader,GL_COMPILE_STATUS,&ok);
    if(!ok){char message[2048]{};glGetShaderInfoLog(shader,sizeof(message),nullptr,message);Status(message);glDeleteShader(shader);return 0;}
    return shader;
}
bool Pipeline() {
    EGLContext context=eglGetCurrentContext();EGLDisplay display=eglGetCurrentDisplay();
    if(context==EGL_NO_CONTEXT || display==EGL_NO_DISPLAY){Status("No current GLES context");return false;}
    if(s.context!=EGL_NO_CONTEXT && s.context!=context)DropGL(true);
    s.context=context;s.display=display;
    if(s.program)return true;
    s.clientBuffer=reinterpret_cast<PFNEGLGETNATIVECLIENTBUFFERANDROIDPROC>(eglGetProcAddress("eglGetNativeClientBufferANDROID"));
    s.createImage=reinterpret_cast<PFNEGLCREATEIMAGEKHRPROC>(eglGetProcAddress("eglCreateImageKHR"));
    s.destroyImage=reinterpret_cast<PFNEGLDESTROYIMAGEKHRPROC>(eglGetProcAddress("eglDestroyImageKHR"));
    s.imageTarget=reinterpret_cast<PFNGLEGLIMAGETARGETTEXTURE2DOESPROC>(eglGetProcAddress("glEGLImageTargetTexture2DOES"));
    if(!s.clientBuffer || !s.createImage || !s.destroyImage || !s.imageTarget) {
        Status("AHardwareBuffer EGL image import is unsupported by this driver");return false;
    }
    GLuint vs=Shader(GL_VERTEX_SHADER,vertex),fs=Shader(GL_FRAGMENT_SHADER,fragment);
    if(!vs || !fs){if(vs)glDeleteShader(vs);if(fs)glDeleteShader(fs);return false;}
    s.program=glCreateProgram();glAttachShader(s.program,vs);glAttachShader(s.program,fs);glLinkProgram(s.program);
    glDeleteShader(vs);glDeleteShader(fs);
    GLint ok=0;glGetProgramiv(s.program,GL_LINK_STATUS,&ok);
    if(!ok){char message[2048]{};glGetProgramInfoLog(s.program,sizeof(message),nullptr,message);Status(message);
        glDeleteProgram(s.program);s.program=0;return false;}
    glGenVertexArrays(1,&s.vao);glGenTextures(1,&s.texture);glGenFramebuffers(1,&s.fbo);
    glBindTexture(GL_TEXTURE_2D,s.texture);
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR);glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_S,GL_CLAMP_TO_EDGE);glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_T,GL_CLAMP_TO_EDGE);
    return true;
}
void Worker(int socket) {
    uint32_t sequence=0;
    while(!s.stop.load()) {
        auto start=std::chrono::steady_clock::now();
        wire::Request request;request.sequence=++sequence;
        int fps;
        {std::lock_guard<std::mutex> lock(s.mutex);request.maxEdge=static_cast<uint32_t>(s.maxEdge);fps=s.fps;}
        wire::Response response;
        if(!wire::Write(socket,&request,sizeof(request)) || !wire::Read(socket,&response,sizeof(response))) {
            if(!s.stop.load())Status(ErrorText("Capture helper disconnected / timed out"));break;
        }
        if(!wire::Valid(response,sequence)){Status("Invalid capture protocol header");break;}
        if(response.status) {
            response.message[sizeof(response.message)-1]=0;s.live.store(false);Status(response.message);
            std::unique_lock<std::mutex> lock(s.mutex);
            s.wake.wait_for(lock,std::chrono::milliseconds(response.status==2?30:1000),[]{return s.stop.load();});
            continue;
        }
        AHardwareBuffer* buffer=nullptr;
        int error=AHardwareBuffer_recvHandleFromUnixSocket(socket,&buffer);
        if(error || !buffer){Status("Failed to receive AHardwareBuffer: "+std::to_string(error));break;}
        AHardwareBuffer_Desc desc{};AHardwareBuffer_describe(buffer,&desc);
        if(desc.width!=response.width || desc.height!=response.height || desc.layers!=1 ||
           desc.format!=AHARDWAREBUFFER_FORMAT_R8G8B8A8_UNORM ||
           !(desc.usage & AHARDWAREBUFFER_USAGE_GPU_SAMPLED_IMAGE) ||
           (desc.usage & AHARDWAREBUFFER_USAGE_PROTECTED_CONTENT)) {
            AHardwareBuffer_release(buffer);Status("Unsupported or protected capture buffer refused");break;
        }
        {std::lock_guard<std::mutex> lock(s.mutex);ReleasePending(s.pending);s.pending.buffer=buffer;s.pending.meta=response;++s.captured;}
        s.live.store(true);
        std::unique_lock<std::mutex> lock(s.mutex);
        s.wake.wait_until(lock,start+std::chrono::microseconds(1000000/fps),[]{return s.stop.load();});
    }
    s.live.store(false);
}
std::string RuntimeDirectory() {
    if(const char* env=std::getenv("YTBL_CAPTURE_DIR")) if(*env)return env;
    char path[PATH_MAX];ssize_t size=readlink("/proc/self/exe",path,sizeof(path)-1);
    if(size<=0)return {};
    path[size]=0;std::string p=path;auto slash=p.rfind('/');
    return slash==std::string::npos ? std::string() : p.substr(0,slash)+"/capture_runtime";
}
} // namespace

bool Start() {
    if(!s.stop.load())return true;
    if(s.thread.joinable())Stop();
    if(getuid()!=0 || geteuid()!=0){Status("Run the owner UI with root; this module does not elevate privileges");return false;}
    const int sdk=android_get_device_api_level();
    if(sdk<34 || sdk>36){Status("Capture helper supports Android 14-16 (SDK 34-36)");return false;}
    std::string dir=RuntimeDirectory();
    std::string dex=dir+"/capture.dex.jar",library=dir+"/libglass_capture.so";
    if(dir.empty() || access(dex.c_str(),R_OK) || access(library.c_str(),R_OK)) {
        Status("Missing capture_runtime/capture.dex.jar or libglass_capture.so next to executable");return false;
    }
    int pair[2];
    if(socketpair(AF_UNIX,SOCK_STREAM|SOCK_CLOEXEC,0,pair)){Status(ErrorText("socketpair"));return false;}
    timeval timeout{6,0};setsockopt(pair[0],SOL_SOCKET,SO_RCVTIMEO,&timeout,sizeof(timeout));
    setsockopt(pair[0],SOL_SOCKET,SO_SNDTIMEO,&timeout,sizeof(timeout));
    posix_spawn_file_actions_t actions;posix_spawn_file_actions_init(&actions);
    posix_spawn_file_actions_addclose(&actions,pair[0]);
    posix_spawn_file_actions_adddup2(&actions,pair[1],3);
    if(pair[1]!=3)posix_spawn_file_actions_addclose(&actions,pair[1]);
    std::vector<std::string> envStrings;
    for(char** p=environ;p && *p;++p)if(std::strncmp(*p,"CLASSPATH=",10)!=0)envStrings.emplace_back(*p);
    envStrings.emplace_back("CLASSPATH="+dex);
    std::vector<char*> env;for(auto& value:envStrings)env.push_back(value.data());env.push_back(nullptr);
    const char* path="/system/bin/app_process";
    char* argv[]={const_cast<char*>(path),const_cast<char*>("/system/bin"),
                  const_cast<char*>("--nice-name=ytbl-screen-background"),
                  const_cast<char*>("com.ytbl.capture.Main"),const_cast<char*>("3"),library.data(),nullptr};
    pid_t pid=-1;int error=posix_spawn(&pid,path,&actions,nullptr,argv,env.data());
    posix_spawn_file_actions_destroy(&actions);close(pair[1]);
    if(error){close(pair[0]);Status(ErrorText("Cannot launch capture helper",error));return false;}
    s.socket=pair[0];s.child=pid;s.stop.store(false);s.live.store(false);
    Status("Starting local screen background; secure capture OFF");
    try {s.thread=std::thread(Worker,s.socket);}
    catch(...) {s.stop.store(true);shutdown(s.socket,SHUT_RDWR);close(s.socket);s.socket=-1;
        kill(s.child,SIGTERM);waitpid(s.child,nullptr,0);s.child=-1;Status("Cannot create capture receiver thread");return false;}
    return true;
}
void Configure(int edge,int fps) {
    std::lock_guard<std::mutex> lock(s.mutex);s.maxEdge=std::clamp(edge,320,2560);s.fps=std::clamp(fps,5,60);
}
void UpdateTexture() {
    if(s.stop.load())return;
    // Completed GPU copies release imported AHBs without blocking every UI frame.
    for(auto it=s.retired.begin();it!=s.retired.end();) {
        GLenum result=glClientWaitSync(it->fence,0,0);
        if(result==GL_ALREADY_SIGNALED || result==GL_CONDITION_SATISFIED){Retire(*it);it=s.retired.erase(it);}
        else if(result==GL_WAIT_FAILED){Status("Capture GPU fence failed");s.live.store(false);return;}
        else ++it;
    }
    if(s.retired.size()>=4)return; // bounded in-flight memory; producer mailbox keeps only newest frame
    Pending pending;
    {std::lock_guard<std::mutex> lock(s.mutex);pending=s.pending;s.pending={};}
    if(!pending.buffer)return;
    const uint64_t now=wire::NowNs();
    if(pending.meta.timestampNs>now || now-pending.meta.timestampNs>1200000000ull){ReleasePending(pending);return;}
    GLState saved;
    if(!Pipeline()){ReleasePending(pending);s.current={};return;}
    Imported imported;imported.buffer=pending.buffer;
    const EGLint attributes[]={EGL_IMAGE_PRESERVED_KHR,EGL_TRUE,EGL_NONE};
    imported.image=s.createImage(s.display,EGL_NO_CONTEXT,EGL_NATIVE_BUFFER_ANDROID,s.clientBuffer(imported.buffer),attributes);
    if(imported.image==EGL_NO_IMAGE_KHR){Status("eglCreateImageKHR(AHardwareBuffer) failed: "+std::to_string(eglGetError()));Retire(imported);s.current={};return;}
    glGenTextures(1,&imported.texture);glActiveTexture(GL_TEXTURE0);glBindSampler(0,0);
    glBindTexture(GL_TEXTURE_2D,imported.texture);
    s.imageTarget(GL_TEXTURE_2D,imported.image);
    GLenum importError=glGetError();
    if(importError!=GL_NO_ERROR){Status("AHardwareBuffer cannot be sampled as GL_TEXTURE_2D: "+std::to_string(importError));Retire(imported);s.current={};return;}
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR);glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_S,GL_CLAMP_TO_EDGE);glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_T,GL_CLAMP_TO_EDGE);
    glBindTexture(GL_TEXTURE_2D,s.texture);glBindBuffer(GL_PIXEL_UNPACK_BUFFER,0);
    if(s.width!=static_cast<int>(pending.meta.width) || s.height!=static_cast<int>(pending.meta.height)) {
        s.width=static_cast<int>(pending.meta.width);s.height=static_cast<int>(pending.meta.height);
        glTexImage2D(GL_TEXTURE_2D,0,GL_RGBA8,s.width,s.height,0,GL_RGBA,GL_UNSIGNED_BYTE,nullptr);
    }
    glBindFramebuffer(GL_DRAW_FRAMEBUFFER,s.fbo);
    glFramebufferTexture2D(GL_DRAW_FRAMEBUFFER,GL_COLOR_ATTACHMENT0,GL_TEXTURE_2D,s.texture,0);
    const GLenum attachment=GL_COLOR_ATTACHMENT0;glDrawBuffers(1,&attachment);
    if(glCheckFramebufferStatus(GL_DRAW_FRAMEBUFFER)!=GL_FRAMEBUFFER_COMPLETE){Status("Capture copy framebuffer incomplete");Retire(imported);s.current={};return;}
    glViewport(0,0,s.width,s.height);glDisable(GL_SCISSOR_TEST);glDisable(GL_BLEND);glDisable(GL_CULL_FACE);
    glDisable(GL_DEPTH_TEST);glDisable(GL_STENCIL_TEST);glDisable(GL_RASTERIZER_DISCARD);
    glDisable(GL_SAMPLE_COVERAGE);glDisable(GL_SAMPLE_ALPHA_TO_COVERAGE);glColorMask(GL_TRUE,GL_TRUE,GL_TRUE,GL_TRUE);
    glUseProgram(s.program);glBindVertexArray(s.vao);glBindTexture(GL_TEXTURE_2D,imported.texture);
    glUniform1i(glGetUniformLocation(s.program,"image"),0);
    glUniform1i(glGetUniformLocation(s.program,"displayP3"),pending.meta.colorSpace==7 ? 1 : 0);
    glDrawArrays(GL_TRIANGLES,0,3);
    GLenum drawError=glGetError();
    imported.fence=glFenceSync(GL_SYNC_GPU_COMMANDS_COMPLETE,0);glFlush();
    if(!imported.fence){glFinish();Retire(imported);}
    else s.retired.push_back(imported);
    if(drawError!=GL_NO_ERROR){Status("Screen background GPU copy failed: "+std::to_string(drawError));s.current={};return;}
    s.current=pending.meta;
    Status("LIVE: local screen / AHB / GPU copy; secure capture OFF");
}
Texture GetTexture() {
    Texture result;
    const uint64_t now=wire::NowNs();
    if(s.stop.load() || !s.live.load() || !s.texture || !s.current.width ||
       now<s.current.timestampNs || now-s.current.timestampNs>1200000000ull)return result;
    result.id=s.texture;result.width=s.width;result.height=s.height;
    result.screenWidth=static_cast<int>(s.current.screenWidth);result.screenHeight=static_cast<int>(s.current.screenHeight);
    result.rotation=static_cast<int>(s.current.rotation);result.sequence=s.current.sequence;
    result.ageMs=double(now-s.current.timestampNs)/1000000.0;
    return result;
}
std::string GetStatus(){std::lock_guard<std::mutex> lock(s.mutex);return s.status;}
uint64_t CapturedFrames(){std::lock_guard<std::mutex> lock(s.mutex);return s.captured;}
void Stop() {
    s.stop.store(true);s.live.store(false);s.wake.notify_all();
    if(s.socket>=0)shutdown(s.socket,SHUT_RDWR);
    if(s.child>0)kill(s.child,SIGTERM);
    if(s.thread.joinable())s.thread.join();
    if(s.socket>=0){close(s.socket);s.socket=-1;}
    if(s.child>0){
        int status=0;pid_t result=0;
        for(int i=0;i<50 && result==0;++i){result=waitpid(s.child,&status,WNOHANG);if(result==0)usleep(10000);}
        if(result==0){kill(s.child,SIGKILL);while(waitpid(s.child,&status,0)<0 && errno==EINTR){}}
        s.child=-1;
    }
    {std::lock_guard<std::mutex> lock(s.mutex);ReleasePending(s.pending);}
    const bool lost=s.context==EGL_NO_CONTEXT || s.context!=eglGetCurrentContext();
    DropGL(lost);Status("Real screen capture is OFF");
}
} // namespace screenbackdrop
