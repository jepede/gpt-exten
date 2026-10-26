#!/usr/bin/env python3
"""Read-only inspection of a provided AArch64 game simulation ELF; no process injection."""
import collections,hashlib,json,mmap,struct,sys,subprocess
from pathlib import Path
p=Path(sys.argv[1]);dest=Path("reports/hok/coordinate_static.json")
dest.parent.mkdir(parents=True,exist_ok=True)
h=hashlib.sha256()
with p.open("rb") as f:
 for b in iter(lambda:f.read(8<<20),b""):h.update(b)
with p.open("rb") as f:
 mm=mmap.mmap(f.fileno(),0,access=mmap.ACCESS_READ)
 hdr=struct.unpack_from("<16sHHIQQQIHHHHHH",mm,0)
 ident,typ,machine,version,entry,phoff,shoff,flags,ehsz,phsz,phn,shsz,shn,shstr=hdr
 assert ident[:6]==b"\x7fELF\x02\x01" and machine==183
 secs=[]
 for i in range(shn):
  no,st,fl,va,off,size,link,info,align,entsz=struct.unpack_from("<IIQQQQIIQQ",mm,shoff+i*shsz)
  secs.append(dict(name_off=no,type=st,flags=fl,va=va,off=off,size=size))
 sn=secs[shstr];names=mm[sn["off"]:sn["off"]+sn["size"]]
 for s in secs:
  at=s["name_off"];s["name"]=names[at:names.find(b"\0",at)].decode("ascii","replace")
 segments=[]
 for i in range(phn):
  t,fl,off,va,pa,fs,ms,al=struct.unpack_from("<IIQQQQQQ",mm,phoff+i*phsz)
  if t==1:segments.append(dict(va=va,off=off,filesz=fs,memsz=ms,flags=fl))
 def vaddr(off):
  for seg in segments:
   if seg["off"]<=off<seg["off"]+seg["filesz"]:
    return seg["va"]+(off-seg["off"])
  return None
 terms=["Position","PosInfo","PosRecord","Move","Movement","Hero","Actor","VInt3","VInt2",
  "Vector3","Vector2","Encrypt","Decrypt","Crypt","Xor","Fow","Fog","Visibility",
  "World","Transform","FrameSync","Frame","Sync","Hurt","Coordinate","Location",
  "Fixed","PositionRecorder","Visible","Security","ByteArray","Obfuscate"]
 # Occurrence counts in ASCII and UTF16LE without assuming all data is stored as text.
 evidence={}
 for term in terms:
  vals=[]
  for codec,key in (("ascii","ascii"),("utf-16le","utf16")):
   search=term.encode(codec);start=0;hits=[]
   while len(hits)<24:
    n=mm.find(search,start)
    if n<0:break
    addr=vaddr(n)
    context=mm[max(0,n-36):n+len(search)+65]
    hits.append({"off":hex(n),"va":hex(addr) if addr is not None else None,
                 "context":context[:110].replace(b"\0",b"|").decode("ascii","backslashreplace")})
    start=n+len(search)
   vals.append((key,hits))
  evidence[term]={k:v for k,v in vals}
 sections=[{"name":s["name"],"va":hex(s["va"]),"size":s["size"],"flags":s["flags"]} for s in secs]
 unoptimized_symbols=subprocess.run(["readelf","-W","--dyn-syms",str(p)],capture_output=True,text=True,timeout=100)
 syms=[s[:250] for s in unoptimized_symbols.stdout.splitlines()
       if any(x.lower() in s.lower() for x in ["hero","pos","move","fow","fog","enc","crypt","sync","frame","vector","transform"])][:260]
 result={"filename":p.name,"sha256":h.hexdigest(),"size":len(mm),"ELF_machine":machine,
         "segments":segments,"sections":sections,
         "candidate_literals":evidence,"candidate_dynsyms":syms,
         "limitations":"No runtime values or keys; literal presence is not evidence of coordinate encryption."}
 dest.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
 print("ELF_IDENTITY",h.hexdigest(),len(mm),flush=True)
 print("ELF_SECTIONS",json.dumps(sections,ensure_ascii=False),flush=True)
 print("LITERAL_HITS",json.dumps({x:{k:len(v) for k,v in row.items()} for x,row in evidence.items()},ensure_ascii=False),flush=True)
 print("CANDIDATE_LITERAL_CONTEXTS",json.dumps({k:v for k,v in evidence.items() if k in ["PositionRecorder","VInt3","Encrypt","Decrypt","Fow","Hero","Move","Position","Transform","Fixed"]},ensure_ascii=False)[:24000],flush=True)
 print("DYNAMIC_SYMBOLS",json.dumps(syms[:40],ensure_ascii=False),flush=True)
 mm.close()
