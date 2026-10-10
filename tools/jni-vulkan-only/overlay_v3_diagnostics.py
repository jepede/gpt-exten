#!/usr/bin/env python3
"""Vulkan overlay v3: fix 2-second background teardown, add compositor/input diagnostics."""
from pathlib import Path
import sys, json
root=Path(sys.argv[1]).resolve()
jni=root/"jni"
nw=jni/"NativeWindow.h"
ib=jni/"InputBridge.h"
lg=jni/"Logger.h"
assert all(p.is_file() for p in (nw, ib, lg)), "Input project not complete"
s=nw.read_text(encoding="utf-8")
assert 'stopReason = "parent window invalid for 2 seconds"' in s
assert "ASurfaceTransaction_setEnableBackPressure" in s
assert "ImGui_ImplVulkan_NewFrame()" in s

old='''        if (currentWidth <= 0 || currentHeight <= 0) {
            // Surface can be resized to zero during login -> gameplay.
            // Wait for recovery or a newer surface notification.
            int retries = 0;
            while (overlay_runtime::current(sessionToken) && retries++ < 40 &&
                   (ANativeWindow_getWidth(gameWindow) <= 0 ||
                    ANativeWindow_getHeight(gameWindow) <= 0))
                std::this_thread::sleep_for(std::chrono::milliseconds(50));
            if (!overlay_runtime::current(sessionToken)) break;
            if (ANativeWindow_getWidth(gameWindow) <= 0 ||
                ANativeWindow_getHeight(gameWindow) <= 0) {
                stopReason = "parent window invalid for 2 seconds";
                break;
            }
            continue;
        }'''
new='''        if (currentWidth <= 0 || currentHeight <= 0) {
            // Sleep until the same window recovers, or a NEW session supersedes us.
            std::uint64_t polls = 0;
            LOGW("[surface] SUSPENDED token=%llu window=%p size=%dx%d",
                 static_cast<unsigned long long>(sessionToken),
                 gameWindow, currentWidth, currentHeight);
            while (overlay_runtime::current(sessionToken) &&
                   (ANativeWindow_getWidth(gameWindow) <= 0 ||
                    ANativeWindow_getHeight(gameWindow) <= 0)) {
                std::this_thread::sleep_for(std::chrono::milliseconds(100));
                if (++polls % 50 == 0)
                    LOGW("[surface] SUSPENDED %.1fs token=%llu parent=%p",
                         0.1 * static_cast<double>(polls),
                         static_cast<unsigned long long>(sessionToken), gameWindow);
            }
            if (!overlay_runtime::current(sessionToken)) break;
            LOGI("[surface] RESUMED token=%llu window=%p size=%dx%d",
                 static_cast<unsigned long long>(sessionToken), gameWindow,
                 ANativeWindow_getWidth(gameWindow), ANativeWindow_getHeight(gameWindow));
            continue;
        }'''
assert old in s, "2-second window timeout changed"
s=s.replace(old,new,1)

# Initial zero-sized surface should also wait for a later valid geometry.
a=s.index('    for (int attempt = 0;')
b=s.index('    VulkanState.ScreenWidth',a)
assert 'overlay_runtime::current(sessionToken)' in s[a:b]
s=s[:a]+'''    std::uint64_t initialPolls = 0;
    while ((width <= 0 || height <= 0) && overlay_runtime::current(sessionToken)) {
        if (initialPolls % 50 == 0) {
            LOGW("[surface] waiting for window geometry token=%llu win=%p",
                 static_cast<unsigned long long>(sessionToken), gameWindow);
        }
        ++initialPolls;
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
        width = ANativeWindow_getWidth(gameWindow);
        height = ANativeWindow_getHeight(gameWindow);
    }
    if (!overlay_runtime::current(sessionToken)) return;
'''+s[b:]

vis='        ASurfaceTransaction_setEnableBackPressure(tx, control, true);'
assert vis in s
s=s.replace(vis,vis+
  '\n        ASurfaceTransaction_setVisibility(tx, control, ASURFACE_TRANSACTION_VISIBILITY_SHOW);',1)
assert '#include <atomic>\n' in s
s=s.replace('#include <atomic>\n','#include <atomic>\n#include <unistd.h>\n#include <new>\n',1)
needle='void RunSurfaceControlOverlay(ANativeWindow* gameWindow, std::uint64_t sessionToken) {'
callback='''namespace overlay_diagnostics {
struct Receipt { std::uint64_t token, frame; };
// Called by SurfaceFlinger on a separate thread. Never access ImGui or VkDevice.
inline void onComplete(void* opaque, ASurfaceTransactionStats* stats) {
    std::unique_ptr<Receipt> receipt(static_cast<Receipt*>(opaque));
    if (!receipt || !stats) return;
    const auto latch = ASurfaceTransactionStats_getLatchTime(stats);
    const int presentFd = ASurfaceTransactionStats_getPresentFenceFd(stats);
    LOGI("[present] token=%llu frame=%llu latch_ns=%lld fence_available=%d",
         static_cast<unsigned long long>(receipt->token),
         static_cast<unsigned long long>(receipt->frame),
         static_cast<long long>(latch), presentFd >= 0 ? 1 : 0);
    if (presentFd >= 0) ::close(presentFd);
}
} // namespace overlay_diagnostics
'''
assert needle in s
s=s.replace(needle,callback+'\n'+needle,1)
old='''        ASurfaceTransaction_setBuffer(update, control, buffer, -1);
        ASurfaceTransaction_apply(update);'''
