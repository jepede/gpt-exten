#!/usr/bin/env python3
import json, re, struct, hashlib, sys
from collections import defaultdict, Counter
from pathlib import Path
from elftools.elf.elffile import ELFFile
from capstone import Cs, CS_ARCH_ARM64, CS_MODE_LITTLE_ENDIAN
from capstone.arm64 import *

P=Path(sys.argv[1])
OUT=Path(sys.argv[2] if len(sys.argv)>2 else "scan_out")
OUT.mkdir(parents=True, exist_ok=True)
data=P.read_bytes()

KNOWN_DYN = {
0:"edbcba1dc6b11068b44a",1:"4fdf06dd5830dea4a927",2:"92bd3c6ca58d471b03df",
3:"5267814520c2b1904294",4:"f31085d8cefbf7e4adaf",5:"589df0f2a3203ef9b9cc",
6:"354d3b38e8e518477d8c",7:"b57b1eeeed9d590e4692",8:"2cbdd9c8cc6d20867fa2",
9:"d47158ca2923a75af7ef",10:"2a1138b5e375c7c9101a",11:"c9347da5d7111fe9f1d9",
12:"8e74503f8a94724dbb08",13:"0259d21abd4adf59ca05",14:"18ca7d8e7b13f4760404",
15:"e9528dbafe091b886af5",16:"d6860287a330f9a92210",17:"751a5feeb49616d1cceb",
18:"6955d9dfab070681d752",19:"068b4cfc607fa13a1ffb",20:"4fb7a2e36b9d156b79f8",
21:"44e497e008d6789f2dbf",22:"0dc887496bb94080f2c4",23:"032a5c6c206b96db376a",
24:"e4bb6ceb363e5841d946",25:"06d780b85eade141e5fd",26:"a6a915cd11add12a94e9",
27:"5967e403b057bc02a8a9",28:"87bae21ce1a1631ad6c9",29:"14f8efdb5552af690d44",
30:"9477ecd3fee28c7d2a34",31:"b4ecef20999b7ccb205e",32:"ec7c6575fc2a54caeb0d",
33:"afa22d65c9f5a95f0f73",34:"e5901d4631734da09feb",35:"e31c6f4e994cb4330504",
36:"df473da3aa9b5704ce73",37:"46e490567d02cdb312b3",38:"f838b560ec26d4ba67fd",
42:"56eed0401753d9e5ee86",43:"5412cc837199fa08d229",44:"48750e47caff0540e2ee",
}
STATIC_SALTS=[
"xG2qW5lP7lV2iN5fN5pG","xT1cJ6dL5wC0kK1rB4dK","qC4jS5bZ6fL5xE6nD4zA",
"gD4jQ2aL3bS3lC3xT0iW","xU1yQ8wE9zY3gZ3bT5aE","uQ3cO2dX7xY4xU7gH7iS",
"gW1fR0jK6wQ4oN0oK1kZ","aJ4pV7iZ7pU4wP2aC2cZ","cX6jT3cM2oT3vK0kJ1qN",
"iT2vS0cS6yT6cZ1sE1lO","hM1pH9iY8wM9hT4lN5uJ","kG6bC8jK0fL0dE4sH4mL",
"dB6lB3vE0eZ8wM8rI0aC","tP7sP7nI9rA2vQ4cV5yQ","aT0cL1yN4pT3sZ7eM2vY",
"uV6fU8fC9zN3mP5dH8mN","rT6aQ6oZ1yM0gO5tO1aN","jU5bH7lQ0fM9hK2kI0oF",
"iQ0eM0mJ7uT0kV6kL5zY","wD2rP3lP9xF4mE1eC5jS","rG0lR2rZ5vM6mW5lM1rR",
"fO3kW1fE6eD0pU1kY7xK"]

