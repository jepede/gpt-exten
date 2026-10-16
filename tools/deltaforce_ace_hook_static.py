#!/usr/bin/env python3
"""Static-only ACE Hook audit on authenticated DeltaForce 1.201.37117.67 APK."""
import bisect,hashlib,json,mmap,shutil,struct,subprocess,sys,zipfile
from pathlib import Path
apk=Path(sys.argv[1]); wd=Path("work/deltaforce_ace"); wd.mkdir(parents=True,exist_ok=True)
out=Path("reports/deltaforce_ace");out.mkdir(parents=True,exist_ok=True)
expect_apk="af03179c62ac57f05e4e6d425b2471bdf651b46c2f5a636f5a9e3fa94c78337d"
expect_so="387cd911a67eca1069bd5e4c874bce5dfb14823ca75f55f1ae7c43a09f2f1441"
def sha(path):
 h=hashlib.sha256()
 with path.open("rb") as f:
  for b in iter(lambda:f.read(8<<20),b""):h.update(b)
 return h.hexdigest()
assert apk.stat().st_size==1519215938 and sha(apk)==expect_apk
with zipfile.ZipFile(apk) as z:
 for n in ["libUE4.so","libtersafe.so","libtprt.so"]:
  member="lib/arm64-v8a/"+n
  if member not in z.namelist():continue
  target=wd/n
  if not target.exists() or target.stat().st_size!=z.getinfo(member).file_size:
   with z.open(member) as r,target.open("wb") as w:shutil.copyfileobj(r,w,8<<20)
so=wd/"libUE4.so"; assert sha(so)==expect_so
print("INPUT_SHA_VERIFIED",expect_so,flush=True)
def elf(mm):
 h=struct.unpack_from("<16sHHIQQQIHHHHHH",mm,0)
 ident,typ,mach,ver,entry,phoff,shoff,fl,ehsz,phsz,phn,shsz,shn,shstr=h
 assert ident[:6]==b"\x7fELF\x02\x01" and mach==183
 sh=[]
 for i in range(shn):
  name,typ,flags,va,off,size,lk,inf,al,es=struct.unpack_from("<IIQQQQIIQQ",mm,shoff+i*shsz)
  sh.append({"nameoff":name,"type":typ,"flags":flags,"va":va,"off":off,"size":size})
 q=sh[shstr];buf=mm[q["off"]:q["off"]+q["size"]]
 for s in sh:
  p=s["nameoff"];s["name"]=buf[p:buf.find(b"\0",p)].decode("utf8","replace")
 ph=[]
 for i in range(phn):
  typ,flags,off,va,pa,fs,ms,al=struct.unpack_from("<IIQQQQQQ",mm,phoff+i*phsz)
  ph.append({"type":typ,"flags":flags,"off":off,"va":va,"filesz":fs,"memsz":ms})
 return {s["name"]:s for s in sh},ph
