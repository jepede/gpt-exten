#!/usr/bin/env python3
# Production-only cleanup of the exact v7 JNI sources confirmed working on-device.
# The GitHub Actions workflow overlays the archived v7 source onto a cached
# older complete project to restore binary font, Dobby and ImGui dependencies.
# All rendering, SurfaceView discovery, lifecycle and deduplicated touch logic
# are retained. This patch is deliberately assertion-heavy: upstream changes
# fail closed instead of silently deleting the wrong source range.
from pathlib import Path
import re
import shutil
import sys

if len(sys.argv)!=3:
    raise SystemExit("usage: strip_debug_v7.py <cached-complete-project> <v7-source-root>")
project=Path(sys.argv[1]).resolve()
base=Path(sys.argv[2]).resolve()
jni=project/"jni"
required = ["Android.mk","Application.mk","EventDedup.h","Injector.cpp",
            "InputBridge.h","Logger.h","MotionQueue.h","NativeWindow.h",
            "OverlayPolicy.h","OverlayProbe.h","OverlayRoute.h",
            "OverlaySupervisor.h","SurfaceBridge.h","VulkanOverlay.h"]
for name in required:
    assert (base/name).is_file(), name
    shutil.copyfile(base/name,jni/name)
assert (jni/"third_party/imgui/backends/imgui_impl_vulkan.cpp").is_file()
assert (jni/"Library/Imgui/include/font_zt.h").is_file()
assert (jni/"Library/dobby/arm64-v8a/libdobby.a").is_file()

def between(s, first, last, replacement="", expect=1):
    assert s.count(first)==expect, ("missing/ambiguous",first,s.count(first))
    i=s.index(first)
    assert s.count(last)>=1,("missing end",last)
    j=s.index(last,i)
    assert i<j,(first,last)
    return s[:i]+replacement+s[j:]

def replace_once(s,old,new):
    assert s.count(old)==1,("replace requires exact match",repr(old[:110]),s.count(old))
    return s.replace(old,new,1)

# Remove debug-only virtual parent selection and manual screen-flip controls.
# v7 stable default: broadcast to any native windows until a SurfaceView root
# exists; after successful SurfaceView registration, publish ONLY to that root.
(jni/"OverlayProbe.h").unlink()
(jni/"OverlayRoute.h").write_text("""#pragma once
namespace ys_overlay {
inline int surfaceRoutePriority(bool surfaceView, int nativePriority) noexcept {
    return surfaceView ? 1000 : nativePriority;
}
inline bool submitToParent(bool sourceIsSurfaceView,
                           bool hasLiveSurfaceView) noexcept {
    return !hasLiveSurfaceView || sourceIsSurfaceView;
}
} // namespace ys_overlay
""",encoding="utf-8")
(jni/"OverlayPolicy.h").write_text("""#pragma once
namespace ys_overlay {
constexpr int kPixelRgba8888 = 1;
constexpr int kPixelRgbx8888 = 2;
constexpr int kPixelRgb565 = 4;
inline int parentPriority(int format) noexcept {
    switch (format) {
    case kPixelRgba8888: return 100;
    case kPixelRgbx8888: return 90;
    case kPixelRgb565: return 40;
    default: return 50;
    }
}
inline bool validWindowSize(int w,int h) noexcept {
    return w>0 && h>0 && w<=8192 && h<=8192;
}
inline bool windowQueryFailed(int w,int h) noexcept {
    return w<0 || h<0;
}
} // namespace ys_overlay
""",encoding="utf-8")
(jni/"Logger.h").write_text("""#pragma once
// Production build: errors/warnings only, no per-frame/diagnostic log traffic.
#include <android/log.h>
#define YS_LOG_TAG "YS"
#define LOGE(...) ((void)__android_log_print(ANDROID_LOG_ERROR, YS_LOG_TAG, __VA_ARGS__))
#define LOGW(...) ((void)__android_log_print(ANDROID_LOG_WARN, YS_LOG_TAG, __VA_ARGS__))
#define ALOGE(...) LOGE(__VA_ARGS__)
#define ALOGW(...) LOGW(__VA_ARGS__)
""",encoding="utf-8")

