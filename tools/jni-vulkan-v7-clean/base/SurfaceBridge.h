#pragma once
// v7 optional Java SurfaceView discovery. No Java bytecode or JNI exports
// are required. Attaches an ordinary daemon thread to the game's JVM and
// uses PUBLIC SurfaceView.getSurfaceControl() and SurfaceHolder.getSurface().
// ActivityThread/mActivities are non-SDK internals used only as a best-effort
// bootstrapping path; strict Android hidden API policy can block discovery.
// If blocked, existing ANativeWindow hook remains operational.
#include <jni.h>
#include <dlfcn.h>
#include <thread>
#include <chrono>
#include <atomic>
#include <cstdint>

namespace ys_bridge {
using FromJavaSurfaceControl = ASurfaceControl* (*)(JNIEnv*, jobject);
using GetCreatedJavaVMs = jint (*)(JavaVM**,jsize,jsize*);
inline std::atomic<bool>& started() { static std::atomic<bool> flag{false};return flag; }
inline void warnOnce(unsigned bit,const char* stage) {
    static std::atomic<unsigned> warned{0};
    if(!(warned.fetch_or(bit,std::memory_order_relaxed)&bit))
        LOGW("[bridge] lookup failed stage=%s; fallback to native window hook",stage);
}

inline bool clearException(JNIEnv* e) {
    if (!e->ExceptionCheck()) return false;
    e->ExceptionClear();
    return true;
}
inline bool hasActivityThread(JNIEnv* e,jobject& activityThread,jobject& map) {
    jclass cls=e->FindClass("android/app/ActivityThread");
    if(clearException(e) || !cls){warnOnce(1,"ActivityThread class");return false;}
    jmethodID mid=e->GetStaticMethodID(cls,"currentActivityThread","()Landroid/app/ActivityThread;");
    if(clearException(e) || !mid){warnOnce(2,"ActivityThread.currentActivityThread");return false;}
    activityThread=e->CallStaticObjectMethod(cls,mid);
    if(clearException(e) || !activityThread){warnOnce(4,"current ActivityThread object");return false;}
    jfieldID fid=e->GetFieldID(cls,"mActivities","Landroid/util/ArrayMap;");
    if(clearException(e) || !fid){warnOnce(8,"ActivityThread.mActivities (non-SDK API)");return false;}
    map=e->GetObjectField(activityThread,fid);
    if(clearException(e) || !map){warnOnce(16,"ActivityThread.mActivities object");return false;}
    return true;
}

inline bool findViews(JNIEnv* env,jobject root,FromJavaSurfaceControl convert,
                      jclass groupClass,jclass surfaceClass) {
    jclass viewClass=env->FindClass("android/view/View");
    jmethodID shown=env->GetMethodID(viewClass,"isShown","()Z");
    jmethodID width=env->GetMethodID(viewClass,"getWidth","()I");
    jmethodID height=env->GetMethodID(viewClass,"getHeight","()I");
    jmethodID childCount=env->GetMethodID(groupClass,"getChildCount","()I");
    jmethodID childAt=env->GetMethodID(groupClass,"getChildAt","(I)Landroid/view/View;");
    jmethodID surfaceCtl=env->GetMethodID(surfaceClass,"getSurfaceControl","()Landroid/view/SurfaceControl;");
    jmethodID holder=env->GetMethodID(surfaceClass,"getHolder","()Landroid/view/SurfaceHolder;");
    jclass holderClass=env->FindClass("android/view/SurfaceHolder");
    jmethodID getSurface=env->GetMethodID(holderClass,"getSurface","()Landroid/view/Surface;");
    jclass ctrlClass=env->FindClass("android/view/SurfaceControl");
    jmethodID ctrlValid=env->GetMethodID(ctrlClass,"isValid","()Z");
    jclass surfClass=env->FindClass("android/view/Surface");
    jmethodID surfValid=env->GetMethodID(surfClass,"isValid","()Z");
    if(clearException(env) || !shown || !width || !height || !childCount ||
       !childAt || !surfaceCtl || !holder || !getSurface || !ctrlValid || !surfValid)
        return false;
    // View hierarchy can be large. Bound traversal, and release local refs.
    std::vector<jobject> todo;todo.reserve(192);
    todo.push_back(env->NewLocalRef(root));
    bool got=false;
    for(size_t i=0;i<todo.size() && i<192;++i) {
        jobject view=todo[i];
        if(!view)continue;
        if(env->IsInstanceOf(view,surfaceClass) && env->CallBooleanMethod(view,shown)) {
            const int w=env->CallIntMethod(view,width), h=env->CallIntMethod(view,height);
            if(w>0 && h>0 && w<10000 && h<10000) {
                jobject ctrl=env->CallObjectMethod(view,surfaceCtl);
                jobject hld=env->CallObjectMethod(view,holder);
                jobject surface=hld?env->CallObjectMethod(hld,getSurface):nullptr;
                bool valid=false;
                if(ctrl && surface) {
                    const jboolean a=env->CallBooleanMethod(ctrl,ctrlValid);
                    const jboolean b=env->CallBooleanMethod(surface,surfValid);
                    valid=(a==JNI_TRUE && b==JNI_TRUE && !clearException(env));
                }
                if(valid) {
                    ASurfaceControl* anchor=convert(env,ctrl);
                    ANativeWindow* win=orig_ANativeWindow_fromSurface
                        ? orig_ANativeWindow_fromSurface(env,surface):nullptr;
                    if(!clearException(env) && anchor && win) {
                        overlay_runtime::observedSurfaceView(win,anchor,w,h);
                        got=true;
                    } else {
                        if(anchor)ASurfaceControl_release(anchor);
                        if(win)ANativeWindow_release(win);
                    }
                }
                if(ctrl)env->DeleteLocalRef(ctrl);
                if(hld)env->DeleteLocalRef(hld);
                if(surface)env->DeleteLocalRef(surface);
            }
        }
        if(env->IsInstanceOf(view,groupClass)) {
            jint n=env->CallIntMethod(view,childCount);
            if(clearException(env))n=0;
            n=std::min(n,static_cast<jint>(192-todo.size()));
            for(jint ci=0;ci<n;++ci) {
                jobject child=env->CallObjectMethod(view,childAt,ci);
                if(clearException(env))break;
                if(child)todo.push_back(child);
            }
        }
    }
    for(jobject v:todo)if(v)env->DeleteLocalRef(v);
    clearException(env);
    return got;
}

inline bool discover(JNIEnv* e,FromJavaSurfaceControl convert) {
    if(e->PushLocalFrame(256)!=JNI_OK)return false;
    jobject at=nullptr, map=nullptr;
    if(!hasActivityThread(e,at,map)) {
        e->PopLocalFrame(nullptr);
        return false;
    }
    jclass arrayMap=e->FindClass("android/util/ArrayMap");
    jmethodID size=e->GetMethodID(arrayMap,"size","()I");
    jmethodID valueAt=e->GetMethodID(arrayMap,"valueAt","(I)Ljava/lang/Object;");
    jclass activityClass=e->FindClass("android/app/Activity");
    jmethodID getWindow=e->GetMethodID(activityClass,"getWindow","()Landroid/view/Window;");
    jclass windowClass=e->FindClass("android/view/Window");
    jmethodID decor=e->GetMethodID(windowClass,"getDecorView","()Landroid/view/View;");
    jclass vg=e->FindClass("android/view/ViewGroup");
    jclass sv=e->FindClass("android/view/SurfaceView");
    if(clearException(e) || !size || !valueAt || !getWindow || !decor || !vg || !sv) {
        e->PopLocalFrame(nullptr);return false;
    }
    jint count=e->CallIntMethod(map,size);
    if(clearException(e))count=0;
    bool got=false;
    for(jint i=0;i<std::min(count,32);++i) {
        jobject rec=e->CallObjectMethod(map,valueAt,i);
        if(clearException(e) || !rec)continue;
        jclass recClass=e->GetObjectClass(rec);
        jfieldID field=e->GetFieldID(recClass,"activity","Landroid/app/Activity;");
        if(clearException(e) || !field){warnOnce(32,"ActivityClientRecord.activity (non-SDK API)");continue;}
        jobject activity=e->GetObjectField(rec,field);
        if(clearException(e) || !activity)continue;
        jobject window=e->CallObjectMethod(activity,getWindow);
        if(clearException(e) || !window)continue;
        jobject root=e->CallObjectMethod(window,decor);
        if(clearException(e) || !root)continue;
        got |= findViews(e,root,convert,vg,sv);
    }
    e->PopLocalFrame(nullptr);
    return got;
}

inline void run() {
    using namespace std::chrono_literals;
    auto getVms=reinterpret_cast<GetCreatedJavaVMs>(dlsym(RTLD_DEFAULT,"JNI_GetCreatedJavaVMs"));
    if(!getVms){
        void* art=dlopen("libart.so",RTLD_NOW|RTLD_NOLOAD);
        if(art)getVms=reinterpret_cast<GetCreatedJavaVMs>(dlsym(art,"JNI_GetCreatedJavaVMs"));
    }
    auto convert=reinterpret_cast<FromJavaSurfaceControl>(dlsym(RTLD_DEFAULT,"ASurfaceControl_fromJava"));
    if(!getVms || !convert){
        LOGW("[bridge] unavailable: JNI_GetCreatedJavaVMs=%d ASurfaceControl_fromJava=%d",getVms!=nullptr,convert!=nullptr);
        return;
    }
    JavaVM* vm=nullptr;jsize n=0;
    if(getVms(&vm,1,&n)!=JNI_OK || n<=0 || !vm){LOGW("[bridge] no JVM");return;}
    JNIEnv* e=nullptr;
    if(vm->AttachCurrentThread(&e,nullptr)!=JNI_OK || !e) {LOGW("[bridge] attach JVM failed");return;}
    LOGI("[bridge] Java SurfaceView scan started; tries root SurfaceView parent (not BLAST)");
    bool found=false;int tries=0;
    while(true) {
        const bool got=discover(e,convert);
        if(got && !found){LOGI("[bridge] SurfaceView route discovered");found=true;}
        if(!got && (++tries==1 || tries==10 || tries==60))
            LOGW("[bridge] main Activity not reachable; hidden API access or SurfaceView lifecycle may block scanning (tries=%d)",tries);
        std::this_thread::sleep_for(650ms);
    }
}
// Optional bridge for callers already holding the Activity or SurfaceView.
// This uses ONLY Android public APIs and bypasses ActivityThread hidden APIs.
inline bool registerKnownSurfaceView(JNIEnv* e, jobject view) {
    if(!e || !view || !orig_ANativeWindow_fromSurface)return false;
    auto convert=reinterpret_cast<FromJavaSurfaceControl>(dlsym(RTLD_DEFAULT,"ASurfaceControl_fromJava"));
    if(!convert) return false;
    if(e->PushLocalFrame(128)!=JNI_OK)return false;
    jclass groupClass=e->FindClass("android/view/ViewGroup");
    jclass svClass=e->FindClass("android/view/SurfaceView");
    const bool ok=groupClass && svClass && !clearException(e)
        && findViews(e,view,convert,groupClass,svClass);
    e->PopLocalFrame(nullptr);
    return ok;
}
inline bool registerKnownActivity(JNIEnv* e, jobject activity) {
    if(!e || !activity)return false;
    if(e->PushLocalFrame(32)!=JNI_OK)return false;
    jclass cls=e->FindClass("android/app/Activity");
    jmethodID getWindow=cls?e->GetMethodID(cls,"getWindow","()Landroid/view/Window;"):nullptr;
    jobject window=getWindow?e->CallObjectMethod(activity,getWindow):nullptr;
    jclass winClass=e->FindClass("android/view/Window");
    jmethodID decor=winClass?e->GetMethodID(winClass,"getDecorView","()Landroid/view/View;"):nullptr;
    jobject root=window && decor?e->CallObjectMethod(window,decor):nullptr;
    const bool good = !clearException(e) && root && registerKnownSurfaceView(e,root);
    e->PopLocalFrame(nullptr);
    return good;
}

inline void start() {
    if(started().exchange(true))return;
    try{std::thread(run).detach();}
    catch(...){LOGE("[bridge] scanner thread creation failed");}
}
} // namespace ys_bridge
