/*
 * Bounded Android APS2 relocation reader, C11, architecture-independent.
 * Standalone public compatibility component. No AOSP source copied.
 * Android AArch64 relocation consumer validates target & symbol separately.
 */
#ifndef CUSTOM_APS2_DECODER_H
#define CUSTOM_APS2_DECODER_H
#include <stddef.h>
#include <stdint.h>
#include <limits.h>
#include <string.h>

enum {
  APS2_GROUP_INFO = 1,
  APS2_GROUP_DELTA = 2,
  APS2_GROUP_ADDEND = 4,
  APS2_HAS_ADDEND = 8
};

typedef struct {
  uint64_t offset;
  uint64_t info;
  int64_t addend;
} aps2_relocation;

typedef int (*aps2_visit_fn)(void *opaque, const aps2_relocation *rel);

typedef struct {
  const uint8_t *cur, *end;
} aps2_reader;

static int aps2_read_signed(aps2_reader *r, int64_t *out) {
  uint64_t x = 0;
  unsigned shift = 0;
  unsigned char b = 0;
  if (!r || !out) return -1;
  for (unsigned i = 0; i < 10; ++i) {
    if (r->cur == r->end) return -1;
    b = *r->cur++;
    if (i == 9 && (b != 0x00 && b != 0x7f)) return -1;
    x |= (uint64_t)(b & 0x7fu) << shift;
    shift += 7;
    if (!(b & 0x80u)) {
      if (shift < 64 && (b & 0x40u)) x |= UINT64_MAX << shift;
      *out = (int64_t)x;
      return 0;
    }
  }
  return -1;
}

static int aps2_add_s64(int64_t *value, int64_t delta) {
  if ((delta > 0 && *value > INT64_MAX - delta) ||
      (delta < 0 && *value < INT64_MIN - delta)) return -1;
  *value += delta;
  return 0;
}

static int aps2_add_offset(uint64_t *off, int64_t delta) {
  if (delta >= 0) {
    if (*off > UINT64_MAX - (uint64_t)delta) return -1;
    *off += (uint64_t)delta;
  } else {
    /* Relative offsets normally increase but negative deltas are representable. */
    const uint64_t magnitude = (uint64_t)(-(delta + 1)) + 1;
    if (*off < magnitude) return -1;
    *off -= magnitude;
  }
  return 0;
}

/*
 * Returns 0 on a valid APS2 stream, -1 on malformed input, callback's
 * nonzero return as -2. max_relocs limits decompression expansion.
 * The caller must validate r_offset, type, width and sym index for each item.
 */
static int aps2_decode(const uint8_t *data, size_t len, uint64_t max_relocs,
                       aps2_visit_fn visit, void *opaque, uint64_t *decoded) {
  if (decoded) *decoded = 0;
  if (!data || !visit || len < 6 || memcmp(data, "APS2", 4)) return -1;
  aps2_reader r = {data + 4, data + len};
  int64_t n_signed, first;
  if (aps2_read_signed(&r, &n_signed) || n_signed < 0 ||
      (uint64_t)n_signed > max_relocs || aps2_read_signed(&r, &first) || first < 0) return -1;
  const uint64_t n = (uint64_t)n_signed;
  uint64_t consumed = 0;
  aps2_relocation rel = {(uint64_t)first, 0, 0};
  while (consumed < n) {
    int64_t size_signed, flags_signed;
    if (aps2_read_signed(&r, &size_signed) || aps2_read_signed(&r, &flags_signed) ||
        size_signed <= 0 || flags_signed < 0 ||
        (uint64_t)size_signed > n - consumed ||
        (flags_signed & ~(int64_t)15) != 0) return -1;
    const uint64_t group_size = (uint64_t)size_signed;
    const unsigned flags = (unsigned)flags_signed;
    int64_t group_delta = 0, x = 0;
    if ((flags & APS2_GROUP_DELTA) && aps2_read_signed(&r, &group_delta)) return -1;
    if (flags & APS2_GROUP_INFO) {
      if (aps2_read_signed(&r, &x)) return -1;
      rel.info = (uint64_t)x;
    }
    if (!(flags & APS2_HAS_ADDEND)) {
      rel.addend = 0;
    } else if (flags & APS2_GROUP_ADDEND) {
      if (aps2_read_signed(&r, &x) || aps2_add_s64(&rel.addend, x)) return -1;
    }
    for (uint64_t i = 0; i < group_size; ++i) {
      if (!(flags & APS2_GROUP_DELTA) && aps2_read_signed(&r, &group_delta)) return -1;
      if (aps2_add_offset(&rel.offset, group_delta)) return -1;
      if (!(flags & APS2_GROUP_INFO)) {
        if (aps2_read_signed(&r, &x)) return -1;
        rel.info = (uint64_t)x;
      }
      if ((flags & (APS2_HAS_ADDEND | APS2_GROUP_ADDEND)) == APS2_HAS_ADDEND) {
        if (aps2_read_signed(&r, &x) || aps2_add_s64(&rel.addend, x)) return -1;
      }
      if (visit(opaque, &rel)) return -2;
      ++consumed;
    }
  }
  /* Section padding is permitted only if it is zero-filled. */
  while (r.cur < r.end) if (*r.cur++ != 0) return -1;
  if (decoded) *decoded = consumed;
  return 0;
}
#endif