s=(jni/"InputBridge.h").read_text(encoding="utf-8")
s=replace_once(s,'''            const float localX = AMotionEvent_getX(input, i);
            const float localY = AMotionEvent_getY(input, i);
            const float rawX = AMotionEvent_getRawX(input, i);
            const float rawY = AMotionEvent_getRawY(input, i);
            // Fullscreen overlay at position=(0,0): prefer display coordinates.
            // For a transformed/multi-window layer, disable and calibrate.
#ifndef YS_USE_RAW_TOUCH_COORDS
#define YS_USE_RAW_TOUCH_COORDS 1
#endif
            p.x = YS_USE_RAW_TOUCH_COORDS ? rawX : localX;
            p.y = YS_USE_RAW_TOUCH_COORDS ? rawY : localY;
''','''            // v7 verified display-space mapping. Keep the proven raw source.
            p.x = AMotionEvent_getRawX(input, i);
            p.y = AMotionEvent_getRawY(input, i);
''')
s=between(s,'''        if (overlay_input::eventDeduplicator().isDuplicate(identity)) {''',
          '''        overlay_input::queue().push(motion, generation);''',
          '''        if (overlay_input::eventDeduplicator().isDuplicate(identity))
            return;
''')
s=between(s,'''        const auto flip = ys_overlay::configuredFlip().load(std::memory_order_acquire);''',
          '''        const auto source = changed.tool == AMOTION_EVENT_TOOL_TYPE_MOUSE''',
          '''        const auto mousePos = [&](float x, float y) {
            io.AddMousePosEvent(x,y);
        };
''')
assert "[touch]" not in s
assert "configuredFlip" not in s and "YS_USE_RAW_TOUCH_COORDS" not in s
(jni/"InputBridge.h").write_text(s,encoding="utf-8")

s=(jni/"OverlaySupervisor.h").read_text(encoding="utf-8")
s=replace_once(s,"#include <sys/system_properties.h>\n","")
s=replace_once(s,'#include "OverlayProbe.h"\n',"")
s=between(s,"inline int getPropertyInt(const char* key, int fallback) {","struct Parent {")
s=between(s,"// Snapshot immutable submission info so callback can safely run after a",
          "inline Parent* choosePrimary(")
s=between(s,"inline void drawCalibration() {",
          "// Per-frame Vulkan render loop")
s=replace_once(s,'''    Clock::time_point firstSeen=Clock::now();
    Clock::time_point lastSubmit{};
    std::uint64_t submitted=0;
''',"")
s=replace_once(s,'''    int mirrorMode=-1,bufferFlip=-1, offsetX=0,offsetY=0;
    int debugOnly=-1, debugProbe=-1, debugTrace=-1;
    std::uint64_t lastEffectiveId=~0ULL;
    const Clock::time_point probeEpoch=Clock::now();
''',"")
s=between(s,'''                LOGI("[diag] new_parent id=%llu win=%p reason=%s",''',
          '''            }
        }
        // Attach pending candidates''')
# Remove the old per-host detailed retire log; retaining native-window reference cleanup.
s=between(s,'''                LOGW("[diag] retire id=%llu submitted=%llu ever_attached=%d size=%dx%d fmt=%d layer=%p",''',
          '''                registerRemoval(p.window,p.anchor);''')
s=between(s,'''        if (frames%120==0) {''',
          '''        auto frameStart=Clock::now();''')
s=between(s,'''        BeginDraw();''',
          '''        ImGui::Render();''',
          '''        BeginDraw();
''')
s=between(s,'''        if(debugTrace>0 && (frames==0 || frames%120==0)) {''',
          '''        AHardwareBuffer* buffer=nullptr;''')
s=between(s,'''        Parent* latest=nullptr;''',
          '''        const bool hasSurfaceView=std::any_of(''',
          '''        int published=0;
''')
s=replace_once(s,'''            if(!ys_overlay::submitToParent(host.isSurfaceView(),hasSurfaceView,
                                            selectedMode,&host==primary,&host==latest,
                                            effectiveId,host.id)) {''',
          '''            if(!ys_overlay::submitToParent(host.isSurfaceView(),hasSurfaceView)) {''')
