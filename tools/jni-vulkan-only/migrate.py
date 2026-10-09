#!/usr/bin/env python3
"""Rebuild the user's JNI SurfaceControl overlay as Vulkan-only."""
from pathlib import Path
import shutil
import sys
import re

ROOT = Path(sys.argv[1]).resolve()
UPSTREAM = Path(sys.argv[2]).resolve()
JNI = ROOT / "jni"
assert (JNI / "NativeWindow.h").exists()
assert (UPSTREAM / "backends/imgui_impl_vulkan.cpp").exists()

source = (JNI / "NativeWindow.h").read_text(encoding="utf-8")
parts = source.split("struct sConfig {", 1)
assert len(parts) == 2
menu_and_rest = "struct sConfig {" + parts[1]
menu = menu_and_rest.split("void RunSurfaceControlOverlay(ANativeWindow* gameWindow)", 1)[0]
assert "void BeginDraw()" in menu
hooks = source.split("inline std::atomic<bool>& OverlayRunning()", 1)
assert len(hooks) == 2
menu = menu.replace("OpenGL.ScreenWidth", "VulkanState.ScreenWidth")
menu = menu.replace("OpenGL.ScreenHeight", "VulkanState.ScreenHeight")

prologue = r'''#pragma once
#include "VulkanOverlay.h"
#include <atomic>
#include <algorithm>
#include <chrono>
#include <exception>
#include <functional>
#include <memory>
#include <thread>
#include <android/native_window.h>
#include <android/native_window_jni.h>
#include <android/surface_control.h>
'''

renderer = r'''
void RunSurfaceControlOverlay(ANativeWindow* gameWindow) {
    if (!gameWindow) return;
    const auto releaseWindow = [](ANativeWindow* p) { ANativeWindow_release(p); };
    std::unique_ptr<ANativeWindow, decltype(releaseWindow)> ownedWindow(gameWindow, releaseWindow);
    overlay_input::SessionInputGuard inputGuard;
    int width = ANativeWindow_getWidth(gameWindow);
    int height = ANativeWindow_getHeight(gameWindow);
    if (width <= 0 || height <= 0) return;
    VulkanState.ScreenWidth = static_cast<float>(width);
    VulkanState.ScreenHeight = static_cast<float>(height);
    LOGI("Vulkan overlay start: %d x %d", width, height);

    ASurfaceControl* control = ASurfaceControl_createFromWindow(gameWindow, "VulkanOverlay");
    if (!control) { LOGE("ASurfaceControl_createFromWindow failed"); return; }
    const auto releaseControl = [](ASurfaceControl* p) { ASurfaceControl_release(p); };
    std::unique_ptr<ASurfaceControl, decltype(releaseControl)> ownedControl(control, releaseControl);

    {
        ASurfaceTransaction* tx = ASurfaceTransaction_create();
        if (!tx) return;
        ASurfaceTransaction_setZOrder(tx, control, 1000);
        ASurfaceTransaction_setPosition(tx, control, 0, 0);
        const ARect crop{0, 0, width, height};
        ASurfaceTransaction_setCrop(tx, control, crop);
        ASurfaceTransaction_setBufferAlpha(tx, control, 1.0f);
        ASurfaceTransaction_apply(tx);
        ASurfaceTransaction_delete(tx);
    }

    VulkanOffscreen renderer;
    if (!renderer.initialize(static_cast<uint32_t>(width), static_cast<uint32_t>(height))) {
        LOGE("Vulkan device initialization failed"); return;
    }

    IMGUI_CHECKVERSION();
    ImGui::CreateContext();
    bool platformReady = ImGui_ImplAndroid_Init(gameWindow);
    if (!platformReady || !renderer.initializeImGui()) {
        LOGE("ImGui Vulkan backend initialization failed");
        renderer.shutdown();
        if (platformReady) ImGui_ImplAndroid_Shutdown();
        ImGui::DestroyContext();
        return;
    }
    ImGui::StyleColorsClassic();
    ImGui::GetStyle().ScaleAllSizes(3.0f);
    if (!LoadFont(25.2f)) LOGW("Custom Chinese font load failed; using fallback");
    overlay_input::queue().enable();

    const auto targetFrameTime = std::chrono::duration<float>(1.0f / 60.0f);
    while (true) {
        auto frameStart = std::chrono::steady_clock::now();
        const int currentWidth = ANativeWindow_getWidth(gameWindow);
        const int currentHeight = ANativeWindow_getHeight(gameWindow);
        if (currentWidth <= 0 || currentHeight <= 0) break;
        if (currentWidth != width || currentHeight != height) {
            if (!renderer.resize(static_cast<uint32_t>(currentWidth),
                                 static_cast<uint32_t>(currentHeight))) {
                LOGE("Vulkan resize failed"); break;
            }
            width = currentWidth;
            height = currentHeight;
            VulkanState.ScreenWidth = static_cast<float>(width);
            VulkanState.ScreenHeight = static_cast<float>(height);
            ASurfaceTransaction* tx = ASurfaceTransaction_create();
            if (tx) {
                const ARect crop{0, 0, width, height};
                ASurfaceTransaction_setCrop(tx, control, crop);
                ASurfaceTransaction_apply(tx);
                ASurfaceTransaction_delete(tx);
            }
        }
        ImGui_ImplVulkan_NewFrame();
        ImGui_ImplAndroid_NewFrame();
        DrainOverlayInput();
        ImGui::NewFrame();
        BeginDraw();
        ImGui::Render();

        AHardwareBuffer* buffer = nullptr;
        if (!renderer.render(ImGui::GetDrawData(), &buffer)) {
            LOGE("Vulkan render/readback failed"); break;
        }
        ASurfaceTransaction* update = ASurfaceTransaction_create();
        if (!update) {
            AHardwareBuffer_release(buffer);
            LOGE("SurfaceTransaction allocation failed"); break;
        }
        ASurfaceTransaction_setBuffer(update, control, buffer, -1);
        ASurfaceTransaction_apply(update);
        ASurfaceTransaction_delete(update);
        AHardwareBuffer_release(buffer);

        auto spent = std::chrono::steady_clock::now() - frameStart;
        if (spent < targetFrameTime) std::this_thread::sleep_for(targetFrameTime - spent);
    }

    overlay_input::queue().disable();
    renderer.shutdown();
    ImGui_ImplAndroid_Shutdown();
    ImGui::DestroyContext();
    LOGI("Vulkan overlay stopped");
}

'''
(JNI / "NativeWindow.h").write_text(
    prologue + "\n" + menu + "\n" + renderer +
    "\ninline std::atomic<bool>& OverlayRunning()" + hooks[1], encoding="utf-8"
)

