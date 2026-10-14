#!/usr/bin/env python3
import sys, os, re, json, zipfile, hashlib, struct, subprocess
from pathlib import Path
from collections import defaultdict, Counter

APK_PATH = Path(sys.argv[1])
OUT = Path(sys.argv[2])
OUT.mkdir(parents=True, exist_ok=True)

KEYWORDS = [
    b"SetDecryptionKey", b"key_manifest", b"FPakInfo", b"PakFile", b"pak",
    b"encrypt", b"decrypt", b"SM4", b"ZUC", b"RSA", b"AES",
    b"AnoSDKOnRecvData", b"AnoSDKOnRecvSignature", b"tcp", b"socket",
    b"download", b"manifest", b"patch", b"hotfix", b"dynamic", b"key"
]
KNOWN_DYN = {
    37: b"46e490567d02cdb312b3",
    38: b"f838b560ec26d4ba67fd",
    42: b"56eed0401753d9e5ee86",
    43: b"5412cc837199fa08d229",
    44: b"48750e47caff0540e2ee",
}
KNOWN_STATIC = [
    b"xG2qW5lP7lV2iN5fN5pG", b"rT6aQ6oZ1yM0gO5tO1aN", b"wD2rP3lP9xF4mE1eC5jS",
    b"rG0lR2rZ5vM6mW5lM1rR", b"fO3kW1fE6eD0pU1kY7xK"
]
URL_RE = re.compile(rb"https?://[A-Za-z0-9._~:/?#\[\]@!$&'()*+,;=%-]{8,}")
HEX20_RE = re.compile(rb"(?<![0-9a-f])[0-9a-f]{20}(?![0-9a-f])")
PRINT_RE = re.compile(rb"[\x20-\x7e]{6,}")

def sha256b(b): return hashlib.sha256(b).hexdigest()

def scan_blob(name, b):
    rec = {"name": name, "size": len(b), "sha256": sha256b(b)}
    hex20 = []
    for m in HEX20_RE.finditer(b):
        s = m.group().decode()
        if s not in [x[1].decode() for x in KNOWN_DYN.items()]:
            hex20.append((m.start(), s))
        else:
            hex20.append((m.start(), s))
    rec["hex20"] = hex20[:500]
    urls = []
    for m in URL_RE.finditer(b):
        try: u = m.group().decode("ascii", "ignore")
        except: continue
        if any(k in u.lower() for k in ("pubg","tencent","qq","patch","download","config","key","pak","game")):
            urls.append((m.start(), u))
    rec["urls"] = urls[:300]
    hits = {}
    low = b.lower()
    for kw in KEYWORDS:
        k = kw.lower()
        pos=[]; st=0
        while True:
            i=low.find(k,st)
            if i < 0: break
            pos.append(i); st=i+1
            if len(pos)>=30: break
        if pos: hits[kw.decode("ascii","ignore")] = pos
    rec["keyword_hits"] = hits
    return rec

# APK inventory and extraction
apk_sha = hashlib.sha256(APK_PATH.read_bytes()).hexdigest()
print(f"APK={APK_PATH.name} size={APK_PATH.stat().st_size} sha256={apk_sha}")
inventory=[]
scans=[]
with zipfile.ZipFile(APK_PATH) as z:
    names=z.namelist()
    for zi in z.infolist():
        inventory.append((zi.filename, zi.file_size, zi.compress_size))
    print(f"APK entries={len(inventory)}")
    # extract all arm64 libs + dex + manifest + likely config assets
    for zi in z.infolist():
        n=zi.filename
        want = (
            n.startswith("lib/arm64-v8a/") and n.endswith(".so")
        ) or n.endswith(".dex") or n=="AndroidManifest.xml" or any(x in n.lower() for x in (
            "manifest","config","patch","pak","key","hotfix","download","version"
        ))
        if want and zi.file_size <= 300*1024*1024:
            try:
                b=z.read(zi)
            except Exception:
                continue
            scans.append(scan_blob(n,b))
            if n.startswith("lib/arm64-v8a/") and n.endswith(".so"):
                p=OUT/"libs"/Path(n).name
                p.parent.mkdir(parents=True,exist_ok=True); p.write_bytes(b)
            elif zi.file_size <= 10*1024*1024 and not n.endswith(".dex"):
                p=OUT/"selected"/n
                p.parent.mkdir(parents=True,exist_ok=True); p.write_bytes(b)