s=replace_once(s,'''            ASurfaceTransaction_setPosition(tx,host.layer,offsetX,offsetY);''',
          '''            ASurfaceTransaction_setPosition(tx,host.layer,0,0);''')
s=replace_once(s,'''            ASurfaceTransaction_setBufferTransform(tx,host.layer,bufferFlip<0?0:bufferFlip);''',
          '''            ASurfaceTransaction_setBufferTransform(tx,host.layer,0);''')
s=between(s,'''            if(published<static_cast<int>(kMaxParents)) {''',
          '''            ++published;''')
s=between(s,'''        if (published>0) {''',
          '''        ASurfaceTransaction_delete(tx);''',
          '''        if(published>0)ASurfaceTransaction_apply(tx);
''')
s=between(s,'''        if(frames==1||frames%120==0) {''',
          '''        const auto elapsed=Clock::now()-frameStart;''')
# Drop line-by-line informational logs, physically (leaves production error logs).
# This strips the call expression AND its format strings. It leaves any
# surrounding conditional structure intact until dead-code cleanup by Clang.
def erase_info_calls(src):
    pattern=re.compile(r'\b(?:LOGI|LOGD)\s*\(')
    while True:
        hit=pattern.search(src)
        if hit is None: break
        i=hit.end()
        depth=1
        in_string=False
        in_char=False
        escaped=False
        while i<len(src) and depth>0:
            c=src[i]
            if escaped:
                escaped=False
            elif (in_string or in_char) and c=='\\':
                escaped=True
            elif not in_char and c=='"':
                in_string=not in_string
            elif not in_string and c=="'":
                in_char=not in_char
            elif not in_string and not in_char:
                if c=="(": depth+=1
                elif c==")": depth-=1
            i+=1
        assert depth==0,"unterminated logging call"
        src=src[:hit.start()]+"((void)0)"+src[i:]
    src=re.sub(r'(?m)^[ \t]*\(\(void\)0\);[ \t]*\n','',src)
    return src
s=erase_info_calls(s)
assert "debug.ys.overlay" not in s and "[diag]" not in s
assert "[probe]" not in s and "[present.parent]" not in s
assert "drawCalibration" not in s and "ASurfaceTransaction_setOnComplete" not in s
assert "Receipt" not in s and "OverlayProbe.h" not in s
assert "publishedMask" not in s and "debugTrace" not in s and "effectiveId" not in s
assert "std::snprintf" not in s and "bufferFlip" not in s
(jni/"OverlaySupervisor.h").write_text(s,encoding="utf-8")

s=(jni/"SurfaceBridge.h").read_text(encoding="utf-8")
# Keep the scanning algorithm and public SurfaceView route unmodified.
# Info logging was only discovery/trace; error/warning for real failures stays.
s=erase_info_calls(s)
# Remove the obsolete one-time info-latch which only tracked LOGI output.
s=replace_once(s,"    bool found=false;int tries=0;","    int tries=0;")
s=replace_once(s,'''        if(got && !found){((void)0);found=true;}''', '''        (void)got;''')
assert "LOGI" not in s and "found=true" not in s
(jni/"SurfaceBridge.h").write_text(s,encoding="utf-8")

s=(jni/"VulkanOverlay.h").read_text(encoding="utf-8")
s=erase_info_calls(s)
(jni/"VulkanOverlay.h").write_text(s,encoding="utf-8")

# Also remove information calls from the glue file, preserving its exports.
s=(jni/"Injector.cpp").read_text(encoding="utf-8")
s=erase_info_calls(s)
(jni/"Injector.cpp").write_text(s,encoding="utf-8")

s=(jni/"Android.mk").read_text(encoding="utf-8")
s=s.replace('    # Stable default: parent auto-switching must be explicitly enabled via setprop.\n',"")
s=s.replace("    LOCAL_CPPFLAGS += -DYS_DEFAULT_AUTO_PROBE=0\n","")
(jni/"Android.mk").write_text(s,encoding="utf-8")

