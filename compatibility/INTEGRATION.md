# Custom Linker: Android ARM64 compatibility modules (work branch)

These **standalone** C11 components address testable ABI parsing/mapping primitives.
They do **not** patch the uploaded private `shell/linker.c`: that ZIP is not
present in this public GitHub repository. Never label this bundle a fully
compatible production linker.

## Verified CI

- [Standalone native GCC/Clang ASan/UBSan regression](https://github.com/jepede/gpt-exten/actions/runs/38434886312) — PASS.
- [Android NDK r28c / API 28 / AArch64 LLD real-ELF APS2](https://github.com/jepede/gpt-exten/actions/runs/38435474384) — PASS:
  - Retrieved both previously cached NDK r28c parts; both SHA256 verified.
  - Reassembled NDK archive SHA256 verified; **no new NDK download**.
  - Compiled C11 compatibility tests into arm64-v8a Android object files.
  - Linked an actual arm64-v8a Android shared object with `-Wl,--pack-dyn-relocs=android`.
  - `DT_ANDROID_RELA=0x450`, `DT_ANDROID_RELASZ=147 bytes`.
  - `cv_walk_aps2_rela` decoded 100 LLD-generated AArch64 relocations successfully.
- These checks are **not** an Android device or complete shell-loader execution test.

## Components

| File | What it provides | What it does NOT provide |
|---|---|---|
| `aps2_decoder.h` | Bounded signed LEB128/group decoder | Actual relocation writes |
| `arm64_aps2_rela.h` | Streaming APS2 → `Elf64_Rela` callback, no full table buffer | DSO symbol resolution, dynamic TLS |
| `elf_versions.h` | Bounded `DT_VERSYM`, `DT_VERNEED`, `DT_VERDEF` lookup/match | Search-order / `RTLD_NEXT` / namespace semantics |
| `elf_load_plan.h` | PT_LOAD validation, 4K/16K mapping-mode detection, anonymous segment copy | Page permissions, RELRO, memory tagging, BTI |
| `*_test.c` and `aps2_elf_inspect.c` | Unit and real ELF format regression | Real Android process integration |

## Main loader integration sequence

1. **Dynamic parser** (`shell/linker.c:parse_dynamic`): save `DT_ANDROID_RELA`
   and `DT_ANDROID_RELASZ`, `DT_VERSYM`, `DT_VERNEED`,
   `DT_VERNEEDNUM`, `DT_VERDEF`, `DT_VERDEFNUM`, alongside existing
   `DT_RELA`, `DT_JMPREL` and `DT_RELR`. Convert each `d_ptr` from ELF
   virtual address with the loaded module's load bias; verify the resulting
   pointer and reported length against mapped PT_LOAD segments.
2. **Relocation phase**: apply RELR, APS2, ordinary RELA and PLT RELA in the
   expected dependency order. Supply `cv_walk_aps2_rela` with the APS2
   byte range, a maximum relocation count, loaded image vaddr envelope and
   a callback that invokes the **existing** per-RELA handler. Bounds-check
   the destination against the **actual** mapped PT_LOAD ranges, not merely
   the envelope; validate relocation type, width, symbol index and TLS
   module before any writes. On malformed streams, abort the load and
   release all mappings. Do not blindly process overlapping relocation
   ranges twice.
3. **GNU symbol versions**: get undefined symbol requirements from
   `cv_get_symbol_requirement`. For custom DSO candidates use
   `cv_def_symbol_matches`; for Bionic-managed dependencies resolve through
   `dlvsym` where appropriate. Evaluate provider selection, DT_NEEDED
   scope, global/local groups and weak symbol fallback **separately**:
   version matching alone does not implement lookup scope.
4. **4K / 16K PT_LOAD**: preflight with `cv_plan_loads`. When the runtime
   page size exceeds an ELF's alignment, don't MAP_FIXED each 4K segment
   on 16K pages. Reserve anonymous RW image space (+ a full kernel page
   if selecting an alignment shift), choose an eligible RX/RW boundary,
   optionally compute shift with `cv_bias_shift_for_boundary`, copy
   PT_LOAD bytes with a complete-read callback into the reserved image
   via `cv_copy_loads`, relocate and then apply correct final RX, R,
   RW and GNU_RELRO permissions. A special two-region/RELRO scheme is
   required for mixed-permission 16K pages; **this bundle does not include
   the protection-phase code or a safe RWX fallback**.
5. **Entry and TLS are not solved** by these components. Executing `_start`
   with an invented C signature is not Android PIE startup; synthetic
   `__tls_get_addr` wrappers cannot register modules into Bionic's
   private linker TLS-module array. Do not claim parity before actual
   Android/Arm64 device tests.

## Regressions still required on the private main project

- Android API 28, 30, 33, 35 and 36 on 4K and 16K devices/emulators.
- ET_DYN PIE with/without PT_INTERP, `-fno-plt`, `-Wl,-z,relro,-z,now`.
- LLD APS2, RELR, normal RELA, weak/global/versioned symbols, GNU+SYSV hash.
- C++ unwind (`.eh_frame`, cross-DSO exceptions), `dl_iterate_phdr`,
  `dladdr`, `RTLD_NEXT`, global/local dependency scopes.
- TLS GD/LD/IE/LE, TLSDESC, threads, destructors, DSO unload and reload.
- BTI/PAC, 16K mixed segment permissions, GNU_RELRO and BSS.

## Upstream reference

- Official AOSP Bionic: `android-15.0.0_r36`,
  `android-16.0.0_r2` (both pinned in the repository's artifact cache).
- `linker/linker_relocate.cpp`, `linker/linker_soinfo.cpp`,
  `linker/linker_tls.cpp`, `linker/linker_phdr.cpp`,
  `linker/linker_phdr_16kib_compat.cpp`.
- 16K compat loader reads segments into anonymous RW memory because fixed
  file mappings aligned to 16K can overwrite neighboring 4K segments.

Everything in `compatibility/` is independently authored test and adapter
code, not pasted AOSP implementation.
