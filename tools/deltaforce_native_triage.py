#!/usr/bin/env python3
"""Read-only Delta Force ARM64 libUE4 initial reverse engineering triage.
Uses ELF program headers (PT_LOAD) when section headers are missing.
Never executes APK or .so. Outputs bounded, auditable results.
"""
import hashlib, json, mmap, os, re, shutil, struct, subprocess, sys, time, zipfile
from pathlib import Path
from collections import defaultdict

ROOT=Path("reports/deltaforce")
ROOT.mkdir(parents=True, exist_ok=True)
APK=Path(sys.argv[1])
LIB=Path("work/native/libUE4.so")
PREFIX="DeltaForce-CN-Android-v1.201.37117.67.apk"
SHAS={
  "00":"ff89045d63daf2101f83357729c6fd501c2623d6db87fb3dd973c6e48fdb03be",
  "01":"727fc9db85ce8e9df1d612d536b2c2919f05f94ae93f44141716d1f1a52655ef",
  "02":"1be7e7ef8ca01bdd6677095fb6e5c20b297d0c2386a9269e58a9f3cc59773639",
  "03":"ac3582fae315b8cc283df13dd1216df3f07245791f50cb90feecfc2ff74cb169",
}
EXAPK="af03179c62ac57f05e4e6d425b2471bdf651b46c2f5a636f5a9e3fa94c78337d"
def sha(path):
 h=hashlib.sha256()
 with open(path,"rb") as f:
  for chunk in iter(lambda: f.read(16<<20),b""): h.update(chunk)
 return h.hexdigest()
def run(cmd,timeout=180):
 try:
  p=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=timeout,check=False,text=True,errors="replace")
  return {"rc":p.returncode,"output":p.stdout[:120000]}
 except Exception as e:
  return {"rc":-1,"output":str(e)}
def parse_elf(path):
 with open(path,"rb") as f:
  hdr=f.read(64)
  if hdr[:4]!=b"\x7fELF" or hdr[4]!=2 or hdr[5]!=1:raise ValueError("not ELF64 LE")
  _,_,_,_,entry,phoff,shoff,_,ehsize,phentsize,phnum,shentsize,shnum,shstrndx=struct.unpack("<16sHHIQQQIHHHHHH",hdr)
  segments=[]
  f.seek(phoff)
  for i in range(phnum):
   f.seek(phoff+i*phentsize)
   a=f.read(phentsize)
   if len(a)<56: continue
   p_type,p_flags,p_offset,p_vaddr,p_paddr,p_filesz,p_memsz,p_align=struct.unpack_from("<IIQQQQQQ",a,0)
   segments.append(dict(type=p_type,flags=p_flags,offset=p_offset,vaddr=p_vaddr,filesz=p_filesz,memsz=p_memsz,align=p_align))
  return {"entry":entry,"phnum":phnum,"shnum":shnum,"shoff":shoff,"segments":segments}
def va(segments,off):
 for s in segments:
  if s["type"]==1 and s["offset"]<=off<s["offset"]+s["filesz"]:
   return s["vaddr"]+(off-s["offset"])
 return None
def off_from_va(segments,addr):
 for s in segments:
  if s["type"]==1 and s["vaddr"]<=addr<s["vaddr"]+s["filesz"]:
   return s["offset"]+(addr-s["vaddr"])
 return None
def signext(n,bits):
 return n-(1<<bits) if n&(1<<(bits-1)) else n