# Rebuild Dear ImGui from a coherent upstream version; the old precompiled
# archive contains only the GL-oriented renderer.
DEST = JNI / "third_party/imgui"
DEST.mkdir(parents=True, exist_ok=True)
core = ("imgui.cpp", "imgui_draw.cpp", "imgui_tables.cpp", "imgui_widgets.cpp",
        "imgui.h", "imgui_internal.h", "imconfig.h",
        "imstb_truetype.h", "imstb_textedit.h", "imstb_rectpack.h", "LICENSE.txt")
backend = ("imgui_impl_android.cpp", "imgui_impl_android.h",
           "imgui_impl_vulkan.cpp", "imgui_impl_vulkan.h")
for name in core:
    shutil.copy2(UPSTREAM / name, DEST / name)
(DEST / "backends").mkdir(exist_ok=True)
for name in backend:
    shutil.copy2(UPSTREAM / "backends" / name, DEST / "backends" / name)
shutil.copy2(Path(__file__).parent / "VulkanOverlay.h", JNI / "VulkanOverlay.h")

vendor = JNI / "Library/Imgui"
for path in (vendor / "arm64-v8a/libimgui.a",
             vendor / "include/OpenGL.h", vendor / "include/imgui_impl_opengl3.h"):
    path.unlink(missing_ok=True)
for filename in ("imgui.h", "imgui_internal.h", "imconfig.h",
                 "imstb_rectpack.h", "imstb_textedit.h", "imstb_truetype.h",
                 "imgui_impl_android.h"):
    (vendor / "include" / filename).unlink(missing_ok=True)
if (vendor / "arm64-v8a").is_dir() and not any((vendor / "arm64-v8a").iterdir()):
    (vendor / "arm64-v8a").rmdir()

