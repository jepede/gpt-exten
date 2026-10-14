#!/usr/bin/env python3
"""Extended read-only ELF analysis. Do not infer coordinate crypto from generic tokens."""
from pathlib import Path
import hashlib,json,math,mmap,os,struct,subprocess,sys,zipfile
ROOT=Path("reports/deltaforce2"); ROOT.mkdir(parents=True,exist_ok=True)
APK=Path(sys.argv[1]); ELF=Path("work/deep/libUE4.so")
with zipfile.ZipFile(APK) as z:
 name="lib/arm64-v8a/libUE4.so"
 assert name in z.namelist()
 ELF.parent.mkdir(parents=True,exist_ok=True)
 with z.open(name) as src,ELF.open("wb") as out:
  while True:
   b=src.read(8<<20)
   if not b: break
   out.write(b)
def sha(path):
 h=hashlib.sha256()
 with path.open("rb") as f:
  for b in iter(lambda:f.read(8<<20),b""):h.update(b)
 return h.hexdigest()
def run(args,seconds=90):
 try:
  p=subprocess.run(args,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,encoding="utf8",errors="replace",timeout=seconds)
  return {"status":p.returncode,"text":p.stdout[:55000]}
 except Exception as e:return {"status":-1,"text":str(e)}
def entropy(data):
 if not data:return 0.
 from collections import Counter
 freq=Counter(data)
 return round(-sum((v/len(data))*math.log2(v/len(data)) for v in freq.values()),4)
