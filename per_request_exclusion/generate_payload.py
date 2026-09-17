#!/usr/bin/env python3
from pathlib import Path
import re, shutil
ROOT=Path(__file__).resolve().parent
BASE=ROOT.parent/'real_screen_backdrop/payload'
OUT=ROOT/'payload'

def once(text,old,new):
    if text.count(old)!=1:raise RuntimeError('Unexpected source anchor: '+old[:110])
    return text.replace(old,new,1)

protocol=(BASE/'jni/real_backdrop/Protocol.h').read_text()
protocol=once(protocol,'constexpr uint32_t Version = 1;','constexpr uint32_t Version = 2;')
protocol=once(protocol,'char message[192]{};','char message[192]{};\n    uint64_t exclusionGeneration=0;\n    uint32_t excludedCount=0, reserved=0;')
protocol=once(protocol,'static_assert(sizeof(Response)==240);','static_assert(sizeof(Response)==256);')
protocol=once(protocol,'return r.width>0 && r.height>0',
              'return r.exclusionGeneration>0 && r.excludedCount>0 && r.excludedCount<=64 && r.width>0 && r.height>0')
(OUT/'jni/real_backdrop/Protocol.h').write_text(protocol)

bridge=(BASE/'capture/native_bridge.cpp').read_text()
a=bridge.index('    // This helper does not elevate privileges')
b=bridge.index('    return JNI_TRUE;',a)
bridge=bridge[:a]+'''    // Both ends now belong to this process. No external sender may inject handles.
    if(fd<0 || getuid()!=0 || geteuid()!=0) return JNI_FALSE;
    ucred peer{}; socklen_t size=sizeof(peer);
    if(getsockopt(fd,SOL_SOCKET,SO_PEERCRED,&peer,&size) || peer.uid!=0 || peer.pid!=getpid()) return JNI_FALSE;
'''+bridge[b:]
bridge=once(bridge,'jint rotation, jint colorSpace) {',
                   'jint rotation, jint colorSpace, jlong generation, jint excluded) {')
bridge=once(bridge,'response.timestampNs=NowNs();\n    if(desc.format',
'''response.timestampNs=NowNs();
    response.exclusionGeneration=static_cast<uint64_t>(generation);
    response.excludedCount=static_cast<uint32_t>(excluded);
    if(desc.format''')
bridge+='''
extern "C" JNIEXPORT void JNICALL
Java_com_ytbl_capture_Main_nativeClose(JNIEnv*,jclass,jint fd){if(fd>=0)close(fd);}
'''
(OUT/'jni/real_backdrop/native_bridge.cpp').write_text(bridge)

text=(BASE/'capture/Main.java').read_text()
text=once(text,'int rotation, int colorSpace);','int rotation, int colorSpace, long generation, int excluded);')
text=once(text,'    private Main() {}','''    private static native void nativeClose(int fd);
    private static LayerRegistry registry;
    private static Thread captureThread;
    private Main() {}
    private static synchronized LayerRegistry registry() throws Exception {
        if(registry==null)registry=new LayerRegistry(Class.forName("android.view.SurfaceControl"));
        return registry;
    }
    public static long registerSurface(long window,long nativeObject,int width,int height) throws Exception {
        return registry().register(window,nativeObject,width,height);
    }
    public static long unregisterSurface(long window) throws Exception { return registry().unregister(window); }
    public static int excludedCount() throws Exception { return registry().count(); }
    public static void clearSurfaces() { synchronized(Main.class){if(registry!=null)registry.clear();} }
    public static synchronized boolean startCapture(final int fd) {
        if(captureThread!=null && captureThread.isAlive())return false;
        Thread worker=new Thread(new Runnable(){public void run(){runCapture(fd);}},"ytbl-request-capture");
        worker.setDaemon(true);
        try {worker.start();captureThread=worker;return true;}
        catch(Throwable error){System.err.println("[YtblExclude] Cannot start capture thread: "+error);return false;}
    }''')
text=once(text,'Object frame(Info info,int maxEdge) throws Exception {',
              'Object frame(Info info,int maxEdge,Object excludedLayers) throws Exception {')
text=once(text,'            Object args=get(b,"build");',
'''            if(excludedLayers==null || java.lang.reflect.Array.getLength(excludedLayers)==0)
                throw new IllegalStateException("Empty exclusions: unfiltered capture is disabled");
            call(b,"setExcludeLayers",new Class<?>[]{excludedLayers.getClass()},excludedLayers);
            Object args=get(b,"build");''')