SBOX=bytes([
0x34,0x66,0x25,0x74,0x89,0x78,0xE4,0xA9,0x5A,0x41,0xBC,0x7A,0xD6,0x16,0x21,0x23,
0x4D,0x61,0xDA,0x94,0x9B,0xDF,0x13,0x3C,0x69,0x3A,0x31,0x0A,0x5F,0xD7,0x99,0x95,
0xF1,0xAE,0x72,0x3D,0x07,0x60,0x24,0xB6,0x98,0xEE,0xC4,0xA2,0x2D,0x88,0xDD,0x8D,
0x04,0xEA,0xBB,0x11,0xCA,0x3E,0x5D,0xA1,0xF6,0x3F,0xB0,0x97,0x80,0x47,0x2B,0xA6,
0xE6,0xF7,0xD9,0xB1,0x59,0xC0,0x7C,0xBE,0x54,0x28,0xB7,0x7E,0x4F,0xF8,0x43,0x6E,
0xA0,0x50,0x0E,0xF5,0x90,0xB8,0xFB,0xA3,0x7B,0x62,0x19,0x46,0x03,0x2A,0xB9,0x8F,
0x9F,0x77,0xB4,0x5B,0x83,0x87,0x08,0xEB,0xE2,0x1E,0x42,0xF0,0x0F,0xE8,0x71,0x6A,
0x75,0xAD,0x55,0x1F,0xB5,0xAB,0x33,0xFA,0x7F,0x15,0xBD,0x85,0xD8,0x06,0x68,0xB3,
0x52,0x30,0x48,0x0B,0x00,0xED,0xEF,0xB2,0x57,0x8E,0xE7,0x6C,0xD5,0xE5,0x2E,0x53,
0x82,0x05,0xF9,0x81,0xF4,0x56,0xBF,0x8C,0x4B,0xE3,0xDB,0x4A,0x91,0x4C,0x2C,0xD3,
0x40,0x29,0x4E,0x20,0x14,0x36,0x79,0x09,0x6F,0xD1,0x37,0xE0,0x39,0x0C,0x8A,0x92,
0x38,0x12,0x35,0x6D,0xE1,0xFD,0x93,0x9A,0x17,0xD4,0xC9,0x9C,0x6B,0x84,0x26,0x9D,
0xAF,0x76,0xC1,0x9E,0xD0,0x96,0xC5,0xCB,0xE9,0x73,0x49,0xD2,0xCD,0x64,0xC3,0xC7,
0x01,0x7D,0xF3,0xAC,0xFC,0xDE,0xA4,0x44,0x32,0x1B,0xC2,0xBA,0x1C,0x02,0xC6,0x27,
0x45,0x8B,0xF2,0x18,0xA7,0x10,0x51,0x1D,0xC8,0xCF,0x63,0xFF,0x2F,0x0D,0x58,0xCE,
0x65,0xA5,0xDC,0x1A,0x3B,0x86,0xFE,0x22,0x5C,0xA8,0x5E,0x67,0xAA,0xEC,0x70,0xCC])

with P.open("rb") as f:
    elf=ELFFile(f)
    segs=[]
    execsegs=[]
    for s in elf.iter_segments():
        if s["p_type"]!="PT_LOAD": continue
        ent={"vaddr":int(s["p_vaddr"]),"off":int(s["p_offset"]),"filesz":int(s["p_filesz"]),"memsz":int(s["p_memsz"]),"flags":int(s["p_flags"])}
        segs.append(ent)
        if ent["flags"] & 1: execsegs.append(ent)

def off_to_va(o):
    for s in segs:
        if s["off"] <= o < s["off"]+s["filesz"]:
            return s["vaddr"] + (o-s["off"])
    return None

def va_to_off(va):
    for s in segs:
        if s["vaddr"] <= va < s["vaddr"]+s["filesz"]:
            return s["off"] + (va-s["vaddr"])
    return None

def find_all(needle):
    out=[]; start=0
    while True:
        i=data.find(needle,start)
        if i<0: break
        out.append({"off":i,"va":off_to_va(i)})
        start=i+1
    return out

targets={}
for k,v in KNOWN_DYN.items():
    for hit in find_all(v.encode()):
        targets[f"dyn[{k}]={v}"]=hit["va"]
for idx,v in enumerate(STATIC_SALTS):
    for hit in find_all(v.encode()):
        targets[f"static[{idx}]={v}"]=hit["va"]
