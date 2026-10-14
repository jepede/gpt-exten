/* SPDX-License-Identifier: MIT */
/*
 * Compatible helpers for embedding into an Android ARM64 user-space ELF loader.
 * This standalone module does not replace Bionic's soinfo, TLS module registry,
 * or the process startup ABI.
 */
#ifndef CUSTOM_LINKER_COMPAT_HARDEN_H
#define CUSTOM_LINKER_COMPAT_HARDEN_H
#include <stddef.h>
#include <stdint.h>
#ifdef __cplusplus
extern "C" {
#endif

/* Each successful dlopen acquisition must have a matching dlclose. */
typedef struct {
    void **items;
    size_t count;
    size_t capacity;
    size_t hard_limit;
} clh_handle_vector;

int clh_handles_init(clh_handle_vector *v, size_t hard_limit);
int clh_handles_push(clh_handle_vector *v, void *handle);
typedef void (*clh_close_fn)(void *handle, void *user);
void clh_handles_destroy(clh_handle_vector *v, clh_close_fn close_fn, void *user);

/*
 * Calls visit("/origin/dir/libX.so", user) for each nonempty DT_RUNPATH
 * component in original order. Callback: 0=continue, >0=stop, <0=abort.
 * Returns 0 (exhausted), 1 (stopped), or -1 (error).
 *
 * runpath_len comes from the checked ELF STRTAB: never scan past this bound.
 * No fixed-length buffer or silent truncation.
 * Supports both $ORIGIN and dollar-braced ORIGIN forms.
 * Caller still manages namespaces, DT_NEEDED order and RTLD_* semantics.
 */
typedef int (*clh_path_visit_fn)(const char *candidate, void *user);
int clh_foreach_runpath(const char *runpath, size_t runpath_len,
                       const char *origin, const char *soname,
                       clh_path_visit_fn visit, void *user);

/*
 * Validate PT_TLS before copying to caller-owned TLS storage. Caller passes
 * actual TLS buffer base so p_align can be checked. Return 1=valid, 0=reject.
 * This prevents buffer overwrite but does not create a Bionic TLS module.
 */
int clh_tls_image_fits(uint64_t p_filesz, uint64_t p_memsz, uint64_t p_align,
                       uint64_t destination_offset, uintptr_t area_base,
                       size_t area_capacity);

#ifdef __cplusplus
}
#endif
#endif
