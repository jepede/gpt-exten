# Ytbl Real Screen Backdrop — AHB 1.0

这是一套实际的屏幕采集、硬件缓冲区传输、GPU 导入和 Ytbl 接入代码，不是仅声明 ExternalBackdrop 的空接口。支持目标：root、Android 14–16、ARM64、GLES 3、已接入 Ytbl 的 Surface 1.47 工程。

**交付边界：本包是新增模块、已构建的辅助程序和自动对接器，不含用户原始 ZIP。本地执行环境故障使原始 ZIP 未能在本轮应用补丁和编译；安装器在本机校验源码锚点后生成整合工程。完整宿主和 Android/Adreno 运行尚未验证。不要把独立模块编译成功理解为手机实测成功。**

## 安装到您这份工程

解压本包到一个新目录，将您的最新修改版 ZIP 放在旁边，然后执行：

```sh
python3 install.py "[ndk]Surface_9~17(SymbolChain1.47)修改.zip" -o Surface_RealBackdrop
cd Surface_RealBackdrop
sh build_real_backdrop.sh -j4
```

NDK 命令不在 PATH 时，在上述构建命令前设置 `NDK_BUILD=/实际路径/ndk-build`。原始 ZIP 不会被覆盖，安装器生成新目录及 `Surface_RealBackdrop.zip`。源码锚点不匹配则停止，不猜测另一分支结构。需要 Python 3.9+；无需在手机上安装 Java、Gradle、D8 或额外 APK。辅助 DEX 和 JNI .so 已随包提供，源码也在 `capture/`。

构建后一起使用：

```text
libs/arm64-v8a/
├── imgui_chain_1_47
└── capture_runtime/
    ├── capture.dex.jar
    └── libglass_capture.so
```

不要只复制 ELF；两个 runtime 文件也要在其旁边。放到您自己控制的可执行目录，例如 `/data/local/tmp/SurfaceReal/`，目录设为 `0700`，以您原来的 root 方式运行。不要直接从 `/sdcard` 加载辅助 .so。亦可设置 `YTBL_CAPTURE_DIR=/绝对路径/capture_runtime`。Android 14+ 的 DEX 文件保持只读，构建脚本已将其设为 `0444`。

## 操作

默认不采集。进入“真实屏幕背景 / Local screen backdrop”，勾选“启用真实屏幕背景（仅本机使用）”。只有状态变为 LIVE 且帧号增长时才启用外部纹理。采集未就绪、失败或超过 1.2 秒未更新时不继续显示旧截图；请求真实采集期间也不会拿内部彩色演示背景冒充真实画面。

初始目标：采集长边 1280、24 FPS。这里是采集请求上限，不是实测帧率或 UI 帧率承诺。先使用原玻璃参数中约 3–4 px 的轻模糊，再按设备情况调整。出现上下颠倒可使用明确的“上下翻转校准”选项。显示区域映射采用实际屏幕宽高，不是这个项目可能分配的方形 native surface 尺寸。

关闭开关或退出 UI 会关闭 socketpair、停止并回收子进程，释放帧、EGLImage 和纹理。“减少透明度”开启时暂停采集。父 UI 异常退出时，辅助进程设置了父进程死亡信号并在连接结束时退出，没有常驻后台服务或开机启动。

## 实际链路

1. 沿用您提供的 ANativeWindowCreator，在每次创建/重建自己 Surface 时使用既有 `eSkipScreenshot` 路径。这样屏幕采集不应包含玻璃本身。**副作用：遵循此标记的其他系统截图/录屏通常也看不到本悬浮窗。厂商是否遵循该标记仍要实机确认。**
2. 可见 UI 开关启动它自己的 root `app_process` 子进程。通过 Android 14–16 的平台 ScreenCapture 方法请求显示内容，`captureSecureLayers=false`、`allowProtected=false`，不更改权限或 SELinux。
3. AOSP Java ScreenCapture 回调在原生采集 fence 等待后提供 HardwareBuffer。JNI 只通过继承的匿名 socketpair 发送 AHardwareBuffer 句柄和有限元数据，没有开放 TCP、公开 Unix socket 或图像文件。
4. 接收线程保留最新一帧，旧待处理帧释放，不无限排队。主 GL 线程通过 EGLImage 导入并做一次 GPU 拷贝到自有 RGBA8 纹理；GPU fence 完成后才释放导入缓冲区，最多四个在途引用。
5. 支持 SDR sRGB 和 SDR Display P3（GPU 转换到 sRGB，超出色域的值裁剪）。HDR 或其他色彩空间明确拒绝并显示错误，不假装已经正确映射。
6. Ytbl 通过 ExternalBackdrop 使用该纹理，沿用工程已有的液态流场、触摸折射、色散和模糊。真实模式不绘制内部演示背景，也不重新捕获自己 framebuffer。

## 限制与排错

- 仅针对用户本人设备上的可采集画面。安全窗口、DRM/受保护图像遵循系统结果；不会改第三方保护标记，也不会通过权限/SELinux 绕过实现采集。
- 平台 ScreenCapture/DisplayControl 属于非公开接口；编译不保证所有厂商 ROM 都接受。状态显示 `captureDisplay status=...`、方法不存在或加载失败时，保留终端日志诊断，不反复执行提权或修改系统策略。
- 只处理默认物理显示，未实现折叠屏跨显示切换、虚拟显示、多显示器选择和 HDR。采集中检测到旋转/尺寸变化会丢弃混合帧并重试；ROM 的额外显示变换仍需设备验证。
- 当前整屏采集排除自身，不是逐层“只选比悬浮窗 Z 值更低的图层”的通用系统合成器。
- 原工程的 ImGui 和字体保持用户本地原样，本包不附带字体，不重新打包用户的原始源码。
- 原液态库的动态效果仍由其实现决定；本次没有把固定模糊伪称为完整流体模拟或 Apple 官方 Liquid Glass。

## 文件

`jni/real_backdrop/NativeBackdrop.cpp` 为宿主接收、纹理和资源生命周期；`SurfaceBackdropUi.h` 为 Ytbl 接线与可见控制；`capture/Main.java` 和 `capture/native_bridge.cpp` 为辅助采集；`install.py` 为非破坏性对接器；`validation/` 保存本次实际构建/测试日志。

验证报告以包内 `VALIDATION.json` 为准。Linux 上的协议/安装器测试不是 Android 屏幕采集实测，辅助程序的 NDK 构建也不是原始宿主工程构建。
