# ARM64 Bionic linker compatibility edge cases

These fixtures exercise Android ABI behaviors that are easy to miss in normal linker pressure matrices. They do **not** contain any private custom-linker source/binary.

| Case | ABI boundary | Expected native stdout |
|---|---|---|
| `needed72` | 72 direct DT_NEEDED libraries | `EDGE_NEEDED72=2628` |
| `host_reverse` | dlopened plugin imports main executable function | `EDGE_HOST_EXPORT=42` |
| `host_tls` | plugin imports main executable TLS symbol | `EDGE_HOST_TLS=12` |
| `long_runpath` | DT_RUNPATH 1915 bytes; DSO in final directory | `EDGE_LONG_RUNPATH=2718` |
| `stripped_main` | stripped PIE, e_entry startup instead of main hint | `EDGE_STRIPPED_MAIN=12345` |
| `huge_tls` | 5 MiB PT_TLS, stresses fixed-size static TLS arenas | `EDGE_HUGE_TLS=163200` |

## Build

`python3 generate.py --ndk /opt/android-ndk-r28c --out ./fixtures`

In CI the workflow restores the two cached NDK r28c parts, validates their SHA256 hashes and runs native tests against the Android 36 Bionic sysroot with QEMU 7.2.22 at 4096 and 16384 guest page sizes.

## True packed regression (must use the private Phase2 packer/shell)

```bash
python3 packed_compare.py \
  --fixtures-dir ./fixtures \
  --packer /path/to/packer_linux_x86_64 \
  --shell /path/to/shell_android_arm64_api35 \
  --qemu /path/to/qemu-aarch64-static \
  --sysroot /path/to/android36/sysroot \
  --out ./packed-results \
  --repeats 3 --concurrent 4 --timeout 50
```

The script checks the Packer exit status, runs native and packed binaries for both guest page sizes, compares deterministic outputs and exit codes, and writes `edgecase-results.json`, `edgecase-results.tsv` and individual logs.

**Important:** The GitHub workflow's `copy_only_packer.py` is deliberately a wiring canary, NOT a custom linker, NOT encrypted packing, and its results cannot be counted as actual packed passes.

## Current source audit hypothesis (pending real packed execution)

- `shell/linker.h`: fixed 64 dependency handles; `linker.c` returns overflow error for additional DT_NEEDED.
- `shell/linker.c`: `char copy[1024]` truncates a 1915-byte DT_RUNPATH.
- `shell/linker.c`: `g_payload_tls_area` is 4 MiB, but `custom_payload_tls_init_current` copies `PT_TLS.p_filesz` without a capacity check. Protect the boundary before attempting to scale.
- Bionic does not see a manually mapped main payload as a real soinfo, which can affect backward symbol lookup from dlopened libraries and TLS module identities.
- A stripped PIE without a saved main hint may end up calling `_start` as if it were a normal C function rather than with the process-entry ABI.

Use the real packed runner to turn each hypothesis into a measured failure or pass. Keep private Packer/Shell artifacts local; do not upload them to public GitHub Actions.