mask=bytes(x^0xe2 for x in range(256))
with so.open("rb") as f:
 m=mmap.mmap(f.fileno(),0,access=mmap.ACCESS_READ)
 sec,ph=elf(m);t=sec[".text"];r=sec[".rodata"]
 decoded=wd/"libUE4.decoded.so"
 if not decoded.exists() or decoded.stat().st_size!=so.stat().st_size: shutil.copyfile(so,decoded)
 with decoded.open("r+b") as g:
  w=mmap.mmap(g.fileno(),0,access=mmap.ACCESS_WRITE)
  for s in (t,r):
   a=s["off"];b=a+s["size"]
   for x in range(a,b,16<<20):
    y=min(x+(16<<20),b)
    w[x:y]=m[x:y].translate(mask)
  w.flush();w.close()
 print("DECODED_SO_READY",flush=True)
 def mapped(va):
  for x in ph:
   if x["type"]==1 and x["va"]<=va<x["va"]+x["memsz"]:
    return {"kind":"file-backed" if va<x["va"]+x["filesz"] else "zero-fill memory",
            "segment":x}
  return None
 def dataat(va,n=48):
  for x in ph:
   if x["type"]==1 and x["va"]<=va and va+n<=x["va"]+x["filesz"]:
    p=x["off"]+(va-x["va"]);return bytes(m[p:p+n])
  return b""
 eh=sec[".eh_frame_hdr"];q=m[eh["off"]:eh["off"]+12];starts=[]
 if q[:4]==b"\x01\x1b\x03\x3b":
  count=struct.unpack_from("<I",q,8)[0]
  if count<=2500000:
   for i in range(count):
    d=struct.unpack_from("<i",m,eh["off"]+12+i*8)[0]
    va=eh["va"]+d
    if t["va"]<=va<t["va"]+t["size"]:starts.append(va)
   starts=sorted(set(starts))
 def boundary(pc):
  ix=bisect.bisect_right(starts,pc)-1
  if ix<0:return []
  return [hex(starts[ix]),hex(starts[ix+1]) if ix+1<len(starts) else ""]
 sites={
  "old_public_hook_rva":0x0d1fbb84,
  "old_public_original_xyz_rva":0x0d1fbb98,
  "old_public_fde":0x0d1fbb60,
  "component_data_accessor":0x104f6ecc,
  "component_transform_reader":0x104f6fc4,
  "component_state_branch_A":0x104f70c8,
  "component_state_branch_B":0x104f7284,
  "callback_indirect_call":0x104f7334,
  "callback_entry":0x0aae708c,
  "callback_validate":0x0aaea4e4,
  "callback_data_read":0x0aaea6ec,
  "callback_data_write":0x0aae7098,
  "initializer_A":0x131204cc,
  "initializer_B":0x10c25ad4}
 data={}
 for name,pc in sites.items():
  orig=dataat(pc);dec=orig.translate(mask)
  data[name]={"rva":hex(pc),"fde":boundary(pc),
              "raw48":orig.hex(),"decoded48":dec.hex(),
              "is_direct_ldr_x16_br_x16":dec[:8]==bytes.fromhex("5000005800021fd6")}
 print("SITE_HEADER",json.dumps({k:{"rva":v["rva"],"decoded_first16":v["decoded48"][:32],"fde":v["fde"]} for k,v in data.items()}),flush=True)
 # Existing on-disk trampoline pattern: indicates code patch ONLY if confirmed against baseline.
 patterns={}
 for label,pattern in {
    "ldr_x16_lit8_br_x16":bytes.fromhex("5000005800021fd6"),
    "ldr_x17_lit8_br_x17":bytes.fromhex("5100005820021fd6")}.items():
  patternX=pattern.translate(mask)
  rows={}
  for mode,needle in (("raw",pattern),("decoded",patternX)):
   found=[];p=t["off"];e=p+t["size"]
   while len(found)<48:
    idx=m.find(needle,p,e)
    if idx<0:break
    found.append(hex(t["va"]+idx-t["off"]));p=idx+4
   rows[mode]={"at_least":len(found),"first":found}
  patterns[label]=rows
 print("TRAMPOLINE_PATTERNS",json.dumps(patterns),flush=True)
 # Find the hook/callback SLOT's file-vs-BSS state and all direct ADRP+LDR/STR references.
 ptr=0x20258db8;ptrpage=ptr&~0xfff
 refs=[];ad_count=0
 bufsize=8<<20
 for pos in range(0,t["size"],bufsize):
  ln=min(bufsize,t["size"]-pos)
  x=m[t["off"]+pos:t["off"]+pos+min(ln+128,t["size"]-pos)].translate(mask)
  for i in range(0,ln-(ln%4),4):
   ins=struct.unpack_from("<I",x,i)[0]
   if ins&0x9f000000!=0x90000000:continue
   ad_count+=1
   field=(((ins>>5)&0x7ffff)<<2)|((ins>>29)&3)
   offbits=(field-(1<<21) if field&(1<<20) else field)<<12
   pc=t["va"]+pos+i
   if ((pc&~4095)+offbits)!=ptrpage:continue
   reg=ins&31
   for j in range(i+4,min(i+80,len(x)-3),4):
    nxt=struct.unpack_from("<I",x,j)[0]
    kind="";addr=-1
    if nxt&0xffc00000 in (0xf9400000,0xf9000000) and ((nxt>>5)&31)==reg:
     addr=ptrpage+(((nxt>>10)&4095)<<3)
     kind="LDR X" if nxt&0xffc00000==0xf9400000 else "STR X"
    elif nxt&0xff000000==0x91000000 and ((nxt>>5)&31)==reg:
     addr=ptrpage+(((nxt>>10)&4095)<<(12 if nxt&(1<<22) else 0))
     kind="ADD"
    if addr==ptr and len(refs)<300:
     refs.append({"adrp":hex(pc),"site":hex(pc+j-i),"kind":kind,"fde":boundary(pc)})
    if nxt&0xfc000000==0x14000000 or nxt&0xfffffc1f==0xd65f0000:break
 print("PTR_XREFS",len(refs),"ADRP_WORDS",ad_count,json.dumps(refs[:65]),flush=True)
 m.close()
 related={}
 for n in ("libUE4.so","libtersafe.so","libtprt.so"):
  path=wd/n
  if not path.exists():continue
  stat=subprocess.run(["readelf","-W","--dyn-syms",str(path)],capture_output=True,text=True,timeout=70).stdout
  dyn=subprocess.run(["readelf","-W","-d",str(path)],capture_output=True,text=True,timeout=60).stdout
  filtered=[s.strip() for s in stat.splitlines() if any(k in s.lower() for k in ["mprotect","mmap","dlopen","dlsym","memcpy","ptrace","sigaction","syscall","cacheflush","pthread_create"])]
  related[n]={"sha256":sha(path),"size":path.stat().st_size,"imports":filtered[:100],"dynamic":dyn[:8000]}
 disasm={}
 for name,pc in sites.items():
  rs=subprocess.run(["r2","-2","-q","-e","scr.color=false","-e","asm.bytes=true","-c","pd 70 @ "+hex(pc),str(decoded)],capture_output=True,text=True,timeout=130)
  disasm[name]={"rva":hex(pc),"returncode":rs.returncode,"text":(rs.stdout+rs.stderr)[:16000]}
  print("SITE_DISASM",name,disasm[name]["text"][:1200].replace("\n"," | "),flush=True)
 report={"apk_sha":expect_apk,"libue4_sha":expect_so,"decoded_scratch_sha":sha(decoded),
  "source":"APK on-disk static investigation, no runtime process snapshot",
  "ptr_slot":hex(ptr),"ptr_mapping":mapped(ptr),"fde_entries":len(starts),
  "sites":data,"trampoline_signatures":patterns,"ptr_adrp_refs":refs,"ADRP_scanned":ad_count,
  "libraries":related,"disassembly":disasm,"limits":[
   "Static on-disk bytes cannot demonstrate an ACE runtime-installed Hook.",
   "Historical published hook offsets may be illustrative rather than reliable for current version.",
   "Indirection via BLR is not automatically hooking; it can be a normal callback or vtable.",
   "Unmapped executable shellcode cannot be extracted from an unlaunched APK file.",
   "0xB4 in a top pointer byte alone is not proof hardware MTE mode is enabled."]}
 (out/"ace_hook_static.json").write_text(json.dumps(report,ensure_ascii=False,indent=2))
 lines=["# Delta Force 1.201.37117.67 — ACE coordinate Hook static audit",
        "","Verified libUE4 SHA256: "+expect_so,"Callback pointer VA: "+hex(ptr),
        "Callback pointer mapping: "+json.dumps(mapped(ptr),ensure_ascii=False),
        "","## Direct references to callback pointer"]
 for x in refs:lines.append("- "+str(x))
 lines+=["","## Hook jump sequence candidates",json.dumps(patterns,indent=2),
         "","## Function entry bytes and decoded disassembly"]
 for name,row in data.items():
  lines+=["","### "+name+" "+row["rva"],"Original 48: "+row["raw48"],
          "Decoded 48: "+row["decoded48"],"FDE "+str(row["fde"]),"~~~asm",
          disasm[name]["text"],"~~~"]
 lines+=["","## Other native libraries",json.dumps(related,ensure_ascii=False,indent=2)[:20000],
         "","## Interpretation boundary","The stock file is a baseline only. To prove ACE inline hook, a matched runtime memory snapshot and executable anonymous mappings are needed."]
 (out/"ace_hook_static.md").write_text("\n".join(lines)+"\n")
 print("HOOK_AUDIT_COMPLETE",json.dumps({"ptr_mapping":mapped(ptr),"refs":len(refs),"fde":len(starts),"patterns":patterns}),flush=True)
