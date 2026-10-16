# Delta Force 1.201.37117.67 — ACE coordinate callback vs runtime Hook: verified facts

Research date: 2026-10-16. All target code addresses below are **libUE4.so-relative virtual addresses (RVA)**, *not* device absolute addresses.

## Reproducible identity and analysis

- APK: `DeltaForce-CN-Android-v1.201.37117.67.apk`, 1,519,215,938 bytes, SHA256 `af03179c62ac57f05e4e6d425b2471bdf651b46c2f5a636f5a9e3fa94c78337d`.
- Extracted `lib/arm64-v8a/libUE4.so`: 566,193,496 bytes, SHA256 `387cd911a67eca1069bd5e4c874bce5dfb14823ca75f55f1ae7c43a09f2f1441`.
- The APK was restored from 4 valid cached Actions Artifacts (run 38596903200), not downloaded anew from Tencent CDN.
- ELF `.text` and `.rodata` bytes were XOR-decoded with 0xE2 to a **scratch** copy for analysis only. Other ELF sections were not modified.
- Independent audit runs:
  - [Primary full .text scan](https://github.com/jepede/gpt-exten/actions/runs/38885471543)
  - [Independent 9-site baseline check](https://github.com/jepede/gpt-exten/actions/runs/38886407697)
  - [Actual callback registrar trace](https://github.com/jepede/gpt-exten/actions/runs/38886914854)
- Source scripts: `tools/deltaforce_ace_hook_static.py`, `tools/deltaforce_ace_hook_fast.py`, `tools/deltaforce_ace_init_trace.py`.

## 1. Old public Hook offset does not identify the current code's trampoline

A public *different-version* emulator repository claims `libUE4.so+0x0D1FBB84` is a detour. However, for **this exact APK**, XOR-unmasked instructions are:

```asm
0x0D1FBB60  sub  sp, sp, #0xB0
0x0D1FBB64  str  x25, [sp, #0x60]
...
0x0D1FBB84  mov  x19, x1
0x0D1FBB88  ldr  x8, [x23, #0x28]
0x0D1FBB8C  mov  x20, x0
0x0D1FBB90  stur x8, [x29, #-0x48]
0x0D1FBB94  add  x8, sp, #0x18
0x0D1FBB98  ldr  x9, [x10, #8]!
```

Exact decoded words at 0x0D1FBB84: `F30301AA E81640F9 F40300AA A8831BF8`.

They are not the `LDR X16; BR X16; .quad destination` trampoline. The independent audit also reports **0 matches** of the exact literal-8/X16/BR signature (`5000005800021fd6`) in the raw or XOR E2-decoded `.text`, and 0 matches of the corresponding X17 variant. This is an exact-pattern negative result only: it does not exclude another trampoline form or later runtime mutation.

The same public project author acknowledges its UE4 offsets are illustrative/mutated: https://github.com/libtersafe/dfm_android_unicorn/issues/1

## 2. Verified engine-installed 12-byte coordinate callback

The exact recovered instructions in current `libUE4.so`:

```asm
; Within the function 0x104F7284–0x104F735C
0x104F7334  adrp x8, 0x20258000
0x104F7338  str  x0, [sp]
0x104F733C  add  x0, sp, #8
0x104F7340  ldr  x9, [x8, #0xDB8]   ; x9 = *(u64*)(module+0x20258DB8)
0x104F7344  ldr  x8, [sp]
0x104F7348  mov  w1, #0xC          ; 12-byte result
0x104F734C  add  x2, x8, #0x28     ; pointer to 4-byte protection record
0x104F7350  blr  x9
0x104F7354  ldr  x0, [sp]
0x104F7358  b    0x104F72D0
```

The protected component path around `0x104F72A4` first reads an object pointer at +0x180, calls the `0x104F6ECC` accessor (returns `x0+0x210`), copies 12 bytes from +0x10/+0x18 into a stack buffer, reads a global mode byte from +0x20258DC0 and checks mode==2, then checks a 16-bit field at protected data +0x28 is not 0xFFFF before invoking the above callback. The function later populates a transform-like output.

**An indirect call is not proof of a Hook.** It is a general callback mechanism until a post-initialization pointer overwrite to a different target is demonstrated.

## 3. Default function pointer registration — now proven on TWO independent initialization paths

**Initialization A** (0x13120490–0x13120538):
```asm
0x131204B8  adrp x8, 0x20258000
0x131204BC  adrp x9, 0x0AAE7000
0x131204C0  add  x9, x9, #0x8C     ; x9 = module+0x0AAE708C
0x131204CC  str  x9, [x8, #0xDB8] ; *(module+0x20258DB8) = x9
```

**Initialization B** repeats the same operation:
```asm
0x10C25AC0  adrp x8, 0x20258000
0x10C25AC4  adrp x9, 0x0AAE7000
0x10C25AC8  add  x9, x9, #0x8C
0x10C25AD4  str  x9, [x8, #0xDB8]
```

The default callback is therefore **UE4-internal `0x0AAE708C`**. This is proven through full ADRP+ADD effective address calculation plus the following STR, not by an unsupported individual-instruction xref.

Other co-registered callbacks:
| Data slot RVA | Function RVA | Verifiable source |
|---|---|---|
| 0x20258DC8 | 0x0AAE7088 | 0x131204A8–B4 |
| 0x20258DB8 | 0x0AAE708C | 0x131204B8–CC |
| 0x20257A60 | 0x0AAE7098 | 0x131204D0–E0 |
| 0x20258E10 | 0x0AAE7670 | 0x131204E4–F0 |
| 0x20257A68 | 0x0AAE7848 | 0x131204F4–500 |

The slot RVA 0x20258DB8 is in the zero-filled part of an RW PT_LOAD segment, not backed by initial file bytes (file-backed part of the segment ends at 0x1F7B0750, memory mapping ends at 0x20660878). Thus it is populated at runtime even with zero ACE modification.

## 4. Default callback is an index/flag dispatcher

```asm
0x0AAE708C  ldrb w3, [x2, #3]
0x0AAE7090  ldrh w2, [x2]
0x0AAE7094  b    0x0AAEA4E4

0x0AAEA4E4  tbz  w3, #0, 0x0AAEA53C
0x0AAEA4FC  and  w19, w2, #0xffff
0x0AAEA500  tbz  w19, #12, 0x0AAEA52C
...
0x0AAEA6EC  [index-based pool lookup and data copy]
```

Previous isolated Unicorn synth tests support the 12-byte vector recovery branch, but **not** a live ACE-injected Hook: only explicit synthetic registers, memory tables and stubbed external context were tested.

## 5. What is proven and what is NOT

**Proven for this exact stock APK:** Protected vector-related types; stock `.text` XOR E2 protection; engine-provided callback dispatcher and initialization; 12-byte callback used by transform reader; old public RVA mismatch; absence of the *specific* X16 8-byte literal trampoline form on disk.

**Not proven:** Current runtime ACE inline patch address; which ACE library/page installs or owns that patch; post-init contents of +0x20258DB8; presence of a 940KB injected blob; hook entry / return trampoline; actual encrypted enemy coordinate sample or real-output control data; whether ACE rebinds this callback after native initialization.

To establish an ACE runtime Hook, a read-only synchronized authorized process snapshot is required, including: executable original RVA bytes and adjacent code after runtime startup; mapped module ownership; anonymous executable region mappings and bytes if present; current callback slot and other co-registered pointer values; and time/provenance of any executable-page writes. Analyze BTI/PAC/AUT instructions and normal PLT veneers before classifying `BR`/`BLR` as a Hook. Tag-looking high address byte alone does not certify MTE.

Public background (unverified current offsets): https://github.com/libtersafe/dfm_android_unicorn

## Summary

For version 1.201.37117.67, **the actual statically demonstrated coordinate redirection is a built-in UE4 callback table**. Its index-based data restore implementation is verified in static ARM64 code and isolated emulation. **ACE post-startup Hooking remains an open runtime question, not a completed reverse-engineering claim.**
