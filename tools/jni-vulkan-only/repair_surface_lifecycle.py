#!/usr/bin/env python3
"""Patch a compiled JNI Vulkan-only project with a renewable surface session manager.
Never touches GLES/EGL/OpenGL and never hooks another graphics renderer.
"""
from pathlib import Path
import sys
p = Path(sys.argv[1]) / "jni" / "NativeWindow.h"
src = p.read_text()
needle='#include <atomic>\n'
assert needle in src
src=src.replace(needle,needle+"#include <condition_variable>\n#include <mutex>\n#include <cstdint>\n",1)
marker="void RunSurfaceControlOverlay(ANativeWindow* gameWindow) {"
assert marker in src
src=src.replace(marker,'''namespace overlay_runtime {
    bool current(std::uint64_t sessionToken);
}
void RunSurfaceControlOverlay(ANativeWindow* gameWindow, std::uint64_t sessionToken) {''',1)
old = """    int width = ANativeWindow_getWidth(gameWindow);
    int height = ANativeWindow_getHeight(gameWindow);
    if (width <= 0 || height <= 0) return;"""
new = """    int width = ANativeWindow_getWidth(gameWindow);
    int height = ANativeWindow_getHeight(gameWindow);
    // During Activity / SurfaceHolder transitions the window can briefly have
    // no geometry. Do not permanently abandon a session on one zero-size read.
    for (int attempt = 0;
         (width <= 0 || height <= 0) && attempt < 40 &&
         overlay_runtime::current(sessionToken); ++attempt) {
        if (attempt == 0) {
            LOGW("[surface] pending geometry: window=%p token=%llu", gameWindow,
                 static_cast<unsigned long long>(sessionToken));
        }
        std::this_thread::sleep_for(std::chrono::milliseconds(50));
        width = ANativeWindow_getWidth(gameWindow);
        height = ANativeWindow_getHeight(gameWindow);
    }
    if (!overlay_runtime::current(sessionToken) || width <= 0 || height <= 0) {
        LOGW("[surface] unable to initialize session: token=%llu size=%dx%d",
             static_cast<unsigned long long>(sessionToken), width, height);
        return;
    }"""
assert old in src
src=src.replace(old,new,1)
old = """    const auto targetFrameTime = std::chrono::duration<float>(1.0f / 60.0f);
    while (true) {"""
new = """    const auto targetFrameTime = std::chrono::duration<float>(1.0f / 60.0f);
    std::uint64_t renderedFrames = 0;
    const char* stopReason = "superseded by another window";
    LOGI("[surface] session started: token=%llu window=%p control=%p size=%dx%d",
         static_cast<unsigned long long>(sessionToken), gameWindow, control, width, height);
    while (overlay_runtime::current(sessionToken)) {"""
assert old in src
src=src.replace(old,new,1)
old="""        if (currentWidth <= 0 || currentHeight <= 0) break;"""
new="""        if (currentWidth <= 0 || currentHeight <= 0) {
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
        }"""
assert old in src
src=src.replace(old,new,1)
old='''        if (!renderer.render(ImGui::GetDrawData(), &buffer)) {
            LOGE("Vulkan render/readback failed"); break;
        }'''
new='''        if (!renderer.render(ImGui::GetDrawData(), &buffer)) {
            stopReason = "Vulkan render/readback failed";
            LOGE("[surface] Vulkan render/readback failed: token=%llu frame=%llu",
                 static_cast<unsigned long long>(sessionToken),
                 static_cast<unsigned long long>(renderedFrames));
            break;
        }'''
assert old in src
src=src.replace(old,new,1)
old = """        ASurfaceTransaction_apply(update);
        ASurfaceTransaction_delete(update);
        AHardwareBuffer_release(buffer);

        auto spent = std::chrono::steady_clock::now() - frameStart;"""
new = """        ASurfaceTransaction_apply(update);
        ASurfaceTransaction_delete(update);
        AHardwareBuffer_release(buffer);
        ++renderedFrames;
        // This distinguishes 'still rendering but invisible' from 'thread exited'.
        if (renderedFrames == 1 || (renderedFrames % 120) == 0) {
            LOGI("[surface] frames=%llu token=%llu window=%p size=%dx%d",
                 static_cast<unsigned long long>(renderedFrames),
                 static_cast<unsigned long long>(sessionToken),
                 gameWindow, width, height);
        }

        auto spent = std::chrono::steady_clock::now() - frameStart;"""
assert old in src
src=src.replace(old,new,1)
old = """    overlay_input::queue().disable();
    renderer.shutdown();"""
new = """    LOGW("[surface] session ended: token=%llu frames=%llu reason=%s",
         static_cast<unsigned long long>(sessionToken),
         static_cast<unsigned long long>(renderedFrames), stopReason);
    overlay_input::queue().disable();
    renderer.shutdown();"""