new='''        ASurfaceTransaction_setBuffer(update, control, buffer, -1);
        // CPU frame counter does not imply composition/presentation.
        // Sample the compositor completion callback every 120 frames.
        if (renderedFrames == 0 || (renderedFrames + 1) % 120 == 0) {
            auto* receipt = new (std::nothrow) overlay_diagnostics::Receipt{
                sessionToken, renderedFrames + 1};
            if (receipt)
                ASurfaceTransaction_setOnComplete(
                    update, receipt, overlay_diagnostics::onComplete);
        }
        ASurfaceTransaction_apply(update);'''
assert old in s
s=s.replace(old,new,1)
assert 'parent window invalid for 2 seconds' not in s
nw.write_text(s,encoding="utf-8")

logger=lg.read_text(encoding="utf-8")
assert '"NDK"' in logger, logger[:250]
logger=logger.replace('"NDK"','"YS"')
logger+='''

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
'''
lg.write_text(logger,encoding="utf-8")

inp=ib.read_text(encoding="utf-8")
assert 'p.x = AMotionEvent_getX(input, i);' in inp
assert 'p.y = AMotionEvent_getY(input, i);' in inp
inp=inp.replace('#include <android/input.h>\n',
                '#include <android/input.h>\n#include <atomic>\n#include "Logger.h"\n',1)
old='''            p.x = AMotionEvent_getX(input, i);
            p.y = AMotionEvent_getY(input, i);'''
new='''            const float localX = AMotionEvent_getX(input, i);
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
            if (i == 0 && (motion.action == AMOTION_EVENT_ACTION_DOWN ||
                           motion.action == AMOTION_EVENT_ACTION_POINTER_DOWN)) {
                static std::atomic<unsigned> samples{0};
                if (samples.fetch_add(1, std::memory_order_relaxed) < 80) {
                    LOGI("[touch] action=%d local=(%.1f,%.1f) raw=(%.1f,%.1f) "
                         "offset=(%.1f,%.1f) mapped=(%.1f,%.1f) mode=%s",
                         motion.action, localX, localY, rawX, rawY,
                         AMotionEvent_getXOffset(input), AMotionEvent_getYOffset(input),
                         p.x, p.y, YS_USE_RAW_TOUCH_COORDS ? "RAW" : "LOCAL");
                }
            }'''
assert old in inp
inp=inp.replace(old,new,1)
needle='''        const auto& changed = m.points[m.index];'''
assert needle in inp
inp=inp.replace(needle,needle+'''
        if (m.action == AMOTION_EVENT_ACTION_DOWN ||
            m.action == AMOTION_EVENT_ACTION_POINTER_DOWN) {
            static thread_local unsigned drainLogs = 0;
            if (drainLogs++ < 80) {
                LOGI("[touch] imgui=(%.1f,%.1f) viewport=(%.1f,%.1f) mode=%s",
                     changed.x, changed.y, io.DisplaySize.x, io.DisplaySize.y,
                     YS_USE_RAW_TOUCH_COORDS ? "RAW" : "LOCAL");
            }
        }''',1)
ib.write_text(inp,encoding="utf-8")

(root/"README_SURFACE_V3.md").write_text("""# Vulkan overlay v3 diagnosis and partial repair

Tested symptom: session 1 emitted 2190 frames; session 2 emitted 832 frames,
then stopped because its parent window returned zero geometry for two seconds.

Changes:
- No more fixed 2-second teardown: suspend until the parent returns or a new
  window supersedes it, with detailed SUSPENDED/RESUMED logs under TAG YS.
- Make SurfaceControl visibility SHOW explicit (cannot override a hidden parent).
- Sample compositor ASurfaceTransaction_OnComplete receipts at frames 1/120/240...
  [present] proves that a transaction reached composition, not visual visibility.
  The sampled callback context is heap allocated and freed upon callback.
- Default touch mapping to RawX/RawY for the fullscreen overlay at origin (0,0).
  If the actual parent is transformed, screen coordinates may remain wrong.
  Toggle YS_USE_RAW_TOUCH_COORDS=0 and rebuild to restore local coords.
- Log the first 80 taps local/raw/offset/mapped and render-thread ImGui viewport.
- Keep Vulkan-only render path and existing ImGui and JNI hooks.

Capture:
  su -c 'logcat -b all -d -v threadtime -s YS:V > /sdcard/Download/YS-v3.log'
  su -c 'dumpsys SurfaceFlinger --list > /sdcard/Download/layers.txt'
  su -c 'dumpsys SurfaceFlinger > /sdcard/Download/surfaceflinger.txt'
  su -c 'dumpsys window windows > /sdcard/Download/windows.txt'

If frames continue and [present] logs occur while the overlay is invisible,
the active parent may be occluded/hidden. Child Z-order cannot override a
parent higher/lower layer ordering. Attach the overlay to a persistent app
window through a controlled Activity/Surface lifecycle; the current native
window hook cannot guarantee it observed the app's visible main Surface.

Real game display, touch, background and resume were NOT tested here.
""",encoding="utf-8")
print(json.dumps({"result":"PATCH_APPLIED","surface_bytes":len(s),
                  "input_bytes":len(inp),"log_tag":"YS",
                  "touch_mode":"RAW","frame_receipts":True,
                  "zero_geometry_timeout_removed":True},indent=2))
