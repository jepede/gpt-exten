# Android / ImGui 输入崩溃：证据与条件补丁工具包

日期：2026-10-10。状态：**诊断与条件源码补丁工具，不是用户原工程的完整修复压缩包。**

## 先看边界

本包没有包含、解压或修改用户上传的原始 `jni.zip`；也没有编译或运行原始项目。当前会话的本地执行服务持续返回 ClientError，因此不能假称原项目已修复。这里交付的是离线工具：在您自己的机器上读取原 ZIP，识别标准 ImGui Android 后端，满足严格前置条件时插入一个上下文保护，并保留所有其他原文件内容。

**不能把本包的单元测试通过，解释为您的 Android 项目已编译成功或真机不再崩溃。**

## 从 tombstone 能确定的事实

崩溃帧模块为 `libAndroid.so`。前三个相对 PC：`0x5297c`、`0x899cc`、`0x4a92c`。输入事件链中可见 `android_view_MotionEvent_obtainAsCopy`。

故障 PC 对应的 ARM64 指令字为 `0xf9406808`：

```asm
ldr x8, [x0, #0xd0]
```

寄存器 `x0 = 0x28`，所以本次加载地址为：

```text
0x28 + 0xd0 = 0xf8
```

这与日志中的 `SIGSEGV / SEGV_MAPERR / fault addr 0xf8` 一致。包内 `decode` 子命令可复核指令位域，使用纯 Python 标准库。

紧接着的指令字 `0xb9141101` 对应向通过该指针取得的对象写入整型参数，形态与 ImGui `ImGuiIO::AddMouseSourceEvent()` 的 `Ctx` 访问及鼠标来源设置高度吻合。官方 ImGui Android 后端先取得 `ImGui::GetIO()`，再根据 MotionEvent 工具类型调用 `AddMouseSourceEvent()`。这是源码对照推断，不是使用崩溃时同一构建的符号文件确认的函数名；也尚不能区分初始化过早、销毁后回调、上下文切换、跨线程竞争或对象损坏。

参考代码：Dear ImGui 官方仓库 `ocornut/imgui`，标签 `v1.91.9b` 的 `backends/imgui_impl_android.cpp`、`imgui.cpp`。此参考版本不代表用户项目的实际版本。

## 使用方法

需要 Python 3.10 或更高版本。工具不联网、不执行 ZIP 内代码、不运行项目构建脚本、不向磁盘解压原工程，也不会覆盖原 ZIP。

把 `toolkit.py` 与 `jni.zip` 放在同一目录，先读取源码位置清单：

```sh
python3 toolkit.py audit jni.zip > source_audit.json
```

在能识别标准后端时，生成带有限保护的新工程压缩包：

```sh
python3 toolkit.py patch jni.zip -o jni_context_guard_unverified.zip
```

输出名字刻意带 `unverified`：表示原项目尚未做编译和真机验证。这个文件只有在命令实际成功后才会生成，不在本工具包中预先伪造。

存在多个 `imgui_impl_android.cpp` 时，工具会拒绝猜测。根据 `audit` 输出，显式选择真正参与构建的后端路径：

```sh
python3 toolkit.py patch jni.zip \
  --member 'jni/imgui/backends/imgui_impl_android.cpp' \
  -o jni_context_guard_unverified.zip
```

上面的成员路径只是示例，必须替换为 `audit` 返回的真实路径。若项目采用非标准函数签名、函数开头不是预期的 GetIO、编码不是 UTF-8、或存在多个函数定义，工具会停止，不会盲改。

复核本次故障指令：

```sh
python3 toolkit.py decode --instruction 0xf9406808 --base-value 0x28
```

## 条件补丁究竟做了什么

只在标准 `ImGui_ImplAndroid_HandleInputEvent()` 函数体的最前面、任何 `ImGui::GetIO()` 之前，插入：

```cpp
if (input_event == nullptr || ImGui::GetCurrentContext() == nullptr)
    return 0;
```

工具会识别实际参数名称，并保留 UTF-8 BOM、CRLF 换行以及其他文件原始内容。返回 0 表示此后端没有处理该事件；上层回调仍需正确遵守原框架的输入分发约定。

生成的新 ZIP 保留原有文件路径、逐文件内容（仅目标源码改变）以及可保留的 ZIP 元数据；重打包后的 ZIP 字节不保证与原压缩编码一致。额外添加：

- `.imgui_context_guard/PATCH.diff`：精确改动。
- `.imgui_context_guard/REPORT.json`：输入 ZIP、改动前后源码的 SHA256，以及明确的未验证状态。
- `.imgui_context_guard/SHA256SUMS`：逐文件校验表。
- `.imgui_context_guard/README.txt`：补丁边界。

## 这个保护仍然没有解决什么

单独检查空指针不是跨线程同步。检查后，另一线程仍可能销毁或切换上下文；`NewFrame/Render` 与输入写入也仍可能并发。这些问题需要结合原工程：把 ImGui 生命周期和使用固定在同一线程；或者让输入线程只复制事件数据，由 ImGui 所在线程消费；或者对完整的初始化、输入、渲染和销毁临界区采用统一同步。不能只在某一个输入函数中加锁就声称线程安全。

上层输入回调可能在调用此后端之前就访问 GetIO，本工具不会修改那个未知调用点。输入对象类型、ABI、生命周期和坐标变换也不在本补丁的修复范围内。不要保存已失效的原始事件指针供另一线程稍后使用。

若初始化根本未成功，这个保护最多避免该路径继续解引用，界面仍可能无法出现；不能把“不崩溃但没有 UI”称为完整修复。

## 真正完成修复仍需核验

使用**崩溃时相同构建**的未剥离 `libAndroid.so` 对 `0x5297c / 0x899cc / 0x4a92c` 符号化；不能用重新编译后的不同二进制套旧地址。日志缺少该模块 Build ID 时，应保留当时的二进制和对应符号产物，不能凭文件名认定一致。

```sh
/path/to/ndk/toolchains/llvm/prebuilt/linux-x86_64/bin/llvm-symbolizer \
  --obj=/path/to/matching-unstripped/libAndroid.so \
  0x5297c 0x899cc 0x4a92c
```

然后在原工程完成生命周期修正、Android NDK 编译和目标设备验证。应覆盖：启动后立即触摸、首帧之前的输入、多指输入、切后台再恢复、旋转或表面重建，以及销毁/重建时的输入。上述实机检查没有在本会话执行。

## 本包测试与复现

`VALIDATION.txt` 是 GitHub Actions 上实际执行的测试输出；`DECODE.json` 是实际指令解码输出；`BUILD_INFO.json` 记录工作流和工具版本。测试只覆盖本工具及合成 C++ 测试夹具，并不覆盖用户原工程。

```sh
python3 -m unittest -v test_toolkit.py
```

完整测试还需要 `g++` 及其 AddressSanitizer / UndefinedBehaviorSanitizer 运行库。测试覆盖空事件、无上下文、正常上下文、上下文清除后的事件、源文件识别、BOM/换行保持、ZIP 非目标文件保持、拒绝覆盖、路径安全、以及指令解码。

`SHA256SUMS` 记录本工具包文件的 SHA256。自行运行 patch 后，终端还会打印新生成工程 ZIP 的 SHA256。
