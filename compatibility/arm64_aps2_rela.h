/*
 * Android ARM64 APS2 -> Elf64_Rela streaming adapter.
 * Feed each record to the *same* relocation consumer used for ordinary RELA.
 * No temporary relocation table and no complete ELF memory copy is needed.
 * Standalone public component; none of the application's private code here.
 */
#ifndef CUSTOM_ARM64_APS2_RELA_H
#define CUSTOM_ARM64_APS2_RELA_H
#include "aps2_decoder.h"
#include <elf.h>
#include <stddef.h>
#include <stdint.h>

#ifndef R_AARCH64_TLSDESC
#define R_AARCH64_TLSDESC 1031
#endif

typedef int (*cv_on_rela_fn)(void *opaque, const Elf64_Rela *rel);

typedef struct {
  cv_on_rela_fn on_rela;
  void *opaque;
  uint64_t image_vaddr_lo;
  uint64_t image_vaddr_hi; /* Exclusive. Must cover mapped image, including bss. */
  uint64_t dynsym_count;   /* 0 = not available; caller must then check sym index. */
} cv_aps2_rela_context;

static int cv_aps2_rela_item(void *opaque, const aps2_relocation *in) {
  cv_aps2_rela_context *ctx = (cv_aps2_rela_context *)opaque;
  uint32_t type = (uint32_t)(in->info & UINT32_MAX);
  uint32_t sym = (uint32_t)(in->info >> 32);
  if (ctx->dynsym_count && sym >= ctx->dynsym_count) return -1;
  /* AArch64 TLSDESC writes two pointer-sized cells, other supported
     integer relocations write at most one. The normal consumer validates
     other type-specific constraints and symbol binding. */
  const uint64_t width = type == R_AARCH64_TLSDESC ? 16 :
      (type == R_AARCH64_NONE ? 0 : 8);
  if (width &&
      (in->offset < ctx->image_vaddr_lo ||
       in->offset >= ctx->image_vaddr_hi ||
       width > ctx->image_vaddr_hi - in->offset)) return -1;
  Elf64_Rela rela;
  rela.r_offset = in->offset;
  rela.r_info = in->info;
  rela.r_addend = in->addend;
  return ctx->on_rela(ctx->opaque, &rela);
}

/*
 * 0 = success, -1 = malformed stream, -2 = invalid relocation or
 * callback failure. 'limit' bounds stream expansion before visiting.
 * Caller MUST also bounds-check relocation destination against actual
 * mapped PT_LOAD ranges rather than only the address-space envelope.
 */
static int cv_walk_aps2_rela(const uint8_t *blob, size_t blob_len,
                            uint64_t limit, cv_aps2_rela_context *ctx,
                            uint64_t *visited) {
  if (!ctx || !ctx->on_rela ||
      ctx->image_vaddr_hi <= ctx->image_vaddr_lo) return -1;
  return aps2_decode(blob, blob_len, limit, cv_aps2_rela_item, ctx, visited);
}
#endif
