#ifndef Logger_h
#define Logger_h
#include <jni.h>
#include <android/log.h>

enum LogType {
    oDEBUG = 3,
    oERROR = 6,
    oINFO  = 4,
    oWARN  = 5
};

#define TAG "YS"
#define LOGD(...) ((void)__android_log_print(oDEBUG, TAG, __VA_ARGS__))
#define LOGE(...) ((void)__android_log_print(oERROR, TAG, __VA_ARGS__))
#define LOGI(...) ((void)__android_log_print(oINFO,  TAG, __VA_ARGS__))
#define LOGW(...) ((void)__android_log_print(oWARN,  TAG, __VA_ARGS__))
#endif /* Logger_h */

// Compatible with both ALOGx and existing LOGx call-sites.
#ifndef ALOGI
#define ALOGI(...) LOGI(__VA_ARGS__)
#endif
#ifndef ALOGW
#define ALOGW(...) LOGW(__VA_ARGS__)
#endif
#ifndef ALOGE
#define ALOGE(...) LOGE(__VA_ARGS__)
#endif
#ifndef ALOGD
#define ALOGD(...) ((void)__android_log_print(ANDROID_LOG_DEBUG, "YS", __VA_ARGS__))
#endif