android_mk = r'''LOCAL_PATH := $(call my-dir)
BUILD_MODE ?= debug

include $(CLEAR_VARS)
LOCAL_MODULE := dobby
LOCAL_SRC_FILES := Library/dobby/$(TARGET_ARCH_ABI)/libdobby.a
LOCAL_EXPORT_C_INCLUDES := $(LOCAL_PATH)/Library/dobby/include
include $(PREBUILT_STATIC_LIBRARY)

include $(CLEAR_VARS)
LOCAL_MODULE := Android
LOCAL_CPPFLAGS := -std=c++20 -fexceptions -Werror=format-security -Werror=return-type -Wno-error=c++11-narrowing
LOCAL_C_INCLUDES += $(LOCAL_PATH)
LOCAL_C_INCLUDES += $(LOCAL_PATH)/third_party/imgui
LOCAL_C_INCLUDES += $(LOCAL_PATH)/third_party/imgui/backends
LOCAL_C_INCLUDES += $(LOCAL_PATH)/Library/Imgui/include
LOCAL_C_INCLUDES += $(LOCAL_PATH)/Library/dobby/include
LOCAL_SRC_FILES := Injector.cpp \
    third_party/imgui/imgui.cpp \
    third_party/imgui/imgui_draw.cpp \
    third_party/imgui/imgui_tables.cpp \
    third_party/imgui/imgui_widgets.cpp \
    third_party/imgui/backends/imgui_impl_android.cpp \
    third_party/imgui/backends/imgui_impl_vulkan.cpp
LOCAL_LDLIBS := -llog -landroid -lvulkan -ldl -lm
LOCAL_LDFLAGS += -Wl,--exclude-libs,ALL -Wl,--build-id
LOCAL_STATIC_LIBRARIES := dobby

ifeq ($(BUILD_MODE),debug)
    LOCAL_CPPFLAGS += -g -O0 -frtti -fvisibility=default -fno-omit-frame-pointer
    LOCAL_LDFLAGS += -Wl,--export-dynamic
else ifeq ($(BUILD_MODE),release)
    LOCAL_CPPFLAGS += -O2 -fno-rtti -fvisibility=hidden -fomit-frame-pointer
    LOCAL_LDFLAGS += -Wl,-s
else
    $(error BUILD_MODE must be debug or release)
endif
include $(BUILD_SHARED_LIBRARY)
'''
(JNI / "Android.mk").write_text(android_mk, encoding="utf-8")
(JNI / "Application.mk").write_text(
    "APP_ABI := arm64-v8a\nAPP_PLATFORM := android-29\nAPP_STL := c++_static\n"
    "APP_CPPFLAGS += -std=c++20\n", encoding="utf-8"
)
readme = """# JNI Overlay - Vulkan Only

Original ImGui menu, InputBridge/MotionQueue, SurfaceControl composition,
built-in Chinese font and Dobby hooks are preserved.

The rendering path is VkImage + Vulkan render pass + vkCmdCopyImageToBuffer,
followed by CPU copying the RGBA result into AHardwareBuffer and publishing
it with ASurfaceTransaction_setBuffer. There is no EGL, GLES, VkSurfaceKHR
or Vulkan swapchain. The latter is intentional: SurfaceControl does not
expose a normal native-window swapchain in this project.

Dear ImGui v1.92.6 and its Vulkan and Android backends are built from source.
The old GLES prebuilt libimgui.a was removed. Android API 29+ / ARM64.

Build:
    cd <project directory>
    $ANDROID_NDK_HOME/ndk-build -j4 BUILD_MODE=debug

Outputs:
    libs/arm64-v8a/libAndroid.so
    obj/local/arm64-v8a/libAndroid.so (unstripped, when available)

Known performance tradeoff: a CPU readback/row copy per frame; this is a
compatibility-first migration, not zero-copy AHardwareBuffer Vulkan external
memory. Device Vulkan driver, SurfaceControl permission, overlay direction and
touch mapping still need on-device validation.
"""
(ROOT / "README-Vulkan.md").write_text(readme, encoding="utf-8")

bad = []
for file in JNI.rglob("*"):
    if file.suffix.lower() not in (".h", ".hpp", ".cpp", ".c", ".mk"):
        continue
    data = file.read_text(encoding="utf-8", errors="replace")
    if re.search(r'#\s*include\s*[<"](?:EGL/|GLES(?:2|3)?/|GL/|imgui_impl_opengl)', data) \
            or re.search(r'\-l(?:EGL|GLESv\d|GLESv1_CM)\b', data):
        bad.append(str(file.relative_to(ROOT)))
if bad:
    raise RuntimeError("OpenGL API reference still present: " + ", ".join(bad))
print("Vulkan migration complete, no EGL/GLES/OpenGL includes or link flags.")
