#!/usr/bin/env python3
"""Vulkan v4 diagnostics: correct invalid native windows and duplicate input copies.

Input: complete v3 project extracted from cached GitHub Actions artifact.
Rewrites only NativeWindow.h and InputBridge.h, preserving Vulkan-only renderer.
"""
from pathlib import Path
import sys,re
root=Path(sys.argv[1])
nw=root/"jni"/"NativeWindow.h"
ib=root/"jni"/"InputBridge.h"
assert nw.is_file() and ib.is_file()
s=nw.read_text(encoding="utf-8")
inp=ib.read_text(encoding="utf-8")
assert 'SUSPENDED' in s and 'ASurfaceTransaction_setOnComplete' in s
assert 'AMotionEvent_getRawX' in inp

# Initial window: negative values are query error codes, not dimensions.
start=s.index('    std::uint64_t initialPolls = 0;')
stop=s.index('    VulkanState.ScreenWidth',start)
segment=s[start:stop]
assert 'initialPolls' in segment and 'overlay_runtime::current(sessionToken)' in segment
new_initial='''    // NativeWindow width/height return negative error codes, e.g. -ENODEV.
    // Do not wait forever on a permanently disconnected producer.
    if (width < 0 || height < 0) {
        LOGE("[surface] window query failed on init token=%llu width_error=%d height_error=%d",
             static_cast<unsigned long long>(sessionToken), width, height);
        return;
    }
    std::uint32_t initialPolls = 0;
    while ((width == 0 || height == 0) && overlay_runtime::current(sessionToken) &&
           initialPolls++ < 50) {
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
        width = ANativeWindow_getWidth(gameWindow);
        height = ANativeWindow_getHeight(gameWindow);
        if (width < 0 || height < 0) {
            LOGE("[surface] init parent disconnected token=%llu width_error=%d height_error=%d",
                 static_cast<unsigned long long>(sessionToken), width, height);
            break;
        }
    }
    if (!overlay_runtime::current(sessionToken) || width <= 0 || height <= 0) {
        LOGW("[surface] initial window unavailable token=%llu size=%dx%d",
             static_cast<unsigned long long>(sessionToken), width, height);
        return;
    }
'''
s=s[:start]+new_initial+s[stop:]
start=s.index('''        if (currentWidth <= 0 || currentHeight <= 0) {''')
stop=s.index('''        if (currentWidth != width || currentHeight != height) {''',start)
segment=s[start:stop]
assert '[surface] SUSPENDED' in segment
assert '[surface] RESUMED' in segment
new_runtime='''        // Negative return values are native window query errors, not a
        // temporary zero-sized render target. -19 is usually -ENODEV.
        if (currentWidth < 0 || currentHeight < 0) {
            LOGE("[surface] WINDOW_DISCONNECTED token=%llu win=%p width_error=%d height_error=%d",
                 static_cast<unsigned long long>(sessionToken),
                 gameWindow, currentWidth, currentHeight);
            stopReason = "parent ANativeWindow query failed";
            break;
        }
        if (currentWidth == 0 || currentHeight == 0) {
            // A short zero-sized transition can recover with the same parent.
            // Bound the wait so the worker doesn't hold stale Vulkan resources.
            LOGW("[surface] SUSPENDED_ZERO_SIZE token=%llu win=%p",
                 static_cast<unsigned long long>(sessionToken), gameWindow);
            std::uint32_t attempts = 0;
            int testWidth = currentWidth, testHeight = currentHeight;
            while (overlay_runtime::current(sessionToken) && attempts++ < 50) {
                std::this_thread::sleep_for(std::chrono::milliseconds(100));
                testWidth = ANativeWindow_getWidth(gameWindow);
                testHeight = ANativeWindow_getHeight(gameWindow);
                if (testWidth < 0 || testHeight < 0 ||
                    (testWidth > 0 && testHeight > 0)) break;
            }
            if (!overlay_runtime::current(sessionToken)) break;
            if (testWidth < 0 || testHeight < 0) {
                LOGE("[surface] WINDOW_DISCONNECTED_AFTER_SUSPEND width_error=%d height_error=%d",
                     testWidth, testHeight);
                stopReason = "parent disconnected during suspended geometry";
                break;
            }
            if (testWidth <= 0 || testHeight <= 0) {
                LOGW("[surface] ZERO_SIZE_TIMEOUT token=%llu, awaiting a new native window callback",
                     static_cast<unsigned long long>(sessionToken));
                stopReason = "parent zero-size timeout";
                break;
            }
            LOGI("[surface] RESUMED token=%llu width=%d height=%d",
                 static_cast<unsigned long long>(sessionToken), testWidth, testHeight);
            continue;
        }
'''
s=s[:start]+new_runtime+s[stop:]
anchor='''    VulkanState.ScreenHeight = static_cast<float>(height);'''
assert anchor in s
s=s.replace(anchor,anchor+'''
    const int nativeFormat = ANativeWindow_getFormat(gameWindow);
    LOGI("[surface] native_window_pixel_format=%d", nativeFormat);
''',1)

