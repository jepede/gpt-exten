#!/usr/bin/env python3
import sys,json,mmap,struct,bisect,re,subprocess,hashlib
from pathlib import Path
SO=Path(sys.argv[1]);ROOT=Path("reports/deltaforce_candidate_context");ROOT.mkdir(parents=True,exist_ok=True)
TARGETS=[(0x081D2498,"float_xyz_A"),(0x081D2738,"float_xyz_B"),
 (0x0823C800,"float_xyz_X0"),(0x09353524,"float_xyz_X0_B"),
 (0x0A40CF20,"float_xyz_X0_C"),(0x085233BC,"flag_x0_0x176"),
 (0x0D1FBB60,"protected_control")]
def shasum(p):
 h=hashlib.sha256()
 with p.open("rb") as f:
  for b in iter(lambda:f.read(8<<20),b""):h.update(b)
 return h.hexdigest()
def disasm(data,name):
 target=ROOT/(name+".bin");target.write_bytes(data)
 try:
  p=subprocess.run(["r2","-2","-q","-n","-a","arm","-b","64",
    "-c","e scr.color=false;pd 105 @ 0",str(target)],
    capture_output=True,text=True,timeout=100)
  return (p.stdout+p.stderr)[-17000:]
 except Exception as e:return str(e)
with SO.open("rb") as fd:
 vals=struct.unpack("<16sHHIQQQIHHHHHH",fd.read(64))
 ident,etype,machine,version,entry,phoff,shoff,flags,ehsize,phentsize,phnum,shentsize,shnum,shstrndx=vals
 assert ident[:6]==b"\x7fELF\x02\x01" and machine==183
 secs=[]
 for i in range(shnum):
  fd.seek(shoff+i*shentsize)
  nam,typ,sflags,addr,off,size,link,info,align,entsize=struct.unpack_from("<IIQQQQIIQQ",fd.read(shentsize))
  secs.append(dict(nameoff=nam,va=addr,off=off,size=size))
 st=secs[shstrndx];fd.seek(st["off"]);names=fd.read(st["size"])
 for s in secs:
  k=s["nameoff"];s["name"]=names[k:names.find(b"\0",k)].decode("ascii","replace") if k<len(names) else "?"
 text=next(s for s in secs if s["name"]==".text")
 eh=next(s for s in secs if s["name"]==".eh_frame_hdr")
 mm=mmap.mmap(fd.fileno(),0,access=mmap.ACCESS_READ)
 assert mm[eh["off"]:eh["off"]+4] == b"\x01\x1b\x03\x3b"
 count=struct.unpack_from("<I",mm,eh["off"]+8)[0]
 starts=sorted(set(eh["va"]+struct.unpack_from("<i",mm,eh["off"]+12+8*i)[0] for i in range(count)))
 starts=[s for s in starts if text["va"]<=s<text["va"]+text["size"]]
 def read(va,n):
  assert text["va"]<=va<text["va"]+text["size"]
  off=text["off"]+va-text["va"]
  return mm[off:off+min(n,text["size"]-(va-text["va"]))]
 def dec_word(va):
  return struct.unpack("<I",read(va,4))[0]^0xe2e2e2e2
 def access(w):
  op=w&0xffc00000; imm=(w>>10)&0xfff; base=(w>>5)&31;reg=w&31
  if op==0xbd400000:return ("LDR_S",imm*4,base,reg)
  if op==0xb9400000:return ("LDR_W",imm*4,base,reg)
  if op==0x39400000:return ("LDRB",imm,base,reg)
  if op==0xbd000000:return ("STR_S",imm*4,base,reg)
  if op==0xb9000000:return ("STR_W",imm*4,base,reg)
  return None
 rows=[]
 for va,kind in TARGETS:
  idx=bisect.bisect_right(starts,va)-1
  fstart=starts[idx] if idx>=0 else va
  fend=starts[idx+1] if idx+1<len(starts) else va+0x1000
  base=max(fstart,va-0xa0)
  if va-fstart>0x2000:base=va-0x80
  data=read(base,0x480)
  decoded=bytes(b^0xe2 for b in data)
  dr=disasm(decoded,kind+"_xor_e2")
  raw_listing=disasm(data,kind+"_disk") if kind=="float_xyz_X0" else ""
  accesses=[]
  for pc in range(fstart,min(fend,fstart+0x2000),4):
   a=access(dec_word(pc))
   if a and a[1] in (0x168,0x16c,0x170,0x174,0x176):
    accesses.append({"pc":hex(pc),"op":a[0],"off":hex(a[1]),"base":a[2],"dest":a[3]})
  row={"va":hex(va),"kind":kind,"fde_start":hex(fstart),"fde_next":hex(fend),
       "window_start":hex(base),"xor_decoded_listing":dr,
       "raw_listing":raw_listing,"coord_like_accesses":accesses[:120]}
  rows.append(row)
  print("TARGET",kind,hex(va),"FDE",hex(fstart),hex(fend),"ACCESS",len(accesses),flush=True)
  print("DECODED",dr[:9000],flush=True)
 out={"sha256":shasum(SO),"FDE_total":len(starts),"samples":rows}
 (ROOT/"candidate_context.json").write_text(json.dumps(out,indent=2,ensure_ascii=False))
 md=["# Candidate ARM64 code contexts after XOR E2 unmasking",
     "ELF SHA256: "+out["sha256"],"FDE entries: "+str(len(starts)),
     "These are offset-based candidates, not identified game coordinate functions."]
 for row in rows:
  md.extend(["","## "+row["kind"]+" @ "+row["va"],
     "FDE "+row["fde_start"]+" to "+row["fde_next"]+" (disasm window "+row["window_start"]+")",
     "Relevant field accesses: "+str(row["coord_like_accesses"]),
     "Decoded disassembly:",row["xor_decoded_listing"]])
 (ROOT/"candidate_context.md").write_text("\n".join(md)+"\n")
 print("REPORT_READY",flush=True)
 mm.close()
