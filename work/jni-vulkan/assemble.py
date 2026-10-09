#!/usr/bin/env python3
"""Offline assembly; dependencies are supplied by the cache-aware build workflow."""
from pathlib import Path
import argparse, importlib.util, shutil, json, hashlib

MENU = r'''#pragma once
#include <imgui.h>
struct sConfig {
    struct sMenu {
        bool Bones = false, Line = false, Box = false, Health = false;
        bool Name = false, Distance = false, TeamID = false, Vehicle = false, Radar = false;
    } Menu;
    struct sRadar { float x = 0, y = 0; } Radar;
};
inline sConfig Config;
inline bool MenuUseChinese = false;
inline const char* Label(const char* chinese, const char* english) {
    return MenuUseChinese ? chinese : english;
}
inline void BeginDraw(float screen_width, float screen_height) {
    ImGui::SetNextWindowSize(ImVec2(810, 470), ImGuiCond_FirstUseEver);
    if (ImGui::Begin("Mind Mod")) {
        ImGui::TextUnformatted("Renderer: Vulkan / AHardwareBuffer");
        ImGui::Checkbox(Label("方框", "Box"), &Config.Menu.Box); ImGui::SameLine();
        ImGui::Checkbox(Label("射线", "Line"), &Config.Menu.Line); ImGui::SameLine();
        ImGui::Checkbox(Label("骨骼", "Bones"), &Config.Menu.Bones); ImGui::SameLine();
        ImGui::Checkbox(Label("距离", "Distance"), &Config.Menu.Distance);
        ImGui::Checkbox(Label("名称", "Name"), &Config.Menu.Name); ImGui::SameLine();
        ImGui::Checkbox(Label("血量", "Health"), &Config.Menu.Health); ImGui::SameLine();
        ImGui::Checkbox(Label("阵营", "Team ID"), &Config.Menu.TeamID); ImGui::SameLine();
        ImGui::Checkbox(Label("雷达", "Radar"), &Config.Menu.Radar);
        ImGui::Spacing();
        ImGui::SliderFloat(Label("雷达 X", "Radar X"), &Config.Radar.x, 0, screen_width,
                           "%.2f", ImGuiSliderFlags_AlwaysClamp);
        ImGui::SliderFloat(Label("雷达 Y", "Radar Y"), &Config.Radar.y, 0, screen_height,
                           "%.2f", ImGuiSliderFlags_AlwaysClamp);
        ImGui::Separator();
        const float fps = ImGui::GetIO().Framerate;
        ImGui::Text(Label("帧间隔 %.3f ms (%.1f FPS)", "Frame interval %.3f ms (%.1f FPS)"),
                    fps > 0 ? 1000.0f / fps : 0.0f, fps);
    }
    ImGui::End();
}
'''
ANDROID_MK = '''LOCAL_PATH := $(call my-dir)
BUILD_MODE ?= release

include $(CLEAR_VARS)
LOCAL_MODULE := Imgui
LOCAL_CPPFLAGS := -std=c++20 -fexceptions -fvisibility=hidden
LOCAL_C_INCLUDES := $(LOCAL_PATH)/Library/Imgui $(LOCAL_PATH)/Library/Imgui/backends
LOCAL_EXPORT_C_INCLUDES := $(LOCAL_C_INCLUDES)
LOCAL_SRC_FILES := Library/Imgui/imgui.cpp Library/Imgui/imgui_draw.cpp \\
                   Library/Imgui/imgui_tables.cpp Library/Imgui/imgui_widgets.cpp \\
                   Library/Imgui/backends/imgui_impl_vulkan.cpp
include $(BUILD_STATIC_LIBRARY)

include $(CLEAR_VARS)
LOCAL_MODULE := dobby
LOCAL_SRC_FILES := Library/dobby/$(TARGET_ARCH_ABI)/libdobby.a
LOCAL_EXPORT_C_INCLUDES := $(LOCAL_PATH)/Library/dobby/include
include $(PREBUILT_STATIC_LIBRARY)

include $(CLEAR_VARS)
LOCAL_MODULE := Android
LOCAL_C_INCLUDES := $(LOCAL_PATH) $(LOCAL_PATH)/renderer
LOCAL_SRC_FILES := Injector.cpp renderer/VulkanRenderer.cpp
LOCAL_CPPFLAGS := -std=c++20 -fexceptions -fvisibility=hidden -DVK_USE_PLATFORM_ANDROID_KHR
LOCAL_CPPFLAGS += -Wall -Wextra -Werror=format-security -Werror=return-type
LOCAL_CPPFLAGS += -Wno-missing-field-initializers
LOCAL_LDLIBS := -llog -landroid -lvulkan -ldl
LOCAL_STATIC_LIBRARIES := Imgui dobby
# Bind this library's ImGui state locally; never interpose the host application's copy.
LOCAL_LDFLAGS := -Wl,--exclude-libs,ALL -Wl,-Bsymbolic -Wl,--build-id -Wl,-z,max-page-size=16384
ifeq ($(BUILD_MODE),debug)
LOCAL_CPPFLAGS += -O0 -g -fno-omit-frame-pointer
else ifeq ($(BUILD_MODE),release)
LOCAL_CPPFLAGS += -O2 -g -fno-omit-frame-pointer
else
$(error Invalid BUILD_MODE: $(BUILD_MODE))
endif
include $(BUILD_SHARED_LIBRARY)
'''
BUILD_SH = '''#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
if [[ -n "${NDK_BUILD:-}" ]]; then BUILD="$NDK_BUILD"
elif [[ -n "${ANDROID_NDK_HOME:-}" ]]; then BUILD="$ANDROID_NDK_HOME/ndk-build"
elif [[ -n "${NDK_HOME:-}" ]]; then BUILD="$NDK_HOME/ndk-build"
else BUILD="$(command -v ndk-build || true)"; fi
if [[ -z "$BUILD" || ! -x "$BUILD" ]]; then
    echo 'Set ANDROID_NDK_HOME to your Android NDK directory.' >&2; exit 1
fi
exec "$BUILD" -C "$ROOT" NDK_PROJECT_PATH="$ROOT" \\
    APP_BUILD_SCRIPT="$ROOT/jni/Android.mk" \\
    NDK_APPLICATION_MK="$ROOT/jni/Application.mk" BUILD_MODE="${BUILD_MODE:-release}" "$@"
'''
REBUILD_DOBBY = '''#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
: "${ANDROID_NDK_HOME:?Set ANDROID_NDK_HOME}"
cmake -S "$ROOT/jni/Library/dobby/source" -B "$ROOT/.build-dobby" \\
    -DCMAKE_TOOLCHAIN_FILE="$ANDROID_NDK_HOME/build/cmake/android.toolchain.cmake" \\
    -DCMAKE_POLICY_VERSION_MINIMUM=3.5 -DANDROID_ABI=arm64-v8a -DANDROID_PLATFORM=android-31 \\
    -DANDROID_STL=c++_static -DCMAKE_BUILD_TYPE=Release \\
    -DDOBBY_BUILD_TEST=OFF -DDOBBY_BUILD_EXAMPLE=OFF -DPlugin.SymbolResolver=ON
cmake --build "$ROOT/.build-dobby" --target dobby_static -j "${JOBS:-4}"
LIB="$(find "$ROOT/.build-dobby" -name libdobby.a -print -quit)"
test -n "$LIB"
mkdir -p "$ROOT/jni/Library/dobby/arm64-v8a"
cp "$LIB" "$ROOT/jni/Library/dobby/arm64-v8a/libdobby.a"
'''
README = '''# JNI Vulkan 渲染版

## 内容与边界
这是完整、可独立 ndk-build 的 Vulkan JNI 工程，不是只替换函数名的补丁。
绘制链路：ImGui -> Vulkan render pass -> Vulkan 导入的 AHardwareBuffer -> SurfaceControl。
没有 EGL / OpenGL ES 渲染路径，没有 glReadPixels 或 CPU 像素回读呈现，也不在父窗口上创建交换链。
保留既有输入快照队列、入口挂接方式、Config 菜单字段与复选框。菜单本身只维护开关状态，
此工程没有新增读取其他程序数据、游戏逻辑、权限规避或反检测功能。

旧工程的 ImGui 1.92.6 WIP 静态库不再使用；核心和 Vulkan 后端统一从官方 1.92.5 源码编译。
Dobby 采用固定官方提交 5dfc8546954ce3b3198132ab13fddb89ee92cdd7 重编译，附带源码、许可证与静态库。
这不是与原始 ZIP 每个条目逐字节一致的包，而是按已读取 r2 工程重构的完整 Vulkan 版本。
输入与窗口回调基于同一 r2 修复工具中的代码，未扩大挂接范围。

## 编译
Android 12 / API 31+，arm64-v8a，Vulkan 1.1+；已构建结果见 verification/BUILD_STATUS.json。
还要求设备支持 VK_ANDROID_external_memory_android_hardware_buffer 和 VK_EXT_queue_family_foreign。
不支持时记录错误并停止覆盖层，不回退 OpenGL、不接管父窗口的图像生产者。

    export ANDROID_NDK_HOME="$HOME/android-ndk-r28c"
    bash build.sh -j4

也可直接：

    ndk-build NDK_PROJECT_PATH=. APP_BUILD_SCRIPT=jni/Android.mk NDK_APPLICATION_MK=jni/Application.mk

输出 libs/arm64-v8a/libAndroid.so。调试符号在 obj/local/arm64-v8a/libAndroid.so。
交付包预编译库在 prebuilt/arm64-v8a/libAndroid.so；必须结合 BUILD_STATUS 确认验证范围。
debug 编译：BUILD_MODE=debug bash build.sh -j4。
Dobby 重新构建：bash tools/rebuild_dobby.sh。常规构建已附带该静态库，不需要 CMake 或联网。

## 同步与生命周期
三张持久 AHardwareBuffer，只在初始化或尺寸变化时重新分配。
每帧 FOREIGN -> Vulkan graphics ownership acquire，透明清屏并绘制，
再 graphics -> FOREIGN release，同时切换到 GENERAL layout。
GPU fence 在 CPU 上完成等待以后才 setBuffer(..., -1)，因此这里的 -1 不是跳过 GPU 同步。
SurfaceControl OnComplete 回调回收“上一张”缓冲区的 release fence，等待信号后才复用。
同时最多存在一个未完成的呈现事务，避免事务合并造成前一缓冲区对应关系不明确。
回调不碰 ImGui / VkDevice；回调状态独立持有引用，退出后到达的回调不会访问已销毁的渲染器。
窗口尺寸改变后创建新的一代缓冲区；旧缓冲区仍由系统合成器独立持有直到不用为止。
退出先停输入并等待 GPU，再隐藏、detach 覆盖层并释放对象。Overlay_RequestStop() 可请求停止。

这里选择的是保守同步实现：GPU fence CPU 等待 + 一个未完成的呈现事务，目标上限 60 FPS，
不是承诺 Vulkan 一定比原 OpenGL 更快。后续性能优化应以设备测量为依据，不能删掉 fence 来提速。

## 字体
不附带原 font_zt.h 或独立字体文件。优先加载设备 /system/fonts 内的中文字体。
找不到已知中文字体路径时使用 ImGui 自带默认字体并将标签切换为英文，避免方框乱码。
可在 VulkanRenderer.cpp 的 LoadSystemFont() 调整为设备实际已有且可读的字体路径。

## 文件说明
- jni/renderer/VulkanCore.h：共享的 Vulkan 初始化、RenderPass、命令、descriptor 与 fence 管理。
- jni/renderer/VulkanRenderer.cpp：Android 硬件缓冲区导入、三缓冲、释放栅栏、透明呈现和尺寸变化。
- jni/NativeWindow.h：延续 r2 的窗口与输入回调安装代码，不再包含 OpenGL 渲染器。
- jni/InputBridge.h、MotionQueue.h：输入线程只复制事件，渲染线程消费；防止未初始化/跨线程 ImGui 访问。
- jni/Menu.h：原菜单字段和控件，屏幕宽高现在从 Vulkan 目标尺寸传入。
- jni/Library/Imgui：统一版本的官方核心源码与 Vulkan 后端；不保留旧 OpenGL backend。
- tests/vulkan_smoke.cpp：使用同一个 VulkanCore 实际离屏绘制并验证透明、颜色和 alpha。
- tests/test_motion_queue.cpp：生命周期、有界队列和多线程输入测试。
- verification：构建日志、ELF 检查、测试日志与可能生成的离屏图像。

## 验证不能替代真机
宿主 Vulkan 离屏测试不等于 Android AHardwareBuffer / SurfaceFlinger / GPU 驱动验证。
请实际测试冷启动触摸、拖动、多指、旋转、前后台切换、透明背景、尺寸变化和关闭。
原有 MotionEvent::copyFrom 是私有平台符号，仍可能随 Android/OEM 变化而失效。
挂接到哪个 Surface 仍沿用原工程策略；多 Surface / 窗口替换的上层选择策略没有全面重写。
不要在回调尚未结束时 dlclose 此库；没有实现运行中卸载挂接和代码段的能力。
设备日志：logcat -s NDK；重点查找 Vulkan GPU、target pool rebuilt 或明确错误信息。

## 资料
- https://developer.android.com/ndk/reference/group/native-activity
- https://developer.android.com/ndk/reference/group/a-hardware-buffer
- https://docs.vulkan.org/refpages/latest/refpages/source/VK_ANDROID_external_memory_android_hardware_buffer.html
- https://github.com/ocornut/imgui/tree/v1.92.5/backends
'''