assert old in src
src=src.replace(old,new,1)
old="""inline std::atomic<bool>& OverlayRunning() {"""
assert old in src
head=src[:src.index(old)]
tail=r'''
// The original code allowed exactly one overlay lifetime, so the login
// screen's transient ANativeWindow permanently consumed the overlay.
// This supervisor owns references to all window candidates and rebinds
// whenever the hook observes another ANativeWindow.
namespace overlay_runtime {
struct Supervisor {
    std::mutex mutex;
    std::condition_variable wake;
    ANativeWindow* pending = nullptr; // owns one ANativeWindow_acquire()
    ANativeWindow* active = nullptr;  // owns one ANativeWindow_acquire()
    std::atomic<std::uint64_t> generation{0};
    bool workerStarted = false;
};
inline Supervisor& supervisor() {
    static Supervisor value;
    return value;
}
inline bool current(std::uint64_t sessionToken) {
    return sessionToken != 0 &&
           supervisor().generation.load(std::memory_order_acquire) == sessionToken;
}
inline void workerLoop() {
    auto& s = supervisor();
    while (true) {
        ANativeWindow* window = nullptr;
        std::uint64_t token = 0;
        {
            std::unique_lock<std::mutex> lock(s.mutex);
            s.wake.wait(lock, [&] { return s.pending != nullptr; });
            window = s.pending;
            s.pending = nullptr;
            // Only one worker exists. It retains the active reference and
            // runs a single ImGui context and Vulkan device at a time.
            s.active = window;
            token = s.generation.load(std::memory_order_acquire);
        }
        // RunSurfaceControlOverlay consumes its window reference. Keep the
        // supervisor's separate reference until after active is cleared.
        ANativeWindow_acquire(window);
        try {
            RunSurfaceControlOverlay(window, token);
        } catch (const std::exception& e) {
            LOGE("[surface] worker exception: %s", e.what());
        } catch (...) {
            LOGE("[surface] worker unknown exception");
        }
        {
            std::lock_guard<std::mutex> lock(s.mutex);
            if (s.active == window) s.active = nullptr;
        }
        ANativeWindow_release(window);
    }
}
inline void observedWindow(ANativeWindow* window) {
    if (!window) return;
    // JNI has already given the caller its own reference. Acquire another
    // one for the asynchronous supervisor before the hook returns.
    ANativeWindow_acquire(window);
    auto& s = supervisor();
    ANativeWindow* retired = nullptr;
    bool accepted = false;
    {
        std::lock_guard<std::mutex> lock(s.mutex);
        if (window != s.active && window != s.pending) {
            if (!s.workerStarted) {
                try {
                    std::thread([] { workerLoop(); }).detach();
                    s.workerStarted = true;
                } catch (const std::exception& e) {
                    LOGE("[surface] unable to start supervisor: %s", e.what());
                } catch (...) {
                    LOGE("[surface] unable to start supervisor");
                }
            }
            if (s.workerStarted) {
                retired = s.pending;
                s.pending = window;
                const auto token = s.generation.fetch_add(1, std::memory_order_acq_rel) + 1;
                if (token == 0) {
                    // Practically unreachable, but reserve 0 as invalid.
                    s.generation.store(1, std::memory_order_release);
                }
                LOGI("[surface] observed new window=%p size=%dx%d gen=%llu",
                     window, ANativeWindow_getWidth(window), ANativeWindow_getHeight(window),
                     static_cast<unsigned long long>(s.generation.load()));
                accepted = true;
                s.wake.notify_one();
            }
        }
    }
    if (retired) ANativeWindow_release(retired);
    if (!accepted) ANativeWindow_release(window);
}
}  // namespace overlay_runtime

inline ANativeWindow* (*orig_ANativeWindow_fromSurface)(JNIEnv*, jobject) = nullptr;
inline ANativeWindow* Hook_ANativeWindow_fromSurface(JNIEnv* env, jobject surface) {
    if (!orig_ANativeWindow_fromSurface) return nullptr;
    ANativeWindow* result = orig_ANativeWindow_fromSurface(env, surface);
    if (result) overlay_runtime::observedWindow(result);
    return result; // Original caller retains its own ANativeWindow reference.
}

inline void hack_main() noexcept {
    void* sym = DobbySymbolResolver("libandroid.so", "ANativeWindow_fromSurface");
    if (!sym) { LOGE("[surface] symbol ANativeWindow_fromSurface unavailable"); return; }
    const int rc = DobbyHook(sym, (void*)Hook_ANativeWindow_fromSurface,
                             (void**)&orig_ANativeWindow_fromSurface);
    if (rc != 0 || !orig_ANativeWindow_fromSurface) {
        LOGE("[surface] ANativeWindow_fromSurface hook failed rc=%d", rc);
        return;
    }
    LOGI("[surface] NativeWindow hook installed, awaiting game surface creation");
    void* inputSym = DobbySymbolResolver("libinput.so", "_ZN7android11MotionEvent8copyFromEPKS0_b");
    if (!inputSym) {
        LOGW("[surface] MotionEvent copyFrom symbol unavailable; input disabled");
        return;
    }
    const int inputRc = DobbyHook(inputSym, (void*)hook_input, (void**)&orig_input);
    if (inputRc != 0 || !orig_input) {
        LOGE("[surface] MotionEvent copyFrom hook failed rc=%d", inputRc);
    }
}
'''
src=head+tail
assert src.count("RunSurfaceControlOverlay(")==2
assert "OverlayRunning" not in src
assert "ImGui_ImplVulkan_NewFrame" in src
assert "ImGui_ImplOpenGL3" not in src
p.write_text(src)
print("SURFACE_SUPERVISOR_PATCH=APPLIED")
print("NativeWindow.h bytes:", len(src))
