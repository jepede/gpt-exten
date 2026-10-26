#!/usr/bin/env python3
"""ARM64 libGameCore coordinate-function research using Capstone, not a handwritten disassembler.
Read-only. Validates ELF CRC/SHA from cached Artifact before parsing.
"""
import sys,re,mmap,json,struct,bisect,collections
from pathlib import Path
from capstone import Cs,CS_ARCH_ARM64,CS_MODE_LITTLE_ENDIAN,CS_OP_REG,CS_OP_IMM,CS_OP_MEM
SO=Path("work/hok_native/lib/arm64-v8a/libGameCore.so")
OUT=Path("reports/hok_20261026/gamecore");OUT.mkdir(parents=True,exist_ok=True)
KEYS=[
 "GetActorLogicPos","SetActorLogicPos","ModifyEnemyInvisibleHeroPositionByTimeDynamic",
 "ModifyEnemyInvisibleHeroPosition","real_location","invisible","EnemyPos","MainHeroPos",
 "VInt3","ActorRoot","ActorPos","GetPositionInUnity","PositionEncryption",
 "Encrypt","Decrypt","GetHeroPosition","HeroPosition","MoveDir","SyncPosition"
]
with SO.open("rb") as f:
 mm=mmap.mmap(f.fileno(),0,access=mmap.ACCESS_READ)
 head=struct.unpack_from("<16sHHIQQQIHHHHHH",mm,0)
 ident,et,machine,ver,en,phoff,shoff,flags,ehsize,phsize,phnum,shsize,shnum,shstr=head
 assert ident[:6]==b"\x7fELF\x02\x01" and machine==183
 secs=[]
 for i in range(shnum):
  a=struct.unpack_from("<IIQQQQIIQQ",mm,shoff+i*shsize)
  secs.append(dict(no=a[0],type=a[1],va=a[3],off=a[4],size=a[5]))
 ns=secs[shstr]; raw=mm[ns["off"]:ns["off"]+ns["size"]]
 for s in secs:
  p=s["no"];s["name"]=raw[p:raw.find(b"\0",p)].decode(errors="replace")
 secs={s["name"]:s for s in secs}
 ro=secs[".rodata"];text=secs[".text"];e=secs[".eh_frame_hdr"]
 strdata=mm[ro["off"]:ro["off"]+ro["size"]]
 target={}
 labels=collections.defaultdict(list)
 for key in KEYS:
  b=key.encode();p=0;hits=0
  while hits<200:
   off=strdata.find(b,p)
   if off<0:break
   hits+=1
   start=strdata.rfind(b"\0",max(0,off-500),off)+1
   if start<off-200:start=off
   end=strdata.find(b"\0",off)
   if end<0 or end-start>650:end=min(len(strdata),off+160)
   full=strdata[start:end]
   printable=sum(32<=v<127 for v in full)/max(1,len(full))
   if printable>.8:
    va=ro["va"]+start
    text_name=full.decode("utf8","replace")
    if len(text_name)>350:text_name=text_name[:350]
    if va not in target:target[va]={"name":text_name,"keywords":[]}
    target[va]["keywords"].append(key)
    labels[va].append(key)
   p=off+len(b)
 print("COORDINATE_STRING_TARGETS",json.dumps([{**v,"va":hex(k)} for k,v in list(target.items())[:65]],ensure_ascii=False),flush=True)
 # ELF's PC-relative .eh_frame_hdr function starts for nearest boundaries.
 FDE=[]
 hdr=mm[e["off"]:e["off"]+12]
 if hdr[:4]==b"\x01\x1b\x03\x3b":
  ct=struct.unpack_from("<I",hdr,8)[0]
  assert ct<1500000
  for i in range(ct):
   delta=struct.unpack_from("<i",mm,e["off"]+12+i*8)[0]
   addr=e["va"]+delta
   if text["va"]<=addr<text["va"]+text["size"]:FDE.append(addr)
 FDE=sorted(set(FDE))
 def fn(pc):
  j=bisect.bisect_right(FDE,pc)-1
  return (FDE[j], FDE[j+1]) if j>=0 and j+1<len(FDE) else (pc,pc+0x400)
 # Find R_AARCH64_RELATIVE data references; plaintext pointers can locate registration records.
 rel=secs.get(".rela.dyn")
 reloc_refs=[]
 if rel:
  for p in range(rel["off"],rel["off"]+rel["size"]-23,24):
   location,info,addend=struct.unpack_from("<QQq",mm,p)
   if addend in target:
    reloc_refs.append({"location":hex(location),"points_to":hex(addend),"label":target[addend]["name"],"kind":info&0xffffffff})
 # Capstone must decode all ARM64 instructions, no manual opcode parsing.
 cap=Cs(CS_ARCH_ARM64,CS_MODE_LITTLE_ENDIAN)
 cap.detail=True
 cap.skipdata=True
 active=collections.defaultdict(list)
 pages=collections.defaultdict(list)
 for x in target:pages[x&~0xfff].append(x)
 refs=[]
 mnems=collections.Counter()
 total=0; skipped=0
 for off in range(0,text["size"],512*1024):
  length=min(512*1024,text["size"]-off)
  chunk=mm[text["off"]+off:text["off"]+off+length]
  for ins in cap.disasm(chunk,text["va"]+off):
   total+=1
   pc=ins.address;mn=ins.mnemonic
   if mn.startswith("."):
    skipped+=1;active.clear();continue
   ops=ins.operands
   if mn=="adrp" and len(ops)>=2 and ops[0].type==CS_OP_REG and ops[1].type==CS_OP_IMM:
    dest=ops[0].reg
    page=ops[1].imm
    if (page&~0xfff) in pages:
     active[dest].append((pc,page&~0xfff))
   if mn=="adr" and len(ops)>=2 and ops[1].type==CS_OP_IMM:
    a=ops[1].imm
    if a in target:refs.append({"pc":hex(pc),"adrp":hex(pc),"target":hex(a),"label":target[a]["name"],"kind":"ADR"})
   if mn in ("add","ldr","ldrsw","str") and len(ops)>=2:
    if mn=="add" and len(ops)>=3 and ops[1].type==CS_OP_REG and ops[2].type==CS_OP_IMM:
     base_reg=ops[1].reg; disp=ops[2].imm
    elif ops[1].type==CS_OP_MEM:
     base_reg=ops[1].mem.base;disp=ops[1].mem.disp
    else:base_reg=-1;disp=0
    for start,page in active.get(base_reg,[]):
     if 0<=pc-start<=64:
      tgt=page+disp
      if tgt in target:
       fs,fe=fn(pc)
       refs.append({"pc":hex(pc),"adrp":hex(start),"target":hex(tgt),
                    "label":target[tgt]["name"],"keywords":target[tgt]["keywords"],
                    "fde_start":hex(fs),"fde_end":hex(fe),"kind":mn,
                    "reg":cap.reg_name(base_reg)})
   for r in list(active):
    active[r]=[(addr,pg) for addr,pg in active[r] if pc-addr<=64 and pc>=addr]
    if not active[r]:del active[r]
   if mn in ("bl","blr","br","ret","b"):
    active.clear()
   if total%2500000==0:print("ARM64_SCANNED",total,"XREF",len(refs),flush=True)
 print("ARM64_SCAN_DONE",total,"SKIPDATA",skipped,"XREF",len(refs),"FDE",len(FDE),"RELOC_REF",len(reloc_refs),flush=True)
 # Strict grouping by function (FDE) and label; keep only validated string address calculations.
 groups=collections.defaultdict(list)
 for x in refs:groups[x["fde_start"]].append(x)
 snippets={}
 for start,hitlist in list(groups.items())[:120]:
  begin=int(start,16)
  end=min(int(hitlist[0]["fde_end"],16),begin+0x1200)
  if begin<text["va"] or end>text["va"]+text["size"]:continue
  pos=text["off"]+begin-text["va"]
  bs=mm[pos:pos+(end-begin)]
  code=[]
  for inst in cap.disasm(bs,begin):
   code.append(f"0x{inst.address:08X}: {inst.mnemonic:8s} {inst.op_str}")
   if len(code)>=280:break
  snippets[start]={"references":hitlist,"insns":code,"candidate_function_bytes":end-begin}
 result={
 "engine":"HoK 12.1.1.1 libGameCore.so AArch64",
 "elf":{x:secs[x] for x in (".rodata",".text",".rela.dyn",".eh_frame_hdr")},
 "candidate_string_count":len(target),"candidate_strings":[{"va":hex(k),**v} for k,v in target.items()],
 "total_instructions_decoded":total,"skipdata_pseudoinstructions":skipped,"function_entries":len(FDE),"validated_code_xrefs":refs[:3000],
 "relocation_xrefs":reloc_refs[:1000],"snippets":snippets,
 "interpretation":["These are actual Capstone-parsed ARM64 address references, not a proof of encryption.",
 "The use of ViewManager ModifyEnemyInvisibleHeroPosition may indicate fog-of-war coordinate obfuscation, different from cryptographic encryption.",
 "Relevant function behavior must be checked before claiming an algorithm."]}
 (OUT/"gamecore_coordinate_xrefs.json").write_text(json.dumps(result,ensure_ascii=False,indent=2))
 lines=["# libGameCore.so current-version ARM64 coordinate/obfuscation functions","",
  f"Sections: .text {text['size']} bytes, .rodata {ro['size']} bytes, FDE {len(FDE)}.",
  f"Capstone decoded instructions: {total}. Matched string XREF: {len(refs)}.",
  "","## Verified string references"]
 for x in refs[:180]:lines.append("- "+json.dumps(x,ensure_ascii=False))
 lines+=["","## Candidate functions and disassembly"]
 for st,evidence in list(snippets.items())[:65]:
  lines+=["","### Function start "+st,
          "Hits: "+json.dumps(evidence["references"][:15],ensure_ascii=False),"~~~asm",
          "\n".join(evidence["insns"][:240]),"~~~"]
 (OUT/"gamecore_coordinate_xrefs.md").write_text("\n".join(lines)+"\n")
 print("GAMECORE_REPORT_SAVED",str(OUT),len(refs),len(snippets),flush=True)
 mm.close()
