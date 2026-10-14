#!/usr/bin/env python3
"""Read-only ARM64 xref context of FEncVector/FEncHandler and EncLocation metadata."""
from pathlib import Path
import mmap,struct,subprocess,sys,hashlib,json,bisect
SO=Path(sys.argv[1]);OUT=Path("reports/deltaforce_fenc_context");OUT.mkdir(parents=True,exist_ok=True)
sites=[
 (0x09B337C8,"FEncHandler","0x205405b"),
 (0x0C3703A0,"FEncVector_register_A","0x2509232"),
 (0x0E77912C,"FEncVector_register_B","0x2509232"),
 (0x1B065C54,"FEncVector_register_C","0x2509232"),
 (0x160ADD94,"GetActorLocation","0x1a3ed44"),
]
def sha(p):
 h=hashlib.sha256()
 with p.open("rb") as f:
  for b in iter(lambda:f.read(4<<20),b""):h.update(b)
 return h.hexdigest()
def r2(data,label):
 file=OUT/(label+".bin");file.write_bytes(data)
 try:
  r=subprocess.run(["r2","-2","-q","-n","-a","arm","-b","64",
       "-c","e scr.color=false;pd 145 @ 0",str(file)],
        capture_output=True,text=True,timeout=120,errors="replace")
  return {"rc":r.returncode,"listing":(r.stdout+r.stderr)[-24000:]}
 except Exception as e:return {"rc":-1,"listing":str(e)}
with SO.open("rb") as fd:
 hdr=fd.read(64)
 fields=struct.unpack("<16sHHIQQQIHHHHHH",hdr)
 ident,etype,machine,ev,entry,phoff,shoff,flags,ehsize,phentsize,phnum,shentsize,shnum,shstrndx=fields
 assert ident[:6]==b"\x7fELF\x02\x01" and machine==183
 sec=[]
 for i in range(shnum):
  fd.seek(shoff+i*shentsize);n,t,fl,addr,off,size,l,info,al,es=struct.unpack_from("<IIQQQQIIQQ",fd.read(shentsize))
  sec.append({"nameoff":n,"va":addr,"off":off,"size":size})
 sh=sec[shstrndx];fd.seek(sh["off"]);names=fd.read(sh["size"])
 for x in sec:
  n=x["nameoff"];x["name"]=names[n:names.find(b"\0",n)].decode(errors="replace")
 txt=next(s for s in sec if s["name"]==".text")
 eh=next(s for s in sec if s["name"]==".eh_frame_hdr")
 mm=mmap.mmap(fd.fileno(),0,access=mmap.ACCESS_READ)
 count=struct.unpack_from("<I",mm,eh["off"]+8)[0]
 starts=sorted(set(eh["va"]+struct.unpack_from("<i",mm,eh["off"]+12+8*i)[0] for i in range(count)))
 starts=[x for x in starts if txt["va"]<=x<txt["va"]+txt["size"]]
 def read(va,n):
  assert txt["va"]<=va<txt["va"]+txt["size"]
  off=txt["off"]+(va-txt["va"])
  return mm[off:off+min(n,txt["size"]-(va-txt["va"]))]
 def u32(va):return struct.unpack("<I",read(va,4))[0]
 def signext(x,b):return x-(1<<b) if x&(1<<(b-1)) else x
 reports=[]
 for pc,name,target in sites:
  idx=bisect.bisect_right(starts,pc)-1
  start=starts[idx];end=starts[idx+1] if idx+1<len(starts) else start+0x1000
  # Validate ADRP effective page and find an ADD referencing the string.
  adrp=u32(pc)^0xe2e2e2e2
  imm=((((adrp>>5)&0x7ffff)<<2)|((adrp>>29)&3))
  page=(pc&~4095)+(signext(imm,21)<<12)
  addmatch=[]
  for off in range(4,64,4):
   w=u32(pc+off)^0xe2e2e2e2
   if w&0xff000000==0x91000000 and ((w>>5)&31)==(adrp&31):
    val=((w>>10)&4095)<< (12 if (w>>22)&1 else 0)
    addmatch.append({"pc":hex(pc+off),"calculated_target":hex(page+val),
      "wanted":target,"exact":page+val==int(target,16)})
  # Show bounded full-function beginning and localized xref snippet.
  fnlen=min(0x5c0,end-start)
  decoded=bytes(b^0xe2 for b in read(start,fnlen))
  window_start=max(start,pc-0x40)
  near=bytes(b^0xe2 for b in read(window_start,min(0x220,end-window_start)))
  primary=r2(decoded,name+"_FDE")
  nearby=r2(near,name+"_NEAR")
  row={"pc":hex(pc),"purpose":name,"rodata_string_va":target,
       "fde_start":hex(start),"fde_end":hex(end),"masked_first_word":hex(u32(start)),
       "decoded_first_word":hex(u32(start)^0xe2e2e2e2),
       "target_adrp_word":hex(adrp),"target_page":hex(page),"xref_add_matches":addmatch,
       "full_disassembly":primary["listing"],"nearby_disassembly":nearby["listing"],
       "near_window_va":hex(window_start)}
  reports.append(row)
  print("FUNC",name,hex(start),"REF",hex(pc),"RODATA",target,"ADRP_PAGE",hex(page),"ADD",addmatch,flush=True)
  print("NEARBY_DISASM",name,nearby["listing"][:10500],flush=True)
 (OUT/"fenc_xref_context.json").write_text(json.dumps({"sha256":sha(SO),"functions":reports},
                         indent=2,ensure_ascii=False))
 lines=["# FEncVector and FEncHandler ARM64 code-use disassembly","",
   "SO SHA256 "+sha(SO)]
 for x in reports:
  lines+=["","## "+x["purpose"],"FDE "+x["fde_start"]+".."+x["fde_end"],
     "Code XREF "+x["pc"]+" -> "+x["rodata_string_va"],
     "ADRP+ADD calculated targets: "+str(x["xref_add_matches"]),
     "XOR E2 decoded function code (addresses are FDE start + displayed offset):",
     x["full_disassembly"],"",
     "Near cross reference (addresses = near_window_va + displayed offset):",
     "Base "+x["near_window_va"],x["nearby_disassembly"]]
 (OUT/"fenc_xref_context.md").write_text("\n".join(lines)+"\n")
 print("FENC_XREF_COMPLETE",len(reports),flush=True)
 mm.close()
