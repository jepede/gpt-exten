#include "HostedCapture.h"
#include "NativeBackdrop.h"
#include <jni.h>
#include <atomic>
#include <cstdint>
#include <cstdio>
#include <string>
#include <vector>
#include <unistd.h>

extern "C" int ytbl_run_original(int argc,char** argv);
namespace screenbackdrop::hosted {
namespace {
JavaVM* vm=nullptr;
jclass mainClass=nullptr;
jmethodID start=nullptr,add=nullptr,remove=nullptr,count=nullptr,clear=nullptr;
std::atomic<uint64_t> generation{0};
std::atomic<int> excluded{0};
struct Env {
    JNIEnv* p=nullptr;bool attached=false;
    Env(){if(!vm)return;if(vm->GetEnv(reinterpret_cast<void**>(&p),JNI_VERSION_1_6)!=JNI_OK){
        if(vm->AttachCurrentThread(&p,nullptr)!=JNI_OK)p=nullptr;else attached=true;}}
    ~Env(){if(attached)vm->DetachCurrentThread();}
};
bool Check(JNIEnv* env,const char* where) {
    if(!env->ExceptionCheck())return true;
    std::fprintf(stderr,"[YtblExclude] %s failed; unfiltered capture is disabled.\n",where);
    env->ExceptionDescribe();env->ExceptionClear();excluded.store(-1);return false;
}
bool Bind(JNIEnv* env) {
    if(env->GetJavaVM(&vm)!=JNI_OK)return false;
    jclass local=env->FindClass("com/ytbl/capture/Main");
    if(!Check(env,"capture class lookup") || !local)return false;
    mainClass=static_cast<jclass>(env->NewGlobalRef(local));env->DeleteLocalRef(local);
    start=env->GetStaticMethodID(mainClass,"startCapture","(I)Z");if(!Check(env,"startCapture"))return false;
    add=env->GetStaticMethodID(mainClass,"registerSurface","(JJII)J");if(!Check(env,"registerSurface"))return false;
    remove=env->GetStaticMethodID(mainClass,"unregisterSurface","(J)J");if(!Check(env,"unregisterSurface"))return false;
    count=env->GetStaticMethodID(mainClass,"excludedCount","()I");if(!Check(env,"excludedCount"))return false;
    clear=env->GetStaticMethodID(mainClass,"clearSurfaces","()V");if(!Check(env,"clearSurfaces"))return false;
    return start && add && remove && count && clear;
}
}
bool Ready(){return vm && mainClass && start && add && remove && count && clear;}
uint64_t Generation(){return generation.load();}
int ExcludedCount(){return excluded.load();}
bool Launch(int fd) {
    if(!Ready() || excluded.load()<=0)return false;
    Env e;if(!e.p)return false;
    jboolean ok=e.p->CallStaticBooleanMethod(mainClass,start,fd);
    return Check(e.p,"capture thread start") && ok==JNI_TRUE;
}
bool Register(void* window,void* surface,int width,int height) {
    // Called synchronously before the new native surface can present UI buffers.
    excluded.store(-1);generation.fetch_add(1);
    if(!Ready() || !window || !surface)return false;
    Env e;if(!e.p)return false;
    jlong g=e.p->CallStaticLongMethod(mainClass,add,
        static_cast<jlong>(reinterpret_cast<uintptr_t>(window)),
        static_cast<jlong>(reinterpret_cast<uintptr_t>(surface)),width,height);
    if(!Check(e.p,"owned surface registration") || g<=0)return false;
    jint n=e.p->CallStaticIntMethod(mainClass,count);
    if(!Check(e.p,"exclusion count") || n<=0)return false;
    generation.store(static_cast<uint64_t>(g));excluded.store(n);return true;
}
void Unregister(void* window) {
    excluded.store(-1);generation.fetch_add(1);
    if(!Ready())return;
    Env e;if(!e.p)return;
    jlong g=e.p->CallStaticLongMethod(mainClass,remove,static_cast<jlong>(reinterpret_cast<uintptr_t>(window)));
    if(!Check(e.p,"owned surface removal") || g<=0)return;
    jint n=e.p->CallStaticIntMethod(mainClass,count);
    if(!Check(e.p,"exclusion count"))return;
    generation.store(static_cast<uint64_t>(g));excluded.store(n);
}
}

extern "C" JNIEXPORT jint JNICALL
Java_com_ytbl_capture_HostMain_nativeRun(JNIEnv* env,jclass,jobjectArray strings) {
    if(getuid()!=0 || geteuid()!=0){std::fprintf(stderr,"[YtblExclude] Owner-root launch required.\n");return 1;}
    if(!screenbackdrop::hosted::Bind(env)) {
        std::fprintf(stderr,"[YtblExclude] Cannot bind hosted capture runtime.\n");return 2;
    }
    std::vector<std::string> storage;
    if(strings){
        const jsize n=env->GetArrayLength(strings);
        for(jsize i=0;i<n;++i){
            jstring item=static_cast<jstring>(env->GetObjectArrayElement(strings,i));
            const char* utf=item?env->GetStringUTFChars(item,nullptr):nullptr;
            if(env->ExceptionCheck()){env->ExceptionClear();return 2;}
            storage.emplace_back(utf?utf:"");
            if(utf)env->ReleaseStringUTFChars(item,utf);if(item)env->DeleteLocalRef(item);
        }
    }
    if(storage.empty())storage.emplace_back("imgui_chain_1_47");
    std::vector<char*> argv;for(auto& item:storage)argv.push_back(item.data());argv.push_back(nullptr);
    int result=1;
    try {result=ytbl_run_original(static_cast<int>(storage.size()),argv.data());}
    catch(const std::exception& error){std::fprintf(stderr,"[YtblExclude] Native UI exception: %s\n",error.what());}
    catch(...){std::fprintf(stderr,"[YtblExclude] Native UI exception\n");}
    // Stop joins the receiver and shuts its connection. Java capture is a daemon
    // thread; its snapshots own independent refs and are released in finally.
    screenbackdrop::Stop();
    if(screenbackdrop::hosted::mainClass && screenbackdrop::hosted::clear){
        env->CallStaticVoidMethod(screenbackdrop::hosted::mainClass,screenbackdrop::hosted::clear);
        if(env->ExceptionCheck()){env->ExceptionDescribe();env->ExceptionClear();}
    }
    return result;
}
