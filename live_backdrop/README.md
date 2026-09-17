# Surface Liquid-Flow：真实后层背景模块 v0.1

本包只包含新增模块、构建产物和离线安装脚本；不包含用户上传的完整 Surface 工程、字体或其他资产。它不是“整工程已实机验收”的声明。

## 这次实现的链路

已有 root 的原生宿主 → 一次启动 app_process 辅助进程 → Android ScreenCapture → 等待平台截图 fence → HardwareBuffer → 私有继承 socketpair 传递缓冲区句柄 → AHardwareBuffer / EGLImage → GL_TEXTURE_2D → Ytbl ExternalBackdrop → 原来的液态折射与模糊。

没有逐帧启动 screencap，没有 PNG 编解码，没有把整屏像素拷到 CPU 后再上传。不是持续虚拟显示编码流：每一帧仍是系统 ScreenCapture 请求，有系统合成开销。默认采集上限 15 FPS、分辨率 0.5 倍；界面帧率与采集帧率分开。30 FPS 设置只是上限，不是实测性能承诺。

## 与您提供的 ANativeWindowCreator.h 的连接点

该头文件已保存 native window 到 SurfaceControl 的映射，并在 Android 12+ 的 skipScrenshot 路径设置 0x40（eSkipScreenshot）。安装脚本保留原来的私有 Surface 创建实现，不伪造新的 sp<IBinder> / DisplayCaptureArgs ABI。

脚本通过编译宏 `SURFACEGLASS_EXCLUDE_OWN_CAPTURE=1`，仅要求这个创建器自己创建的 Surface 排除在截图中，并记录创建时请求的状态。每次重建窗口也重新设置。`IsBackdropExclusionReady()` 是创建参数的检查，不是 OEM 合成器行为的运行验证。

**重要副作用：这不是仅对此采集请求的局部排除。外部截图以及某些录屏也可能看不到本窗口；原 UI 的“过录制”开关不能再使捕获模式下的窗口进入截图。**如需保留外部录屏中的完整悬浮窗，应改用按请求 excludeHandles 的平台版本桥，不应去掉排除却继续开启本模块（会造成递归）。

## 安装

将此模块 ZIP 解压到独立目录，例如 `live_backdrop_module/`。对您现在的 Liquid-Flow 工程执行：

```sh
python3 live_backdrop_module/install.py \
  '/路径/[ndk]Surface_9~17(SymbolChain1.47)_liquid-flow.zip' \
  --output ./Surface_LiveBackdrop
```

也可输入已经解压的工程目录。脚本不覆盖输入，不联网，不上传源码。源码定位不匹配会报错停止，而不是忽略。您收到的单独 ANativeWindowCreator.h 必须与工程内同名文件一致；需要先手动放入工程时请保留原文件备份。

只生成已修改头文件：

```sh
python3 live_backdrop_module/install.py ./ANativeWindowCreator.h \
  --header-only --output ./ANativeWindowCreator_live.h
```

头文件独立修改不等于完成采集；完整模式还会接入源文件、生命周期和运行时。

## 编译和部署

```sh
ndk-build -C ./Surface_LiveBackdrop -j4
cp -a ./Surface_LiveBackdrop/runtime/live_backdrop \
      ./Surface_LiveBackdrop/libs/arm64-v8a/
```

实际启动目录必须一起放置：

```text
运行目录/
├── imgui_chain_1_47            # 您重新编译的宿主 ELF
└── live_backdrop/
    ├── capture-helper.jar     # 含 classes.dex，不是 APK
    └── liblivebg_jni.so       # Android ARM64 JNI 辅助库
```

沿用原工程在您自己设备上的 root 启动方式。模块不会执行 su、修改 SELinux、修改系统权限或开启受保护画面捕获。运行目录应由您信任的用户拥有，不要从他人可写目录加载 root 辅助代码。Java 辅助库用绝对路径加载；默认路径是宿主可执行文件的同级 live_backdrop/，也支持明确指定绝对路径环境变量 `SURFACEGLASS_RUNTIME`。

## 使用与验收

默认关闭。启动后找到 **Cross-app background / 真实后层背景**，勾选“启用本机画面采集（不保存、不上传）”。设置在下一帧生效，避免当前 ImGui 回调仍引用纹理时释放资源。

