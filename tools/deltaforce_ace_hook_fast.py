#!/usr/bin/env python3
"""Fast bounded independent audit: ACE Hook candidate and internal coordinate callback."""
import hashlib,json,mmap,struct,subprocess,sys,zipfile
from pathlib import Path
APK=Path(sys.argv[1]);OUT=Path("reports/deltaforce_ace_fast");OUT.mkdir(parents=True,exist_ok=True)
SHA="387cd911a67eca1069bd5e4c874bce5dfb14823ca75f55f1ae7c43a09f2f1441"
with zipfile.ZipFile(APK) as z:
 name="lib/arm64-v8a/libUE4.so"; dst=Path("work/deltaforce_ace_fast/libUE4.so")
 dst.parent.mkdir(parents=True,exist_ok=True)
 if not dst.exists():
  with z.open(name) as i,dst.open("wb") as f:
   for b in iter(lambda:i.read(16<<20),b""):f.write(b)
h=hashlib.sha256()
with dst.open("rb") as f:
 for b in iter(lambda:f.read(16<<20),b""):h.update(b)
assert h.hexdigest()==SHA
print("STOCK_SHA256",SHA,flush=True)
with dst.open("rb") as f:
 mm=mmap.mmap(f.fileno(),0,access=mmap.ACCESS_READ)
 hd=struct.unpack_from("<16sHHIQQQIHHHHHH",mm,0)
 _,_,mach,_,_,phoff,shoff,_,_,phsz,phn,shsz,shn,shstr=hd
 assert mach==183
 ph=[struct.unpack_from("<IIQQQQQQ",mm,phoff+j*phsz) for j in range(phn)]
 def back(va):
  for typ,flags,off,vaddr,pa,filesz,memsz,align in ph:
   if typ==1 and vaddr<=va<vaddr+filesz:return off+va-vaddr
  raise ValueError("VA not file-backed "+hex(va))
 def phmap(va):
  for typ,flags,off,vaddr,pa,filesz,memsz,align in ph:
   if typ==1 and vaddr<=va<vaddr+memsz:
    return {"start":hex(vaddr),"file_end":hex(vaddr+filesz),"memory_end":hex(vaddr+memsz),
      "backed":va<vaddr+filesz}
  return None
 positions={
  "old_com_public_hook_entry":0x0d1fbb84,
  "old_com_public_original_loads":0x0d1fbb98,
  "component_coord_read":0x104f6fc4,
  "component_indirect_call":0x104f7334,
  "component_offset_accessor":0x104f6ecc,
  "callback_entry":0x0aae708c,
  "callback_data_copy":0x0aaea6ec,
  "callback_install_A":0x131204cc,
  "callback_install_B":0x10c25ad4}
 masks=bytes(x^0xe2 for x in range(256))
 rec=[]
 for name,va in positions.items():
  ix=back(va)
  start=max(ix-64,0)
  # every entry displayed with 64-byte prelude, 192-byte body
  data=mm[start:ix+256]
  decoded=data.translate(masks)
  path=OUT/(name+".bin")
  path.write_bytes(decoded)
  p=subprocess.run(["r2","-2","-q","-n","-a","arm","-b","64",
                    "-c","e scr.color=false;pd 64 @ 64",str(path)],
                    capture_output=True,text=True,timeout=30,errors="replace")
  raw=mm[ix:ix+24]
  plain=raw.translate(masks)
  record={"name":name,"VA":hex(va),"raw_first_24":raw.hex(),"decoded_first_24":plain.hex(),
     "LDR_X16_Br_X16_plain":plain[:8]==bytes.fromhex("5000005800021fd6"),
     "disassembly_offset64":p.stdout[:13000],"r2_rc":p.returncode}
  rec.append(record)
  print("SITE",name,hex(va),"RAW",raw[:16].hex(),"XOR",plain[:16].hex(),"TRAMP",record["LDR_X16_Br_X16_plain"],flush=True)
  print("DISASM",name,p.stdout[:800].replace("\n"," || "),flush=True)
 data={"sha256":SHA,"ptr_slot":"0x20258db8","ptr_map":phmap(0x20258db8),"sites":rec}
 (OUT/"hook_baseline.json").write_text(json.dumps(data,indent=2,ensure_ascii=False))
 lines=["# ACE Hook candidate — fast independent baseline","",
        "Stock libUE4 SHA256 "+SHA,
        "Callback slot +0x20258db8 mapping: "+json.dumps(data["ptr_map"])]
 for v in rec:lines+=["","## "+v["name"]+" RVA="+v["VA"],
  "raw "+v["raw_first_24"],"E2 decoded "+v["decoded_first_24"],
  "Canonical LDR X16/BR X16="+str(v["LDR_X16_Br_X16_plain"]),
  "Disassembly offset 64 is RVA "+v["VA"],"~~~asm",v["disassembly_offset64"],"~~~"]
 (OUT/"hook_baseline.md").write_text("\n".join(lines))
 mm.close()
 print("FAST_BASELINE_COMPLETE",json.dumps(data["ptr_map"]),flush=True)
