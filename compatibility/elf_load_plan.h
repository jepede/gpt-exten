/*
 * 4KiB / 16KiB Android ELF64 PT_LOAD mapper preflight and anonymous image copy.
 * This is a reusable planning component, not a replacement for mapping final
 * permissions, RELRO, AArch64 BTI, TLS or the Android linker namespace.
 *
 * Unlike MAP_FIXED over each segment, the anonymous-copy path does not
 * overwrite neighboring 4KiB segments sharing one 16KiB kernel page.
 * Callers allocate an anonymous RW reservation, copy through cv_load_copy(),
 * relocate, then apply a separately verified page-permission/RELRO plan.
 * Standalone C11 component; no project-private source material.
 */
#ifndef CUSTOM_ELF_LOAD_PLAN_H
#define CUSTOM_ELF_LOAD_PLAN_H
#include <elf.h>
#include <stddef.h>
#include <stdint.h>
#include <string.h>

enum {
  CV_LOAD_INVALID = -1,
  CV_LOAD_DIRECT = 0,
  CV_LOAD_ANON_COMPAT = 1
};
typedef struct {
  uint64_t min_vaddr;
  uint64_t max_vaddr; /* Exclusive */
  uint64_t conflict_page;
  size_t first_segment;
  size_t second_segment;
  size_t load_count;
} cv_load_plan;

static int cv_is_power2(uint64_t n) { return n && ((n & (n - 1)) == 0); }

static int cv_align_up(uint64_t n, uint64_t size, uint64_t *aligned) {
  if (!aligned || !cv_is_power2(size) || n > UINT64_MAX - (size - 1))
    return -1;
  *aligned = (n + size - 1) & ~(size - 1);
  return 0;
}

static int cv_plan_loads(const Elf64_Phdr *phdr, size_t n, uint64_t file_len,
                         uint64_t kernel_page, cv_load_plan *out) {
  if (!phdr || !out || !cv_is_power2(kernel_page) || kernel_page < 4096 ||
      n == 0 || n > 65536) return CV_LOAD_INVALID;
  memset(out, 0, sizeof(*out));
  out->first_segment = out->second_segment = SIZE_MAX;
  out->min_vaddr = UINT64_MAX;
  int mode = CV_LOAD_DIRECT;
  for (size_t i = 0; i < n; ++i) {
    const Elf64_Phdr *a = phdr + i;
    if (a->p_type != PT_LOAD || a->p_memsz == 0) continue;
    if (a->p_filesz > a->p_memsz ||
        a->p_offset > file_len || a->p_filesz > file_len - a->p_offset ||
        a->p_vaddr > UINT64_MAX - a->p_memsz) return CV_LOAD_INVALID;
    if (a->p_align > 1 &&
        (!cv_is_power2(a->p_align) ||
         ((a->p_vaddr ^ a->p_offset) & (a->p_align - 1)) != 0))
      return CV_LOAD_INVALID;
    ++out->load_count;
    uint64_t first = a->p_vaddr & ~(kernel_page - 1);
    uint64_t last;
    if (cv_align_up(a->p_vaddr + a->p_memsz, kernel_page, &last))
      return CV_LOAD_INVALID;
    if (first < out->min_vaddr) out->min_vaddr = first;
    if (last > out->max_vaddr) out->max_vaddr = last;
    if (a->p_align < kernel_page ||
        ((a->p_vaddr ^ a->p_offset) & (kernel_page - 1)) != 0)
      mode = CV_LOAD_ANON_COMPAT;
    for (size_t j = 0; j < i; ++j) {
      const Elf64_Phdr *b = phdr + j;
      if (b->p_type != PT_LOAD || b->p_memsz == 0) continue;
      uint64_t a_end = a->p_vaddr + a->p_memsz;
      uint64_t b_end = b->p_vaddr + b->p_memsz;
      if (a->p_vaddr < b_end && b->p_vaddr < a_end)
        return CV_LOAD_INVALID; /* True VMA content overlap, not just page overlap. */
      uint64_t b_last;
      if (cv_align_up(b_end, kernel_page, &b_last)) return CV_LOAD_INVALID;
      uint64_t b_first = b->p_vaddr & ~(kernel_page - 1);
      uint64_t collision_first = first > b_first ? first : b_first;
      uint64_t collision_end = last < b_last ? last : b_last;
      if (collision_first < collision_end &&
          (a->p_flags & (PF_R|PF_W|PF_X)) !=
          (b->p_flags & (PF_R|PF_W|PF_X))) {
        mode = CV_LOAD_ANON_COMPAT;
        if (out->first_segment == SIZE_MAX) {
          out->conflict_page = collision_first;
          out->first_segment = j;
          out->second_segment = i;
        }
      }
    }
  }
  if (!out->load_count || out->max_vaddr <= out->min_vaddr)
    return CV_LOAD_INVALID;
  return mode;
}

typedef int (*cv_read_segment_fn)(void *opaque, uint64_t file_offset,
                                  void *destination, size_t length);

/*
 * Destination is caller-owned RW anonymous range corresponding exactly to
 * [min_vaddr, min_vaddr + image_size). Pass the cv_load_plan from preflight.
 * Reader returns 0 only if it has filled EXACTLY length bytes (pread loop).
 * This API consumes no extra ELF-sized scratch buffer.
 */
static int cv_copy_loads(const Elf64_Phdr *phdr, size_t n,
                         const cv_load_plan *plan,
                         void *image, size_t image_size,
                         cv_read_segment_fn reader, void *opaque) {
  if (!phdr || !plan || !image || !reader ||
      plan->max_vaddr < plan->min_vaddr ||
      plan->max_vaddr - plan->min_vaddr > image_size) return -1;
  memset(image, 0, image_size);
  for (size_t i = 0; i < n; ++i) {
    const Elf64_Phdr *p = phdr + i;
    if (p->p_type != PT_LOAD || p->p_memsz == 0) continue;
    if (p->p_filesz > p->p_memsz || p->p_vaddr < plan->min_vaddr)
      return -1;
    uint64_t off = p->p_vaddr - plan->min_vaddr;
    if (off > image_size || p->p_memsz > image_size - off ||
        p->p_filesz > SIZE_MAX) return -1;
    if (p->p_filesz && reader(opaque, p->p_offset,
                             (uint8_t*)image + off, (size_t)p->p_filesz))
      return -1;
    /* The reservation was zero-filled; BSS remains zero. */
  }
  return 0;
}

/*
 * When a compat ELF has an RX|RW boundary (e.g. after a RELRO prefix),
 * choose load_bias shift so that boundary lands on a kernel page.
 * Returned shift is 0 .. kernel_page-1 bytes, to be applied to the
 * reserved image start. Caller MUST reserve an additional kernel page.
 */
static int cv_bias_shift_for_boundary(const cv_load_plan *plan,
                                      uint64_t boundary_vaddr,
                                      uint64_t kernel_page,
                                      uint64_t *shift) {
  if (!plan || !shift || !cv_is_power2(kernel_page) ||
      boundary_vaddr < plan->min_vaddr ||
      boundary_vaddr > plan->max_vaddr) return -1;
  uint64_t delta = boundary_vaddr - plan->min_vaddr;
  *shift = (kernel_page - (delta & (kernel_page - 1))) & (kernel_page - 1);
  return 0;
}
#endif
