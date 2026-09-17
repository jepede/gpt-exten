# API references and attribution

Platform behavior was checked against AOSP's Android 16 source, not guessed C++ object layouts. The native transport/import uses NDK APIs; platform capture itself remains non-public and requires on-device verification.

```text
AOSP ScreenCapture (argument builders, listener, result ownership)
https://github.com/aosp-mirror/platform_frameworks_base/blob/android16-release/core/java/android/window/ScreenCapture.java

AOSP ScreenCapture JNI (wait on capture fence before Java callback)
https://github.com/aosp-mirror/platform_frameworks_base/blob/android16-release/core/jni/android_window_ScreenCapture.cpp

AOSP DisplayControl (physical display token)
https://android.googlesource.com/platform/frameworks/base/+/refs/heads/android16-release/services/core/java/com/android/server/display/DisplayControl.java

NDK HardwareBuffer
https://developer.android.com/ndk/reference/group/a-hardware-buffer

Genymobile scrcpy DisplayControl wrapper (Apache-2.0), reference for loading the system-server class and its native library
https://github.com/Genymobile/scrcpy/blob/master/server/src/main/java/com/genymobile/scrcpy/wrappers/DisplayControl.java

Android read-only dynamically loaded code requirement
https://developer.android.com/about/versions/14/behavior-changes-14#safer-dynamic-code-loading
```

The project does not ship Android framework binaries or scrcpy binaries. The user's ANativeWindowCreator and Ytbl sources are processed only on the user's machine by install.py; they were not uploaded into this branch. Existing third-party notices in the user's project remain applicable. No font files are included in this module bundle.