# General whole-APK-file scan for candidate hex20 and URLs across all reasonably sized entries.
hex_candidates=[]
url_candidates=[]
with zipfile.ZipFile(APK_PATH) as z:
    for zi in z.infolist():
        if zi.file_size > 50*1024*1024: continue
        try: b=z.read(zi)
        except Exception: continue
        for m in HEX20_RE.finditer(b):
            hex_candidates.append((zi.filename,m.start(),m.group().decode()))
            if len(hex_candidates)>5000: break
        for m in URL_RE.finditer(b):
            u=m.group().decode("ascii","ignore")
            lu=u.lower()
            if any(k in lu for k in ("pubg","tencent","qq","patch","download","config","key","pak","game")):
                url_candidates.append((zi.filename,m.start(),u))
                if len(url_candidates)>3000: break

# ELF symbol/import/export & interesting strings.
elf_reports=[]
try:
    from elftools.elf.elffile import ELFFile
    from elftools.elf.relocation import RelocationSection
    for p in sorted((OUT/"libs").glob("*.so")):
        item={"file":p.name,"size":p.stat().st_size,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()}
        try:
            with p.open("rb") as f:
                e=ELFFile(f)
                item["machine"]=e["e_machine"]
                item["entry"]=int(e["e_entry"])
                syms=[]
                for sn in (".dynsym",".symtab"):
                    sec=e.get_section_by_name(sn)
                    if not sec: continue
                    for sym in sec.iter_symbols():
                        nm=sym.name
                        lo=nm.lower()
                        if any(k in lo for k in ("pak","decrypt","encrypt","key","acf","aco","hook","stub","tcp","recv","report","anort","anogs")):
                            syms.append({
                                "sec":sn,"name":nm,"value":int(sym["st_value"]),"size":int(sym["st_size"]),
                                "shndx":str(sym["st_shndx"]),"bind":sym["st_info"]["bind"],"type":sym["st_info"]["type"]
                            })
                            if len(syms)>1000: break
                item["symbols"]=syms
                dyn=e.get_section_by_name(".dynamic")
                needed=[]
                if dyn:
                    for tag in dyn.iter_tags():
                        if tag.entry.d_tag=="DT_NEEDED": needed.append(tag.needed)
                item["needed"]=needed
        except Exception as ex:
            item["elf_error"]=repr(ex)
        b=p.read_bytes()
        strs=[]
        for m in PRINT_RE.finditer(b):
            s=m.group().decode("ascii","ignore")
            ls=s.lower()
            if any(k in ls for k in ("pak","decrypt","encrypt","key_manifest","setdecryptionkey",
                                      "tcp","socket","recvdata","manifest","download","patch","hotfix","sm4",
                                      "anort","anogs","stub_decrypt_elf","fpakinfo")):
                strs.append((m.start(),s))
                if len(strs)>1000: break
        item["interesting_strings"]=strs
        item["hex20"]=[(m.start(),m.group().decode()) for m in HEX20_RE.finditer(b)][:1000]
        elf_reports.append(item)
except Exception as ex:
    print("ELF parser setup error",repr(ex))