def scan_xrefs(mm,segments,targets,cap_bytes=640<<20):
 """ARM64 ADRP + ADD/LDR, ADR. Validate full effective address, not ADRP alone."""
 pages=defaultdict(list)
 for a,source in targets.items(): pages[a&~4095].append((a,source))
 results=[]
 scanned=0
 for seg in segments:
  if seg["type"]!=1 or not (seg["flags"]&1): continue
  size=min(seg["filesz"]//4*4,max(0,cap_bytes-scanned))
  base=seg["offset"]; vbase=seg["vaddr"]
  if size<=0:break
  for n in range(0,size,4):
   ins=struct.unpack_from("<I",mm,base+n)[0]
   pc=vbase+n
   if (ins&0x9f000000)==0x90000000:
    immhi=(ins>>5)&0x7ffff; immlo=(ins>>29)&3
    page=(pc&~4095)+(signext(immhi<<2|immlo,21)<<12)
    target_rows=pages.get(page)
    if not target_rows:continue
    dest=ins&31
    for j in range(1,9):
     if n+4*j+4>size:break
     w=struct.unpack_from("<I",mm,base+n+4*j)[0]
     if (w&0x1f000000)==0x11000000 and ((w>>29)&3)==0 and (w>>5)&31==dest:
      disp=((w>>10)&4095) << (12 if (w>>22)&1 else 0)
      addr=page+disp
      if addr in targets:
       results.append(dict(ref_va=hex(pc),use_va=hex(pc+j*4),kind="ADRP+ADD",target_va=hex(addr),string=targets[addr]))
     elif (w&0x3b000000)==0x39000000 and ((w>>5)&31)==dest:
      # unsigned-imm load/store address, element size encoded in 31:30
      addr=page+(((w>>10)&4095)<<(w>>30))
      if addr in targets:
       results.append(dict(ref_va=hex(pc),use_va=hex(pc+j*4),kind="ADRP+LDR/STR",target_va=hex(addr),string=targets[addr]))
     # stop at branch/ret, to reduce false matches
     if w&0x7c000000==0x14000000 or (w&0xfffffc1f)==0xd65f0000:break
   elif (ins&0x9f000000)==0x10000000:
    immhi=(ins>>5)&0x7ffff;immlo=(ins>>29)&3
    addr=pc+signext((immhi<<2)|immlo,21)
    if addr in targets:
     results.append(dict(ref_va=hex(pc),use_va=hex(pc),kind="ADR",target_va=hex(addr),string=targets[addr]))
   if len(results)>=320:return results,scanned+size,True
  scanned+=size
 return results,scanned,False
def extract_apk():
 inv={}
 with zipfile.ZipFile(APK) as z:
  entries=[x for x in z.infolist() if x.filename.endswith(".so") or x.filename.endswith(".pak") or "ue4" in x.filename.lower() or "libunreal" in x.filename.lower()]
  inv["native_and_assets"]=[{"path":i.filename,"size":i.file_size,"zip_method":i.compress_type} for i in entries][:600]
  inv["all_entry_count"]=len(z.infolist())
  found=[i for i in entries if i.filename.endswith("/libUE4.so") or i.filename.endswith("/libUnreal.so")]
  inv["found_main_engine"]=bool(found)
  if found:
   item=sorted(found,key=lambda i:i.file_size,reverse=True)[0]
   inv["main_engine_path"]=item.filename
   LIB.parent.mkdir(parents=True,exist_ok=True)
   with z.open(item) as src,LIB.open("wb") as dst: shutil.copyfileobj(src,dst,16<<20)
 return inv
print("APK provided",APK,APK.stat().st_size,flush=True)
assert APK.stat().st_size==1519215938
assert sha(APK)==EXAPK,"APK SHA256 mismatch"
print("APK SHA256 verified",flush=True)
report={"apk_sha256":EXAPK, "apk_size":APK.stat().st_size,"work_mode":"static only; no APK execution"}
report["apk_inventory"]=extract_apk()
print("ENGINE FOUND",report["apk_inventory"]["found_main_engine"],report["apk_inventory"].get("main_engine_path",""),flush=True)
if not report["apk_inventory"]["found_main_engine"]:
 (ROOT/"triage.json").write_text(json.dumps(report,indent=2,ensure_ascii=False))
 sys.exit(0)
report["engine_size"]=LIB.stat().st_size;report["engine_sha256"]=sha(LIB)
elf=parse_elf(LIB)
report["elf"]={"entry":elf["entry"],"phnum":elf["phnum"],"shnum":elf["shnum"],"shoff":elf["shoff"],"segments":elf["segments"]}
report["elf_dynamic"]=run(["readelf","-W","-d",str(LIB)],timeout=180)
report["elf_notes"]=run(["readelf","-W","-n",str(LIB)],timeout=60)
report["elf_header"]=run(["readelf","-W","-h",str(LIB)],timeout=60)
report["elf_program_headers"]=run(["readelf","-W","-l",str(LIB)],timeout=60)
report["symbols_filtered"]={}
dynsym=run(["readelf","-W","--dyn-syms",str(LIB)],timeout=180)
lines=dynsym["output"].splitlines()
pat=re.compile("FVector|FTransform|GetActorLocation|SetActorLocation|GetComponentLocation|GetWorldLocation|Serialize|Decrypt|Encrypt|Xor|Vector|AntiCheat|Protected|FMatrix|USceneComponent|FRepMovement|NetQuantize",re.I)
report["symbols_filtered"]={"dynamic_total_lines":len(lines),"matched":[x[:220] for x in lines if pat.search(x)][:350],"rc":dynsym["rc"]}
needles=["GetActorLocation","SetActorLocation","GetComponentLocation","SetWorldLocation",
 "RelativeLocation","ComponentToWorld","ReplicatedMovement","K2_GetActorLocation",
 "K2_GetComponentLocation","FVector","FVector3d","FTransform","NetQuantize",
 "GetBoneLocation","GetSocketLocation","WorldPosition","OriginLocation",
 "WorldLocation","LocalToWorld","Location","Transform","Vector","Decrypt",
 "Encrypt","Coordinate","obfuscate","xor","GetActorTransform","GetWorld",
 "SetRelativeLocation","FRepMovement","NetSerialize","ClientAdjustPosition",
 "APlayerController","USkeletalMeshComponent","USceneComponent"]
with open(LIB,"rb") as f:
 mm=mmap.mmap(f.fileno(),0,access=mmap.ACCESS_READ)
 entries={};targets={}
 for kw in needles:
  b=kw.encode()
  pos=0;hits=[]
  for _ in range(32):
   idx=mm.find(b,pos)
   if idx<0:break
   addr=va(elf["segments"],idx)
   if addr is not None:
    hits.append({"file_off":hex(idx),"vaddr":hex(addr),"context":bytes(mm[max(0,idx-28):idx+len(b)+64]).split(b"\x00",1)[0][:120].decode("utf8","replace")})
    if kw in ["GetActorLocation","SetActorLocation","GetComponentLocation","SetWorldLocation",
               "RelativeLocation","ComponentToWorld","ReplicatedMovement","K2_GetActorLocation",
               "K2_GetComponentLocation","GetActorTransform","FVector","FTransform","NetSerialize","Decrypt","Encrypt","WorldPosition"] and len(hits)<=8:
     targets[addr]=kw
   pos=idx+len(b)
  entries[kw]={"hits_first_32":hits,"at_least":len(hits),"capped":len(hits)>=32}
 report["string_evidence"]=entries
 print("CANDIDATE STRINGS",json.dumps({k:v["at_least"] for k,v in entries.items()},ensure_ascii=False),flush=True)
 xrefs,scanned,cap=scan_xrefs(mm,elf["segments"],targets)
 report["matched_ADRP_ADR_xrefs"]={"xrefs":xrefs[:320],"total":len(xrefs),"scanned_exec_bytes":scanned,"truncated":cap,"requested_strings":len(targets)}
 mm.close()
report["radare2_check"]=run(["bash","-lc","command -v r2 && r2 -v | head -3; command -v rabin2 && rabin2 -Ij "+str(LIB)+" | head -c 12000"],timeout=120)
# Human-readable digest; no inference of encryption from mere mention of FVector.
md=["# Delta Force / libUE4 Native Triage", "", "Static APK SHA256: "+EXAPK,
    "Engine ELF SHA256: "+report["engine_sha256"],
    "Main shared object: "+report["apk_inventory"]["main_engine_path"],
    "Engine ELF size (bytes): "+str(report["engine_size"]),
    "ELF sections: "+str(elf["shnum"])+"; PT_LOAD is authoritative.",
    "",
    "## Embedded native libraries and major assets", ""]
for item in report["apk_inventory"]["native_and_assets"][:120]:
 md.append("- "+item["path"]+" ("+str(item["size"])+" bytes)")
md+=["","## Candidate literal occurrences (first 32 each; count is lower bound)",""]
for kw,row in entries.items():
 md.append("- "+kw+": at least "+str(row["at_least"]))
md+=["","## Validated ADRP+ADD/LDR/ADR reference examples",""]
for row in xrefs[:80]:
 md.append("- "+row["kind"]+" @ "+row["ref_va"]+" -> "+row["string"]+" @ "+row["target_va"])
md+=["","## Symbol indicators",""]
for v in report["symbols_filtered"]["matched"][:80]:md.append("- "+v)
md+=["","## Interpretation guardrail","Presence of ordinary UE4 coordinate reflection and transform strings does NOT establish coordinate encryption. Confirmation requires analysis of the effective read/write transforms, invertibility, state and call sites."]
(ROOT/"triage.md").write_text("\n".join(md)+"\n")
(ROOT/"triage.json").write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n")
print("RESULTS",json.dumps({"engine_size":report["engine_size"],"engine_sha256":report["engine_sha256"],"ELF_sections":elf["shnum"],"xrefs":len(xrefs),"native_count":len(report["apk_inventory"]["native_and_assets"])},ensure_ascii=False),flush=True)
