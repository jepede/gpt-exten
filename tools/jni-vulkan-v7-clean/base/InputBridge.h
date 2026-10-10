#pragma once
#include "MotionQueue.h"
#include "OverlayPolicy.h"
#include "EventDedup.h"
#include <android/input.h>
#include <bit>
#include <array>
#include <mutex>
#include <cstdint>
#include <atomic>
#include "Logger.h"
#include <imgui.h>
#include <cfloat>
#include <cmath>


// android::MotionEvent::copyFrom(const MotionEvent*, bool) returns void.
using MotionCopyFrom = void (*)(void*, const void*, bool);
inline MotionCopyFrom orig_input = nullptr;

inline void hook_input(void* event, const void* source, bool keepHistory) {
    if (!orig_input) return;
    orig_input(event, source, keepHistory); // Always preserve the original operation.
    try {
        const auto generation = overlay_input::queue().capture_generation();
        if (!generation || !event) return;
        const auto* input = static_cast<const AInputEvent*>(event);
        if (AInputEvent_getType(input) != AINPUT_EVENT_TYPE_MOTION) return;
        overlay_input::Motion motion;
        const int action = AMotionEvent_getAction(input);
        motion.action = action & AMOTION_EVENT_ACTION_MASK;
        motion.index = (action & AMOTION_EVENT_ACTION_POINTER_INDEX_MASK)
                     >> AMOTION_EVENT_ACTION_POINTER_INDEX_SHIFT;
        if (motion.action == AMOTION_EVENT_ACTION_CANCEL) {
            overlay_input::queue().push(motion, generation); return;
        }
        motion.count = AMotionEvent_getPointerCount(input);
        if (!motion.count || motion.count > motion.points.size() || motion.index >= motion.count) return;
        motion.buttons = AMotionEvent_getButtonState(input);
        for (std::size_t i = 0; i < motion.count; ++i) {
            auto& p = motion.points[i];
            p.id = AMotionEvent_getPointerId(input, i);
            p.tool = AMotionEvent_getToolType(input, i);
            const float localX = AMotionEvent_getX(input, i);
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

            if (!std::isfinite(p.x) || !std::isfinite(p.y)) return;
        }
        if (motion.action == AMOTION_EVENT_ACTION_SCROLL) {
            motion.wheel_x = AMotionEvent_getAxisValue(input, AMOTION_EVENT_AXIS_HSCROLL, motion.index);
            motion.wheel_y = AMotionEvent_getAxisValue(input, AMOTION_EVENT_AXIS_VSCROLL, motion.index);
            if (!std::isfinite(motion.wheel_x) || !std::isfinite(motion.wheel_y)) return;
        }
        std::uint64_t hash = 1469598103934665603ULL;
        const auto mix = [&hash](std::uint64_t value) {
            hash ^= value; hash *= 1099511628211ULL;
        };
        for (std::size_t i = 0; i < motion.count; ++i) {
            const auto& point = motion.points[i];
            mix(static_cast<std::uint32_t>(point.id));
            mix(static_cast<std::uint32_t>(point.tool));
        }
        const overlay_input::EventIdentity identity{
            AMotionEvent_getDownTime(input),
            AMotionEvent_getEventTime(input),
            hash,
            action,
            AInputEvent_getDeviceId(input),
            AInputEvent_getSource(input),
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
    } catch (...) {
        // Do not let a C++ exception cross a platform callback boundary.
    }
}

// This is the only input function allowed to touch ImGui: render thread only.
inline void DrainOverlayInput() {
    if (!ImGui::GetCurrentContext()) return;
    auto batch = overlay_input::queue().drain();
    ImGuiIO& io = ImGui::GetIO();
    static thread_local int active_pointer = -1;
    auto release_buttons = [&] {
        for (int b = 0; b < 3; ++b) io.AddMouseButtonEvent(b, false);
        active_pointer = -1;
    };
    if (batch.reset) release_buttons();
    for (std::size_t n = 0; n < batch.count; ++n) {
        const auto& m = batch.events[n];
        if (m.action == AMOTION_EVENT_ACTION_CANCEL) {
            release_buttons(); io.AddMousePosEvent(-FLT_MAX, -FLT_MAX); continue;
        }
        if (!m.count || m.index >= m.count) continue;
        const auto& changed = m.points[m.index];
        const auto flip = ys_overlay::configuredFlip().load(std::memory_order_acquire);
        const auto transform = [&](float x, float y) {
            // Screen-space touch must be remapped through the same translation
            // and flipping used for the buffer's SurfaceControl transaction.
            const int offsetX = ys_overlay::configuredOffsetX().load(std::memory_order_acquire);
            const int offsetY = ys_overlay::configuredOffsetY().load(std::memory_order_acquire);
            return ys_overlay::screenToImage(x-offsetX,y-offsetY,
                                              io.DisplaySize.x,io.DisplaySize.y,flip);
        };
        const auto mousePos = [&](float x, float y) {
            const auto p = transform(x,y);
            io.AddMousePosEvent(p.x,p.y);
        };
        if (m.action == AMOTION_EVENT_ACTION_DOWN ||
            m.action == AMOTION_EVENT_ACTION_POINTER_DOWN) {
            static thread_local unsigned drainLogs = 0;
            if (drainLogs++ < 80) {
                const auto point = transform(changed.x,changed.y);
                LOGI("[touch] imgui=(%.1f,%.1f) input=(%.1f,%.1f) viewport=(%.1f,%.1f) flip=%d mode=%s",
                     point.x, point.y, changed.x, changed.y,
                     io.DisplaySize.x, io.DisplaySize.y, flip,
                     YS_USE_RAW_TOUCH_COORDS ? "RAW" : "LOCAL");
            }
        }
        const auto source = changed.tool == AMOTION_EVENT_TOOL_TYPE_MOUSE ? ImGuiMouseSource_Mouse
                          : (changed.tool == AMOTION_EVENT_TOOL_TYPE_STYLUS || changed.tool == AMOTION_EVENT_TOOL_TYPE_ERASER)
                          ? ImGuiMouseSource_Pen : ImGuiMouseSource_TouchScreen;
        io.AddMouseSourceEvent(source);
        const bool mouse = source == ImGuiMouseSource_Mouse;
        switch (m.action) {
        case AMOTION_EVENT_ACTION_DOWN:
            active_pointer = changed.id;
            mousePos(changed.x, changed.y);
            if (mouse) {
                io.AddMouseButtonEvent(0, (m.buttons & AMOTION_EVENT_BUTTON_PRIMARY) != 0);
                io.AddMouseButtonEvent(1, (m.buttons & AMOTION_EVENT_BUTTON_SECONDARY) != 0);
                io.AddMouseButtonEvent(2, (m.buttons & AMOTION_EVENT_BUTTON_TERTIARY) != 0);
            } else io.AddMouseButtonEvent(0, true);
            break;
        case AMOTION_EVENT_ACTION_POINTER_DOWN:
            // Secondary fingers do not displace the primary drag pointer.
            if (active_pointer < 0 && !mouse) {
                active_pointer = changed.id;
                mousePos(changed.x, changed.y);
                io.AddMouseButtonEvent(0, true);
            }
            break;
        case AMOTION_EVENT_ACTION_UP:
            mousePos(changed.x, changed.y);
            release_buttons();
            break;
        case AMOTION_EVENT_ACTION_POINTER_UP:
            if (changed.id != active_pointer) break;
            // When the active finger lifts but another remains, keep dragging
            // with that finger instead of unexpectedly releasing ImGui.
            for (std::size_t i = 0; i < m.count; ++i) {
                if (i == m.index) continue;
                active_pointer = m.points[i].id;
                mousePos(m.points[i].x, m.points[i].y);
                io.AddMouseButtonEvent(0, true);
                break;
            }
            if (m.count <= 1) release_buttons();
            break;
        case AMOTION_EVENT_ACTION_MOVE:
            if (mouse) {
                mousePos(m.points[0].x, m.points[0].y);
            } else {
                bool matched = false;
                for (std::size_t i = 0; i < m.count; ++i) {
                    if (m.points[i].id == active_pointer) {
                        mousePos(m.points[i].x, m.points[i].y);
                        matched = true;
                        break;
                    }
                }
                if (!matched && m.count>0) {
                    active_pointer=m.points[0].id;
                    mousePos(m.points[0].x,m.points[0].y);
                }
            }
            break;
        case AMOTION_EVENT_ACTION_HOVER_ENTER:
        case AMOTION_EVENT_ACTION_HOVER_MOVE:
            mousePos(changed.x, changed.y); break;
        case AMOTION_EVENT_ACTION_HOVER_EXIT:
            if (active_pointer < 0) io.AddMousePosEvent(-FLT_MAX, -FLT_MAX);
            break;
        case AMOTION_EVENT_ACTION_BUTTON_PRESS:
        case AMOTION_EVENT_ACTION_BUTTON_RELEASE:
            mousePos(changed.x, changed.y);
            io.AddMouseButtonEvent(0, (m.buttons & AMOTION_EVENT_BUTTON_PRIMARY) != 0);
            io.AddMouseButtonEvent(1, (m.buttons & AMOTION_EVENT_BUTTON_SECONDARY) != 0);
            io.AddMouseButtonEvent(2, (m.buttons & AMOTION_EVENT_BUTTON_TERTIARY) != 0);
            break;
        case AMOTION_EVENT_ACTION_SCROLL:
            io.AddMouseWheelEvent(m.wheel_x, m.wheel_y); break;
        default: break;
        }
    }
}
