#include "wire.h"
#include <android/hardware_buffer.h>
#include <android/hardware_buffer_jni.h>
#include <jni.h>
#include <cstdio>
#include <csignal>
#include <sys/prctl.h>
#include <unistd.h>

namespace {
jboolean Bootstrap(JNIEnv*,jclass,jint parent) {
    if (getuid()!=0 || parent<=1 || getppid()!=parent) return JNI_FALSE;
    if (prctl(PR_SET_PDEATHSIG,SIGTERM)!=0 || getppid()!=parent) return JNI_FALSE;
    return JNI_TRUE;
}
jintArray Next(JNIEnv* env,jclass,jint fd) {
    livebg::Request r;
    if (!livebg::ReceiveAll(fd,&r,sizeof(r)) || !livebg::Valid(r)) return nullptr;
    const jint values[6]={jint(r.generation),r.width,r.height,r.rotation,r.outputWidth,r.outputHeight};
    jintArray result=env->NewIntArray(6);
    if (result) env->SetIntArrayRegion(result,0,6,values);
    return result;
}
jboolean Deliver(JNIEnv* env,jclass,jint fd,jintArray request,jobject object,
                 jint flags,jint error,jstring text) {
    if (!request || env->GetArrayLength(request)!=6) return JNI_FALSE;
    jint values[6]; env->GetIntArrayRegion(request,0,6,values);
    if (env->ExceptionCheck()) return JNI_FALSE;
    livebg::Reply r;
    r.generation=uint32_t(values[0]);r.width=values[1];r.height=values[2];r.rotation=values[3];
    r.flags=uint32_t(flags);r.status=error;r.readyNs=livebg::NowNs();
    if (text) {
        const char* message=env->GetStringUTFChars(text,nullptr);
        if (!message) return JNI_FALSE;
        std::snprintf(r.message,sizeof(r.message),"%s",message);
        env->ReleaseStringUTFChars(text,message);
    }
    AHardwareBuffer* buffer=nullptr;
    if (object && !r.status) {
        buffer=AHardwareBuffer_fromHardwareBuffer(env,object); // Borrowed until JNI returns.
        AHardwareBuffer_Desc d{};
        if (buffer) AHardwareBuffer_describe(buffer,&d);
        if (!buffer || d.format!=AHARDWAREBUFFER_FORMAT_R8G8B8A8_UNORM ||
            (d.usage & AHARDWAREBUFFER_USAGE_PROTECTED_CONTENT) ||
            d.width!=uint32_t(values[4]) || d.height!=uint32_t(values[5]) || d.layers!=1) {
            r.status=-2;buffer=nullptr;
            std::snprintf(r.message,sizeof(r.message),"Unexpected or protected HardwareBuffer");
        } else {r.bufferWidth=int32_t(d.width);r.bufferHeight=int32_t(d.height);}
    } else if (!r.status) {
        r.status=-3;std::snprintf(r.message,sizeof(r.message),"Missing capture buffer");
    }
    if (!livebg::SendAll(fd,&r,sizeof(r))) return JNI_FALSE;
    if (r.status) return JNI_TRUE;
    // Transfers handles, not pixel data; receiver obtains its own reference.
    return AHardwareBuffer_sendHandleToUnixSocket(buffer,fd)==0?JNI_TRUE:JNI_FALSE;
}
}
extern "C" JNIEXPORT jint JNI_OnLoad(JavaVM* vm,void*) {
    JNIEnv* env=nullptr;
    if (vm->GetEnv(reinterpret_cast<void**>(&env),JNI_VERSION_1_6)!=JNI_OK) return JNI_ERR;
    jclass cls=env->FindClass("io/github/surfaceglass/CaptureMain");
    if (!cls) return JNI_ERR;
    const JNINativeMethod methods[]={
        {const_cast<char*>("bootstrap"),const_cast<char*>("(I)Z"),reinterpret_cast<void*>(Bootstrap)},
        {const_cast<char*>("next"),const_cast<char*>("(I)[I"),reinterpret_cast<void*>(Next)},
        {const_cast<char*>("deliver"),const_cast<char*>("(I[ILandroid/hardware/HardwareBuffer;IILjava/lang/String;)Z"),reinterpret_cast<void*>(Deliver)}
    };
    const int result=env->RegisterNatives(cls,methods,3);env->DeleteLocalRef(cls);
    return result==0?JNI_VERSION_1_6:JNI_ERR;
}