# Visual calibration: top-left vs bottom corner labels, and a crosshair
# following ImGui's pointer. Helps discriminate render rotation/mirroring
# from input-space offsets without guessing translation constants.
render_needle='''        BeginDraw();
        ImGui::Render();'''
assert render_needle in s
visual='''        BeginDraw();
#ifndef YS_ENABLE_TOUCH_CALIBRATION
#define YS_ENABLE_TOUCH_CALIBRATION 1
#endif
#if YS_ENABLE_TOUCH_CALIBRATION
        {
            ImGuiIO& debugIo = ImGui::GetIO();
            ImDrawList* fg = ImGui::GetForegroundDrawList();
            const ImVec2 view = debugIo.DisplaySize;
            const ImU32 mark = IM_COL32(255, 220, 60, 255);
            fg->AddText(ImVec2(24.0f, 24.0f), mark, "YS TOP-LEFT");
            fg->AddText(ImVec2(std::max(24.0f, view.x - 200.0f), 24.0f), mark, "YS TOP-RIGHT");
            fg->AddText(ImVec2(24.0f, std::max(24.0f, view.y - 45.0f)), mark, "YS BOTTOM-LEFT");
            const ImVec2 mouse = debugIo.MousePos;
            if (std::isfinite(mouse.x) && std::isfinite(mouse.y) &&
                mouse.x >= 0 && mouse.y >= 0 &&
                mouse.x < view.x && mouse.y < view.y) {
                const ImU32 red = IM_COL32(255, 80, 70, 255);
                fg->AddCircle(mouse, 22.0f, red, 32, 3.0f);
                fg->AddLine(ImVec2(mouse.x - 32, mouse.y),
                            ImVec2(mouse.x + 32, mouse.y), red, 2.0f);
                fg->AddLine(ImVec2(mouse.x, mouse.y - 32),
                            ImVec2(mouse.x, mouse.y + 32), red, 2.0f);
            }
        }
#endif
        ImGui::Render();'''
s=s.replace(render_needle,visual,1)
assert '#include <cmath>' not in s
s=s.replace('#include <atomic>\n','#include <atomic>\n#include <cmath>\n',1)
nw.write_text(s,encoding="utf-8")

# Multiple MotionEvent::copyFrom invocations were observed for one DOWN.
# Deduplicate using Android's original event timestamp, action and complete
# pointer positions. A fixed-size mutex-protected ring avoids allocating
# on the input dispatch thread; no ImGui calls occur inside the hook.
include='#include <bit>\n#include <array>\n#include <mutex>\n#include <cstdint>\n'
assert '#include <android/input.h>' in inp
inp=inp.replace('#include <android/input.h>\n','#include <android/input.h>\n'+include,1)
key_code=r'''
namespace overlay_input {
struct EventIdentity {
    std::int64_t downTime = 0;
    std::int64_t eventTime = 0;
    std::uint64_t pointerHash = 0;
    std::int32_t fullAction = 0;
    std::uint32_t pointerCount = 0;
    bool operator==(const EventIdentity&) const = default;
};
class EventDeduplicator {
public:
    bool isDuplicate(const EventIdentity& identity) {
        if (identity.eventTime <= 0) return false;
        std::lock_guard<std::mutex> lock(mutex_);
        for (std::size_t i = 0; i < valid_; ++i)
            if (history_[i] == identity) return true;
        history_[next_] = identity;
        next_ = (next_ + 1) % history_.size();
        if (valid_ < history_.size()) ++valid_;
        return false;
    }
private:
    std::mutex mutex_;
    std::array<EventIdentity, 128> history_{};
    std::size_t next_ = 0;
    std::size_t valid_ = 0;
};
inline EventDeduplicator& eventDeduplicator() {
    static EventDeduplicator cache;
    return cache;
}
} // namespace overlay_input

'''
needle="// android::MotionEvent::copyFrom"
assert needle in inp
inp=inp.replace(needle,key_code+needle,1)
# v3 logs pointer0 inside its points capture loop. Remove those logs
# so all printed coordinates correspond to actionIndex and changedPointer.
pos=inp.index('            if (i == 0 && (motion.action == AMOTION_EVENT_ACTION_DOWN ||')
end=inp.index('\n            }',pos)+len('\n            }')
old_logs=inp[pos:end]
assert 'LOGI("[touch] action=%d' in old_logs
inp=inp[:pos]+inp[end:]
needle='''        overlay_input::queue().push(motion, generation);
    } catch (...) {'''
