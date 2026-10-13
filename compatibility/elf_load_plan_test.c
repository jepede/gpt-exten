#include "elf_load_plan.h"
#include <assert.h>
#include <stdio.h>
#include <string.h>

struct image_file { const unsigned char *buf; size_t len; };
static int read_from_image(void *opaque, uint64_t off, void *dst, size_t len) {
  struct image_file *f=(struct image_file*)opaque;
  if (off > f->len || len > f->len - off) return -1;
  memcpy(dst, f->buf + off, len);
  return 0;
}
static void test_normal_4k_and_legacy_16k(void) {
  Elf64_Phdr ph[2]={0};
  for (int i=0;i<2;i++) {
    ph[i].p_type=PT_LOAD; ph[i].p_offset=(uint64_t)i*4096;
    ph[i].p_vaddr=(uint64_t)i*4096; ph[i].p_filesz=4096;
    ph[i].p_memsz=4096; ph[i].p_align=4096;
  }
  ph[0].p_flags=PF_R|PF_X; ph[1].p_flags=PF_R|PF_W;
  cv_load_plan plan={0};
  assert(cv_plan_loads(ph,2,8192,4096,&plan)==CV_LOAD_DIRECT);
  assert(plan.min_vaddr==0 && plan.max_vaddr==8192 &&
         plan.first_segment==SIZE_MAX);
  assert(cv_plan_loads(ph,2,8192,16384,&plan)==CV_LOAD_ANON_COMPAT);
  assert(plan.min_vaddr==0 && plan.max_vaddr==16384);
  assert(plan.conflict_page==0 && plan.first_segment==0 &&
         plan.second_segment==1);
  uint64_t shift=0;
  assert(cv_bias_shift_for_boundary(&plan,4096,16384,&shift)==0);
  assert(shift==12288);
  assert((shift+4096)%16384==0);
  unsigned char backing[8192];
  memset(backing,0x11,4096); memset(backing+4096,0x22,4096);
  unsigned char anon[16384];
  memset(anon,0xCC,sizeof anon);
  struct image_file img={backing,sizeof backing};
  assert(cv_copy_loads(ph,2,&plan,anon,sizeof anon,read_from_image,&img)==0);
  assert(anon[0]==0x11 && anon[4095]==0x11);
  assert(anon[4096]==0x22 && anon[8191]==0x22);
  assert(anon[8192]==0 && anon[16383]==0);
  ph[1].p_memsz=8192;
  assert(cv_plan_loads(ph,2,8192,16384,&plan)==CV_LOAD_ANON_COMPAT);
  assert(cv_copy_loads(ph,2,&plan,anon,sizeof anon,read_from_image,&img)==0);
  assert(anon[8192]==0 && anon[12287]==0);
}
static void test_native_16k_and_rejections(void) {
  Elf64_Phdr ph[2]={0};
  for (int i=0;i<2;i++) {
    ph[i].p_type=PT_LOAD; ph[i].p_offset=(uint64_t)i*16384;
    ph[i].p_vaddr=(uint64_t)i*16384; ph[i].p_filesz=4096;
    ph[i].p_memsz=4096; ph[i].p_align=16384;
    ph[i].p_flags=i==0?PF_R|PF_X:PF_R|PF_W;
  }
  cv_load_plan plan;
  assert(cv_plan_loads(ph,2,20480,16384,&plan)==CV_LOAD_DIRECT);
  assert(plan.max_vaddr==32768);
  ph[1].p_filesz=5000;
  assert(cv_plan_loads(ph,2,22000,16384,&plan)==CV_LOAD_INVALID);
  ph[1].p_filesz=4096;
  ph[1].p_offset=16385;
  assert(cv_plan_loads(ph,2,22000,16384,&plan)==CV_LOAD_INVALID);
  ph[1].p_offset=16384;
  ph[1].p_vaddr=2048;
  ph[1].p_align=1;
  assert(cv_plan_loads(ph,2,22000,16384,&plan)==CV_LOAD_INVALID);
  ph[1].p_vaddr=16384;
  ph[1].p_align=16384;
  ph[1].p_offset=22000;
  assert(cv_plan_loads(ph,2,22000,16384,&plan)==CV_LOAD_INVALID);
  ph[1].p_offset=16384;
  ph[1].p_vaddr=UINT64_MAX - 100;
  assert(cv_plan_loads(ph,2,22000,16384,&plan)==CV_LOAD_INVALID);
}
int main(void) {
  test_normal_4k_and_legacy_16k();
  test_native_16k_and_rejections();
  puts("ELF_LOAD_PLAN_4K_16K_TESTS_PASS");
  return 0;
}