# No debug UI, diagnostics, transaction-stat callbacks or debug property code
# should survive in production source. Confirm we did not break the route.
source="\n".join(p.read_text(encoding="utf-8") for p in jni.glob("*.h"))
banned=[
    "OverlayProbe.h", "drawCalibration", "YS TARGET", "YS TL",
    "[present.parent]", "[touchdiag]", "[diag]", "[probe]",
    "debug.ys.overlay", "ASurfaceTransaction_setOnComplete",
    "ASurfaceTransactionStats_get", "YS_USE_RAW_TOUCH_COORDS",
    "configuredFlip", "configuredOffsetX", "configuredOffsetY",
    "LOGI(", "LOGD(",
]
for token in banned:
    assert token not in source,("debug code not fully removed",token)
for core in [
    "ASurfaceControl_create(parent.anchor", "observedSurfaceView(",
    "ASurfaceTransaction_setBuffer(tx,host.layer,buffer,-1)",
    "ANativeWindow_fromSurface", "ASurfaceTransaction_setVisibility",
    "ImGui_ImplVulkan_NewFrame();",
    "overlay_input::queue().enable();",
]:
    assert core in source,("working route accidentally removed",core)
assert "YS_RegisterSurfaceView" in (jni/"Injector.cpp").read_text()
assert "EventDeduplicator" in (jni/"InputBridge.h").read_text()
assert not (jni/"OverlayProbe.h").exists()
# Older cached archives may contain stale unused GLES-related assets.
old_imgui_static = jni/"Library/Imgui/arm64-v8a"
if old_imgui_static.exists(): shutil.rmtree(old_imgui_static)
old_gles= jni/"Library/Imgui/include/OpenGL.h"
if old_gles.exists():old_gles.unlink()
# Packaging only production files (no 37K-line diagnostic diffs or symbols).
for directory in ["obj","symbols","prebuilt","tests","tools","verification","docs"]:
    shutil.rmtree(project/directory,ignore_errors=True)
for old in ["README_SURFACE_V3.md","README_SURFACE_V4.md",
            "README_v6_仅YS日志调试.md",
            "README_稳定版_v6.1.md","README_交付说明.md",
            "README_v7_SurfaceView_Root_修复说明.md",
            "SURFACE_FIX_VALIDATION.json","VERIFICATION.json",
            "BUILD-REPORT.txt","original_jni1.sha256",
            "dynamic_dependencies.txt","SHA256SUMS.txt"]:
    (project/old).unlink(missing_ok=True)

(project/"README.md").write_text("""# YS Vulkan ImGui Overlay — production v7 clean

This is a production cleanup of the exact v7 source confirmed working on an
Android 16 ARM64 game by the user. Vulkan-only; no OpenGL/EGL/GLES.

Kept:
- JNI constructor + optional YS_RegisterActivity / YS_RegisterSurfaceView.
- Automatic SurfaceView parent discovery, lifetime management, and fallback hook.
- SurfaceView root attachment (not scaled BLAST-buffer child).
- One Vulkan offscreen renderer with AHardwareBuffer transfer.
- Dobby native-window and MotionEvent hooks.
- MotionEvent deduplication, multi-touch dragging, raw screen coordinates.
- Normal user menu and essential error/warning logging.

Removed:
- ImGui calibration corners, cursor crosshair, YS TARGET diagnostic banner.
- Parent auto-probing/5s switching, debug.ys.overlay property polling/forcing.
- SurfaceFlinger transaction-stat receipt callbacks, per-parent present logs.
- Per-frame / input / trace diagnostic logs, probe and calibration helpers.
- Historical debug packages, symbols, test runners and redundant diagnostics.

Build:
    ndk-build -j4 NDK_PROJECT_PATH=. APP_BUILD_SCRIPT=jni/Android.mk \\
      NDK_APPLICATION_MK=jni/Application.mk BUILD_MODE=release

Outputs:
    libs/arm64-v8a/libAndroid.so
    prebuilt/release/libAndroid.so

No actual Android device regression test is possible in GitHub Actions.
User-confirmed behavior applies to the original v7, while cleanup is validated
by compilation, ELF checks and static/host tests.
""",encoding="utf-8")
print("STRIP_V7_DEBUG_CODE=PASS")
print("PRODUCTION_CPP_FILES",sum(1 for p in jni.rglob("*") if p.is_file()))
