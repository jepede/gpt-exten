#include <cstdint>
#include <cstdio>
#include <cstring>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <vector>
#include <array>
#include <string>
#include <algorithm>
#include <map>
struct Ehdr { uint8_t ident[16]; uint16_t type,machine; uint32_t version; uint64_t entry,phoff,shoff; uint32_t flags; uint16_t ehsize,phentsize,phnum,shentsize,shnum,shstrndx; };
struct Shdr { uint32_t name,type; uint64_t flags,addr,offset,size; uint32_t link,info; uint64_t align,entsize; };
struct Load { int kind,imm,base,dest; };
static Load dec(uint32_t w) {
 auto op=(w & 0xffc00000u), imm=(w>>10)&0xfff;
 if(op==0xbd400000u) return {1,int(imm*4),(int)((w>>5)&31),(int)(w&31)}; // LDR S
 if(op==0xfd400000u) return {2,int(imm*8),(int)((w>>5)&31),(int)(w&31)}; // LDR D
 if(op==0xb9400000u) return {3,int(imm*4),(int)((w>>5)&31),(int)(w&31)}; // LDR W
 if(op==0xf9400000u) return {4,int(imm*8),(int)((w>>5)&31),(int)(w&31)}; // LDR X
 if(op==0x39400000u) return {5,int(imm),(int)((w>>5)&31),(int)(w&31)}; // LDRB W
 if(op==0x79400000u) return {6,int(imm*2),(int)((w>>5)&31),(int)(w&31)}; // LDRH W
 return {0,-1,-1,-1};
}
int main(int argc,char **argv) {
 if(argc<2) return 2;
 std::ifstream in(argv[1],std::ios::binary);
 if(!in) return 2;
 Ehdr eh{};
 in.read((char*)&eh,sizeof(eh));
 if(std::memcmp(eh.ident,"\x7f""ELF",4) || eh.machine!=183 || eh.shnum==0 || eh.shentsize!=sizeof(Shdr)) {
  std::cerr<<"Unsupported ELF header";return 2;
 }
 std::vector<Shdr> sections(eh.shnum);
 in.seekg(eh.shoff);in.read((char*)sections.data(),sections.size()*sizeof(Shdr));
 Shdr st=sections[eh.shstrndx];
 std::string names(st.size,'\0');in.seekg(st.offset);in.read(&names[0],names.size());
 Shdr text{};
 bool found=false;
 for(auto s:sections) {
  if(s.name<names.size() && std::strcmp(names.c_str()+s.name,".text")==0) {text=s;found=true;break;}
 }
 if(!found) return 3;
 if(text.size>1000000000) return 4;
 std::vector<uint32_t> words(text.size/4);
 in.seekg(text.offset);in.read((char*)words.data(),words.size()*4);
 std::cout << "TEXT VA 0x"<<std::hex<<text.addr<<std::dec<<" BYTES "<<text.size<<" INSTRUCTIONS "<<words.size()<<"\n";
 uint64_t ldr_s168=0,s16c=0,s170=0,s174=0, flag176=0, ldr_s_other=0;
 std::map<int,uint64_t> other;
 struct Pair{size_t idx;int base;int kind;};
 std::vector<Pair> candidates;
 for(size_t i=0;i<words.size();++i) {
  Load x=dec(words[i]);
  if(x.kind==1) {
   if(x.imm==0x168){ldr_s168++;candidates.push_back({i,x.base,x.kind});}
   if(x.imm==0x16c)s16c++;
   if(x.imm==0x170)s170++;
   if(x.imm==0x174)s174++;
   if(x.imm<0x400)other[x.imm]++;
   ldr_s_other++;
  }
  if(x.kind==5 && x.imm==0x176)flag176++;
 }
 std::cout<<"LDR_S_168 "<<ldr_s168<<" LDR_S_16c "<<s16c<<" LDR_S_170 "<<s170<<" LDR_S_174 "<<s174<<" LDRB_176 "<<flag176<<"\n";
 std::cout<<"Top twenty S imm offsets (up to 0x400):\n";
 std::vector<std::pair<int,uint64_t>> hist(other.begin(),other.end());
 std::sort(hist.begin(),hist.end(),[](auto a,auto b){return a.second>b.second;});
 for(size_t i=0;i<std::min<size_t>(20,hist.size());++i) std::cout<<"0x"<<std::hex<<hist[i].first<<std::dec<<" "<<hist[i].second<<"\n";
 std::cout<<"Potential same-base FVector load (first 70):\n";
 size_t triple=0;
 for(auto c:candidates){
  bool b=false,d=false;
  size_t ia=0,ib=0;
  for(size_t k=c.idx+1;k<std::min(c.idx+49,words.size());++k) {
   auto l=dec(words[k]);
   if(l.kind==1 && l.base==c.base && l.imm==0x16c){b=true;ia=k;}
   if(l.kind==1 && l.base==c.base && l.imm==0x170){d=true;ib=k;}
   if(b&&d) break;
   // stop after RET or unconditional B to avoid cross-function matches
   auto op=words[k];
   if((op&0xfffffc1fu)==0xd65f0000u || (op&0xfc000000u)==0x14000000u)break;
  }
  if(b&&d){triple++;if(triple<=70)std::cout<<"TRIPLE 0x"<<std::hex<<(text.addr+c.idx*4)<<" 0x"<<(text.addr+ia*4)<<" 0x"<<(text.addr+ib*4)<<std::dec<<" base=x"<<c.base<<"\n";}
 }
 std::cout<<"TRIPLE_TOTAL "<<triple<<"\n";
 return 0;
}