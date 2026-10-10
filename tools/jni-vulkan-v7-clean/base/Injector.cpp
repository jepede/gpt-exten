#include <jni.h>
#include <thread>
#include <Logger.h>

#include <dobby.h>

#include <NativeWindow.h>



// 库被加载时自动跑
__attribute__((constructor))
void lib_main() {
    try { std::thread([] { hack_main(); }).detach(); }
    catch (const std::exception& e) { LOGE("startup thread failed: %s", e.what()); }
    catch (...) { LOGE("startup thread failed"); }
}

// Optional public-API bootstrap for native injectors that already have a
// jobject to the app's Activity or SurfaceView. No ActivityThread introspection.
extern "C" __attribute__((visibility("default")))
void YS_RegisterActivity(JNIEnv* env, jobject activity) {
    if(!ys_bridge::registerKnownActivity(env,activity))
        LOGW("[bridge] explicit Activity registration failed");
}
extern "C" __attribute__((visibility("default")))
void YS_RegisterSurfaceView(JNIEnv* env, jobject view) {
    if(!ys_bridge::registerKnownSurfaceView(env,view))
        LOGW("[bridge] explicit SurfaceView registration failed");
}