for label,s in {
"global_sm4_source":"48ea7d82db9995f2",
"alt19_source":"c44d833f54ba436f",
"SetDecryptionKey":"SetDecryptionKey",
"key_manifest":"key_manifest",
"FPakInfoSerialize":"FPakInfo_Serialize",
"tcp":"tcp",
"TCP":"TCP",
}.items():
    for n,hit in enumerate(find_all(s.encode())):
        targets[f"{label}#{n}"]=hit["va"]

special={
"sm4_sbox":find_all(SBOX),
"simple2_e55b4ed1":find_all(bytes.fromhex("E55B4ED1")),
"magic_4c515443":find_all(struct.pack("<I",0x4C515443)),
}
for label,hits in special.items():
    for n,h in enumerate(hits):
        targets[f"{label}#{n}"]=h["va"]

# generic interesting strings
strings=[]
for m in re.finditer(rb"[ -~]{4,}", data):
    s=m.group().decode("ascii","ignore")
    lo=s.lower()
    if any(x in lo for x in ("pak","encrypt","decrypt","key","tcp","socket","manifest","sm4","zstd","aes","rsa")):
        if len(s)<=220:
            strings.append({"va":off_to_va(m.start()),"off":m.start(),"s":s})
strings=strings[:10000]

md=Cs(CS_ARCH_ARM64,CS_MODE_LITTLE_ENDIAN)
md.detail=True
allins=[]
for s in execsegs:
    blob=data[s["off"]:s["off"]+s["filesz"]]
    for ins in md.disasm(blob,s["vaddr"]):
        allins.append(ins)

# map refs using lightweight abstract interpretation over straight-line instructions
target_by_va=defaultdict(list)
for name,va in targets.items():
    if va is not None: target_by_va[va].append(name)

xrefs=[]
regs={}
for ins in allins:
    try:
        ops=ins.operands
        m=ins.mnemonic
        if m=="adrp" and len(ops)>=2 and ops[0].type==ARM64_OP_REG and ops[1].type==ARM64_OP_IMM:
            regs[ops[0].reg]=ops[1].imm
        elif m=="adr" and len(ops)>=2 and ops[0].type==ARM64_OP_REG and ops[1].type==ARM64_OP_IMM:
            regs[ops[0].reg]=ops[1].imm
        elif m=="add" and len(ops)>=3 and ops[0].type==ARM64_OP_REG and ops[1].type==ARM64_OP_REG and ops[2].type==ARM64_OP_IMM:
            if ops[1].reg in regs:
                regs[ops[0].reg]=regs[ops[1].reg]+ops[2].imm
                val=regs[ops[0].reg]
                if val in target_by_va:
                    xrefs.append({"at":ins.address,"target":val,"names":target_by_va[val],"ins":f"{m} {ins.op_str}"})
            else: regs.pop(ops[0].reg,None)
        elif m.startswith("ldr") and len(ops)>=2 and ops[0].type==ARM64_OP_REG:
            if ops[1].type==ARM64_OP_MEM:
                base=ops[1].mem.base
                if base in regs:
                    val=regs[base]+ops[1].mem.disp
                    if val in target_by_va:
                        xrefs.append({"at":ins.address,"target":val,"names":target_by_va[val],"ins":f"{m} {ins.op_str}"})
                regs.pop(ops[0].reg,None)
            elif ops[1].type==ARM64_OP_IMM:
                val=ops[1].imm
                if val in target_by_va:
                    xrefs.append({"at":ins.address,"target":val,"names":target_by_va[val],"ins":f"{m} {ins.op_str}"})
                regs.pop(ops[0].reg,None)
        elif m in ("mov","movz","movn","movk") and ops and ops[0].type==ARM64_OP_REG:
            # do not try to model MOVK chains; clear stale values
            regs.pop(ops[0].reg,None)
        # conservative barrier
        if m in ("ret","br","blr") or m.startswith("b."):
            regs={}
    except Exception:
        pass

# immediate signatures: dynamic-key mask/index logic
imm_hits=[]
interesting_imms={0x01000000,0xFF000000,0xFFFFFF,0x1000000,17,18,19,31,50,222}
for ins in allins:
    vals=[]
    try:
        for o in ins.operands:
            if o.type==ARM64_OP_IMM: vals.append(o.imm & 0xffffffffffffffff)
    except Exception: continue
    matched=[x for x in vals if x in interesting_imms]
    if matched:
        imm_hits.append({"at":ins.address,"ins":f"{ins.mnemonic} {ins.op_str}","imm":matched})

