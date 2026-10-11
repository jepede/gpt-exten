#!/usr/bin/env python3
import sys,zipfile,os,re,json,hashlib
from pathlib import Path
from elftools.elf.elffile import ELFFile
root=Path(sys.argv[1])
needles=[b"g_acf_array",b"g_aco_array",b"xxxxXXXXxxxx",b"stub_decrypt_elf",
         b"ELF_HOOK_BRIDGE_UE4_FPakInfo_Serialize",b"ELF_HOOK_UE4_FPakInfo_Serialize",
         b"SetDecryptionKey",b"48ea7d82db9995f2",b"c44d833f54ba436f"]
res=[]
for p in sorted(root.rglob("*.so")):
    try:b=p.read_bytes()
    except:continue
    item={"file":str(p),"size":len(b),"sha256":hashlib.sha256(b).hexdigest(),"strings":[],"symbols":[]}
    for n in needles:
        hits=[];pos=0
        while True:
            i=b.find(n,pos)
            if i<0:break
            hits.append(i);pos=i+1
        if hits:item["strings"].append({"needle":n.decode(),"offsets":hits[:20],"count":len(hits)})
    try:
        with p.open("rb") as f:
            e=ELFFile(f)
            for sn in (".dynsym",".symtab"):
                s=e.get_section_by_name(sn)
                if not s:continue
                for sym in s.iter_symbols():
                    name=sym.name
                    if name in ("g_acf_array","g_aco_array","xxxxXXXXxxxx","stub_decrypt_elf") or "FPakInfo" in name or "decrypt_elf" in name:
                        item["symbols"].append({
                            "section":sn,"name":name,"value":int(sym["st_value"]),"size":int(sym["st_size"]),
                            "shndx":str(sym["st_shndx"]),"bind":sym["st_info"]["bind"],"type":sym["st_info"]["type"]
                        })
    except Exception as ex:item["elf_error"]=repr(ex)
    if item["strings"] or item["symbols"]:res.append(item)
print("== MATCHING LIBS ==")
for x in res:
    print("\nFILE",x["file"],"size",x["size"],"sha",x["sha256"])
    print("STRINGS",json.dumps(x["strings"],ensure_ascii=False))
    print("SYMS",json.dumps(x["symbols"],ensure_ascii=False))
Path("apk_native_scan.json").write_text(json.dumps(res,indent=2),encoding="utf-8")