assert needle in inp
replace='''        std::uint64_t hash = 1469598103934665603ULL;
        const auto mix = [&hash](std::uint64_t value) {
            hash ^= value; hash *= 1099511628211ULL;
        };
        for (std::size_t i = 0; i < motion.count; ++i) {
            const auto& point = motion.points[i];
            mix(static_cast<std::uint32_t>(point.id));
            mix(std::bit_cast<std::uint32_t>(point.x));
            mix(std::bit_cast<std::uint32_t>(point.y));
        }
        mix(std::bit_cast<std::uint32_t>(motion.wheel_x));
        mix(std::bit_cast<std::uint32_t>(motion.wheel_y));
        const overlay_input::EventIdentity identity{
            AMotionEvent_getDownTime(input),
            AMotionEvent_getEventTime(input),
            hash,
            action,
            static_cast<std::uint32_t>(motion.count)
        };
        if (overlay_input::eventDeduplicator().isDuplicate(identity)) {
            static std::atomic<unsigned> filtered{0};
            const unsigned dropped = filtered.fetch_add(1, std::memory_order_relaxed) + 1;
            if (dropped == 1 || (dropped % 200) == 0)
                LOGI("[touch] dedup dropped=%u last_action=%d event_ns=%lld",
                     dropped, action, static_cast<long long>(identity.eventTime));
            return;
        }
        const auto isPress = motion.action == AMOTION_EVENT_ACTION_DOWN ||
                             motion.action == AMOTION_EVENT_ACTION_POINTER_DOWN;
        if (isPress && motion.index < motion.count) {
            const auto& changed = motion.points[motion.index];
            static std::atomic<unsigned> accepted{0};
            if (accepted.fetch_add(1, std::memory_order_relaxed) < 80) {
                LOGI("[touch] action=%d index=%zu pointer_id=%d count=%zu "
                     "event_ns=%lld changed=(%.1f,%.1f) use_raw=%d",
                     motion.action, motion.index, changed.id, motion.count,
                     static_cast<long long>(identity.eventTime),
                     changed.x, changed.y, YS_USE_RAW_TOUCH_COORDS);
            }
        }
        overlay_input::queue().push(motion, generation);
    } catch (...) {'''
inp=inp.replace(needle,replace,1)
assert 'AMotionEvent_getRawX' in inp
assert 'pointer_id=' in inp
assert 'EventDeduplicator' in inp
ib.write_text(inp,encoding="utf-8")

readme=root/"README_SURFACE_V4.md"
readme.write_text("""# Vulkan-only overlay v4: diagnosis and partial stabilization

Confirmed by the user's October 10 log:
- Session1 and Session2 both render and receive onComplete latch receipts.
- Game still does not show the child SurfaceControl until activity background/foreground.
- In session2, ANativeWindow_getWidth/Height returns -19 (-ENODEV).
  This is a native-window QUERY ERROR, not a temporary negative-size surface.
- One physical down generates about four equivalent InputBridge callbacks.
- Logs for POINTER_DOWN action=5 showed pointer0, while ImGui used actionIndex.

Changes in v4:
1. Stop stale sessions immediately for negative NativeWindow query results;
   allow up to 5 seconds for zero-size transient windows.
2. A fixed-capacity mutex protected EventDeduplicator filters repeated
   MotionEvent::copyFrom captures by timestamp/action/all pointer samples.
3. Pointer-down logs now identify the action index and pointer ID.
4. Optional YS_ENABLE_TOUCH_CALIBRATION=1 draws TOP-LEFT / TOP-RIGHT /
   BOTTOM-LEFT and a red circle/crosshair at ImGui mouse coordinates.
5. Print transformHint. No hardcoded X/Y offset, rotation or flip.
6. Retain Vulkan renderer, AHardwareBuffer, SurfaceControl and ImGui.

The SurfaceControl was created with ASurfaceControl_createFromWindow,
and is a child of the chosen ANativeWindow. Higher unrelated parent
layers may still obscure it. Vulkan rendering success and latch callbacks
do not prove visibility. Correct long-term fix may require replacing this
source-window hook with a controllable root Activity overlay Surface,
rather than any ANativeWindow_fromSurface callback.

Log:
  su -c 'logcat -b all -d -v threadtime -s YS:V > /sdcard/Download/YS-v4.log'
Capture SurfaceFlinger layer tree while in login, gameplay and resumed game:
  su -c 'dumpsys SurfaceFlinger --list > /sdcard/Download/SF-layers.txt'
  su -c 'dumpsys SurfaceFlinger > /sdcard/Download/SF-tree.txt'
  su -c 'dumpsys window windows > /sdcard/Download/WM-windows.txt'

Real game visibility and touch alignment remain UNTESTED.
""",encoding="utf-8")
print("V4_STALE_WINDOW_AND_INPUT_DEDUP_PATCH_APPLIED")
print("NativeWindow.h bytes",len(s),"InputBridge.h bytes",len(inp))
