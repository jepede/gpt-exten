#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdio>
#include <cstring>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
struct ELF { uint8_t ident[16]; uint16_t type,machine; uint32_t version; uint64_t entry,phoff,shoff; uint32_t flags; uint16_t ehsize,phentsize,phnum,shentsize,shnum,shstrndx; };
struct SH { uint32_t name,type; uint64_t flags,addr,off,size; uint32_t link,info; uint64_t align,entsize; };
struct Field { unsigned mask=0; std::array<uint64_t,6> pc{}; };
std::string hx(uint64_t v){char b[30];snprintf(b,sizeof(b),"0x%llx",(unsigned long long)v);return b;}
int main(int argc,char**argv){
 if(argc<2)return 2;
 std::ifstream fd(argv[1],std::ios::binary);if(!fd)return 3;
 ELF e{};fd.read((char*)&e,sizeof(e));
 if(memcmp(e.ident,"\x7f""ELF",4)||e.machine!=183||e.shnum>128)return 4;
 std::vector<SH> sections(e.shnum);
 fd.seekg(e.shoff);fd.read((char*)sections.data(),sections.size()*sizeof(SH));
 std::string names(sections[e.shstrndx].size,'\0');
 fd.seekg(sections[e.shstrndx].off);fd.read(&names[0],names.size());
 SH txt{},eh{};bool t=false,h=false;
 for(auto s:sections){
  if(s.name>=names.size())continue;
  std::string n(names.c_str()+s.name);
  if(n==".text"){txt=s;t=true;}
  if(n==".eh_frame_hdr"){eh=s;h=true;}
 }
 if(!t||!h)return 5;
 std::vector<uint8_t> hdr(std::min<uint64_t>(eh.size,24),0);
 fd.seekg(eh.off);fd.read((char*)hdr.data(),hdr.size());
 if(hdr.size()<12 || hdr[0]!=1 || hdr[1]!=0x1b || hdr[2]!=3 || hdr[3]!=0x3b)return 6;
 uint32_t count;memcpy(&count,hdr.data()+8,4);
 if(count==0 || count>3000000)return 7;
 std::vector<int32_t> deltas(count);
 fd.seekg(eh.off+12);
 for(uint32_t i=0;i<count;i++){
  int32_t fde=0;fd.read((char*)&deltas[i],4);fd.read((char*)&fde,4);
 }
 std::vector<uint32_t> starts;starts.reserve(count);
 for(auto d:deltas) {
  int64_t va=int64_t(eh.addr)+d;
  if(va>=int64_t(txt.addr) && va<int64_t(txt.addr+txt.size) && (va%4==0))
   starts.push_back(uint32_t(va));
 }
 std::sort(starts.begin(),starts.end());
 starts.erase(std::unique(starts.begin(),starts.end()),starts.end());
 std::vector<uint32_t> ins(txt.size/4);
 fd.seekg(txt.off);fd.read((char*)ins.data(),ins.size()*4);
 uint64_t fn3=0,fn4=0,fn5=0, fn4short=0, fn5short=0;
 std::vector<std::string> matches4,matches5;
 std::array<Field,31> states{};
 size_t idx=0;
 auto flush=[&](uint64_t start,uint64_t end){
  for(size_t base=0;base<31;base++){
   auto f=states[base];
   if((f.mask&7)==7)fn3++;
   if((f.mask&15)==15){
    fn4++;
    uint64_t mn=~uint64_t(0),mx=0;
    for(int k=0;k<4;k++){mn=std::min(mn,f.pc[k]);mx=std::max(mx,f.pc[k]);}
    if(mx-mn<=0x400){
     fn4short++;
     if(matches4.size()<110)matches4.push_back("FDE="+hx(start)+".."+hx(end)+" BASE X"+std::to_string(base)+" XYZ "+hx(f.pc[0])+" "+hx(f.pc[1])+" "+hx(f.pc[2])+" FLAG "+hx(f.pc[3])+" SPAN "+hx(mx-mn)+" FLAGS="+hx(f.mask));
    }
   }
   if((f.mask&31)==31){
    fn5++;
    uint64_t mn=~uint64_t(0),mx=0;
    for(int k=0;k<5;k++){mn=std::min(mn,f.pc[k]);mx=std::max(mx,f.pc[k]);}
    if(mx-mn<=0x400){
     fn5short++;
     if(matches5.size()<110)matches5.push_back("FDE="+hx(start)+".."+hx(end)+" BASE X"+std::to_string(base)+" XYZ "+hx(f.pc[0])+" "+hx(f.pc[1])+" "+hx(f.pc[2])+" FLAG "+hx(f.pc[3])+" INDEX "+hx(f.pc[4])+" SPAN "+hx(mx-mn)+" FLAGS="+hx(f.mask));
    }
   }
  }
  states={};
 };
 if(starts.empty())return 8;
 for(size_t i=0;i<ins.size();i++){
  uint64_t va=txt.addr+4*i;
  if(va<starts[0])continue;
  while(idx+1<starts.size() && va>=starts[idx+1]){
   flush(starts[idx],starts[idx+1]);
   idx++;
  }
  uint32_t w=ins[i]^0xe2e2e2e2u;
  uint32_t op=w&0xffc00000u;
  unsigned imm=(w>>10)&0xfff, base=(w>>5)&31;
  if(base>=31)continue;
  int field=-1;
  if(op==0xbd400000u){
   unsigned off=imm*4;
   if(off==0x168)field=0;
   if(off==0x16c)field=1;
   if(off==0x170)field=2;
  }
  if(op==0x39400000u && imm==0x176)field=3;
  if(op==0x79400000u && imm*2==0x174)field=4;
  if((op==0xf9400000u && imm*8==0x210) || (op==0xb9400000u && imm*4==0x210))field=5;
  if(field<0)continue;
  auto &f=states[base];
  unsigned bit=1u<<field;
  if(!(f.mask&bit)){f.mask|=bit;f.pc[field]=va;}
 }
 flush(starts[idx],txt.addr+txt.size);
 std::cout<<"LIB_FUNCTIONS_FROM_EH "<<starts.size()<<"\n";
 std::cout<<"FDE_WITH_SAME_BASE_XYZ "<<fn3<<"\n";
 std::cout<<"FDE_WITH_SAME_BASE_XYZ_AND_FLAG "<<fn4<<"\n";
 std::cout<<"FDE_WITH_SAME_BASE_XYZ_AND_FLAG_WITHIN_0x400 "<<fn4short<<"\n";
 std::cout<<"FDE_WITH_SAME_BASE_XYZ_AND_FLAG_AND_INDEX "<<fn5<<"\n";
 std::cout<<"FDE_WITH_SAME_BASE_ALL_FIVE_WITHIN_0x400 "<<fn5short<<"\n";
 std::cout<<"CANDIDATES_FLAG_AND_TRIPLE\n";
 for(auto const& s:matches4)std::cout<<s<<"\n";
 std::cout<<"CANDIDATES_ALL_FIVE\n";
 for(auto const& s:matches5)std::cout<<s<<"\n";
 std::cout<<"CAVEAT: register value may change between accesses, FDE ranges may contain aliases; candidates require def-use and call graph checks.\n";
 return 0;
}
