# Android NDK r28c / ARM64 / QEMU / GDB 实测指南

## 环境与边界

本仓库的调试探针使用 **Android NDK r28c Clang** 编译成 AArch64 Android/Bionic ELF，不是将 x86_64 ELF 直接丢给 GDB。经过 GitHub Actions Run 38642113778 的真实 CI 验证（Ubuntu 24.04 x86_64 / QEMU user-static 7.2.22 / GDB 15.1 / Android Bionic API36），21 项共 **18 PASS / 3 UNSUPPORTED / 0 FAIL**。

注意：CI 的结果不等同于 ChatGPT 当前容器的本地实测。当前容器 API 曾持续返回 ClientError，NDK 两份缓存 artifact 已下载至 /mnt/data，尚不能声称在本地成功解包安装。

## 缓存 NDK（无须重复下载 Google NDK）

- 缓存仓库：jepede/gpt-exten
- 缓存 run: 31684150811
- 分片 artifact id: 9174697344, 9174699121
- 分片校验值：6e87d3bb98c2bfcdb9a703affd174b85ef00fff69b9aa0056372f79046308fa1, bf9baef30047e4a7e1040034619728cce0b291d76e4d67b44a0d5d0554c0197c
- 原始 android-ndk-r28c-linux.zip: 722261334 bytes
- 完整 SHA256: dfb20d396df28ca02a8c708314b814a4d961dc9074f9a161932746f815aa552f

仓库内有 tooling/arm64-ndk-debug/install_ndk_from_cache.sh，检查两个 artifact 外层 ZIP、提取的每片及重组的完整 NDK ZIP SHA256 后，解压到 /opt/android-ndk-r28c（默认值）。依赖 unzip、sha256sum，预留充足磁盘空间。

## 源码与编译

源码：
- tooling/arm64-ndk-debug/probe.c: 基础/单步/条件断点、全局 watchpoint、线程、信号、mprotect、syscall、dlopen
- tooling/arm64-ndk-debug/probe_plugin.c: SO 构造函数、dlsym 目标、析构函数
- tooling/arm64-ndk-debug/build.sh: NDK Clang/LLVM 编译 Android AArch64 ELF + SO
- tooling/arm64-ndk-debug/runner.py: 实际启动 QEMU、GDB 并验证停机证据，写出原始 stdout、stderr 和 results.json

编译（已安装 NDK 的主机）：

~~~bash
export NDK_ROOT=/opt/android-ndk-r28c
bash tooling/arm64-ndk-debug/build.sh
~~~

编译选项：-g3 -O0 -fno-omit-frame-pointer -fno-inline -fno-optimize-sibling-calls，Android API 28，ARM64。

## 在 QEMU User/Bionic 环境运行

假设 qemu-aarch64-static 和 gdb-multiarch 可执行，并已准备独立 Android Bionic sysroot（含 /system/bin/linker64、/apex/com.android.runtime/lib64/bionic/libc.so）。

~~~bash
SYSROOT=/path/to/android-bionic-rootfs
mkdir -p "$SYSROOT/data/local/tmp"
cp tooling/arm64-ndk-debug/build/probe \
   tooling/arm64-ndk-debug/build/libprobe_plugin.so \
   "$SYSROOT/data/local/tmp/"

python3 tooling/arm64-ndk-debug/runner.py \
  --qemu /usr/local/bin/qemu-aarch64-static \
  --gdb /usr/local/bin/gdb-multiarch \
  --sysroot "$SYSROOT" \
  --elf "$PWD/tooling/arm64-ndk-debug/build/probe" \
  --logs "$PWD/ndk-debug-logs" \
  --environment "local x86_64"
~~~

如果 GDB 是 portable 包，--gdb 指向解压后的 gdb-multiarch.sh；不应把 Android ELF 用系统 glibc ld-linux 来加载。

## CI 实际测试结果（Run 38642113778）

| Test | Result |
|---|---|
| basic_run | PASS |
| write_run | PASS |
| read_run | PASS |
| threads_run | PASS |
| dlopen_run | PASS |
| mprotect_run | PASS |
| syscalls_strace | PASS |
| breakpoint_main | PASS |
| hardware_exec | PASS |
| conditional_break | PASS |
| step_registers | PASS |
| memory_edit | PASS |
| finish_backtrace | PASS |
| thread_break | PASS |
| software_watch | PASS |
| hardware_watch_user | UNSUPPORTED |
| hardware_rwatch_user | UNSUPPORTED |
| hardware_awatch_user | UNSUPPORTED |
| trap_signal | PASS |
| segv_signal | PASS |
| aarch64_brk_signal | PASS |

QEMU User 模式的 GDBstub 不支持硬件内存读/写访问监视点，这是 QEMU TCG User 模式架构限制。其 hbreak 执行断点可以使用。软件 watchpoint 可借助 GDB \`set can-use-hw-watchpoints 0\` 实现，但有性能开销。需要硬件式 read/write/access watchpoints 时，应使用 QEMU System TCG + 对应 ELF/内核 GDBstub，在另一套环境独立测试。

## 已验证产物

- GitHub Run: https://github.com/jepede/gpt-exten/actions/runs/38642113778
- Artifact: arm64-ndk-r28c-debug-validation
- Artifact ID: 11931276591
- SHA256: 9b0c29cc200a5ae2d9f1880d065238dd5508cbd1fdeb4bd033c0a51865164d1d
- 实际 GitHub Expires At: 2027-01-12T21:40:57Z
- ELF SHA256: 19f6263f1829adb9728654f9d2757ba8eaf625d8d5231ce259b298b5a6cbcf70
- SO SHA256: c21aba09005579b57f740bfd576266860ef6552a0c74a78ca67b3264f4d50789

证据 ZIP 内包含构建日志、21 项的独立 GDB/QEMU 原始日志、results.json、C 源码、编译好的 ELF/SO 和重建脚本。原始研究目标 unknown.so 未被修改；本次运行的是专门编写的 ARM64 调试探针。
