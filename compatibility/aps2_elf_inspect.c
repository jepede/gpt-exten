/* Host test utility: inspect a real LLD-built Android ARM64 ELF APS2 table. */
#include "arm64_aps2_rela.h"
#include <elf.h>
#include <fcntl.h>
#include <inttypes.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <unistd.h>

#ifndef DT_ANDROID_RELA
#define DT_ANDROID_RELA 0x60000011
#endif
#ifndef DT_ANDROID_RELASZ
#define DT_ANDROID_RELASZ 0x60000012
#endif

static int within(uint64_t pos, uint64_t n, uint64_t size) {
  return pos <= size && n <= size - pos;
}
static int count_relocation(void *opaque, const Elf64_Rela *r) {
  unsigned *n=(unsigned*)opaque;
  if (!r || *n >= 1000000) return -1;
  ++*n;
  return 0;
}
static int vaddr_to_file(const Elf64_Phdr *ph, unsigned n,
                         uint64_t vaddr, uint64_t amount,
                         size_t file_len, uint64_t *offset) {
  for (unsigned i=0;i<n;++i) {
    if (ph[i].p_type != PT_LOAD || ph[i].p_filesz == 0) continue;
    if (vaddr < ph[i].p_vaddr) continue;
    uint64_t delta=vaddr-ph[i].p_vaddr;
    if (!within(delta,amount,ph[i].p_filesz)) continue;
    if (!within(ph[i].p_offset,delta,file_len)) continue;
    uint64_t result=ph[i].p_offset+delta;
    if (!within(result,amount,file_len)) continue;
    *offset=result;
    return 0;
  }
  return -1;
}
int main(int argc, char **argv) {
  if (argc != 2) { fprintf(stderr,"usage: %s AARCH64_APS2_ELF.so\n",argv[0]);return 2; }
  int fd=open(argv[1],O_RDONLY);
  if(fd<0) {perror("open"); return 2;}
  struct stat st;
  if(fstat(fd,&st)!=0 || st.st_size< (off_t)sizeof(Elf64_Ehdr) ||
     st.st_size>64*1024*1024) {fprintf(stderr,"bad file size\n"); close(fd);return 2;}
  size_t len=(size_t)st.st_size;
  const uint8_t *file=mmap(NULL,len,PROT_READ,MAP_PRIVATE,fd,0);
  close(fd);
  if(file==MAP_FAILED) {perror("mmap"); return 2;}
  Elf64_Ehdr eh; memcpy(&eh,file,sizeof(eh));
  if(memcmp(eh.e_ident,ELFMAG,SELFMAG) ||
     eh.e_ident[EI_CLASS]!=ELFCLASS64 || eh.e_ident[EI_DATA]!=ELFDATA2LSB ||
     eh.e_machine!=EM_AARCH64 || eh.e_phentsize!=sizeof(Elf64_Phdr) ||
     !eh.e_phnum || !within(eh.e_phoff,(uint64_t)eh.e_phnum*sizeof(Elf64_Phdr),len)) {
    fprintf(stderr,"not an AArch64 little-endian ELF64 with bounded PHDR\n");
    munmap((void*)file,len);return 2;
  }
  const Elf64_Phdr *ph=(const Elf64_Phdr*)(const void*)(file+eh.e_phoff);
  uint64_t packed=0,packed_sz=0,lo=UINT64_MAX,hi=0;
  for (unsigned i=0;i<eh.e_phnum;i++) {
    if(ph[i].p_type==PT_LOAD && ph[i].p_memsz) {
      if(ph[i].p_vaddr > UINT64_MAX-ph[i].p_memsz) goto fail;
      if(ph[i].p_vaddr < lo) lo=ph[i].p_vaddr;
      if(ph[i].p_vaddr+ph[i].p_memsz > hi) hi=ph[i].p_vaddr+ph[i].p_memsz;
    }
    if(ph[i].p_type!=PT_DYNAMIC) continue;
    if(!within(ph[i].p_offset,ph[i].p_filesz,len)) goto fail;
    for(size_t j=0;j<ph[i].p_filesz/sizeof(Elf64_Dyn);j++) {
      Elf64_Dyn d;
      memcpy(&d,file+ph[i].p_offset+j*sizeof(d),sizeof(d));
      if(d.d_tag==DT_NULL) break;
      if(d.d_tag==DT_ANDROID_RELA) packed=d.d_un.d_ptr;
      if(d.d_tag==DT_ANDROID_RELASZ) packed_sz=d.d_un.d_val;
    }
  }
  if(!packed || !packed_sz || hi<=lo) {
    fprintf(stderr,"no DT_ANDROID_RELA/RELASZ table found\n");
    munmap((void*)file,len);return 1;
  }
  uint64_t packed_offset=0;
  if(vaddr_to_file(ph,eh.e_phnum,packed,packed_sz,len,&packed_offset)) goto fail;
  unsigned n=0; uint64_t visited=0;
  cv_aps2_rela_context ctx={count_relocation,&n,lo,hi,0};
  int ret=cv_walk_aps2_rela(file+packed_offset,(size_t)packed_sz,1000000,&ctx,&visited);
  if(ret!=0 || n==0 || visited!=n) {
    fprintf(stderr,"APS2 decode invalid: code=%d relocs=%u\n",ret,n);
    munmap((void*)file,len);return 1;
  }
  printf("REAL_LLD_APS2_PASS: %u AArch64 relocations, packed bytes=%" PRIu64 "\n",n,packed_sz);
  munmap((void*)file,len);return 0;
fail:
  fprintf(stderr,"malformed ELF dynamic/PT_LOAD address range\n");
  munmap((void*)file,len);return 2;
}
