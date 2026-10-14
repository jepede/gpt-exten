#include <algorithm>
#include <cstdint>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <array>
struct EH { uint8_t ident[16]; uint16_t type,machine; uint32_t version; uint64_t entry,phoff,shoff; uint32_t flags; uint16_t ehsize,phentsize,phnum,shentsize,shnum,shstrndx; };
struct SH { uint32_t name,type; uint64_t flags,addr,offset,size; uint32_t link,info; uint64_t align,entsize; };
enum { NONE=0, LS=1, LW=2, LB=3, LH=4, LX=5, SS=6, SW=7 };
struct Op {int kind=0,off=0,base=-1,dest=-1;};
static Op decode(uint32_t w) {
 uint32_t op = w & 0xffc00000u;
 int imm=(w>>10)&0xfff, base=(w>>5)&31, dst=w&31;
 if(op==0xbd400000u)return {LS,imm*4,base,dst};
 if(op==0xb9400000u)return {LW,imm*4,base,dst};
 if(op==0x39400000u)return {LB,imm,base,dst};
 if(op==0x79400000u)return {LH,imm*2,base,dst};
 if(op==0xf9400000u)return {LX,imm*8,base,dst};
 if(op==0xbd000000u)return {SS,imm*4,base,dst};
 if(op==0xb9000000u)return {SW,imm*4,base,dst};
 return {};
}
static bool stop(uint32_t w) {
 return (w&0xfffffc1fu)==0xd65f0000u || (w&0xfc000000u)==0x14000000u;
}
struct Results {
 std::array<uint64_t,8> n168{},n16c{},n170{},n174{},n176{};
 uint64_t exacttriple=0,anytriple=0,nearFlag=0,loadS=0;
 std::vector<std::string> exacthits,anyhits,flags;
 std::map<int,uint64_t> shist;
};
static const char *kindName(int k) {
 switch(k){case LS:return "LDRS";case LW:return "LDRW";case LB:return "LDRB";case LH:return "LDRH";case LX:return "LDRX";case SS:return "STRS";case SW:return "STRW";default:return "";}
}
static std::string hx(uint64_t v){char b[40];snprintf(b,sizeof(b),"0x%llx",(unsigned long long)v);return b;}
int main(int argc,char**argv) {
 if(argc<2)return 2;
 std::ifstream file(argv[1],std::ios::binary);if(!file) return 3;
 EH e{};file.read((char*)&e,sizeof(e));
 if(memcmp(e.ident,"\x7f""ELF",4)||e.machine!=183||e.shnum==0||e.shnum>1000)return 4;
 std::vector<SH> sh(e.shnum);
 file.seekg(e.shoff);file.read((char*)sh.data(),sh.size()*sizeof(SH));
 std::string names(sh[e.shstrndx].size,0);file.seekg(sh[e.shstrndx].offset);file.read(&names[0],names.size());
 SH text{};bool found=false;
 for(const auto &s:sh) if(s.name<names.size() && names.compare(s.name,5,".text")==0 && names[s.name+5]==0) {text=s;found=true;break;}
 if(!found||text.size>(1ULL<<31))return 5;
 std::vector<uint32_t> ins(text.size/4);
 file.seekg(text.offset);file.read((char*)ins.data(),ins.size()*4);
 std::cout<<"TEXT VA "<<hx(text.addr)<<" INSTRUCTIONS "<<ins.size()<<" BYTES "<<text.size<<"\n";
 for(int mode=0;mode<2;mode++){
  uint32_t mask= mode?0xe2e2e2e2u:0;
  Results r;
  auto get=[&](size_t i){return ins[i]^mask;};
  for(size_t i=0;i<ins.size();++i){
   uint32_t w=get(i);
   Op a=decode(w);
   if(a.kind==NONE)continue;
   if(a.kind==LS) {
    ++r.loadS;
    if(a.off<=0x600)r.shist[a.off]++;
   }
   if(a.off==0x168)r.n168[a.kind]++;
   if(a.off==0x16c)r.n16c[a.kind]++;
   if(a.off==0x170)r.n170[a.kind]++;
   if(a.off==0x174)r.n174[a.kind]++;
   if(a.off==0x176)r.n176[a.kind]++;
   if(a.kind==LB && a.off==0x176 && r.flags.size()<30)
      r.flags.push_back(hx(text.addr+i*4)+" "+kindName(a.kind)+" [X"+std::to_string(a.base)+", 0x176] register w"+std::to_string(a.dest));
   if((a.kind!=LS && a.kind!=LW)||a.base==31||a.off<0x40||a.off>0x600) continue;
   // Search for three 32-bit values at consecutive offsets on the same base register.
   int y=-1,z=-1;
   for(size_t k=i+1;k<std::min(ins.size(),i+49);k++){
    uint32_t ww=get(k);
    if(stop(ww))break;
    Op x=decode(ww);
    if(x.kind==a.kind && x.base==a.base && x.off==a.off+4 && y<0)y=(int)k;
    if(x.kind==a.kind && x.base==a.base && x.off==a.off+8 && z<0)z=(int)k;
    if(y>=0 && z>=0)break;
   }
   if(y<0||z<0)continue;
   ++r.anytriple;
   std::string s=hx(text.addr+i*4)+" -> "+hx(text.addr+y*4)+" -> "+hx(text.addr+z*4)+
                 " type="+kindName(a.kind)+" base=X"+std::to_string(a.base)+" off="+hx(a.off);
   if(r.anyhits.size()<80)r.anyhits.push_back(s);
   if(a.off==0x168) {++r.exacttriple;if(r.exacthits.size()<80)r.exacthits.push_back(s);}
  }
  std::cout<<"\n===== "<<(mode?"XOR_E2_DECODED":"RAW_ON_DISK")<<" =====\n";
  auto summary=[](std::array<uint64_t,8> const& a) {
   std::string s;
   for(int k=1;k<8;k++) if(a[k]) s+=std::string(kindName(k))+":"+std::to_string(a[k])+" ";
   return s;
  };
  std::cout<<"OFFSET_0x168 "<<summary(r.n168)<<"\n";
  std::cout<<"OFFSET_0x16C "<<summary(r.n16c)<<"\n";
  std::cout<<"OFFSET_0x170 "<<summary(r.n170)<<"\n";
  std::cout<<"OFFSET_0x174 "<<summary(r.n174)<<"\n";
  std::cout<<"OFFSET_0x176 "<<summary(r.n176)<<"\n";
  std::cout<<"TOTAL_LDRS "<<r.loadS<<" ANY_TRIPLES "<<r.anytriple<<" EXACT_168_16C_170_TRIPLES "<<r.exacttriple<<"\n";
  std::vector<std::pair<int,uint64_t>> h(r.shist.begin(),r.shist.end());
  std::sort(h.begin(),h.end(),[](auto a,auto b){return a.second>b.second;});
  std::cout<<"TOP_LDR_S_OFFSETS\n";
  for(size_t i=0;i<std::min<size_t>(20,h.size());i++)std::cout<<hx(h[i].first)<<" "<<h[i].second<<"\n";
  std::cout<<"FIRST_EXACT_TRIPLES\n";for(auto const&s:r.exacthits)std::cout<<s<<"\n";
  std::cout<<"FIRST_ANY_TRIPLES\n";for(auto const&s:r.anyhits)std::cout<<s<<"\n";
  std::cout<<"FIRST_FLAGS\n";for(auto const&s:r.flags)std::cout<<s<<"\n";
 }
 return 0;
}
