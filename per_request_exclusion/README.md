# Surface / Ytbl：逐请求排除自身 v2

目标：系统截图、系统录屏能够包含悬浮窗，而液态玻璃的内部屏幕采集不包含自己。不再依赖全局 `SKIP_SCREENSHOT`，也不通过隐藏/显示窗口制造闪烁。

## 安装与编译

本包是源码升级器和新增模块，不是已经编译完的用户宿主工程。当前会话文件执行器不可用，尚未直接应用到用户上传 ZIP；升级器会在本机检查原始源码锚点，生成新目录和新 ZIP，不覆盖输入。

```sh
python3 upgrade.py "Surface_RealBackdrop.zip" -o Surface_PerRequest
cd Surface_PerRequest
NDK_BUILD="$HOME/android-ndk-r28c/ndk-build" sh build_real_backdrop.sh -j4
```

也可以将已解压的工程目录作为第一个参数。输出目录必须尚不存在。Python 3.9+；NDK 与以前一样使用本机现有环境。Dex 已编译并包含源码，不需要在手机安装 Java/D8/Gradle。不要再次运行旧版 install.py。

最终部署完整的 `dist/`：

```text
dist/
├── imgui_chain_1_47
└── capture_runtime/
    ├── capture.dex.jar
    └── libytbl_host.so
```

这版不再使用旧的 `libglass_capture.so`。不能混用旧 ELF、旧 Dex、旧辅助库。构建脚本将部署目录与 NDK 的 libs 输出分开，避免下一次 make 把 capture_runtime 目录当作普通文件删除。已有 dist 会保留为带时间戳的 dist.previous.*。

以用户原来的 root 方式运行 `imgui_chain_1_47`。它现在是一个小型原生启动器，随后 exec 系统 app_process，加载同目录的 Dex 与 libytbl_host.so。原来的 ImGui C++ main 只改了符号名，仍运行原有窗口/触摸/渲染循环。窗口与采集 Java 线程位于同一地址空间，因此不存在把原生对象指针传到另一个进程的错误。无需额外 APK。

运行目录请使用自己控制的私有可执行目录；构建输出默认 0700 目录、0700 启动器、0444 Dex、0644 .so。启动器拒绝可被其他组或其他用户写入的 runtime 文件。不自动提权，不修改 SELinux。可用 YTBL_CAPTURE_DIR 指定绝对 runtime 路径。

## 实际修改

- 移除 ANativeWindowCreator 的旧全局截图排除分支（Android 9–11 特殊 metadata/windowType，以及 Android 12+ 的 0x40 创建标记），公开 Create 调用传 false。
- 创建本程序的 Surface 后、绘制任何内容前，同步注册该原生 SurfaceControl。使用平台 nativeCopyFromSurfaceControl / assignNativeObject 获得独立持有引用的 Java SurfaceControl；不手工伪造其 C++ 内存布局。
- 每次内部 ScreenCapture 开始前，复制当前全部本程序 SurfaceControl 成 `SurfaceControl[]`，调用 `setExcludeLayers()`。空列表、复制失败或无效对象均拒绝采集；不会退回无排除的整屏捕获。
- 窗口重建/销毁会递增 exclusion generation。Java 采集完成前校验一次，原生接收和使用纹理前再次校验；旧世代帧不会被用于新窗口。请求级 SurfaceControl 副本在 finally 中释放，不随原始窗口提前失效。
- 仍保留已实现的 AHardwareBuffer / EGLImage / GPU RGBA8 拷贝路径。socketpair 此时只用于同一进程内的有界帧传递，不监听外部连接、不传递 SurfaceControl 地址。旧协议版本会被拒绝。
- 模糊默认 3.5、色散 0.18、窗口可读性遮罩 0.06、颗粒 0.0015；默认 Clear 材质。白色表面 tint alpha 为 0.035，暗色 tint alpha 为 0.05，不降低整个 ImGui 窗口或文字的透明度。
- 移除原“排除本窗口截图/录屏”操作控件，避免用户误开全局排除。现在只有内部采集自动排除自己。
- 安全/DRM 内容仍由系统保护；captureSecureLayers=false、allowProtected=false。

## 怎么验收

启动后勾选“启用真实屏幕背景”。成功时日志包含 `LIVE: excludeLayers=N / generation=G / system screenshots VISIBLE`，N 应大于 0，帧号持续增长。将窗口移到有文字或图片的后层应用上，确认后层模糊、前景文字清晰且没有递归白影；再做一次系统截图/录屏确认悬浮窗出现。

仅后层为纯黑时，模糊黑色仍是黑色，折射没有可辨认的纹理参照。浅色 UI 放在黑色背景上可能需要切换暗色主题或提高对比度；不应因此把全窗口 alpha 降低。

如果看到 `No valid per-request exclusion registry`、方法查找失败或 NOT LIVE，采集会被禁用。不要用重新开启 SKIP_SCREENSHOT、放开受保护内容或取消排除列表来绕过错误；保留终端日志即可定位平台接口差异。

## 验证边界

支持目标仍为 Android 14–16、ARM64、GLES3 和用户本人 root 设备。平台 ScreenCapture/SurfaceControl 私有方法需厂商 ROM 实测。本包的云端 NDK 模块/启动器编译、Java/Dex 编译、引用生命周期模拟测试与安装器测试均写入 VALIDATION.json；不把这些说成完整用户工程编译或手机实测。

未新增多显示器、HDR 或完整流体模拟；沿用输入工程已有的液态着色器。没有附带字体文件；升级器保留用户本地原工程资源。

## 主要来源

```text
AOSP Android16 SurfaceControl：nativeCopyFromSurfaceControl / assignNativeObject
https://github.com/aosp-mirror/platform_frameworks_base/blob/android16-release/core/java/android/view/SurfaceControl.java
AOSP Android16 ScreenCapture：CaptureArgs.Builder.setExcludeLayers
https://github.com/aosp-mirror/platform_frameworks_base/blob/android16-release/core/java/android/window/ScreenCapture.java
AOSP JNI：将各 SurfaceControl 的 getHandle() 放入 captureArgs.excludeHandles
https://github.com/aosp-mirror/platform_frameworks_base/blob/android16-release/core/jni/android_window_ScreenCapture.cpp
NDK HardwareBuffer
https://developer.android.com/ndk/reference/group/a-hardware-buffer
```
