#!/usr/bin/env python3
"""Apply the tombstone_07 ImGui input fix to the supplied original jni.zip.
No dependency downloads, font redistribution, application injection, or device access.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import pathlib
import re
import shutil
import subprocess
import tempfile
import zipfile

QUEUE = r'''#pragma once
#include <array>
#include <cstddef>
#include <cstdint>
#include <mutex>

namespace overlay_input {
struct Point { int id = -1; int tool = 0; float x = 0; float y = 0; };
struct Motion {
    int action = 3;
    std::size_t count = 0;
    std::size_t index = 0;
    int buttons = 0;
    float wheel_x = 0, wheel_y = 0;
    std::array<Point, 32> points{};
};

// Copies values only; never retains Android event pointers or calls ImGui.
// enable()/disable() are called on the render thread, not in the input callback.
template<std::size_t Capacity = 128> class Queue {
    static_assert(Capacity > 0);
public:
    struct Batch {
        std::array<Motion, Capacity> events{};
        std::size_t count = 0;
        bool reset = false;
    };
    void enable() {
        std::lock_guard<std::mutex> lock(mutex_);
        ++generation_; if (generation_ == 0) ++generation_;
        enabled_ = true; head_ = count_ = 0; reset_ = true;
    }
    void disable() {
        std::lock_guard<std::mutex> lock(mutex_);
        enabled_ = false; head_ = count_ = 0; reset_ = false;
    }
    std::uint64_t capture_generation() {
        std::lock_guard<std::mutex> lock(mutex_);
        return enabled_ ? generation_ : 0;
    }
    bool push(const Motion& value, std::uint64_t generation) {
        std::lock_guard<std::mutex> lock(mutex_);
        if (!enabled_ || generation == 0 || generation != generation_) return false;
        if (value.count > value.points.size()) return false;
        if (value.action != 3 && (value.count == 0 || value.index >= value.count)) return false;
        // Losing transitions must never leave a mouse button stuck down.
        if (count_ == Capacity) { head_ = count_ = 0; reset_ = true; }
        events_[(head_ + count_) % Capacity] = value;
        ++count_; return true;
    }
    Batch drain() {
        std::lock_guard<std::mutex> lock(mutex_);
        Batch result;
        if (!enabled_) return result;
        result.reset = reset_; result.count = count_;
        for (std::size_t i = 0; i < count_; ++i)
            result.events[i] = events_[(head_ + i) % Capacity];
        head_ = count_ = 0; reset_ = false;
        return result;
    }
private:
    std::mutex mutex_;
    std::array<Motion, Capacity> events_{};
    std::size_t head_ = 0, count_ = 0;
    std::uint64_t generation_ = 0;
    bool enabled_ = false, reset_ = false;
};
inline Queue<>& queue() { static Queue<> q; return q; }
struct SessionInputGuard {
    ~SessionInputGuard() { queue().disable(); }
};
} // namespace overlay_input
'''

BRIDGE = r'''#pragma once
#include "MotionQueue.h"
#include <android/input.h>
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
            p.x = AMotionEvent_getX(input, i);
            p.y = AMotionEvent_getY(input, i);
            if (!std::isfinite(p.x) || !std::isfinite(p.y)) return;
        }
        if (motion.action == AMOTION_EVENT_ACTION_SCROLL) {
            motion.wheel_x = AMotionEvent_getAxisValue(input, AMOTION_EVENT_AXIS_HSCROLL, motion.index);
            motion.wheel_y = AMotionEvent_getAxisValue(input, AMOTION_EVENT_AXIS_VSCROLL, motion.index);
            if (!std::isfinite(motion.wheel_x) || !std::isfinite(motion.wheel_y)) return;
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
        const auto source = changed.tool == AMOTION_EVENT_TOOL_TYPE_MOUSE ? ImGuiMouseSource_Mouse
                          : (changed.tool == AMOTION_EVENT_TOOL_TYPE_STYLUS || changed.tool == AMOTION_EVENT_TOOL_TYPE_ERASER)
                          ? ImGuiMouseSource_Pen : ImGuiMouseSource_TouchScreen;
        io.AddMouseSourceEvent(source);
        const bool mouse = source == ImGuiMouseSource_Mouse;
        switch (m.action) {
        case AMOTION_EVENT_ACTION_DOWN:
            active_pointer = changed.id;
            io.AddMousePosEvent(changed.x, changed.y);
            if (mouse) {
                io.AddMouseButtonEvent(0, (m.buttons & AMOTION_EVENT_BUTTON_PRIMARY) != 0);
                io.AddMouseButtonEvent(1, (m.buttons & AMOTION_EVENT_BUTTON_SECONDARY) != 0);
                io.AddMouseButtonEvent(2, (m.buttons & AMOTION_EVENT_BUTTON_TERTIARY) != 0);
            } else io.AddMouseButtonEvent(0, true);
            break;
        case AMOTION_EVENT_ACTION_POINTER_DOWN:
            // A secondary finger must not steal an existing drag.
            break;
        case AMOTION_EVENT_ACTION_UP:
        case AMOTION_EVENT_ACTION_POINTER_UP:
            if (changed.id == active_pointer || m.action == AMOTION_EVENT_ACTION_UP) {
                io.AddMousePosEvent(changed.x, changed.y); release_buttons();
            }
            break;
        case AMOTION_EVENT_ACTION_MOVE:
            if (mouse) io.AddMousePosEvent(m.points[0].x, m.points[0].y);
            else for (std::size_t i = 0; i < m.count; ++i)
                if (m.points[i].id == active_pointer) {
                    io.AddMousePosEvent(m.points[i].x, m.points[i].y); break;
                }
            break;
        case AMOTION_EVENT_ACTION_HOVER_ENTER:
        case AMOTION_EVENT_ACTION_HOVER_MOVE:
            io.AddMousePosEvent(changed.x, changed.y); break;
        case AMOTION_EVENT_ACTION_HOVER_EXIT:
            if (active_pointer < 0) io.AddMousePosEvent(-FLT_MAX, -FLT_MAX);
            break;
        case AMOTION_EVENT_ACTION_BUTTON_PRESS:
        case AMOTION_EVENT_ACTION_BUTTON_RELEASE:
            io.AddMousePosEvent(changed.x, changed.y);
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
'''

OPENGL = r'''#pragma once
#include <EGL/egl.h>
#include <GLES3/gl3.h>
#include <imconfig.h>
#include <imgui.h>
#include <imgui_internal.h>
#include <imgui_impl_opengl3.h>
#include <imgui_impl_android.h>
#include <font_zt.h> // Reuse the original user-provided asset; not supplied by this repair kit.
#include "InputBridge.h"
struct OpenGLState {
    float ScreenWidth = 0, ScreenHeight = 0;
    bool InitOpenGL = false; // Render-thread only.
};
inline OpenGLState OpenGL;
inline bool LoadFont(float size_pixels) {
    if (!ImGui::GetCurrentContext() || !(size_pixels > 0)) return false;
    ImGuiIO& io = ImGui::GetIO();
    ImFontConfig config;
    config.FontDataOwnedByAtlas = false;
    config.SizePixels = size_pixels;
    config.OversampleH = 1;
    ImFont* font = io.Fonts->AddFontFromMemoryTTF(
        (void*)Font, Font_len, size_pixels, &config, io.Fonts->GetGlyphRangesChineseFull());
    if (!font) return io.Fonts->AddFontDefault() != nullptr;
    io.FontDefault = font;
    return true;
}
'''

HOOKS = r'''inline std::atomic<bool>& OverlayRunning() {
    static std::atomic<bool> running{false};
    return running;
}
ANativeWindow* (*orig_ANativeWindow_fromSurface)(JNIEnv*, jobject) = nullptr;
ANativeWindow* Hook_ANativeWindow_fromSurface(JNIEnv* env, jobject surface) {
    if (!orig_ANativeWindow_fromSurface) return nullptr;
    ANativeWindow* win = orig_ANativeWindow_fromSurface(env, surface);
    if (!win) return win;
    bool expected = false;
    if (OverlayRunning().compare_exchange_strong(expected, true)) {
        ANativeWindow_acquire(win); // Independent reference for the worker.
        try {
            std::thread([win] {
                struct ResetRunning { ~ResetRunning() { OverlayRunning().store(false); } } reset;
                try { RunSurfaceControlOverlay(win); }
                catch (const std::exception& e) { LOGE("overlay worker failed: %s", e.what()); }
                catch (...) { LOGE("overlay worker failed: unknown exception"); }
            }).detach();
        } catch (const std::exception& e) {
            ANativeWindow_release(win);
            OverlayRunning().store(false);
            LOGE("cannot start overlay thread: %s", e.what());
        } catch (...) {
            ANativeWindow_release(win); OverlayRunning().store(false);
            LOGE("cannot start overlay thread");
        }
    }
    return win; // The caller still owns its original reference.
}

void hack_main() noexcept {
    void* window_symbol = DobbySymbolResolver("libandroid.so", "ANativeWindow_fromSurface");
    if (!window_symbol) { LOGE("ANativeWindow_fromSurface was not found"); return; }
    const int window_rc = DobbyHook(window_symbol, (void*)Hook_ANativeWindow_fromSurface,
                                   (void**)&orig_ANativeWindow_fromSurface);
    if (window_rc != 0 || !orig_ANativeWindow_fromSurface) {
        LOGE("window callback installation failed: %d", window_rc); return;
    }
    void* input_symbol = DobbySymbolResolver("libinput.so", "_ZN7android11MotionEvent8copyFromEPKS0_b");
    if (!input_symbol) { LOGW("private MotionEvent symbol is unavailable; input disabled"); return; }
    const int input_rc = DobbyHook(input_symbol, (void*)hook_input, (void**)&orig_input);
    if (input_rc != 0 || !orig_input) LOGE("input callback installation failed: %d", input_rc);
}
'''

TEST = r'''#include "MotionQueue.h"
#include <cassert>
#include <atomic>
#include <iostream>
#include <thread>
#include <vector>
using overlay_input::Motion;
using overlay_input::Queue;
Motion event(int x) { Motion m; m.action=2; m.count=1; m.points[0].id=x; return m; }
int main() {
    Queue<8> q;
    assert(q.capture_generation()==0);
    assert(!q.push(event(1), 0));
    assert(q.drain().count==0);
    std::cout << "PASS disabled-before-init\n";
    q.enable(); auto g=q.capture_generation();
    auto m=event(7); assert(q.push(m,g)); m.points[0].id=999;
    auto b=q.drain(); assert(b.count==1 && b.events[0].points[0].id==7 && b.reset);
    std::cout << "PASS snapshot-ownership\n";
    assert(q.drain().count==0);
    for(int i=0;i<8;i++) assert(q.push(event(i),g));
    b=q.drain(); assert(b.count==8);
    for(int i=0;i<8;i++) assert(b.events[i].points[0].id==i);
    std::cout << "PASS fifo\n";
    for(int i=0;i<9;i++) assert(q.push(event(i),g));
    b=q.drain(); assert(b.count==1 && b.reset && b.events[0].points[0].id==8);
    std::cout << "PASS overflow-reset\n";
    auto invalid=event(0); invalid.count=33; assert(!q.push(invalid,g));
    invalid.count=1; invalid.index=1; assert(!q.push(invalid,g));
    invalid.count=0; invalid.index=0; assert(!q.push(invalid,g));
    invalid.action=3; assert(q.push(invalid,g));
    std::cout << "PASS invalid-pointer-bounds-and-cancel\n";
    q.disable(); assert(!q.push(event(3),g)); assert(q.drain().count==0);
    q.enable(); auto new_g=q.capture_generation(); assert(new_g!=g);
    assert(!q.push(event(4),g)); assert(q.push(event(5),new_g));
    std::cout << "PASS lifecycle-generation\n";
    Queue<128> shared; shared.enable(); auto epoch=shared.capture_generation();
    std::atomic<int> live{4}; std::vector<std::thread> threads;
    for(int t=0;t<4;t++) threads.emplace_back([&,t] {
        for(int i=0;i<20000;i++) assert(shared.push(event(t*20000+i),epoch));
        --live;
    });
    while(live.load()) { auto batch=shared.drain(); assert(batch.count<=128); }
    for(auto& t:threads) t.join();
    shared.disable(); assert(shared.drain().count==0);
    std::cout << "PASS 80000-events-four-producers\n";
}
'''

README = '''# tombstone_07 修复工具包

本包不是已编译、已在手机验证的完整工程。它包含修复源码、可重复测试和一键重打包脚本。
将原始 jni.zip 放在脚本旁边，执行：

    python3 jni_tombstone07_fix.py jni.zip -o jni_fixed_full.zip

也支持指定绝对路径。脚本不联网，不覆盖原始压缩包；原有静态库和用户自带字体在本机原样保留，
不会被替换成其他版本。包内 PATCH_REPORT.json 列出修改与输入哈希；SHA256SUMS.txt 记录输出文件哈希。
脚本要求原项目特征匹配；遇到不同版本会中止，而不会悄悄部分打补丁。

## 已确认的直接原因
原始库中的 ImGui::GetIO() 返回 GImGui + 0x28；AddMouseSourceEvent 的首条指令是
ldr x8, [x0, #0xd0]。tombstone 的 x0=0x28、fault addr=0xf8，故 0x28+0xd0=0xf8。
输入回调在 ImGui 上下文尚不存在时进入后端，是这次故障的直接解释。
同时，回调线程直接调用 ImGui 与绘制线程并发访问全局上下文，不能只增加一次判空。

## 修复内容
- 输入线程仅复制事件数据到有界队列，不保存 AInputEvent 指针，不访问 ImGui。
- 绘制线程初始化完成后开放队列，每帧在 NewFrame 前消费。
- 队列溢出清理按键状态；关闭、重启使用 generation 拒绝过期事件。
- 修正 copyFrom 回调为 void(void*, const void*, bool)。
- 工作线程独立 acquire/release ANativeWindow，并使用原子启动标志。
- 正常退出关闭 ImGui 后端和上下文，异常退出至少关闭输入队列。
- GPU 写入硬件缓冲区补 GPU_COLOR_OUTPUT，提交前等待 GPU 完成。
- CPU 回读明确绑定源 FBO；修正 setCrop 参数形式、屏幕尺寸和 DeltaTime 下限。
- 记录回调安装失败，不盲调未解析的函数指针。

## 证据与验证边界
宿主机测试只覆盖有界队列、生命周期与并发，不代替 Android 渲染验证。
没有原始已链接 libAndroid.so，因此不能对历史三个 PC 全部作完整符号化；
核心故障函数由 tombstone 指令字节与原始 libimgui.a 的一致性识别。
保留的私有 MotionEvent 符号不是稳定 NDK API，不保证所有 Android/OEM 版本可用。
此补丁不改动应用注入方式、游戏逻辑、权限、反检测或校验；输入仍转发原函数，不吞掉应用触摸。
渲染路径、窗口重建、旋转、SurfaceFlinger 呈现与设备 GPU 仍需要真机回归。
原工程的每帧 AHardwareBuffer 分配、无 release-fence 的缓冲池优化未在本补丁中实现。

## 建议验证
冷启动时连续触摸；菜单按下/拖动/抬起；多指操作与 ACTION_CANCEL；
切后台/返回、旋转与窗口重建；EGL/AHardwareBuffer 失败分支；确认没有 stuck button。
使用 ndk-build NDK_PROJECT_PATH=. APP_BUILD_SCRIPT=jni/Android.mk NDK_APPLICATION_MK=jni/Application.mk
编译，保留 obj/local/arm64-v8a/libAndroid.so 用于后续符号化。

## 参考
https://raw.githubusercontent.com/ocornut/imgui/master/imgui.cpp
https://android.googlesource.com/platform/frameworks/native/+/master/libs/input/Input.cpp
https://developer.android.com/ndk/reference/group/native-activity
https://developer.android.com/ndk/reference/group/a-hardware-buffer
'''


def once(text: str, old: str, new: str, name: str) -> str:
    count = text.count(old)
    if count != 1:
        raise ValueError(f'{name}: expected one exact source anchor, found {count}; original left unchanged')
    return text.replace(old, new, 1)


def patch_native(text: str) -> str:
    text = text.replace('\r\n', '\n')
    text = '#pragma once\n#include <atomic>\n#include <algorithm>\n#include <exception>\n#include <android/hardware_buffer.h>\n' + text
    text = once(text, 'if (!gameWindow) return;', '''if (!gameWindow) return;
    const auto releaseWindow = [](ANativeWindow* p) { ANativeWindow_release(p); };
    std::unique_ptr<ANativeWindow, decltype(releaseWindow)> ownedWindow(gameWindow, releaseWindow);
    overlay_input::SessionInputGuard inputGuard;''', 'worker window ownership')
    # The RAII object above owns the independently acquired worker reference.
    text = text.replace('ANativeWindow_release(gameWindow);', '')
    text = once(text, 'int glHeight = ANativeWindow_getHeight(gameWindow);', '''int glHeight = ANativeWindow_getHeight(gameWindow);
    if (glWidth <= 0 || glHeight <= 0) return;
    OpenGL.ScreenWidth = static_cast<float>(glWidth);
    OpenGL.ScreenHeight = static_cast<float>(glHeight);''', 'initial dimensions')
    text = once(text, 'ASurfaceTransaction_setCrop(tx, overlayControl, {0, 0, glWidth, glHeight});', '''const ARect crop{0, 0, glWidth, glHeight};
    ASurfaceTransaction_setCrop(tx, overlayControl, &crop);''', 'crop ABI')
    text = once(text, 'ImGuiIO& io = ImGui::GetIO();', '''ImGuiIO& io = ImGui::GetIO();
    overlay_input::queue().enable();''', 'input ready point')
    text = once(text, 'io.DeltaTime = std::chrono::duration<float>(now - last_time).count();',
                'io.DeltaTime = std::clamp(std::chrono::duration<float>(now - last_time).count(), 0.000001f, 0.1f);', 'positive delta time')
    text = once(text, 'ImGui::NewFrame();', 'DrainOverlayInput();\n        ImGui::NewFrame();', 'render-thread queue consumption')
    text = once(text, '.usage = AHARDWAREBUFFER_USAGE_GPU_SAMPLED_IMAGE | AHARDWAREBUFFER_USAGE_CPU_WRITE_RARELY',
                '.usage = AHARDWAREBUFFER_USAGE_GPU_SAMPLED_IMAGE | AHARDWAREBUFFER_USAGE_GPU_COLOR_OUTPUT | AHARDWAREBUFFER_USAGE_CPU_WRITE_RARELY', 'GPU write usage')
    text = once(text, 'glDeleteFramebuffers(1, &tempFbo);', '''// setBuffer(..., -1) is safe only after GPU writes have completed.
                        glFinish();
                        glDeleteFramebuffers(1, &tempFbo);''', 'GPU completion')
    text = once(text, 'glReadPixels(0, 0, glWidth, glHeight, GL_RGBA, GL_UNSIGNED_BYTE, pixels.data());', '''glBindFramebuffer(GL_READ_FRAMEBUFFER, fbo);
                glReadPixels(0, 0, glWidth, glHeight, GL_RGBA, GL_UNSIGNED_BYTE, pixels.data());''', 'CPU read framebuffer')
    text = once(text, 'glDeleteTextures(1, &texture);', '''overlay_input::queue().disable();
    if (OpenGL.InitOpenGL && ImGui::GetCurrentContext()) {
        ImGui_ImplOpenGL3_Shutdown();
        ImGui_ImplAndroid_Shutdown();
        ImGui::DestroyContext();
    }
    OpenGL.InitOpenGL = false;
    glDeleteTextures(1, &texture);''', 'normal context teardown')
    marker = 'ANativeWindow* (*orig_ANativeWindow_fromSurface)'
    if text.count(marker) != 1:
        raise ValueError('window callback section does not match original')
    text = text[:text.index(marker)] + HOOKS
    return text


def apply(source: pathlib.Path, output: pathlib.Path) -> None:
    if source.resolve() == output.resolve():
        raise ValueError('input and output must be different files')
    if output.exists():
        raise FileExistsError(f'output already exists: {output}')
    with zipfile.ZipFile(source) as zin:
        names = zin.namelist()
        if len(names) != len(set(names)):
            raise ValueError('duplicate entries in input ZIP')
        for info in zin.infolist():
            p = pathlib.PurePosixPath(info.filename)
            if p.is_absolute() or '..' in p.parts or '\\' in info.filename:
                raise ValueError('unsafe input ZIP path')
            if (info.external_attr >> 16) & 0o170000 == 0o120000:
                raise ValueError('symlink entries are not accepted')
        required = ['jni/NativeWindow.h', 'jni/Library/Imgui/include/OpenGL.h', 'jni/Injector.cpp', 'jni/Android.mk']
        for name in required:
            if name not in names:
                raise ValueError(f'missing required entry: {name}')
        replacements = {
            'jni/NativeWindow.h': patch_native(zin.read('jni/NativeWindow.h').decode('utf-8')).encode(),
            'jni/Library/Imgui/include/OpenGL.h': OPENGL.encode(),
            'jni/MotionQueue.h': QUEUE.encode(),
            'jni/InputBridge.h': BRIDGE.encode(),
        }
        mk = zin.read('jni/Android.mk').decode().replace('\r\n', '\n')
        mk = once(mk, 'BUILD_MODE := debug', 'BUILD_MODE ?= debug', 'build mode override')
        mk = once(mk, 'LOCAL_LDLIBS := -llog -landroid -lEGL -lGLESv3 -lGLESv2 -lGLESv1_CM',
                  'LOCAL_LDLIBS := -llog -landroid -lEGL -lGLESv3 -lGLESv2 -lGLESv1_CM -ldl\nLOCAL_LDFLAGS += -Wl,--exclude-libs,ALL', 'local static symbols')
        replacements['jni/Android.mk'] = mk.encode()
        injector = zin.read('jni/Injector.cpp').decode().replace('\r\n', '\n')
        injector = re.sub(r'void lib_main\(\)\s*\{[\s\S]*', '''void lib_main() {
    try { std::thread([] { hack_main(); }).detach(); }
    catch (const std::exception& e) { LOGE("startup thread failed: %s", e.what()); }
    catch (...) { LOGE("startup thread failed"); }
}
''', injector, count=1)
        replacements['jni/Injector.cpp'] = injector.encode()
        replacements['REPAIR_README.md'] = README.encode()
        replacements['tests/MotionQueue.h'] = QUEUE.encode()
        replacements['tests/test_motion_queue.cpp'] = TEST.encode()
        replacements['PATCH_REPORT.json'] = json.dumps({
            'input_name': source.name,
            'input_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
            'modified_or_added': sorted(replacements),
            'android_build_verified': False,
            'device_runtime_verified': False,
            'scope': 'targeted ImGui initialization/concurrency crash repair; not a full rendering rewrite',
        }, ensure_ascii=False, indent=2).encode()
        output.parent.mkdir(parents=True, exist_ok=True)
        temporary = output.with_suffix(output.suffix + '.tmp')
        hashes = []
        try:
            with zipfile.ZipFile(temporary, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zout:
                for info in zin.infolist():
                    if info.filename in replacements or info.filename == 'SHA256SUMS.txt': continue
                    data = zin.read(info.filename)
                    zout.writestr(info, data)
                    if not info.is_dir(): hashes.append((info.filename, hashlib.sha256(data).hexdigest()))
                for name, data in sorted(replacements.items()):
                    zout.writestr(name, data)
                    hashes.append((name, hashlib.sha256(data).hexdigest()))
                zout.writestr('SHA256SUMS.txt', ''.join(f'{sha}  {name}\n' for name,sha in sorted(hashes)))
            with zipfile.ZipFile(temporary) as check:
                bad = check.testzip()
                if bad: raise ValueError(f'ZIP CRC failed: {bad}')
            temporary.replace(output)
        except BaseException:
            temporary.unlink(missing_ok=True)
            raise
    print(f'Created: {output}')
    print(f'SHA256: {hashlib.sha256(output.read_bytes()).hexdigest()}')


def self_test(directory: pathlib.Path) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    (directory/'MotionQueue.h').write_text(QUEUE)
    (directory/'test_motion_queue.cpp').write_text(TEST)
    compiler = shutil.which('g++')
    if not compiler: raise RuntimeError('g++ is required for the host regression test')
    binary = directory/'test_motion_queue'
    subprocess.run([compiler, '-std=c++20', '-O1', '-g', '-Wall', '-Wextra', '-Werror',
                    '-fsanitize=address,undefined', '-fno-omit-frame-pointer', '-pthread',
                    str(directory/'test_motion_queue.cpp'), '-o', str(binary)], check=True)
    subprocess.run([str(binary)], check=True)
    # Exercise exact source substitutions and preservation of opaque original assets.
    fixture = '''#include <OpenGL.h>
if (!gameWindow) return;
int glHeight = ANativeWindow_getHeight(gameWindow);
ANativeWindow_release(gameWindow);
ASurfaceTransaction_setCrop(tx, overlayControl, {0, 0, glWidth, glHeight});
ImGuiIO& io = ImGui::GetIO();
io.DeltaTime = std::chrono::duration<float>(now - last_time).count();
ImGui::NewFrame();
.usage = AHARDWAREBUFFER_USAGE_GPU_SAMPLED_IMAGE | AHARDWAREBUFFER_USAGE_CPU_WRITE_RARELY
glDeleteFramebuffers(1, &tempFbo);
glReadPixels(0, 0, glWidth, glHeight, GL_RGBA, GL_UNSIGNED_BYTE, pixels.data());
glDeleteTextures(1, &texture);
ANativeWindow* (*orig_ANativeWindow_fromSurface)(JNIEnv* env, jobject surface);
'''
    source=directory/'fixture.zip'; target=directory/'fixture_fixed.zip'
    target.unlink(missing_ok=True)
    with zipfile.ZipFile(source,'w') as z:
        z.writestr('jni/NativeWindow.h',fixture)
        z.writestr('jni/Library/Imgui/include/OpenGL.h','old')
        z.writestr('jni/Injector.cpp','void lib_main() { old(); }')
        z.writestr('jni/Android.mk','BUILD_MODE := debug\nLOCAL_LDLIBS := -llog -landroid -lEGL -lGLESv3 -lGLESv2 -lGLESv1_CM')
        z.writestr('jni/opaque_asset.bin', bytes(range(256)))
    apply(source,target)
    with zipfile.ZipFile(target) as z:
        assert z.read('jni/opaque_asset.bin')==bytes(range(256))
        native=z.read('jni/NativeWindow.h').decode()
        assert 'DrainOverlayInput();' in native
        assert 'ANativeWindow_acquire(win)' in native
        assert 'ANativeWindow_release(gameWindow);' not in native
        assert 'ImGui_ImplAndroid_HandleInputEvent' not in z.read('jni/Library/Imgui/include/OpenGL.h').decode()
    print('PASS repack-preserves-opaque-assets-and-updates-source')
    try: patch_native('unrelated source')
    except ValueError: pass
    else: raise AssertionError('invalid source must be rejected')
    print('PASS mismatched-source-rejected')


def package(output: pathlib.Path) -> None:
    files = {'jni_tombstone07_fix.py': pathlib.Path(__file__).read_bytes(),
             'README.md': README.encode(), 'fixed_sources/MotionQueue.h': QUEUE.encode(),
             'fixed_sources/InputBridge.h': BRIDGE.encode(), 'fixed_sources/OpenGL.h': OPENGL.encode(),
             'tests/MotionQueue.h': QUEUE.encode(), 'tests/test_motion_queue.cpp': TEST.encode()}
    with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for name, value in files.items(): z.writestr(name, value)
        z.writestr('SHA256SUMS.txt', ''.join(f'{hashlib.sha256(value).hexdigest()}  {name}\n' for name,value in sorted(files.items())))
    print(f'Repair kit: {output}; SHA256={hashlib.sha256(output.read_bytes()).hexdigest()}')


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', nargs='?', type=pathlib.Path)
    parser.add_argument('-o','--output', type=pathlib.Path, default=pathlib.Path('jni_fixed_full.zip'))
    parser.add_argument('--self-test', type=pathlib.Path)
    parser.add_argument('--package', type=pathlib.Path)
    args=parser.parse_args()
    try:
        if args.self_test: self_test(args.self_test)
        if args.package: package(args.package)
        if args.input: apply(args.input,args.output)
        elif not args.self_test and not args.package: parser.error('specify input jni.zip, --self-test, or --package')
    except (OSError, ValueError, zipfile.BadZipFile, subprocess.CalledProcessError) as e:
        parser.exit(1,f'Error: {e}\n')
