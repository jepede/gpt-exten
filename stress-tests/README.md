# Android ARM64 Custom Linker 压力回归样本

此目录只包含**可公开的独立测试样本及脚本**，没有上传用户私有的 Packer/Linker 源码或 ELF。

## 依赖与版本

- Linux x86_64
- Android NDK r28c（Clang + LLD）
- Android API 35 目标（脚本可以 --api 调整）
- QEMU user-mode AArch64（缓存 7.2.22）
- 实际 ARM64 Android Bionic sysroot（这里使用 Android 36，包含 linker64/libc/libdl/libm）
- 用户私有的 `packer/packer` 和 `shell/shell`（加壳对照必需）

## 测试覆盖

| 样本 | 负载 | 验证 |
|---|---|---|
| reloc_rela | 8192 × scale 指针重定位 | 相对指针全部命中 |
| reloc_aps2 | 相同数据，LLD Android packed reloc | DT_ANDROID_RELA 标签存在且可运行 |
| reloc_relr | 相同数据，RELR | DT_RELR 标签存在且可运行 |
| reloc_aps2_4k | 4KiB 对齐的 APS2 ELF | 16KiB Guest 下的兼容性差异 |
| thread_tls | 24 线程、每线程 8192 轮 TLS 修改 | 线程数据隔离、正常退出 |
| big_bss | 32MiB BSS，8192 个页级触点 | 数值校验 |
| dlopen_repeat | 256 次 dlopen/dlsym/dlclose | 地址解析与依赖生命周期 |
| needed_chain | 3 级 DT_NEEDED，16384 次依赖调用 | 符号解析一致性 |
| constructors | 256 × scale 个初始化函数、析构记录 | C ABI 初始化生命周期 |
| ifunc_weak | IFUNC + 未定义弱符号 | 符号选择与弱符号返回值 |
| cpp_catch | 跨 DSO C++ 3000 次调用/1500 次异常 | 异常传播和 unwind |
| dlopen_mt | 8 线程并发共 2048 次 dlopen/dlsym/dlclose | Loader 锁、句柄生命周期与 TLS |
| tls_dtor | 48 线程，跨共享库 thread_local 析构计数 | __cxa_thread_atexit 与跨 DSO TLS 生命周期 |
| phdr_self | 使用 dl_iterate_phdr 覆盖主程序 main 指令地址 | ELF 模块清单、load bias 与 PHDR 正确性 |
| vers_main | 同名双版本导出 VERS_1/VERS_2 | GNU symbol version |

生成的所有 C/C++ 测试源文件和编译、执行日志会保存在 `--out`。

## 加壳回归（本机）

```bash
python3 stress-tests/stress_suite.py \
  --ndk /path/to/android-ndk-r28c \
  --qemu /path/to/qemu-aarch64-static \
  --sysroot /path/to/android36/sysroot \
  --packer /path/to/custom_linker_compat_phase2/packer/packer \
  --shell /path/to/custom_linker_compat_phase2/shell/shell \
  --api 35 --scale 1 --repeats 3 --timeout 90 \
  --out /tmp/linker-pressure-4k
```

使用 `--page16k` 独立验证 QEMU 16KiB Guest（并非 16KiB 真机）。`--scale 4` 表示 32768 指针重定位和 1024 个构造函数。

不提供 `--packer` 与 `--shell` 时只进行**原生基线测试**，不会将基线结果冒充加壳结果。加壳模式按以下条件判断：Packer 正常退出，原生与加壳程序均正常退出，忽略带 `[LINKER]`/ `[SHELL]` 前缀的调试日志后 stdout 一致。另有七类损坏 ELF 负面测试，检查 Packer 必须拒绝。

## 原生 16KiB 边界说明

Android/Bionic 可能拒绝 PT_LOAD `p_align=4096` 的 ELF，这是原生 linker 的预期行为，不应将其记为可运行测试。脚本会在 `--page16k` 模式下把 `reloc_aps2_4k` 标记为 `native_rejection_expected`，并检查实际被拒绝。若指定加壳模式，则另要求壳能够运行该场景；该项应视为**扩展兼容性**，不是原生/加壳 stdout 一致性。

## 诊断与局限

`results.json` 每轮保存退出码及比较结果；`logs/*.native.N.log` 和 `logs/*.packed.N.log` 保存完整 stdout、stderr，日志中含调用命令，方便 GDB 复现。QEMU 的 Guest 模拟无法代替真实 Android 的 linkerconfig、SELinux、bionic 所有 API 版本行为。所有异常或超时都按失败计数，不能用原生退出码等于加壳退出码替代语义比较。

## 测试结果真实性

现有 GitHub Actions 的 `stress-native-reference` Job **只运行原生 Bionic 基线**，没有传入 `--packer/--shell`，不得称为加壳兼容性结果。必须提供实际 Phase2 私有 Packer 与 Shell 可执行文件，在对应 Android/Bionic rootfs 中用 `--packer --shell` 跑通并取得 `packed_mode=true` 的 `results.json` 后才能汇报加壳通过率。