text=once(text,'Object result=get(listener,"getBuffer");',
'''Object result=Class.forName("android.window.ScreenCapture$SynchronousScreenCaptureListener")
                    .getMethod("getBuffer").invoke(listener);''')
a=text.index('    public static void main(String[] args) {')
text=text[:a]+'''    private static void runCapture(int fd) {
        try {
            if(!nativeInit(fd))throw new SecurityException("Same-process owner-root socketpair required");
            Capture capture=null;
            System.err.println("[YtblCapture] Per-request exclusions active; global screenshot flags OFF.");
            for(;;) {
                int[] request=nativeNext(fd);
                if(request==null)break;
                Object hardware=null,result=null;
                LayerRegistry.Snapshot exclusion=null;
                try {
                    exclusion=registry().snapshot();
                    if(capture==null)capture=new Capture();
                    Info before=capture.info();
                    result=capture.frame(before,request[1],exclusion.array);
                    hardware=get(result,"getHardwareBuffer");
                    if(Boolean.TRUE.equals(get(result,"containsSecureLayers")))
                        throw new SecurityException("Refusing a buffer containing secure layers");
                    if(Boolean.TRUE.equals(get(result,"containsHdrLayers")))
                        throw new UnsupportedOperationException("HDR capture is not supported by this SDR pipeline");
                    Object color=get(result,"getColorSpace");
                    int colorId=color==null?0:(Integer)get(color,"getId");
                    if(colorId!=0 && colorId!=7)throw new UnsupportedOperationException("Unsupported colorspace id="+colorId);
                    Info after=capture.info();
                    if(!before.same(after) || !exclusion.current()){
                        if(!nativeError(fd,request[0],2,"Display or exclusion generation changed; frame discarded"))break;
                        continue;
                    }
                    if(!nativeFrame(fd,request[0],hardware,before.width,before.height,before.rotation,colorId,
                                    exclusion.generation,exclusion.count))break;
                }catch(Throwable error){
                    String message=cause(error);System.err.println("[YtblCapture] "+message);
                    if(!nativeError(fd,request[0],-1,message))break;
                }finally{
                    closeBuffer(hardware);
                    if(result!=null)try {closeBuffer(get(result,"getGainmap"));}catch(Exception ignored){}
                    if(exclusion!=null)exclusion.close();
                }
            }
        }catch(Throwable error){System.err.println("[YtblCapture] Stopped: "+cause(error));}
        finally{nativeClose(fd);}
    }
}
'''
text=text.replace('Runs only as a child of the visible native UI.','Runs as a daemon thread INSIDE the visible native UI process.')
(OUT/'capture/Main.java').write_text(text)

cpp=(BASE/'jni/real_backdrop/NativeBackdrop.cpp').read_text()
cpp='#include "HostedCapture.h"\n'+cpp
cpp=once(cpp,'int socket=-1; pid_t child=-1;','int socket=-1;')
# Generation changes invalidate already delivered frames as well as pending ones.
cpp=once(cpp,'AHardwareBuffer_Desc desc{};AHardwareBuffer_describe(buffer,&desc);',
'''if(response.exclusionGeneration!=hosted::Generation() || hosted::ExcludedCount()<=0){
            AHardwareBuffer_release(buffer);s.live.store(false);continue;
        }
        AHardwareBuffer_Desc desc{};AHardwareBuffer_describe(buffer,&desc);''')
