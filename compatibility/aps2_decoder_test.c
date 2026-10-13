#include "aps2_decoder.h"
/* Cross-compiler regression tests. */
#include <assert.h>
#include <stdio.h>
#include <string.h>

struct sink { aps2_relocation rel[16]; unsigned n; };
static int save(void *v, const aps2_relocation *rel) {
  struct sink *s = v;
  if (s->n >= 16) return -1;
  s->rel[s->n++] = *rel;
  return 0;
}
static void test_single(void) {
  /* n=1, initial=0, flags=group_delta|group_info|has_addend */
  const uint8_t b[] = {'A','P','S','2',1,0,1,11,0x80,1,0x83,8,5};
  struct sink s = {0}; uint64_t n;
  assert(aps2_decode(b,sizeof b,16,save,&s,&n)==0);
  assert(n==1 && s.n==1);
  assert(s.rel[0].offset==128 && s.rel[0].info==1027 && s.rel[0].addend==5);
}
static void test_variable_and_negative(void) {
  /* n=2; initial=32; group_info+has_addend; per reloc offset, addend delta */
  const uint8_t b[] = {'A','P','S','2',2,32,2,9,0x81,8,8,0x7f,8,3};
  struct sink s={0}; uint64_t n=0;
  assert(aps2_decode(b,sizeof b,16,save,&s,&n)==0);
  assert(n==2 && s.n==2);
  assert(s.rel[0].offset==40 && s.rel[0].info==1025 && s.rel[0].addend==-1);
  assert(s.rel[1].offset==48 && s.rel[1].info==1025 && s.rel[1].addend==2);
}
static void test_bad(void) {
  const uint8_t good[] = {'A','P','S','2',1,0,1,11,0x80,1,0x83,8,5};
  struct sink s={0};
  assert(aps2_decode(good,sizeof good,0,save,&s,NULL)==-1);
  for (size_t l=0;l<sizeof good;l++) {
    assert(aps2_decode(good,l,16,save,&s,NULL)!=0);
  }
  uint8_t bad[sizeof good];
  memcpy(bad,good,sizeof good); bad[0]='X';
  assert(aps2_decode(bad,sizeof bad,16,save,&s,NULL)==-1);
  memcpy(bad,good,sizeof good); bad[6]=0;
  assert(aps2_decode(bad,sizeof bad,16,save,&s,NULL)==-1);
  memcpy(bad,good,sizeof good); bad[7]=16;
  assert(aps2_decode(bad,sizeof bad,16,save,&s,NULL)==-1);
  memcpy(bad,good,sizeof good); bad[4]=2;
  assert(aps2_decode(bad,sizeof bad,16,save,&s,NULL)==-1);
  memcpy(bad,good,sizeof good); bad[12]=0x80;
  assert(aps2_decode(bad,sizeof bad,16,save,&s,NULL)==-1);
  const uint8_t noprogress[] = {'A','P','S','2',1,0,1,1,0x83,8,0};
  assert(aps2_decode(noprogress,sizeof noprogress,2,save,&s,NULL)==0);
  const uint8_t neg_off[] = {'A','P','S','2',1,0,1,2,0x7f,0};
  assert(aps2_decode(neg_off,sizeof neg_off,2,save,&s,NULL)==-1);
}
int main(void) {
  test_single();
  test_variable_and_negative();
  test_bad();
  puts("APS2_DECODE_TESTS_PASS");
  return 0;
}