# find likely prologue backwards
addresses=[i.address for i in allins]
idx_by_addr={a:i for i,a in enumerate(addresses)}
def fn_guess(addr):
    i=idx_by_addr.get(addr)
    if i is None: return None
    for j in range(i,max(-1,i-300),-1):
        ins=allins[j]
        s=f"{ins.mnemonic} {ins.op_str}"
        if ins.mnemonic=="stp" and "x29, x30" in ins.op_str and "[sp" in ins.op_str:
            return ins.address
        if ins.mnemonic=="sub" and ins.op_str.startswith("sp, sp"):
            # weak fallback
            return ins.address
    return None
for x in xrefs: x["fn_guess"]=fn_guess(x["at"])
for x in imm_hits: x["fn_guess"]=fn_guess(x["at"])

# group interesting immediate functions
func_imm=defaultdict(list)
for h in imm_hits:
    func_imm[h["fn_guess"]].append(h)
func_scores=[]
for fn,hits in func_imm.items():
    vals=set(v for h in hits for v in h["imm"])
    score=len(vals & {0x01000000,0xFF000000,0xFFFFFF})*10 + len(vals & {17,19,31,50,222})
    if score:
        func_scores.append({"fn":fn,"score":score,"values":sorted(vals),"hits":hits[:80]})
func_scores.sort(key=lambda x:-x["score"])

# dump windows around top candidates and xrefs
def disasm_window(addr,before=0x40,after=0x100):
    o=va_to_off(max(0,addr-before))
    if o is None:return []
    start=max(0,addr-before)
    blob=data[o:o+before+after]
    return [f"0x{i.address:x}: {i.mnemonic} {i.op_str}" for i in md.disasm(blob,start)]

windows={}
for x in xrefs[:200]:
    windows[f"xref_0x{x['at']:x}"]=disasm_window(x["at"])
for f in func_scores[:80]:
    if f["fn"] is not None:
        windows[f"func_0x{f['fn']:x}"]=disasm_window(f["fn"],0,0x600)

# find all 20 lowercase hex strings and ASCII hex-ish tables
hex20=[]
for m in re.finditer(rb"(?<![0-9a-f])[0-9a-f]{20}(?![0-9a-f])",data):
    hex20.append({"va":off_to_va(m.start()),"off":m.start(),"s":m.group().decode()})

summary={
"file":P.name,
"size":len(data),
"sha256":hashlib.sha256(data).hexdigest(),
"load_segments":segs,
"known_target_count":len(targets),
"targets":targets,
"special":special,
"xrefs":xrefs,
"immediate_hits":imm_hits[:5000],
"top_dynamic_signature_functions":func_scores[:100],
"hex20":hex20,
"interesting_strings":strings,
"windows":windows,
}
(OUT/"scan.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")

with (OUT/"report.txt").open("w",encoding="utf-8") as w:
    w.write(f"file={P.name}\nsize={len(data)}\nsha256={summary['sha256']}\n")
    w.write("\n== SPECIAL BYTE HITS ==\n")
    for k,v in special.items(): w.write(f"{k}: {v}\n")
    w.write("\n== KNOWN STRING/TABLE TARGETS ==\n")
    for k,v in sorted(targets.items(), key=lambda z:(z[1] is None,z[1] or 0)): w.write(f"{k}: {hex(v) if v else None}\n")
    w.write("\n== XREFS ==\n")
    for x in xrefs: w.write(json.dumps(x)+"\n")
    w.write("\n== TOP DYNAMIC SIGNATURE FUNCTIONS ==\n")
    for x in func_scores[:100]: w.write(json.dumps(x)+"\n")
    w.write("\n== 20-HEX CANDIDATES ==\n")
    for x in hex20: w.write(json.dumps(x)+"\n")
    w.write("\n== INTERESTING STRINGS ==\n")
    for x in strings: w.write(json.dumps(x,ensure_ascii=False)+"\n")
    w.write("\n== DISASM WINDOWS ==\n")
    for k,lines in windows.items():
        w.write(f"\n-- {k} --\n"+"\n".join(lines)+"\n")
print("wrote",OUT)
