// Static read-only ARM64 instruction scanner for DFM libUE4.so
// No process memory, no patching, no anti-cheat interaction.
// ARMv8 PAC/BTI/BR/BLR are not interpreted as protection solely by opcode.
#include <elf.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <unistd.h>
#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <tuple>
#include <unordered_map>
#include <vector>
using u8=uint8_t;using u32=uint32_t;using u64=uint64_t;
struct Mem{int fd=-1;u8* p=nullptr;size_t size=0;
 Mem(const char* s){fd=open(s,O_RDONLY);if(fd<0)perror("open");struct stat st{};if(fd>=0&&fstat(fd,&st)==0){size=st.st_size;p=(u8*)mmap(nullptr,size,PROT_READ,MAP_PRIVATE,fd,0);if(p==MAP_FAILED){p=nullptr;perror("mmap");}}}
 ~Mem(){if(p)munmap(p,size);if(fd>=0)close(fd);}
 bool ok(u64 off,u64 length)const{return p&&off<=size&&length<=size-off;}
 template<typename T>T at(u64 off)const{if(!ok(off,sizeof(T)))return T{};T v;memcpy(&v,p+off,sizeof(v));return v;}
};
static const Elf64_Shdr* secByName(const Mem& m,const char* name){
 if(!m.ok(0,sizeof(Elf64_Ehdr)))return nullptr;
 auto e=(Elf64_Ehdr*)m.p;
 if(e->e_shentsize!=sizeof(Elf64_Shdr) || e->e_shstrndx>=e->e_shnum || !m.ok(e->e_shoff,(u64)e->e_shnum*sizeof(Elf64_Shdr)))return nullptr;
 auto ss=(Elf64_Shdr*)(m.p+e->e_shoff),str=&ss[e->e_shstrndx];
 if(!m.ok(str->sh_offset,str->sh_size))return nullptr;
 auto names=(const char*)m.p+str->sh_offset;
 for(int i=0;i<e->e_shnum;i++){
  if(ss[i].sh_name<str->sh_size && strcmp(names+ss[i].sh_name,name)==0)return &ss[i];
 }
 return nullptr;
}
struct FdeIndex{
 std::vector<u64> starts;
 u64 hdr_vaddr=0;
 bool parsed=false;
 bool read(const Mem& m){
  auto s=secByName(m,".eh_frame_hdr");
  if(!s||!m.ok(s->sh_offset,s->sh_size)||s->sh_size<12)return false;
  auto b=m.p+s->sh_offset;
  const int ver=b[0], ptr=b[1], countenc=b[2], table=b[3];
  std::cout<<"EH_HDR version="<<ver<<" ptrenc=0x"<<std::hex<<ptr<<" countenc=0x"<<countenc<<" tableenc=0x"<<table<<std::dec<<"\n";
  if(ver!=1 || ptr!=0x1b || countenc!=3 || table!=0x3b) return false;
  u32 count;memcpy(&count,b+8,4);
  if(count==0 || count>4000000 || 12ull+8ull*count>s->sh_size)return false;
  hdr_vaddr=s->sh_addr;
  starts.reserve(count);
  for(u32 i=0;i<count;i++){
   int32_t start;memcpy(&start,b+12+8ull*i,4);
   starts.push_back(hdr_vaddr+start);
  }
  if(!std::is_sorted(starts.begin(),starts.end())){std::cout<<"EH_HDR UNSORTED!\n";return false;}
  parsed=true;
  std::cout<<"EH_FDE_COUNT "<<starts.size()<<" FIRST=0x"<<std::hex<<starts.front()<<" LAST=0x"<<starts.back()<<std::dec<<"\n";
  return true;
 }
 std::pair<u64,u64> region(u64 pc)const {
  if(!parsed)return{0,0};
  auto it=std::upper_bound(starts.begin(),starts.end(),pc);
  if(it==starts.begin())return{0,0};
  u64 lo=*(it-1),hi=it==starts.end()?0:*it;
  return {lo,hi}; // upper bound is NEXT start, not proven function size
 }
};
enum Kind{OTHER,LS,SS,LD,SD,LQ,SQ,LW,SW,LX,SX,LB,SB,LH,SH};
struct Ins{
 Kind type=OTHER;int imm=-1,base=-1,dst=-1;bool isload=false;
};
static Ins decode(u32 w){
 int imm12=(w>>10)&4095;int base=(w>>5)&31,dst=w&31;
 u32 masked=w&0xffc00000;
 #define OP(op,kind,scale,ld) if(masked==op) return{kind,imm12*scale,base,dst,ld};
 OP(0xbd400000u,LS,4,true) OP(0xbd000000u,SS,4,false)
 OP(0xfd400000u,LD,8,true) OP(0xfd000000u,SD,8,false)
 OP(0x3dc00000u,LQ,16,true) OP(0x3d800000u,SQ,16,false)
 OP(0xb9400000u,LW,4,true) OP(0xb9000000u,SW,4,false)
 OP(0xf9400000u,LX,8,true) OP(0xf9000000u,SX,8,false)
 OP(0x39400000u,LB,1,true) OP(0x39000000u,SB,1,false)
 OP(0x79400000u,LH,2,true) OP(0x79000000u,SH,2,false)
 #undef OP
 return{};
}
static bool stops(u32 w){
 return (w&0xfffffc1fu)==0xd65f0000u /*ret*/
    ||(w&0xfc000000u)==0x14000000u /*b imm unconditional*/
    ||(w&0xfffffc1fu)==0xd61f0000u /*br reg*/;
}
static const char* kind(Kind k){
 static const char* n[]={"?","ldr s","str s","ldr d","str d","ldr q","str q","ldr w","str w","ldr x","str x","ldrb","strb","ldrh","strh"};
 return n[int(k)];
}
struct Candidate{
 u64 va=0;int off=0,base=0;std::string ty;
 u64 ref1=0,ref2=0;
 int dist=0;bool retSoon=false;bool flagNear=false;int dst=0;
};
int main(int argc,char **argv){
 if(argc<2){std::cerr<<"Usage: scanner libUE4.so\n";return 2;}
 Mem m(argv[1]);auto eh=m.ok(0,sizeof(Elf64_Ehdr))?(Elf64_Ehdr*)m.p:nullptr;
 if(!eh||eh->e_machine!=EM_AARCH64||eh->e_ident[EI_CLASS]!=ELFCLASS64){std::cerr<<"Not AArch64 ELF\n";return 2;}
 auto sec=secByName(m,".text");
 u64 off=0,size=0,va=0;
 if(sec){off=sec->sh_offset;size=sec->sh_size;va=sec->sh_addr;}
 else{
  for(int i=0;i<eh->e_phnum;i++){
   auto ph=m.at<Elf64_Phdr>(eh->e_phoff+(u64)i*eh->e_phentsize);
   if(ph.p_type==PT_LOAD&&(ph.p_flags&PF_X)&&ph.p_filesz>size){off=ph.p_offset;size=ph.p_filesz;va=ph.p_vaddr;}
  }
 }
 if(!m.ok(off,size)){std::cerr<<"No executable load\n";return 2;}
 FdeIndex idx;idx.read(m);
 size_t n=size/4;u32* ws=(u32*)(m.p+off);
 std::cout<<"TEXT_BYTES "<<size<<" TEXT_VA 0x"<<std::hex<<va<<std::dec<<" WORDS "<<n<<"\n";
 std::map<std::pair<int,int>,u64> regCount;
 std::map<int,u64> histogramFP, histogramPack, histogramStore;
 std::vector<Candidate> candidates;
 std::map<int,u64> tripCounts,packedCounts;
 u64 nld=0,nstr=0,arithCount=0;
 for(size_t i=0;i<n;i++){
  Ins a=decode(ws[i]);
  if(a.type==OTHER)continue;
  regCount[{int(a.type),a.imm}]++;
  if(a.isload)nld++;else nstr++;
  if((a.type==LS||a.type==LD||a.type==LQ) && a.imm<=0x600)histogramFP[a.imm]++;
  if(a.type==LX && a.imm<=0x600)histogramPack[a.imm]++;
  if((a.type==SX||a.type==SW||a.type==SS) && a.imm<=0x600)histogramStore[a.imm]++;
  if(a.type==LS && a.imm>=0x40 && a.imm<=0x500){
   size_t b=0,c=0,lr=0;bool stop=false;
   for(size_t j=i+1;j<std::min(n,i+49);j++){
    Ins z=decode(ws[j]);
    if(z.type==LS && z.base==a.base){
     if(z.imm==a.imm+4 && !b)b=j;
     if(z.imm==a.imm+8 && !c)c=j;
    }
    if(stops(ws[j])){stop=true;break;}
    if(b&&c){for(size_t k=std::max(b,c)+1;k<std::min(n,std::max(b,c)+8);k++)if((ws[k]&0xfffffc1f)==0xd65f0000)lr=k;break;}
   }
   if(b&&c){
    tripCounts[a.imm]++;
    if(candidates.size()<10000) candidates.push_back({va+4ull*i,a.imm,a.base,"triple-s",va+4ull*b,va+4ull*c,int(std::max(b,c)-i),lr!=0,false,a.dst});
   }
  }
  if((a.type==LX||a.type==SX) && a.imm>=0x40 && a.imm<=0x500 && a.imm%4==0){
   // 12-byte FVector aggregate moved with 8+4-byte operations.
   size_t found=0,ret=0;bool flag=false;
   for(size_t j=i+1;j<std::min(n,i+41);j++){
    auto z=decode(ws[j]);
    if(z.base==a.base){
     if(a.type==LX && z.type==LW && z.imm==a.imm+8){found=j;}
     if(a.type==SX && z.type==SW && z.imm==a.imm+8){found=j;}
     if((z.type==LB||z.type==LH) && z.imm>=a.imm+12 && z.imm<=a.imm+16)flag=true;
    }
    if(stops(ws[j])){ret=j;break;}
   }
   if(found){
    packedCounts[a.imm]++;
    if(candidates.size()<20000) candidates.push_back({va+4ull*i,a.imm,a.base,a.type==LX?"packed-ldr":"packed-str",va+4ull*found,0,int(found-i),ret!=0,flag,a.dst});
   }
  }
 }
 auto sortmap=[](const auto& hist,size_t take=40){
  std::vector<std::pair<int,u64>> v(hist.begin(),hist.end());
  std::sort(v.begin(),v.end(),[](auto&x,auto&y){return x.second>y.second;});
  for(size_t i=0;i<std::min(take,v.size());i++)std::cout<<" 0x"<<std::hex<<v[i].first<<std::dec<<" "<<v[i].second<<"\n";
 };
 std::cout<<"MEM_OPS load "<<nld<<" store "<<nstr<<"\n";
 std::cout<<"FP_OFFSETS\n";sortmap(histogramFP);
 std::cout<<"PACK_OFFSETS\n";sortmap(histogramPack);
 std::cout<<"STORE_OFFSETS\n";sortmap(histogramStore);
 std::cout<<"TRIPLE_HIST\n";sortmap(tripCounts,60);
 std::cout<<"PACKED_HIST\n";sortmap(packedCounts,60);
 std::cout<<"OFFSET_COUNTS\n";
 for(int v:{0x100,0x108,0x138,0x150,0x160,0x164,0x168,0x16c,0x170,0x174,0x176,0x178,0x180,0x188,0x1f0,0x210,0x220,0x228}){
  std::cout<<" 0x"<<std::hex<<v<<std::dec;
  for(auto t:{LS,SS,LD,SD,LQ,SQ,LW,SW,LX,SX,LB,LH})
   std::cout<<" "<<kind(t)<<"="<<regCount[{int(t),v}];
  std::cout<<"\n";
 }
 // Detailed candidates weighted toward the coordinate offsets; remaining list bounded.
 std::sort(candidates.begin(),candidates.end(),[](const Candidate&a,const Candidate&b){
  auto score=[](const Candidate&c){
   return (c.off>=0x150&&c.off<=0x250?10:0)
    +(c.ty=="triple-s"?3:0)
    +(c.retSoon?2:0)+(c.flagNear?1:0)
    +(c.off==0x168?30:0)+(c.off==0x210?3:0);
  };
  int sa=score(a),sb=score(b);
  if(sa!=sb)return sa>sb;
  return a.va<b.va;
 });
 std::cout<<"CANDIDATES_COUNT "<<candidates.size()<<"\n";
 size_t printed=0;
 for(auto c:candidates){
  if(printed++>=95)break;
  auto [fde,next]=idx.region(c.va);
  std::cout<<"CANDIDATE "<<c.ty<<" 0x"<<std::hex<<c.va
   <<" off=0x"<<c.off<<" base=x"<<c.base
   <<" other=0x"<<c.ref1<<" next=0x"<<c.ref2
   <<" fde=0x"<<fde<<" next_fde=0x"<<next
   <<std::dec<<" delta_inst="<<c.dist<<" ret="<<c.retSoon<<" flag="<<c.flagNear
   <<" dst="<<c.dst<<"\n";
 }
 for(u64 a:{0x0d1fbb84ull,0x0d1fbb98ull,0x0d1fbba4ull,0x0815cdb0ull}){
  auto [start,next]=idx.region(a);
  std::cout<<"OLD_REFERENCE 0x"<<std::hex<<a<<" FDE=0x"<<start<<" NEXT=0x"<<next<<std::dec<<"\n";
 }
 std::cout<<"END_SCAN\n";
 return 0;
}