with ELF.open("rb") as f:
 header=f.read(64)
 assert header[:6]==b"\x7fELF\x02\x01"
 data=struct.unpack("<16sHHIQQQIHHHHHH",header)
 _,e_type,e_machine,e_version,e_entry,e_phoff,e_shoff,e_flags,e_ehsize,e_phentsize,e_phnum,e_shentsize,e_shnum,e_shstrndx=data
 sections=[]
 for i in range(e_shnum):
  f.seek(e_shoff+i*e_shentsize)
  d=f.read(e_shentsize)
  if len(d)<64:break
  name,typ,flags,addr,off,size,link,info,addralign,entsize=struct.unpack_from("<IIQQQQIIQQ",d)
  sections.append(dict(index=i,name_off=name,type=typ,flags=flags,addr=addr,offset=off,size=size,link=link,info=info,alignment=addralign))
 if e_shstrndx<len(sections):
  s=sections[e_shstrndx]
  f.seek(s["offset"]);names=f.read(min(2<<20,s["size"]))
  for v in sections:
   k=v["name_off"];v["name"]=names[k:names.find(b"\0",k)].decode("ascii","replace") if k<len(names) else "UNKNOWN"
 segments=[]
 for i in range(e_phnum):
  f.seek(e_phoff+i*e_phentsize);b=f.read(e_phentsize)
  p_type,p_flags,p_offset,p_vaddr,p_paddr,p_filesz,p_memsz,p_align=struct.unpack_from("<IIQQQQQQ",b)
  segments.append(dict(type=p_type,flags=p_flags,offset=p_offset,va=p_vaddr,filesz=p_filesz,memsz=p_memsz,align=p_align))
 report={"ELF_size":ELF.stat().st_size,"sha256":sha(ELF),"ELF_type":e_type,"machine":e_machine,"entry":e_entry,"section_count":e_shnum,"sections":sections,"segments":segments}
 f.seek(0)
 mm=mmap.mmap(f.fileno(),0,access=mmap.ACCESS_READ)
 section_metrics=[]
 for s in sections:
  if s["type"]==8 or s["size"]==0 or s["offset"]>=len(mm):continue
  avail=min(s["size"],len(mm)-s["offset"])
  # sample 64 near-even chunks across section; deterministic
  chunks=[]
  for j in range(min(64,max(1,(avail+4095)//4096))):
   at=s["offset"]+int(j*max(0,avail-4096)/max(1,min(64,(avail+4095)//4096)-1))
   chunks.append(mm[at:at+min(4096,avail)])
  sam=b"".join(chunks)
  printable=sum(32<=v<127 for v in sam)/max(1,len(sam))
  section_metrics.append({"name":s.get("name",""),"bytes":s["size"],"entropy_sample":entropy(sam),"ascii_ratio_sample":round(printable,4),"va":hex(s["addr"])})
 report["section_metrics"]=section_metrics
 needles=["USceneComponent","FEncVector","FEncHandler","RelativeLocation","ComponentToWorld","GetActorLocation","SetActorLocation","FVector","FTransform","/Script/Engine","UWorld","GWorld","Unreal","ue4","Engine","bEncrypted","Encrypt","Decrypt","ACE","tprt","tersafe","sm4","aes","Quaternion","LocalToWorld","transform","Location","Vector"]
 matches={}
 for name in needles:
  a=name.encode();w=name.encode("utf-16le")
  def findall(b,limit=10):
   pos=0;out=[]
   while len(out)<limit:
    i=mm.find(b,pos)
    if i<0:break
    surrounding=mm[max(0,i-16):i+len(b)+60]
    out.append({"offset":hex(i),"context_hex":surrounding[:72].hex(),"context_ascii":surrounding.decode("latin1","replace")[:90]})
    pos=i+len(b)
   return out
  matches[name]={"ascii":findall(a),"utf16le":findall(w)}
 report["candidate_strings"]=matches
 pattern=bytes.fromhex("006841bd016c41bd027041bdc0035fd6")
 offsets=[];start=0
 while len(offsets)<16:
  x=mm.find(pattern,start)
  if x<0:break
  offsets.append(hex(x));start=x+16
 report["old_proposed_coordinate_ldr_pattern"]=offsets
 # Indirect branch instructions; these alone are not evidence of OLLVM.
 info={}
 for nam,bits in {"br_x16":"00021fd6","br_x17":"20021fd6","paciasp":"3f2303d5","autiasp":"bf2303d5","retaa":"ff0b5fd6"}.items():
  pattern=bytes.fromhex(bits);ofs=[];p=0
  while len(ofs)<10:
   x=mm.find(pattern,p)
   if x<0:break
   ofs.append(hex(x));p=x+4
  info[nam]={"sample":ofs,"count_at_least":len(ofs)}
 report["instruction_signatures_filewide_bounded"]=info
 mm.close()
report["rabin2_header"]=run(["rabin2","-I",str(ELF)],seconds=120)
report["rabin2_sections"]=run(["rabin2","-S",str(ELF)],seconds=120)
report["readelf_dynamic"]=run(["readelf","-W","-d",str(ELF)],seconds=120)
report["readelf_segments"]=run(["readelf","-W","-l",str(ELF)],seconds=90)
report["readelf_sections"]=run(["readelf","-W","-S",str(ELF)],seconds=90)
code_sec=next((x for x in sections if x.get("name") in (".text",".text.hot",".text1")),None)
if code_sec:
 report["r2_disasm_text_start"]=run(["r2","-2","-q","-c","pd 42 @ "+hex(code_sec["addr"]),str(ELF)],seconds=180)
else:
 report["r2_disasm_text_start"]={"status":-1,"text":"No .text section; refer to executable PT_LOAD"}
out=["# DeltaForce native ELF deeper static inspection","",
     "Main ELF SHA256: "+report["sha256"],
     "ELF64 e_type/e_machine: "+str(e_type)+"/"+str(e_machine),
     "Sections: "+str(len(sections))+" Program headers: "+str(len(segments)),"",
     "## Sections with bounded entropy/ascii sampling",""]
for x in section_metrics:
 out.append("- "+x["name"]+": bytes="+str(x["bytes"])+", sample H="+str(x["entropy_sample"])+", printable="+str(x["ascii_ratio_sample"]))
out+=["","## Type/coordinate signatures (ASCII + UTF16LE first ten hits)"]
for k,v in matches.items():
 out.append("- "+k+": ASCII="+str(len(v["ascii"]))+" UTF16LE="+str(len(v["utf16le"])))
 if k in ("FEncVector","FEncHandler","USceneComponent","RelativeLocation","GetActorLocation","bEncrypted","FVector"):
  out.extend(["    - "+str(j["offset"])+" (ASCII)" for j in v["ascii"][:8]])
  out.extend(["    - "+str(j["offset"])+" (UTF16)" for j in v["utf16le"][:8]])
out+=["","## Hypothesis test","Candidate old-version consecutive X/Y/Z ARM64 float loads followed by RET: "+str(offsets),
      "Signature matches are only pattern candidates, NOT function identity or current offsets.",
      "","## Program headers","",report["readelf_segments"]["text"],
      "","## Section headers","",report["readelf_sections"]["text"],
      "","## radare2 ELF inspection","",report["rabin2_header"]["text"],
      "","## Disassembly at first .text instruction","",report["r2_disasm_text_start"]["text"]]
(ROOT/"elf_deep.md").write_text("\n".join(out))
(ROOT/"elf_deep.json").write_text(json.dumps(report,ensure_ascii=False,indent=2))
print("ELF FULL SUMMARY",json.dumps({"sha256":report["sha256"],"bytes":report["ELF_size"],"sections":len(sections),"segments":len(segments),"old_relative_coord_ldr_hits":offsets,"exact_name_hits":{x:[len(v["ascii"]),len(v["utf16le"])] for x,v in matches.items() if x in ("FEncVector","FEncHandler","USceneComponent","RelativeLocation","GetActorLocation","bEncrypted","FVector")} },ensure_ascii=False),flush=True)
print("SECTION METRICS",json.dumps(section_metrics,ensure_ascii=False),flush=True)
print("ELF READ ELF",report["readelf_sections"]["text"][:13000],flush=True)
print("ELF PROGRAM HEADERS",report["readelf_segments"]["text"][:8000],flush=True)
print("R2 HEADER",report["rabin2_header"]["text"][:8000],flush=True)
print("R2 CODE SAMPLE",report["r2_disasm_text_start"]["text"][:9000],flush=True)