start=cpp.index('bool Start() {')
end=cpp.index('void Configure(',start)
cpp=cpp[:start]+'''bool Start() {
    if(!s.stop.load())return true;
    if(s.thread.joinable())Stop();
    if(getuid()!=0 || geteuid()!=0){Status("Owner-root launch is required");return false;}
    const int sdk=android_get_device_api_level();
    if(sdk<34 || sdk>36){Status("Per-request capture supports Android 14-16 (SDK 34-36)");return false;}
    if(!hosted::Ready() || hosted::ExcludedCount()<=0){
        Status("No valid per-request exclusion registry; unfiltered capture is disabled");return false;
    }
    int pair[2];
    if(socketpair(AF_UNIX,SOCK_STREAM|SOCK_CLOEXEC,0,pair)){Status(ErrorText("socketpair"));return false;}
    timeval timeout{6,0};setsockopt(pair[0],SOL_SOCKET,SO_RCVTIMEO,&timeout,sizeof(timeout));
    setsockopt(pair[0],SOL_SOCKET,SO_SNDTIMEO,&timeout,sizeof(timeout));
    if(!hosted::Launch(pair[1])){
        close(pair[0]);close(pair[1]);Status("Capture thread is stopping or registry setup failed; re-enable after a moment");return false;
    }
    // The Java thread owns pair[1] until its finally block. Never close/reuse it
    // here: a delayed callback must not write into a descriptor reused elsewhere.
    s.socket=pair[0];s.stop.store(false);s.live.store(false);
    Status("Starting ScreenCapture with per-request excludeLayers");
    try{s.thread=std::thread(Worker,s.socket);}
    catch(...){s.stop.store(true);shutdown(s.socket,SHUT_RDWR);close(s.socket);s.socket=-1;
        Status("Cannot create capture receiver thread");return false;}
    return true;
}
'''+cpp[end:]
cpp=once(cpp,'void UpdateTexture() {\n    if(s.stop.load())return;',
'''void UpdateTexture() {
    if(s.stop.load())return;
    if(eglGetCurrentContext()==EGL_NO_CONTEXT){Status("No current GLES context");return;}
    if(s.context!=EGL_NO_CONTEXT && s.context!=eglGetCurrentContext())DropGL(true);''')
cpp=once(cpp,'if(!pending.buffer)return;',
'''if(!pending.buffer)return;
    if(pending.meta.exclusionGeneration!=hosted::Generation() || hosted::ExcludedCount()<=0){ReleasePending(pending);return;}''')
cpp=once(cpp,'Status("LIVE: local screen / AHB / GPU copy; secure capture OFF");',
'''Status("LIVE: excludeLayers="+std::to_string(s.current.excludedCount)+
           " / generation="+std::to_string(s.current.exclusionGeneration)+" / system screenshots VISIBLE");''')
cpp=once(cpp,'if(s.stop.load() || !s.live.load() || !s.texture || !s.current.width ||',
'''if(s.stop.load() || !s.live.load() || !s.texture || !s.current.width ||
       s.current.exclusionGeneration!=hosted::Generation() || hosted::ExcludedCount()<=0 ||''')
cpp=cpp.replace('    if(s.child>0)kill(s.child,SIGTERM);\n','')
a=cpp.index('    if(s.child>0){',cpp.index('void Stop()'))
b=cpp.index('    {std::lock_guard<std::mutex> lock(s.mutex);ReleasePending(s.pending);}',a)
cpp=cpp[:a]+cpp[b:]
# Remove obsolete child runtime lookup and process-spawning includes.
a=cpp.index('std::string RuntimeDirectory() {');b=cpp.index('} // namespace',a)
cpp=cpp[:a]+cpp[b:]
for include in ['#include <spawn.h>\n','#include <sys/wait.h>\n','#include <signal.h>\n']:
    cpp=cpp.replace(include,'')
cpp=cpp.replace('extern char** environ;\n','')
(OUT/'jni/real_backdrop/NativeBackdrop.cpp').write_text(cpp)
header=(BASE/'jni/real_backdrop/NativeBackdrop.h').read_text()
header=header.replace('// Files default to <directory of executable>/capture_runtime/. Override with\n// YTBL_CAPTURE_DIR when installing somewhere else. The child is not persistent.',
                      '// Hosted app_process thread uses the registry of this same UI process.')
header=header.replace('// Render thread, BEFORE EGL context destruction. Stops/reaps the helper.',
                      '// Render thread, BEFORE EGL context destruction. Stops the receiver and capture connection.')
(OUT/'jni/real_backdrop/NativeBackdrop.h').write_text(header)
ui=(BASE/'jni/real_backdrop/SurfaceBackdropUi.h').read_text()
ui=ui.replace('Stops/reaps','Stops')
ui=ui.replace('LIVE：正在折射其他应用的可采集画面','LIVE：逐请求排除自身，正在折射后层画面')
ui=once(ui,'"悬浮窗已设置排除截图；系统截图或录屏通常也不会显示本窗口。"',
               '"系统截图/录屏保留本窗口；仅本程序每次采集通过 excludeLayers 排除自身。"')
ui=ui.replace('停止并重新连接','停止采集（重新勾选以重连）')
(OUT/'jni/real_backdrop/SurfaceBackdropUi.h').write_text(ui)
print('Generated hosted capture transport, per-request exclusions, generation-gated receiver and UI.')
