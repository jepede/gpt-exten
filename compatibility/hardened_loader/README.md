# Android ARM64 custom linker — bounded-loader compatibility helpers

This package is a **standalone source module**, not a claim that the user's
private Phase2 shell/linker.c has been modified. The public repository does
not contain any private uploaded linker source.

## Component-level fixes

1. A dynamically growing dependency handle vector with a caller-selected
   hard limit replaces the problematic 64-entry fixed array. It preserves
   ordering and releases references in reverse acquisition order.
2. RUNPATH parsing has no 1024-byte truncation. The implementation uses an
   already checked DT_STRTAB length, supports $ORIGIN and its braced form,
   and preserves search order.
3. PT_TLS metadata is validated against caller-owned per-thread storage:
   p_filesz <= p_memsz, destination offset + length, required alignment,
   and pointer overflow. A 5 MiB TLS image is safely rejected when the
   available area is 4 MiB.

## Integration into the private Phase2 source

Compile compatibility/hardened_loader/compat_harden.c as part of the Shell
and include compat_harden.h.

Change each per-module DT_NEEDED collection from a fixed array to:

    clh_handle_vector needed = {0};
    if (clh_handles_init(&needed, 4096) < 0) {
        /* return a descriptive load error */
    }

For each successfully opened dependency:

    void *h = dlopen(resolved_path, existing_flags);
    if (!h) {
        /* abort and unwind */
    }
    if (clh_handles_push(&needed, h) != 0) {
        dlclose(h);  /* never leak an untracked reference */
        /* abort, release earlier handles, unwind */
    }

During final module teardown, after correct destructor coordination:

    static void close_one(void *h, void *ignored) {
        (void)ignored;
        dlclose(h);
    }
    clh_handles_destroy(&needed, close_one, NULL);

Keep Phase2's existing RTLD flags and loader lookup order; the example is
not intended to bypass Bionic namespace restrictions. Do not destroy handles
while another thread or module still requires them.

Validate DT_STRTAB before reading DT_RUNPATH and determine the origin from
the **original payload's directory**, not from the Shell stub. Then call:

    clh_foreach_runpath(dt_runpath, checked_len, original_origin,
                        needed_soname, candidate_cb, ctx);

The candidate pointer is temporary and valid only during callback execution.
Once a dlopen succeeds, keep its handle and stop iteration. Handle namespace
restrictions and other lookup fallback in your caller.

Before any TLS image copy, zero fill or TP-relative offset installation:

    if (!clh_tls_image_fits(phdr.p_filesz, phdr.p_memsz, phdr.p_align,
                             destination_offset, (uintptr_t)tls_area,
                             tls_area_capacity)) {
        /* fail closed instead of writing outside the TLS arena */
    }

Also validate source image bounds separately; this guard checks destination
buffer boundaries, not the source payload's file map.

## Important architectural limitations

This makes a huge TLS image safely reject when the arena is too small; it
does not dynamically register a larger TLS module with Bionic.

A native dlopened plugin that references symbols exported only by a manually
mapped main payload may fail without integration into the system soinfo global
group. Cross-module TLS needs correct module IDs and __tls_get_addr semantics.
A stripped PIE needs a full ELF entry-stack ABI; calling an arbitrary _start
with guessed arguments is unsafe.

This module does not replace namespace, RELRO, page permissions, symbol
version lookup, DT_SYMBOLIC, or C++ exception registration logic.

## Reproducible test

Workflow: .github/workflows/custom-linker-hardening.yml

- GCC strict compile and Clang ASan/UBSan on Linux x86_64
- Android NDK r28c API35 ARM64 PIE compilation
- Android 36 Bionic with qemu-aarch64, 4 KiB and simulated 16 KiB pages
- 8192 dependency references with reverse release
- 72-dependency capacity test with explicit 73rd rejection
- 101 RUNPATH entries, a last-entry hit, input longer than 1024 bytes
- 200,000 TLS boundary probes and 5 MiB-in-4 MiB rejection

These are helper-level tests, NOT full private Phase2 packed-runtime tests.

## License

Independently authored MIT-licensed helper implementation and tests.