开启后，内部彩色演示背景不再绘制，Ytbl 不再使用自身帧缓冲快照作为玻璃来源。界面显示 CAPTURE ON，以及真实采集帧数、采集 FPS 和纹理大小。首次采集尚未完成、旋转切换、错误或图像超过 750ms 未刷新时，不使用过期图像，降级为材质底色。错误不静默自动重试；修复原因后关闭再开启。

请在没有敏感信息的终端或测试页面做首次验证：

1. 显示大号文字和彩色棋盘，开启采集；确认玻璃内为真实页面，而不是原演示条纹。
2. 拖动玻璃，检查文字位置连续、没有“窗口里套窗口”。若出现递归，立即关闭采集；该 ROM 需要按请求的图层排除桥。
3. 检查顶部/底部位置；若仅上下颠倒，用“校正纹理上下颠倒”。不要用此开关掩盖 90 度旋转或比例错误。
4. 横竖屏切换后，应丢弃旧代次帧，再出现新尺寸画面；核对实际位置。
5. 关闭开关：下一帧停止工作线程和子进程，释放硬件缓冲区、纹理及 EGLImage，恢复演示模式。

## 安全与生命周期

- 默认不开启；只采集用户本机、当前会话的可采集内容。
- 私有 socketpair，无监听端口、网络传输、图像文件或后台自动启动服务。
- ScreenCapture 的 captureSecureLayers=false、allowProtected=false；也拒绝返回的 secure/protected 缓冲区。不改变其他应用的保护标志。
- 辅助进程名称为 surface-glass-capture，宿主退出后退出；正常关闭时等待并回收子进程。
- 截图 fence 的等待发生在平台 ScreenCapture JNI；本模块传输的是已回调的 HardwareBuffer。
- GL 操作只在宿主渲染线程。新纹理每个 ImGui 帧只导入一次；同帧所有任务使用同一纹理。
- 必须在执行完最后一帧 ImGui 回调、销毁 EGL 之前调用 SurfaceBackdrop::Shutdown()。

## 兼容性与未完成的实机验证

参考实现是 AOSP android16-release 的 ScreenCapture 和 JNI。Java 辅助进程允许 API 34..36，接口通过正常反射查找；不调用 hidden-API exemption。ROM 禁止访问、方法签名变化或权限拒绝时会失败并提示，不能只凭“Android 16”保证所有定制 ROM 可运行。

默认使用与您头文件一致的第一个物理显示器；不支持多显示器选择、折叠屏独立显示器热切换。显示旋转和缩放采用宿主真实显示尺寸及 ImGui FramebufferScale；Android/Adreno 导入方向仍需上述实测。当前没有完整 HDR/广色域色彩管理，包含 HDR 时会显示提示。

云端验证记录位于 validation/：新增 JNI 库与消费者的 NDK 编译/链接、Java/DEX 构建、传输协议测试、安装器测试。**没有用户整工程构建、Android 设备、SurfaceFlinger 排除效果或 Adreno 性能测试。**不能将新增模块的编译成功写成整个悬浮窗已运行成功。

## 重建新增模块

```sh
ANDROID_NDK_HOME=/path/to/android-ndk-r28c \
ANDROID_HOME=/path/to/android-sdk bash build.sh
```

不会自行联网安装依赖；需要现有 NDK、android.jar、d8、JDK 和 C++ 编译器。

## 参考依据

- 用户提供的 ANativeWindowCreator.h：Create / CreateSurface / m_cachedSurfaceControl。
- AOSP android16-release: frameworks/base/core/java/android/window/ScreenCapture.java
- AOSP android16-release: frameworks/base/core/jni/android_window_ScreenCapture.cpp
- AOSP android14-release: frameworks/native/libs/gui/aidl/android/gui/ISurfaceComposerClient.aidl（eSkipScreenshot = 0x40）
- Android NDK hardware_buffer.h：AHardwareBuffer_sendHandleToUnixSocket / recvHandleFromUnixSocket。

新增模块为工程原型。现有 Surface 封装、液态着色器、原工程字体/图像/触摸实现不在本次新增模块的验证范围内。
