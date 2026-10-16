#!/usr/bin/env python3
"""Confirm original ARM64 callback slot registration value from source ELF. Static only."""
from pathlib import Path
import hashlib,json,mmap,struct,subprocess,sys,zipfile
apk=Path(sys.argv[1]);target=Path("work/ace_hook_init_libue4.so");target.parent.mkdir(parents=True,exist_ok=True)
OUT=Path("reports/deltaforce_ace_init");OUT.mkdir(parents=True,exist_ok=True)
if not target.exists():
 with zipfile.ZipFile(apk) as z:
  with z.open("lib/arm64-v8a/libUE4.so") as inp,target.open("wb") as out:
   for chunk in iter(lambda:inp.read(12<<20),b""):out.write(chunk)
h=hashlib.sha256()
with target.open("rb") as fd:
 for b in iter(lambda:fd.read(12<<20),b""):h.update(b)
assert h.hexdigest()=="387cd911a67eca1069bd5e4c874bce5dfb14823ca75f55f1ae7c43a09f2f1441"
CODE_BASE=0x815cdb0
FNS=[
 ("initialize_A",0x13120490,0x13120538),
 ("initialize_B",0x10c259d4,0x10c25b40),
 ("component_coord_read",0x104f7284,0x104f735c),
 ("component_handler",0x0aae708c,0x0aae7098),
]
with target.open("rb") as f:
 mm=mmap.mmap(f.fileno(),0,access=mmap.ACCESS_READ)
 hdr=struct.unpack_from("<16sHHIQQQIHHHHHH",mm,0)
 _,_,_,_,_,_,shoff,_,_,_,_,shsz,shn,shstr=hdr
 sh=[]
 for i in range(shn):
  fields=struct.unpack_from("<IIQQQQIIQQ",mm,shoff+i*shsz)
  sh.append(fields)
 namesec=sh[shstr]
 names=mm[namesec[4]:namesec[4]+namesec[5]]
 sections={}
 for q in sh:
  no=q[0];name=names[no:names.find(b"\0",no)].decode(errors="replace")
  sections[name]={"addr":q[3],"off":q[4],"size":q[5]}
 t=sections[".text"];mask=bytes(x^0xe2 for x in range(256))
 def word(pc):
  off=t["off"]+pc-t["addr"]
  return struct.unpack_from("<I",mm,off)[0]^0xe2e2e2e2
 def sext(v,n):return v-(1<<n) if v&(1<<(n-1)) else v
 evidence=[]
 for label,begin,end in FNS:
  off=t["off"]+begin-t["addr"]
  raw=mm[off:off+(end-begin)]
  dec=raw.translate(mask)
  tmp=OUT/(label+".bin");tmp.write_bytes(dec)
  o=subprocess.run(["r2","-2","-q","-n","-a","arm","-b","64","-c","e scr.color=false;pd "+str(min(130,len(dec)//4))+" @ 0",str(tmp)],capture_output=True,text=True,timeout=60)
  stat={"label":label,"rva_begin":hex(begin),"rva_end":hex(end),"disasm_local":o.stdout[:17000]}
  if label.startswith("initialize"):
   addresses=[]
   for pc in range(begin,end,4):
    w=word(pc)
    if (w&0xffc00000)==0xf9000000:
     base=(w>>5)&31;src=w&31;imm=((w>>10)&4095)*8
     if imm!=0xdb8:continue
     preceding=[]
     # Search backwards 20 insns for ADRP X8 and ADRP+ADD X9 yielding exact target.
     for prev in range(max(begin,pc-80),pc,4):
      a=word(prev)
      if (a&0x9f000000)!=0x90000000:continue
      page=(prev&~4095)+(sext(((((a>>5)&0x7ffff)<<2)|((a>>29)&3)),21)<<12)
      dst=a&31
      vals=[]
      for after in range(prev+4,pc,4):
       x=word(after)
       if (x&0xff000000)==0x91000000 and ((x>>5)&31)==dst and (x&31)==dst:
        add=((x>>10)&4095)<<(12 if x&(1<<22) else 0)
        vals.append({"pc":hex(after),"effective":hex(page+add)})
      preceding.append({"adrp_pc":hex(prev),"dest":"X"+str(dst),"page":hex(page),"ADD":vals})
     addresses.append({"STR_pc":hex(pc),"src":"X"+str(src),"base":"X"+str(base),"offset":hex(imm),"candidates":preceding})
   stat["writes"]=addresses
  evidence.append(stat)
  print("INIT_TRACE",label,json.dumps(stat.get("writes",[]),ensure_ascii=False)[:8500],flush=True)
  print("INIT_DISASM",label,o.stdout[:7500].replace("\n"," | "),flush=True)
 mm.close()
(OUT/"registration.json").write_text(json.dumps(evidence,ensure_ascii=False,indent=2))
lines=["# Delta Force native callback installation exact values","",
       "Source ELF SHA256 "+h.hexdigest()]
for item in evidence:
 lines+=["","## "+item["label"]+" from "+item["rva_begin"],
  "Decoded registration records: "+json.dumps(item.get("writes",[]),ensure_ascii=False),
  "Disasm display starts at 0; real RVA is begin + shown offset.","~~~asm",item["disasm_local"],"~~~"]
(OUT/"registration.md").write_text("\n".join(lines))
print("REGISTRATION_AUDIT_DONE",flush=True)
