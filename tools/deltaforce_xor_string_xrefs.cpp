#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdio>
#include <cstring>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>
#include <map>
struct EH { unsigned char e[16];uint16_t type,machine;uint32_t version;uint64_t entry,phoff,shoff;uint32_t flags;uint16_t ehsize,phentsize,phnum,shentsize,shnum,shstrndx; };
struct SH { uint32_t name,type;uint64_t flags,addr,offset,size;uint32_t link,info;uint64_t align,entsize; };
struct Str {uint64_t addr;std::string name;};
struct Ref {uint64_t pc,target,fn;unsigned idx;std::string how;bool decoded;};
static std::string hx(uint64_t v){char b[40];snprintf(b,sizeof(b),"0x%llx",(unsigned long long)v);return b;}
static int64_t signext(uint64_t x,int bits){uint64_t hi=uint64_t(1)<<(bits-1);return int64_t((x^hi)-hi);}
int main(int argc,char** argv){
 if(argc<3){std::cerr<<"Usage ELF targets.tsv";return 2;}
 std::ifstream f(argv[1],std::ios::binary);
 std::ifstream lines(argv[2]);
 if(!f||!lines)return 3;
 EH e{}; f.read((char*)&e,sizeof(e));
 if(std::memcmp(e.e,"\x7f""ELF",4)||e.machine!=183)return 4;
 std::vector<SH> sect(e.shnum);f.seekg(e.shoff);f.read((char*)sect.data(),sect.size()*sizeof(SH));
 std::string shstr(sect[e.shstrndx].size,'\0');f.seekg(sect[e.shstrndx].offset);f.read(&shstr[0],shstr.size());
 SH text{},eh{};bool tf=false,hf=false;
 for(auto const&s:sect){
  if(s.name>=shstr.size())continue;
  const char*n=shstr.c_str()+s.name;
  if(!std::strcmp(n,".text")){text=s;tf=true;}
  if(!std::strcmp(n,".eh_frame_hdr")){eh=s;hf=true;}
 }
 if(!tf||!hf||text.size>1000000000)return 5;
 std::vector<Str> targets;std::unordered_map<uint64_t,std::vector<size_t>> targetPages;
 std::string row;
 while(std::getline(lines,row)){
  auto tab=row.find('\t');if(tab==std::string::npos)continue;
  uint64_t va=0;try{va=std::stoull(row.substr(0,tab),nullptr,0);}catch(...){continue;}
  if(targets.size()>=50000)break;
  size_t idx=targets.size();
  targets.push_back({va,row.substr(tab+1)});
  targetPages[va&~uint64_t(0xfff)].push_back(idx);
 }
 std::cout<<"TARGETS "<<targets.size()<<" UNIQUE_PAGES "<<targetPages.size()<<"\n";
 std::vector<uint32_t> instructions(text.size/4);
 f.seekg(text.offset);f.read((char*)instructions.data(),text.size/4*4);
 // Parse function starts from .eh_frame_hdr.
 std::vector<uint64_t> starts;
 f.seekg(eh.offset);std::array<unsigned char,12> hdr{};f.read((char*)hdr.data(),12);
 if(hdr[0]==1&&hdr[1]==0x1b&&hdr[2]==3&&hdr[3]==0x3b){
  uint32_t count=0;std::memcpy(&count,hdr.data()+8,4);
  if(count<3000000){
   starts.reserve(count);
   for(uint32_t i=0;i<count;i++){
    int32_t delta=0,fde=0;f.read((char*)&delta,4);f.read((char*)&fde,4);
    int64_t va=int64_t(eh.addr)+delta;
    if(va>=int64_t(text.addr)&&va<int64_t(text.addr+text.size))starts.push_back(uint64_t(va));
   }
   std::sort(starts.begin(),starts.end());
   starts.erase(std::unique(starts.begin(),starts.end()),starts.end());
  }
 }
 auto nearest=[&](uint64_t v){
  auto i=std::upper_bound(starts.begin(),starts.end(),v);
  return i==starts.begin()?uint64_t(0):*(i-1);
 };
 std::vector<Ref> results;
 std::map<std::string,uint64_t> found;
 constexpr uint64_t MASK=0xe2e2e2e2;
 constexpr int WINDOWS=12;
 uint64_t testedAdrps[2]={0,0},hitAdrps[2]={0,0};
 for(int mode=0;mode<2;mode++){
  uint32_t mask=mode?uint32_t(MASK):0;
  for(size_t i=0;i<instructions.size();i++){
   uint64_t pc=text.addr+i*4;
   uint32_t w=instructions[i]^mask;
   if((w&0x9f000000u)==0x90000000u){
    testedAdrps[mode]++;
    uint64_t field=(((uint64_t(w)>>5)&0x7ffff)<<2)|((w>>29)&3);
    int64_t delta=signext(field,21)*4096;
    uint64_t page=(pc&~uint64_t(0xfff))+delta;
    auto it=targetPages.find(page);
    if(it==targetPages.end())continue;
    hitAdrps[mode]++;
    int reg=w&31;
    for(size_t k=i+1;k<std::min(instructions.size(),i+WINDOWS+1);k++){
     uint32_t next=instructions[k]^mask;
     if((next&0xff000000u)==0x91000000u&&int((next>>5)&31)==reg){
      uint64_t imm=(next>>10)&0xfff;
      if(next&(1u<<22))imm<<=12;
      uint64_t addr=page+imm;
      for(auto x:it->second)if(targets[x].addr==addr){
       results.push_back({pc,addr,nearest(pc),unsigned(x),"ADRP+ADD",mode!=0});
       found[targets[x].name.substr(0,targets[x].name.find(' '))]++;
      }
     }
     if((next&0xffc00000u)==0xf9400000u&&int((next>>5)&31)==reg){
      uint64_t addr=page+uint64_t((next>>10)&0xfff)*8;
      for(auto x:it->second)if(targets[x].addr==addr){
       results.push_back({pc,addr,nearest(pc),unsigned(x),"ADRP+LDR_X",mode!=0});
       found[targets[x].name.substr(0,targets[x].name.find(' '))]++;
      }
     }
     if((next&0xfc000000u)==0x14000000u||(next&0xfffffc1fu)==0xd65f0000u)break;
    }
   } else if((w&0x9f000000u)==0x10000000u){
    uint64_t field=(((uint64_t(w)>>5)&0x7ffff)<<2)|((w>>29)&3);
    uint64_t addr=pc+signext(field,21);
    auto it=targetPages.find(addr&~uint64_t(0xfff));
    if(it==targetPages.end())continue;
    for(auto x:it->second)if(targets[x].addr==addr){
     results.push_back({pc,addr,nearest(pc),unsigned(x),"ADR",mode!=0});
     found[targets[x].name.substr(0,targets[x].name.find(' '))]++;
    }
   }
  }
 }
 std::cout<<"ADRP_TESTED RAW "<<testedAdrps[0]<<" XOR "<<testedAdrps[1]<<"\n";
 std::cout<<"ADRP_TARGET_PAGE_MATCH RAW "<<hitAdrps[0]<<" XOR "<<hitAdrps[1]<<"\n";
 std::cout<<"REFERENCES_FOUND "<<results.size()<<"\n";
 std::cout<<"TERM_REFERENCE_COUNTS\n";
 for(auto const &x:found)std::cout<<x.first<<" "<<x.second<<"\n";
 std::cout<<"FIRST_200_REFERENCES\n";
 size_t n=0;
 for(auto const&x:results){
  if(n++>=200)break;
  std::cout<<(x.decoded?"E2":"RAW")<<" "<<x.how<<" PC="<<hx(x.pc)
      <<" FUNC="<<hx(x.fn)<<" TARGET="<<hx(x.target)
      <<" TERM="<<targets[x.idx].name.substr(0,150)<<"\n";
 }
 std::ofstream t("reports/deltaforce_ref_xrefs/code_string_xrefs.tsv");
 if(!t)return 6;
 t<<"Mode\tPC\tFDE\tKind\tTargetVA\tLabel\n";
 for(auto const&x:results){
  t<<(x.decoded?"XOR_E2":"RAW")<<'\t'<<hx(x.pc)<<'\t'<<hx(x.fn)<<'\t'
   <<x.how<<'\t'<<hx(x.target)<<'\t'<<targets[x.idx].name<<"\n";
 }
 return 0;
}