# Androguard manifest + DEX xrefs, if installed.
andro = {"ok":False}
try:
    from androguard.core.apk import APK
    from androguard.core.dex import DEX
    a=APK(str(APK_PATH))
    andro["ok"]=True
    andro["package"]=a.get_package()
    andro["version_name"]=a.get_androidversion_name()
    andro["version_code"]=a.get_androidversion_code()
    andro["permissions"]=sorted(a.get_permissions())
    andro["activities"]=a.get_activities()
    andro["services"]=a.get_services()
    andro["receivers"]=a.get_receivers()
    # DEX string -> method xrefs with focused terms
    xrefs=[]
    for dexname in [n for n,_,_ in inventory if n.endswith(".dex")]:
        with zipfile.ZipFile(APK_PATH) as z:
            dbytes=z.read(dexname)
        try:
            d=DEX(dbytes)
            # Map string idx usage by scanning method instructions for const-string.
            strings=d.get_strings()
            interesting_idx={}
            for idx,s in enumerate(strings):
                ls=str(s).lower()
                if any(k in ls for k in ("pak","key_manifest","setdecryptionkey","decrypt","encrypt",
                                         "patch","hotfix","download","manifest","tcp","socket","anorecv","anosdk")):
                    interesting_idx[idx]=str(s)
            # low-level method walk
            for c in d.get_classes():
                cname=c.get_name()
                for m in c.get_methods():
                    code=m.get_code()
                    if not code: continue
                    found=[]
                    try:
                        for ins in code.get_bc().get_instructions():
                            out=ins.get_output()
                            opn=ins.get_name()
                            if "string" in opn:
                                # output often includes string literal; use textual keyword match
                                lo=out.lower()
                                for kw in ("pak","key_manifest","setdecryptionkey","decrypt","encrypt","patch",
                                           "hotfix","download","manifest","tcp","socket"):
                                    if kw in lo:
                                        found.append((opn,out))
                                        break
                    except Exception:
                        continue
                    if found:
                        xrefs.append({"dex":dexname,"class":cname,"method":m.get_name(),
                                      "descriptor":m.get_descriptor(),"strings":found[:20]})
                        if len(xrefs)>=1500: break
                if len(xrefs)>=1500: break
            if len(xrefs)>=1500: break
        except Exception as ex:
            xrefs.append({"dex":dexname,"error":repr(ex)})
    andro["dex_xrefs"]=xrefs
except Exception as ex:
    andro={"ok":False,"error":repr(ex)}

# Summaries
Path(OUT/"inventory.tsv").write_text("\n".join(f"{a}\t{b}\t{c}" for a,b,c in inventory),encoding="utf-8")
(OUT/"scan.json").write_text(json.dumps({
    "apk":{"name":APK_PATH.name,"size":APK_PATH.stat().st_size,"sha256":apk_sha},
    "selected_scans":scans,
    "hex_candidates":hex_candidates,
    "url_candidates":url_candidates,
    "elf_reports":elf_reports,
    "androguard":andro
},indent=2,ensure_ascii=False),encoding="utf-8")

# Human report - compact but rich.
print("\n=== ARM64 LIBRARIES ===")
for e in elf_reports:
    print(f"{e['file']}\t{e['size']}\t{e['sha256']}")
print("\n=== DYNAMIC-KEY 20-HEX CANDIDATES (unique, excluding obvious repeated junk) ===")
cnt=Counter(s for _,_,s in hex_candidates)
for s,c in cnt.most_common(200):
    if len(set(s))<=2: continue
    loc=[x for x in hex_candidates if x[2]==s][:4]
    known_slot=next((k for k,v in KNOWN_DYN.items() if v.decode()==s),None)
    print(json.dumps({"secret":s,"count":c,"known_slot":known_slot,"locations":loc},ensure_ascii=False))
print("\n=== KEY/PATCH RELATED URLS ===")
seen=set()
for f,o,u in url_candidates:
    if u in seen: continue
    seen.add(u)
    print(json.dumps({"file":f,"off":o,"url":u},ensure_ascii=False))
    if len(seen)>=150: break
print("\n=== NATIVE KEY/PAK SYMBOLS ===")
for e in elf_reports:
    if e.get("symbols"):
        print(f"-- {e['file']} --")
        for s in e["symbols"][:250]:
            print(json.dumps(s,ensure_ascii=False))
print("\n=== NATIVE INTERESTING STRINGS ===")
for e in elf_reports:
    vals=e.get("interesting_strings",[])
    if vals:
        print(f"-- {e['file']} --")
        for off,s in vals[:250]:
            print(json.dumps({"off":off,"s":s},ensure_ascii=False))
print("\n=== APK META / DEX XREFS ===")
print(json.dumps({k:v for k,v in andro.items() if k!="dex_xrefs"},ensure_ascii=False))
for x in andro.get("dex_xrefs",[])[:500]:
    print(json.dumps(x,ensure_ascii=False))
