#include "LiveBackdrop.h"
#include "wire.h"
#include <android/hardware_buffer.h>
#include <EGL/egl.h>
#include <EGL/eglext.h>
#include <GLES3/gl3.h>
#include <GLES2/gl2ext.h>
#include <algorithm>
#include <atomic>
#include <cmath>
#include <csignal>
#include <cstdio>
#include <cstring>
#include <mutex>
#include <spawn.h>
#include <sys/socket.h>
#include <sys/wait.h>
#include <thread>
#include <unistd.h>
#include <vector>
extern char** environ;

namespace livebg {
namespace {
struct Buffer {
    AHardwareBuffer* hardware=nullptr;
    Reply meta{};
    ~Buffer(){if(hardware)AHardwareBuffer_release(hardware);}
};
Config Normalize(Config c) {
    c.maxFps=std::max(1,std::min(c.maxFps,30));
    c.scale=std::isfinite(c.scale)?std::max(.25f,std::min(c.scale,1.f)):.5f;
    return c;
}
void Reap(pid_t pid) {
    if(pid<=0)return;
    kill(pid,SIGTERM);
    for(int i=0;i<30;i++){
        int status=0;const pid_t r=waitpid(pid,&status,WNOHANG);
        if(r==pid || (r<0 && errno==ECHILD))return;
        usleep(10000);
    }
    kill(pid,SIGKILL);
    while(waitpid(pid,nullptr,0)<0 && errno==EINTR){}
}
}
struct Session::Impl {
    mutable std::mutex mutex;
    Config config;
    uint32_t generation=1;
    Status status;
    std::shared_ptr<Buffer> latest;
    std::shared_ptr<Buffer> imported;
    std::atomic<bool> stop{true};
    std::thread worker;
    int socket=-1;
    pid_t child=-1;
    GLuint texture=0;
    EGLImageKHR image=EGL_NO_IMAGE_KHR;
    EGLDisplay display=EGL_NO_DISPLAY;
    PFNEGLGETNATIVECLIENTBUFFERANDROIDPROC getClient=nullptr;
    PFNEGLCREATEIMAGEKHRPROC createImage=nullptr;
    PFNEGLDESTROYIMAGEKHRPROC destroyImage=nullptr;
    PFNGLEGLIMAGETARGETTEXTURE2DOESPROC bindImage=nullptr;

