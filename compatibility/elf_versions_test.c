#include "elf_versions.h"
#include "arm64_aps2_rela.h"
#include <assert.h>
#include <stdio.h>
#include <string.h>

static void set_bytes(void *dest, size_t offset, const void *src, size_t n) {
  memcpy((unsigned char*)dest + offset, src, n);
}

static void test_requirements(void) {
  const char names[] = "\0libdep.so\0VERS_A\0VERS_B\0";
  uint8_t table[sizeof(Elf64_Verneed)+2*sizeof(Elf64_Vernaux)]={0};
  Elf64_Verneed vn={0};
  vn.vn_version=VER_NEED_CURRENT; vn.vn_cnt=2; vn.vn_file=1;
  vn.vn_aux=sizeof(Elf64_Verneed);
  Elf64_Vernaux a={0},b={0};
  a.vna_name=11; a.vna_other=2; a.vna_next=sizeof(a);
  b.vna_name=18; b.vna_other=3;
  set_bytes(table,0,&vn,sizeof(vn));
  set_bytes(table,sizeof(vn),&a,sizeof(a));
  set_bytes(table,sizeof(vn)+sizeof(a),&b,sizeof(b));
  uint16_t versym[]={0,1,2,0x8003};
  cv_version_view v={0};
  v.versym=versym; v.versym_count=4; v.verneed=table;
  v.verneed_size=sizeof(table); v.verneed_count=1;
  v.dynstr=names; v.dynstr_size=sizeof(names);
  cv_version_requirement out;
  assert(cv_get_symbol_requirement(&v,2,&out)==1);
  assert(strcmp(out.name,"VERS_A")==0 && strcmp(out.needed_soname,"libdep.so")==0);
  assert(out.index==2);
  assert(cv_get_symbol_requirement(&v,3,&out)==1);
  assert(strcmp(out.name,"VERS_B")==0);
  assert(cv_get_symbol_requirement(&v,1,&out)==0);
  assert(cv_get_symbol_requirement(&v,4,&out)==-1);
  v.verneed_size--;
  assert(cv_get_symbol_requirement(&v,3,&out)==-1);
  v.verneed_size++;
  a.vna_next=0;
  set_bytes(table,sizeof(vn),&a,sizeof(a));
  assert(cv_get_symbol_requirement(&v,3,&out)==-1);
  a.vna_next=sizeof(a);
  set_bytes(table,sizeof(vn),&a,sizeof(a));
  b.vna_name=99999;
  set_bytes(table,sizeof(vn)+sizeof(a),&b,sizeof(b));
  assert(cv_get_symbol_requirement(&v,3,&out)==-1);
  b.vna_name=18;
  set_bytes(table,sizeof(vn)+sizeof(a),&b,sizeof(b));
  v.versym=NULL;
  assert(cv_get_symbol_requirement(&v,3,&out)==0);
}
static void test_definitions(void) {
  const char names[] = "\0PROV\0VERS_A\0VERS_B\0";
  uint8_t table[2*(sizeof(Elf64_Verdef)+sizeof(Elf64_Verdaux))]={0};
  Elf64_Verdef vd={0},vd2={0};
  Elf64_Verdaux a={0},b={0};
  vd.vd_version=VER_DEF_CURRENT; vd.vd_cnt=1; vd.vd_ndx=2;
  vd.vd_aux=sizeof(vd); vd.vd_next=sizeof(vd)+sizeof(a);
  a.vda_name=6;
  vd2.vd_version=VER_DEF_CURRENT; vd2.vd_cnt=1; vd2.vd_ndx=3;
  vd2.vd_aux=sizeof(vd2);
  b.vda_name=13;
  set_bytes(table,0,&vd,sizeof(vd));
  set_bytes(table,sizeof(vd),&a,sizeof(a));
  set_bytes(table,sizeof(vd)+sizeof(a),&vd2,sizeof(vd2));
  set_bytes(table,2*sizeof(vd)+sizeof(a),&b,sizeof(b));
  uint16_t versym[]={0,1,2,0x8003};
  cv_version_view v={0};
  v.versym=versym; v.versym_count=4; v.verdef=table;
  v.verdef_size=sizeof(table); v.verdef_count=2;
  v.dynstr=names; v.dynstr_size=sizeof(names);
  assert(cv_def_symbol_matches(&v,1,NULL)==1);
  assert(cv_def_symbol_matches(&v,2,NULL)==1);
  assert(cv_def_symbol_matches(&v,3,NULL)==0);
  assert(cv_def_symbol_matches(&v,2,"VERS_A")==1);
  assert(cv_def_symbol_matches(&v,3,"VERS_B")==1);
  assert(cv_def_symbol_matches(&v,2,"VERS_B")==0);
  assert(cv_def_symbol_matches(&v,1,"VERSION_NOT_DEFINED")==1);
  assert(cv_def_symbol_matches(&v,0,"VERS_A")==0);
  assert(cv_def_symbol_matches(&v,4,NULL)==-1);
  v.versym=NULL;
  assert(cv_def_symbol_matches(&v,3,"VERS_B")==1);
  v.versym=versym;
  v.verdef_size--;
  assert(cv_def_symbol_matches(&v,3,"VERS_B")==-1);
  v.verdef_size++;
  vd.vd_next=0;
  set_bytes(table,0,&vd,sizeof(vd));
  assert(cv_def_symbol_matches(&v,3,"VERS_B")==-1);
}
struct relay_sink { Elf64_Rela got; int n, fail; };
static int relay(void *opaque,const Elf64_Rela *rela) {
  struct relay_sink *s=(struct relay_sink*)opaque;
  s->got=*rela; s->n++;
  return s->fail;
}
static void test_streaming_relocations(void) {
  const uint8_t blob[]={'A','P','S','2',1,0,1,11,0x80,1,0x83,8,5};
  struct relay_sink sink={0}; uint64_t visited=0;
  cv_aps2_rela_context ctx={0};
  ctx.on_rela=relay; ctx.opaque=&sink; ctx.image_vaddr_lo=0;
  ctx.image_vaddr_hi=4096; ctx.dynsym_count=1;
  assert(cv_walk_aps2_rela(blob,sizeof(blob),32,&ctx,&visited)==0);
  assert(visited==1 && sink.n==1);
  assert(sink.got.r_offset==128 && ELF64_R_TYPE(sink.got.r_info)==1027);
  assert(sink.got.r_addend==5);
  ctx.image_vaddr_hi=135;
  assert(cv_walk_aps2_rela(blob,sizeof(blob),32,&ctx,&visited)==-2);
  ctx.image_vaddr_hi=4096;
  sink.fail=1;
  assert(cv_walk_aps2_rela(blob,sizeof(blob),32,&ctx,&visited)==-2);
  sink.fail=0;
  assert(cv_walk_aps2_rela(blob,sizeof(blob),0,&ctx,&visited)==-1);
}
int main(void) {
  test_requirements(); test_definitions(); test_streaming_relocations();
  puts("ELF_VERSION_AND_APS2_RELA_TESTS_PASS");
  return 0;
}
