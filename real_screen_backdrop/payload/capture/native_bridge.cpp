#include "Protocol.h"
#include <android/hardware_buffer.h>
#include <android/hardware_buffer_jni.h>
#include <jni.h>
#include <sys/prctl.h>
#include <signal.h>
#include <cstdio>
#include <cstring>

using namespace screenbackdrop::wire;
extern "C" JNIEXPORT jboolean JNICALL
Java_com_ytbl_capture_Main_nativeInit(JNIEnv*, jclass, jint fd) {
    // This helper does not elevate privileges, relax SELinux, or open a listener.
    if(fd!=3 || getuid()!=0 || geteuid()!=0) return JNI_FALSE;
    ucred peer{}; socklen_t size=sizeof(peer);
    if(getsockopt(fd,SOL_SOCKET,SO_PEERCRED,&peer,&size) || peer.uid!=0) return JNI_FALSE;
    pid_t parent=getppid();
    if(parent==1 || prctl(PR_SET_PDEATHSIG,SIGTERM)!=0 || getppid()!=parent) return JNI_FALSE;
    signal(SIGPIPE,SIG_IGN);
    return JNI_TRUE;
}
extern "C" JNIEXPORT jintArray JNICALL
Java_com_ytbl_capture_Main_nativeNext(JNIEnv* env, jclass, jint fd) {
    Request request;
    if(!Read(fd,&request,sizeof(request)) || !Valid(request)) return nullptr;
    jint values[]={static_cast<jint>(request.sequence),static_cast<jint>(request.maxEdge)};
    jintArray result=env->NewIntArray(2);
    if(result) env->SetIntArrayRegion(result,0,2,values);
    return result;
}
extern "C" JNIEXPORT jboolean JNICALL
Java_com_ytbl_capture_Main_nativeError(JNIEnv* env, jclass, jint fd, jint sequence,
                                      jint status, jstring message) {
    Response response;
    response.sequence=static_cast<uint32_t>(sequence);
    response.status=status ? status : -1;
    response.timestampNs=NowNs();
    const char* text=message ? env->GetStringUTFChars(message,nullptr) : nullptr;
    std::snprintf(response.message,sizeof(response.message),"%s",text ? text : "Capture failed");
    if(text) env->ReleaseStringUTFChars(message,text);
    return Write(fd,&response,sizeof(response)) ? JNI_TRUE : JNI_FALSE;
}
extern "C" JNIEXPORT jboolean JNICALL
Java_com_ytbl_capture_Main_nativeFrame(JNIEnv* env, jclass, jint fd, jint sequence,
                                      jobject hardwareBuffer, jint width, jint height,
                                      jint rotation, jint colorSpace) {
    AHardwareBuffer* buffer=hardwareBuffer ? AHardwareBuffer_fromHardwareBuffer(env,hardwareBuffer) : nullptr;
    if(!buffer) return JNI_FALSE;
    AHardwareBuffer_acquire(buffer);
    AHardwareBuffer_Desc desc{}; AHardwareBuffer_describe(buffer,&desc);
    Response response;
    response.sequence=static_cast<uint32_t>(sequence);
    response.width=desc.width; response.height=desc.height;
    response.screenWidth=static_cast<uint32_t>(width);
    response.screenHeight=static_cast<uint32_t>(height);
    response.rotation=static_cast<uint32_t>(rotation);
    response.colorSpace=static_cast<uint32_t>(colorSpace);
    response.timestampNs=NowNs();
    if(desc.format!=AHARDWAREBUFFER_FORMAT_R8G8B8A8_UNORM || desc.layers!=1 ||
       (desc.usage & AHARDWAREBUFFER_USAGE_PROTECTED_CONTENT) || !Valid(response,response.sequence)) {
        AHardwareBuffer_release(buffer);
        return JNI_FALSE;
    }
    // AOSP ScreenCapture's Java callback is delivered AFTER its capture fence wait.
    // The receiver performs an independent GPU copy before retiring the borrowed storage.
    bool ok=Write(fd,&response,sizeof(response));
    if(ok) ok=AHardwareBuffer_sendHandleToUnixSocket(buffer,fd)==0;
    AHardwareBuffer_release(buffer);
    return ok ? JNI_TRUE : JNI_FALSE;
}