    void Error(const std::string& text) {
        std::lock_guard<std::mutex> lock(mutex);status.error=text;
    }
    void ReleaseImage() {
        if(eglGetCurrentContext()!=EGL_NO_CONTEXT) {
            if(texture)glDeleteTextures(1,&texture);
            if(image!=EGL_NO_IMAGE_KHR && destroyImage && display!=EGL_NO_DISPLAY)
                destroyImage(display,image);
        }
        // With an already-lost context the platform owns GL object teardown.
        texture=0;image=EGL_NO_IMAGE_KHR;imported.reset();
    }
    void Run() {
        uint64_t lastReady=0;
        while(!stop.load()) {
            const uint64_t start=NowNs();
            Config c;Request q;
            {
                std::lock_guard<std::mutex> lock(mutex);
                c=config;q.generation=generation;
            }
            q.width=c.width;q.height=c.height;q.rotation=c.rotation;
            q.outputWidth=std::max(1,int(std::lround(c.width*c.scale)));
            q.outputHeight=std::max(1,int(std::lround(c.height*c.scale)));
            if(!Valid(q)){Error("Invalid display size/rotation");break;}
            Reply r;
            if(!SendAll(socket,&q,sizeof(q)) || !ReceiveAll(socket,&r,sizeof(r))) {
                if(!stop.load())Error("Capture helper disconnected/timed out; inspect terminal or logcat");
                break;
            }
            if(r.magic!=Magic || r.version!=Protocol || r.generation!=q.generation ||
                r.width!=q.width || r.height!=q.height || r.rotation!=q.rotation) {
                Error("Capture protocol or display-generation mismatch");break;
            }
            r.message[sizeof(r.message)-1]=0;
            if(r.status){Error(r.message[0]?r.message:"Capture rejected by helper");break;}
            if(r.bufferWidth!=q.outputWidth || r.bufferHeight!=q.outputHeight){
                Error("Unexpected capture resolution");break;
            }
            auto frame=std::make_shared<Buffer>();frame->meta=r;
            if(AHardwareBuffer_recvHandleFromUnixSocket(socket,&frame->hardware)!=0 || !frame->hardware) {
                Error("AHardwareBuffer receive failed");break;
            }
            AHardwareBuffer_Desc desc{};AHardwareBuffer_describe(frame->hardware,&desc);
            if(desc.width!=uint32_t(r.bufferWidth) || desc.height!=uint32_t(r.bufferHeight) ||
                desc.format!=AHARDWAREBUFFER_FORMAT_R8G8B8A8_UNORM || desc.layers!=1 ||
                (desc.usage&AHARDWAREBUFFER_USAGE_PROTECTED_CONTENT)) {
                Error("Refusing invalid/protected capture buffer");break;
            }
            {
                std::lock_guard<std::mutex> lock(mutex);
                if(generation==q.generation) {
                    latest=std::move(frame);++status.received;
                    if(lastReady && r.readyNs>lastReady) {
                        const double fps=1e9/double(r.readyNs-lastReady);
                        status.captureFps=status.captureFps==0?fps:(status.captureFps*.8+fps*.2);
                    }
                    lastReady=r.readyNs;
                }
            }
            const uint64_t deadline=start+1000000000ull/unsigned(c.maxFps);
            while(!stop.load() && NowNs()<deadline)usleep(2000);
        }
        std::lock_guard<std::mutex> lock(mutex);status.workerRunning=false;latest.reset();
    }
};
Session::Session():impl_(new Impl){}
Session::~Session(){Stop();}
void Session::Configure(const Config& input) {
    auto& s=*impl_;const Config c=Normalize(input);
    std::lock_guard<std::mutex> lock(s.mutex);
    if(c.width!=s.config.width || c.height!=s.config.height || c.rotation!=s.config.rotation || c.scale!=s.config.scale) {
        ++s.generation;s.latest.reset();
    }
    s.config=c;
}
bool Session::Start(const std::string& runtime,const Config& config,bool excluded) {
    Stop();auto& s=*impl_;Configure(config);
    {std::lock_guard<std::mutex> lock(s.mutex);s.status={};}
    if(!excluded){s.Error("Own Surface exclusion is not configured; capture not started");return false;}
    if(getuid()!=0 || geteuid()!=0){s.Error("Existing root UID required; no permission escalation is attempted");return false;}
    if(eglGetCurrentContext()==EGL_NO_CONTEXT){s.Error("No current EGL context");return false;}
    s.getClient=reinterpret_cast<PFNEGLGETNATIVECLIENTBUFFERANDROIDPROC>(eglGetProcAddress("eglGetNativeClientBufferANDROID"));
    s.createImage=reinterpret_cast<PFNEGLCREATEIMAGEKHRPROC>(eglGetProcAddress("eglCreateImageKHR"));
    s.destroyImage=reinterpret_cast<PFNEGLDESTROYIMAGEKHRPROC>(eglGetProcAddress("eglDestroyImageKHR"));
    s.bindImage=reinterpret_cast<PFNGLEGLIMAGETARGETTEXTURE2DOESPROC>(eglGetProcAddress("glEGLImageTargetTexture2DOES"));
    if(!s.getClient || !s.createImage || !s.destroyImage || !s.bindImage){s.Error("EGL native-buffer/image extension unavailable");return false;}
    const std::string jar=runtime+"/capture-helper.jar",so=runtime+"/liblivebg_jni.so";
    const char* app=access("/system/bin/app_process64",X_OK)==0?"/system/bin/app_process64":"/system/bin/app_process";
    if(access(jar.c_str(),R_OK) || access(so.c_str(),R_OK) || access(app,X_OK)) {
        s.Error("Missing runtime/capture-helper.jar or liblivebg_jni.so next to executable");return false;
    }
    int pair[2];
    if(socketpair(AF_UNIX,SOCK_STREAM|SOCK_CLOEXEC,0,pair)!=0){s.Error("socketpair failed");return false;}
    timeval timeout{6,0};
    for(int fd:pair){setsockopt(fd,SOL_SOCKET,SO_RCVTIMEO,&timeout,sizeof(timeout));setsockopt(fd,SOL_SOCKET,SO_SNDTIMEO,&timeout,sizeof(timeout));}
    int inherited=198;while(inherited==pair[0] || inherited==pair[1])++inherited;
    const std::string fdText=std::to_string(inherited),parent=std::to_string(getpid());
    std::vector<std::string> env;
    for(char** e=environ;*e;++e){
        if(!std::strncmp(*e,"CLASSPATH=",10) || !std::strncmp(*e,"LD_PRELOAD=",11) || !std::strncmp(*e,"LD_LIBRARY_PATH=",16))continue;
        env.emplace_back(*e);
    }
    env.emplace_back("CLASSPATH="+jar);
    std::vector<char*> envp;for(auto& e:env)envp.push_back(e.data());envp.push_back(nullptr);
    char* argv[]={const_cast<char*>(app),const_cast<char*>("/system/bin"),
        const_cast<char*>("--nice-name=surface-glass-capture"),
        const_cast<char*>("io.github.surfaceglass.CaptureMain"),const_cast<char*>(fdText.c_str()),
        const_cast<char*>(so.c_str()),const_cast<char*>(parent.c_str()),nullptr};
    posix_spawn_file_actions_t actions;
    int err=posix_spawn_file_actions_init(&actions);
    if(err){close(pair[0]);close(pair[1]);s.Error("spawn actions initialization failed");return false;}
    err=posix_spawn_file_actions_adddup2(&actions,pair[1],inherited);
    if(!err)err=posix_spawn_file_actions_addclose(&actions,pair[0]);
    if(!err)err=posix_spawn_file_actions_addclose(&actions,pair[1]);
    pid_t child=-1;
    if(!err)err=posix_spawn(&child,app,&actions,nullptr,argv,envp.data());
    posix_spawn_file_actions_destroy(&actions);close(pair[1]);
    if(err){close(pair[0]);s.Error(std::string("app_process spawn failed: ")+std::strerror(err));return false;}
    s.socket=pair[0];s.child=child;s.stop.store(false);s.display=eglGetCurrentDisplay();
    {std::lock_guard<std::mutex> lock(s.mutex);s.status.workerRunning=true;}
    try{s.worker=std::thread([&s]{s.Run();});}
    catch(const std::exception& e){s.Error(e.what());Stop();return false;}
    return true;
}
Status Session::GetStatus() const {
    const auto& s=*impl_;std::lock_guard<std::mutex> lock(s.mutex);return s.status;
}
bool Session::Poll(TextureFrame& result) {
    result={};auto& s=*impl_;
    std::shared_ptr<Buffer> frame;uint32_t generation;
    {
        std::lock_guard<std::mutex> lock(s.mutex);
        if(!s.status.workerRunning || !s.status.error.empty())return false;
        frame=s.latest;generation=s.generation;
    }
    if(!frame || frame->meta.generation!=generation)return false;
    const uint64_t now=NowNs();
    if(now<frame->meta.readyNs || now-frame->meta.readyNs>750000000ull)return false;
    if(frame!=s.imported) {
        if(eglGetCurrentDisplay()!=s.display || eglGetCurrentContext()==EGL_NO_CONTEXT) {
            s.Error("EGL context/display changed; stop and restart capture");return false;
        }
        GLint maxSize=0;glGetIntegerv(GL_MAX_TEXTURE_SIZE,&maxSize);
        if(frame->meta.bufferWidth>maxSize || frame->meta.bufferHeight>maxSize){s.Error("Capture exceeds GL texture limit");return false;}
        const EGLClientBuffer client=s.getClient(frame->hardware);
        const EGLint attrs[]={EGL_IMAGE_PRESERVED_KHR,EGL_TRUE,EGL_NONE};
        const EGLImageKHR image=s.createImage(s.display,EGL_NO_CONTEXT,EGL_NATIVE_BUFFER_ANDROID,client,attrs);
        if(image==EGL_NO_IMAGE_KHR){s.Error("eglCreateImageKHR rejected screenshot HardwareBuffer");return false;}
        GLint active=0,binding=0,sampler=0;
        glGetIntegerv(GL_ACTIVE_TEXTURE,&active);glActiveTexture(GL_TEXTURE0);
        glGetIntegerv(GL_TEXTURE_BINDING_2D,&binding);glGetIntegerv(GL_SAMPLER_BINDING,&sampler);
        GLuint texture=0;glGenTextures(1,&texture);glBindTexture(GL_TEXTURE_2D,texture);glBindSampler(0,0);
        glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR);glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR);
        glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_S,GL_CLAMP_TO_EDGE);glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_T,GL_CLAMP_TO_EDGE);
        // No glTexImage2D / CPU readback: attach the RGBA capture storage directly.
        s.bindImage(GL_TEXTURE_2D,image);
        const GLenum error=glGetError();
        glBindTexture(GL_TEXTURE_2D,GLuint(binding));glBindSampler(0,GLuint(sampler));glActiveTexture(GLenum(active));
        if(error!=GL_NO_ERROR){glDeleteTextures(1,&texture);s.destroyImage(s.display,image);s.Error("GL_TEXTURE_2D EGLImage import failed (or pre-existing GL error)");return false;}
        s.ReleaseImage();s.image=image;s.texture=texture;s.imported=frame;
    }
    result.texture=s.texture;result.textureWidth=frame->meta.bufferWidth;result.textureHeight=frame->meta.bufferHeight;
    result.displayWidth=frame->meta.width;result.displayHeight=frame->meta.height;result.rotation=frame->meta.rotation;
    result.readyNs=frame->meta.readyNs;result.hdr=(frame->meta.flags&1)!=0;
    return result.texture!=0;
}
void Session::Stop() {
    auto& s=*impl_;s.stop.store(true);
    if(s.socket>=0)shutdown(s.socket,SHUT_RDWR);
    if(s.worker.joinable())s.worker.join();
    if(s.socket>=0){close(s.socket);s.socket=-1;}
    Reap(s.child);s.child=-1;
    {std::lock_guard<std::mutex> lock(s.mutex);s.latest.reset();s.status.workerRunning=false;}
    s.ReleaseImage();s.display=EGL_NO_DISPLAY;
}
}
