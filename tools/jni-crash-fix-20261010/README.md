# JNI 崩溃诊断与输入隔离包

## 重要：这不是功能完整的修复项目

本包用于验证输入回调是否触发崩溃。它不包含原始 jni.zip、原始第三方静态库、字体、编译后的 libAndroid.so，也不包含新的注入或输入 Hook 实现。

`isolate_input.py` 在本地读取原始 jni.zip，停用 NativeWindow.h 中的一处私有输入回调注册，生成包含原项目其余全部文件的独立副本 `jni_input_isolated.zip`。原文件不被覆盖；除该处源码及新增的说明报告外，其他原文件的解压后内容逐字节保持不变。

**隔离副本会关闭菜单触摸交互，不能用于宣称功能完整的修复已完成。** 原有绘制/资源生命周期问题仍可能存在。它不改变游戏业务逻辑、鉴权或系统安全配置。

## 已有证据与判断边界

日志记录了主线程在输入事件复制调用链中，连续进入项目 libAndroid.so 的三个帧，随后 SIGSEGV / SEGV_MAPERR，fault address 为 0xf8。寄存器中 x0 为 0x28。源码中的输入回调没有等待 ImGui 初始化完成，就直接调用 Android ImGui 输入后端；而 ImGui 初始化和渲染在另一线程进行。

由此可以确认源码存在两个独立问题：初始化前进入 ImGui 输入处理的可能性，以及输入回调线程与渲染线程同时使用 ImGui 的可能性。当前地址形态与空 Context 派生出无效 IO 指针相符，但缺少本次崩溃同一构建的可用 libAndroid.so / 符号文件，不能把帧偏移直接认定为某个已完成符号化的函数或源代码行。

此外，AOSP MotionEvent::copyFrom 的返回类型为 void，最后一个参数为 bool；原回调声明与该类型不一致。类型需要遵守真实 ABI，但本隔离包不会提供新的私有 Hook 绑定实现。

窗口交给异步线程前的独立引用持有、初始化标志的并发访问、GPU 工作完成与 SurfaceControl 提交、失败路径资源释放，也需要单独核对。这些是额外风险，不是已由本日志证明的直接崩溃原因。

## 使用

只需要 Python 3.10 或更新版本的标准库；脚本本身完全离线。

```sh
python3 isolate_input.py /path/to/jni.zip --output "$HOME/jni_input_isolated.zip"
```

请将输出放在支持硬链接的 Linux 文件系统，例如 Termux 的私有 HOME 目录，不要直接放在 Android 的模拟共享存储。脚本使用原子硬链接发布，避免覆盖已有输出。可在生成后自行复制 ZIP 到共享存储。

脚本将拒绝已存在的输出、原路径覆盖、目录穿越、符号链接、重复条目、不熟悉的源码结构及超过限制的压缩包；不会猜测并强行改写文件。运行成功会打印原始压缩包、修改前后源码及输出压缩包的 SHA256。生成的 ZIP 内含 `_CRASH_ISOLATION_REPORT.json`，明确写明触摸已停用、Android 构建及实机运行未验证。

之后可用项目原有构建流程编译隔离副本进行对照；本包不附加任何加载、注入或系统权限修改命令。

## 测试和未完成项

GitHub Actions 只运行本包的 Python 单元测试，使用人工构造的微型 ZIP 测试数据，不使用、不上传原项目源码或二进制。测试覆盖内容保持、CRLF、重复隔离、陌生源码拒绝、禁止覆盖以及路径穿越拒绝。实际结果见同包 `validation.log` 和 `VALIDATION.json`。

这不等于：原始 jni.zip 已被在服务端完整合并；原始项目已通过 NDK 编译和最终链接；原手机上的崩溃已消失；菜单触摸恢复；窗口及 GPU 生命周期问题全部修复。以上均未验证。

## 正确的后续修复结构

在自己控制的应用与公开输入接口中，输入线程只同步复制事件的数值到有界队列；渲染线程在上下文及后端初始化成功后，在 NewFrame 前消费队列；销毁前停止接收并清空队列。不要异步保存借用的 AInputEvent 指针，不要在输入回调线程直接访问渲染线程的 ImGui 对象。私有平台 ABI 不能当作稳定公开接口。

参考：
- Android Native Window: https://developer.android.com/ndk/reference/group/a-native-window
- Android SurfaceControl: https://developer.android.com/ndk/reference/group/native-activity
- AOSP Input: https://android.googlesource.com/platform/frameworks/native/+/refs/heads/main/libs/input/Input.cpp
- Dear ImGui: https://github.com/ocornut/imgui
