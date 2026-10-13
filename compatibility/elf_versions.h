/*
 * Elf64 GNU symbol-version metadata reader for Android/AArch64.
 * Standalone C11 component; no AOSP code copied.
 *
 * Callers provide bounded, already-validated mapped views of DT_VERSYM,
 * DT_VERNEED, DT_VERDEF and DT_STRTAB, not untrusted pointers directly.
 * Return convention: -1 malformed, 0 absent/not matched, 1 found/matched.
 */
#ifndef CUSTOM_ELF_VERSIONS_H
#define CUSTOM_ELF_VERSIONS_H
#include <elf.h>
#include <limits.h>
#include <stddef.h>
#include <stdint.h>
#include <string.h>

#define CV_VERSYM_HIDDEN UINT16_C(0x8000)
#define CV_VERSYM_INDEX UINT16_C(0x7fff)
#define CV_VERIDX_GLOBAL UINT16_C(1)
#ifndef VER_NEED_CURRENT
#define VER_NEED_CURRENT 1
#endif
#ifndef VER_DEF_CURRENT
#define VER_DEF_CURRENT 1
#endif

typedef struct {
  const uint16_t *versym;
  size_t versym_count;
  const uint8_t *verneed;
  size_t verneed_size;
  size_t verneed_count;
  const uint8_t *verdef;
  size_t verdef_size;
  size_t verdef_count;
  const char *dynstr;
  size_t dynstr_size;
} cv_version_view;

typedef struct {
  const char *name;
  const char *needed_soname;
  uint16_t flags;
  uint16_t index;
} cv_version_requirement;

/* Only bounded copies: no alignment assumptions and no off+size overflow. */
static int cv_read_bytes(const uint8_t *p, size_t len, size_t off,
                         void *result, size_t bytes) {
  if (!p || !result || off > len || bytes > len - off) return -1;
  memcpy(result, p + off, bytes);
  return 0;
}
static int cv_get_dynstr(const cv_version_view *v, uint32_t idx, const char **out) {
  if (!v || !out || !v->dynstr || (size_t)idx >= v->dynstr_size) return -1;
  const char *s = v->dynstr + idx;
  if (!memchr(s, '\0', v->dynstr_size - idx)) return -1;
  *out = s;
  return 0;
}
static int cv_advance(size_t *offset, uint32_t delta, size_t limit) {
  if (!offset || !delta || *offset > limit || (size_t)delta > limit - *offset)
    return -1;
  *offset += delta;
  return 0;
}

/*
 * For an undefined dynsym index, return its requested version and DT_NEEDED
 * provider from DT_VERNEED / DT_VERSYM.  0 means no explicit version.
 * Do not use this to implement ELF search scope: honor DT_NEEDED and
 * RTLD_GLOBAL/LOCAL independently.
 */
static int cv_get_symbol_requirement(const cv_version_view *v, size_t sym_index,
                                     cv_version_requirement *out) {
  if (!v || !out) return -1;
  memset(out, 0, sizeof(*out));
  if (!v->versym) return 0;
  if (sym_index >= v->versym_count) return -1;
  uint16_t idx = (uint16_t)(v->versym[sym_index] & CV_VERSYM_INDEX);
  if (idx <= CV_VERIDX_GLOBAL) return 0;
  if (!v->verneed || v->verneed_count == 0 || !v->dynstr) return -1;
  if (v->verneed_count > v->verneed_size / sizeof(Elf64_Verneed)) return -1;

  size_t pos = 0;
  for (size_t i = 0; i < v->verneed_count; ++i) {
    Elf64_Verneed vn;
    if (cv_read_bytes(v->verneed, v->verneed_size, pos, &vn, sizeof(vn)) ||
        vn.vn_version != VER_NEED_CURRENT || vn.vn_cnt == 0 ||
        vn.vn_aux < sizeof(vn)) return -1;
    const char *soname = NULL;
    if (cv_get_dynstr(v, vn.vn_file, &soname)) return -1;
    size_t auxpos = pos;
    if (cv_advance(&auxpos, vn.vn_aux, v->verneed_size)) return -1;
    for (uint16_t j = 0; j < vn.vn_cnt; ++j) {
      Elf64_Vernaux aux;
      if (cv_read_bytes(v->verneed, v->verneed_size, auxpos, &aux, sizeof(aux)))
        return -1;
      const char *name = NULL;
      if (cv_get_dynstr(v, aux.vna_name, &name)) return -1;
      if ((aux.vna_other & CV_VERSYM_INDEX) == idx) {
        out->name = name;
        out->needed_soname = soname;
        out->flags = aux.vna_flags;
        out->index = idx;
        return 1;
      }
      if (j + 1 != vn.vn_cnt &&
          (aux.vna_next < sizeof(aux) ||
           cv_advance(&auxpos, aux.vna_next, v->verneed_size))) return -1;
    }
    if (i + 1 != v->verneed_count &&
        (vn.vn_next < sizeof(vn) ||
         cv_advance(&pos, vn.vn_next, v->verneed_size))) return -1;
  }
  return -1;  /* The versym index is present but has no version requirement. */
}

/*
 * Check whether the defined symbol at sym_index satisfies the required
 * version.  Implements Bionic's unversioned-provider and default-visible
 * version semantics, including global-only fallback if a requested
 * version isn't defined by the provider.
 */
static int cv_def_symbol_matches(const cv_version_view *v, size_t sym_index,
                                 const char *required_name) {
  if (!v) return -1;
  if (!v->versym) return 1;  /* Defining DSO has no version metadata. */
  if (sym_index >= v->versym_count) return -1;
  const uint16_t provided = v->versym[sym_index];
  if (!required_name) return (provided & CV_VERSYM_HIDDEN) == 0;
  if (!*required_name) return -1;

  uint16_t expected = CV_VERIDX_GLOBAL;
  if (v->verdef_count != 0) {
    if (!v->verdef || !v->dynstr ||
        v->verdef_count > v->verdef_size / sizeof(Elf64_Verdef)) return -1;
    size_t pos = 0;
    for (size_t i = 0; i < v->verdef_count; ++i) {
      Elf64_Verdef vd;
      if (cv_read_bytes(v->verdef, v->verdef_size, pos, &vd, sizeof(vd)) ||
          vd.vd_version != VER_DEF_CURRENT || vd.vd_cnt == 0 ||
          vd.vd_aux < sizeof(vd)) return -1;
      size_t auxpos = pos;
      if (cv_advance(&auxpos, vd.vd_aux, v->verdef_size)) return -1;
      for (uint16_t j = 0; j < vd.vd_cnt; ++j) {
        Elf64_Verdaux aux;
        if (cv_read_bytes(v->verdef, v->verdef_size, auxpos, &aux, sizeof(aux)))
          return -1;
        const char *name = NULL;
        if (cv_get_dynstr(v, aux.vda_name, &name)) return -1;
        if (strcmp(name, required_name) == 0) {
          expected = (uint16_t)(vd.vd_ndx & CV_VERSYM_INDEX);
          break;
        }
        if (j + 1 != vd.vd_cnt &&
            (aux.vda_next < sizeof(aux) ||
             cv_advance(&auxpos, aux.vda_next, v->verdef_size))) return -1;
      }
      if (expected != CV_VERIDX_GLOBAL) break;
      if (i + 1 != v->verdef_count &&
          (vd.vd_next < sizeof(vd) ||
           cv_advance(&pos, vd.vd_next, v->verdef_size))) return -1;
    }
  }
  return (provided & CV_VERSYM_INDEX) == expected;
}
#endif
