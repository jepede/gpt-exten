#!/usr/bin/env python3
"""Evidence-focused stratified ARM64 executable-byte / disassembler validity audit.
Use actual ELF PT_LOAD or .text section; no execution and no code patch.
"""
import collections,hashlib,json,math,mmap,os,re,statistics,struct,subprocess,sys
from pathlib import Path
ELF=Path(sys.argv[1]);OUT=Path(sys.argv[2]);OUT.parent.mkdir(parents=True,exist_ok=True)
def entropy(b):
 if not b:return 0.
 c=collections.Counter(b);n=len(b)
 return round(-sum((v/n)*math.log2(v/n) for v in c.values()),4)
with ELF.open("rb") as f:
 mm=mmap.mmap(f.fileno(),0,access=mmap.ACCESS_READ)
 h=struct.unpack_from("<16sHHIQQQIHHHHHH",mm,0)
 _,_,machine,_,entry,phoff,shoff,_,_,phent,phnum,shent,shnum,shidx=h
 assert machine==183
 sections=[]
 for i in range(shnum):
  off=shoff+i*shent
  if off+64>len(mm):break
  name,t,flags,vaddr,foff,size,link,info,align,entsize=struct.unpack_from("<IIQQQQIIQQ",mm,off)
  sections.append(dict(idx=i,nameptr=name,type=t,flags=flags,addr=vaddr,off=foff,size=size))
 name_sh=sections[shidx]
 names=mm[name_sh["off"]:name_sh["off"]+name_sh["size"]]
 for s in sections:
  b=names.find(b"\x00",s["nameptr"])
  s["name"]=names[s["nameptr"]:b].decode("ascii","replace") if b>=0 else ""
 text=next(s for s in sections if s["name"]==".text")
 eh=next(s for s in sections if s["name"]==".eh_frame_hdr")
 hdr=mm[eh["off"]:eh["off"]+16];n_fde=struct.unpack_from("<I",hdr,8)[0]
 assert tuple(hdr[:4])==(1,0x1b,3,0x3b)
 starts=[]
 for i in range(n_fde):
  d=struct.unpack_from("<i",mm,eh["off"]+12+8*i)[0]
  starts.append(eh["addr"]+d)
 assert starts==sorted(starts)
 from bisect import bisect_left
 intervals=48
 special=[0x0815cdb0,0x0815d7f8,0x0815d938,0x0d1fbb60,0x0d1fbb84,0x0d1fbde4,0x1b8c08f0]
 pcs=[]
 for a in special:pcs.append((a,"special"))
 for i in range(intervals):
  addr=text["addr"]+(i*text["size"])//intervals
  j=bisect_left(starts,addr)
  if j<len(starts) and text["addr"]<=starts[j]<text["addr"]+text["size"]:
   pcs.append((starts[j],f"FDE-{i:02d}"))
 pcs.sort(key=lambda x:x[0])
 commands=["e scr.color=false","e asm.lines=false"]
 for a,tag in pcs:commands.append(f"pdj 40 @ 0x{a:x}")
 commands.append("q")
 p=subprocess.run(["r2","-q","-e","scr.color=false","-c",";".join(commands),str(ELF)],
  stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,errors="replace",timeout=240)
 arrays=[]
 for line in p.stdout.splitlines():
  line=line.strip()
  if not line.startswith("["):continue
  try:
   v=json.loads(line)
   if isinstance(v,list):arrays.append(v)
  except:pass
 def is_bad(op):
  name=(str(op.get("opcode",""))+" "+str(op.get("type",""))).lower()
  return any(x in name for x in ("invalid","ill","unk","unimp"))
 report={"r2_returncode":p.returncode,"r2_stderr_lines":[x for x in p.stdout.splitlines() if not x.startswith("[")][:30],
   "section_start":hex(text["addr"]),"section_size":text["size"],"eh_frame_hdr_fde_count":n_fde,
   "sample_requested":len(pcs),"sample_returned":len(arrays),"per_window":[]}
 for i,(addr,tag) in enumerate(pcs):
  op=arrays[i] if i<len(arrays) else []
  at=text["off"]+addr-text["addr"]
  sl=mm[at:at+4096]
  bad=sum(is_bad(v) for v in op)
  counts=collections.Counter(sl)
  row={"addr":hex(addr),"source":tag,"bytes_entropy":entropy(sl),"most_common_bytes":[[f"{k:02x}",v] for k,v in counts.most_common(8)],
        "n_ops":len(op),"bad_ops":bad,"bad_fraction":round(bad/max(1,len(op)),4),
        "first_eight":[{"addr":v.get("offset"),"hex":v.get("bytes"),"opcode":v.get("opcode"),"type":v.get("type")} for v in op[:8]]}
  report["per_window"].append(row)
 # "0xd1fbb60" code sample, relative header bounds
 at=text["off"]+0x0d1fbb60-text["addr"]
 report["historic_start_raw_hex"]=mm[at:at+256].hex(" ")
 mm.close()
 OUT.write_text(json.dumps(report,indent=2,ensure_ascii=False))
 print("R2_RC",p.returncode,"JSON_ARRAYS",len(arrays),"WINDOWS",len(pcs),flush=True)
 print("EH_FDES",n_fde,"SECTION_BYTES",text["size"],flush=True)
 for row in report["per_window"]:
  print("REGION",row["addr"],row["source"],"entropy",row["bytes_entropy"],"invalid",row["bad_ops"],"/",row["n_ops"],"top",row["most_common_bytes"][:3],flush=True)
 for row in report["per_window"]:
  if row["source"]=="special":
   print("DISASM_SAMPLE",row["addr"],json.dumps(row["first_eight"],ensure_ascii=False),flush=True)
 print("RAW_OLD",report["historic_start_raw_hex"][:300],flush=True)