def main():
    p=argparse.ArgumentParser();p.add_argument('--project',type=Path,required=True)
    p.add_argument('--imgui',type=Path,required=True);p.add_argument('--dobby',type=Path,required=True)
    p.add_argument('--base',type=Path,required=True);args=p.parse_args()
    spec=importlib.util.spec_from_file_location('previous_repair',args.base)
    base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
    root=args.project
    values={
        'jni/MotionQueue.h':base.QUEUE,
        'jni/InputBridge.h':base.BRIDGE,
        'tests/MotionQueue.h':base.QUEUE,
        'tests/test_motion_queue.cpp':base.TEST,
        'jni/renderer/Renderer.h':'#pragma once\n#include <android/native_window.h>\nvoid RunSurfaceControlOverlay(ANativeWindow* window);\n',
        'jni/NativeWindow.h': '#pragma once\n#include <atomic>\n#include <thread>\n#include <exception>\n#include <android/native_window_jni.h>\n#include <dobby.h>\n#include "Logger.h"\n#include "InputBridge.h"\n#include "renderer/Renderer.h"\n'+base.HOOKS,
        'jni/Injector.cpp': '#include "NativeWindow.h"\n__attribute__((constructor)) void lib_main() {\n    try { std::thread([] { hack_main(); }).detach(); }\n    catch (const std::exception& e) { LOGE("startup failed: %s", e.what()); }\n    catch (...) { LOGE("startup failed"); }\n}\n',
        'jni/Logger.h':'#pragma once\n#include <android/log.h>\n#define LOGI(...) ((void)__android_log_print(ANDROID_LOG_INFO, "NDK", __VA_ARGS__))\n#define LOGW(...) ((void)__android_log_print(ANDROID_LOG_WARN, "NDK", __VA_ARGS__))\n#define LOGE(...) ((void)__android_log_print(ANDROID_LOG_ERROR, "NDK", __VA_ARGS__))\n',
        'jni/Menu.h':MENU,'jni/Android.mk':ANDROID_MK,
        'jni/Application.mk':'APP_ABI := arm64-v8a\nAPP_PLATFORM := android-31\nAPP_STL := c++_static\nAPP_OPTIM := release\nAPP_SUPPORT_FLEXIBLE_PAGE_SIZES := true\n',
        'build.sh':BUILD_SH, 'tools/rebuild_dobby.sh':REBUILD_DOBBY,'README.md':README,
        '.gitignore':'obj/\nlibs/\n.build-dobby/\n__pycache__/\n'
    }
    for name,content in values.items():
        out=root/name;out.parent.mkdir(parents=True,exist_ok=True);out.write_text(content)
        if name.endswith('.sh'):out.chmod(0o755)
    imgui=root/'jni/Library/Imgui';imgui.mkdir(parents=True,exist_ok=True)
    needed=['imgui.cpp','imgui_draw.cpp','imgui_tables.cpp','imgui_widgets.cpp','imgui.h',
            'imgui_internal.h','imconfig.h','imstb_rectpack.h','imstb_textedit.h','imstb_truetype.h',
            'LICENSE.txt','backends/imgui_impl_vulkan.cpp','backends/imgui_impl_vulkan.h']
    for name in needed:
        dest=imgui/name;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(args.imgui/name,dest)
    dobby=root/'jni/Library/dobby';dobby.mkdir(parents=True,exist_ok=True)
    shutil.copytree(args.dobby,dobby/'source',dirs_exist_ok=True,ignore=shutil.ignore_patterns('.git'))
    (dobby/'include').mkdir(exist_ok=True);shutil.copy2(args.dobby/'include/dobby.h',dobby/'include/dobby.h')
    manifest={'input_basis':'jni_fixed_full_r2.zip, plus matching prior repair-source QUEUE/BRIDGE/HOOKS',
              'imgui_version':'1.92.5','imgui_artifact_id':10480406146,
              'dobby_commit':'5dfc8546954ce3b3198132ab13fddb89ee92cdd7',
              'base_repair_sha256':hashlib.sha256(args.base.read_bytes()).hexdigest(),
              'standalone_font_files_included':False,'android_runtime_verified':False}
    (root/'DEPENDENCIES.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print('Assembled complete Vulkan JNI project:',root)
if __name__=='__main__':main()
