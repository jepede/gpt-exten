#!/usr/bin/env python3
import json, os, re, struct, subprocess, sys, traceback
from collections import defaultdict, deque
from pathlib import Path

from elftools.elf.elffile import ELFFile
from capstone import Cs, CS_ARCH_ARM64, CS_MODE_LITTLE_ENDIAN
from capstone.arm64_const import ARM64_OP_IMM, ARM64_OP_REG, ARM64_OP_MEM

SO = Path(sys.argv[1])
OUT = Path(sys.argv[2])
OUT.mkdir(parents=True, exist_ok=True)
data = SO.read_bytes()

with SO.open("rb") as f:
    elf = ELFFile(f)
    loads = []
    execs = []
    for seg in elf.iter_segments():
        if seg["p_type"] != "PT_LOAD":
            continue
        rec = {
            "vaddr": int(seg["p_vaddr"]), "offset": int(seg["p_offset"]),
            "filesz": int(seg["p_filesz"]), "memsz": int(seg["p_memsz"]),
            "flags": int(seg["p_flags"])
        }
        loads.append(rec)
        if rec["flags"] & 1:
            execs.append(rec)

def off_to_va(off):
    for s in loads:
        if s["offset"] <= off < s["offset"] + s["filesz"]:
            return s["vaddr"] + (off - s["offset"])
    return None

def va_to_off(va):
    for s in loads:
        if s["vaddr"] <= va < s["vaddr"] + s["filesz"]:
            return s["offset"] + (va - s["vaddr"])
    return None

def read_u64_va(va):
    off = va_to_off(va)
    if off is None or off + 8 > len(data): return None
    return struct.unpack_from("<Q", data, off)[0]

# ASCII strings
strings = []
for m in re.finditer(rb"[\x20-\x7e]{5,}", data):
    b = m.group()
    try: s = b.decode("ascii")
    except: continue
    va = off_to_va(m.start())
    if va is not None:
        strings.append({"off":m.start(),"va":va,"s":s})

exact_needles = [
    "SetDecryptionKey",
    "ELF_HOOK_UE4_FPakInfo_Serialize",
    "ELF_HOOK_BRIDGE_UE4_FPakInfo_Serialize",
    "48ea7d82db9995f2",
    "c44d833f54ba436f",
]
known_dynamic = {
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
  42:"56eed0401753d9e5ee86",43:"5412cc837199fa08d229",44:"48750e47caff0540e2ee"
}
static_salts = [
"xG2qW5lP7lV2iN5fN5pG","xT1cJ6dL5wC0kK1rB4dK","qC4jS5bZ6fL5xE6nD4zA",
"gD4jQ2aL3bS3lC3xT0iW","xU1yQ8wE9zY3gZ3bT5aE","uQ3cO2dX7xY4xU7gH7iS",
"gW1fR0jK6wQ4oN0oK1kZ","aJ4pV7iZ7pU4wP2aC2cZ","cX6jT3cM2oT3vK0kJ1qN",
"iT2vS0cS6yT6cZ1sE1lO","hM1pH9iY8wM9hT4lN5uJ","kG6bC8jK0fL0dE4sH4mL",
"dB6lB3vE0eZ8wM8rI0aC","tP7sP7nI9rA2vQ4cV5yQ","aT0cL1yN4pT3sZ7eM2vY",
"uV6fU8fC9zN3mP5dH8mN","rT6aQ6oZ1yM0gO5tO1aN","jU5bH7lQ0fM9hK2kI0oF",
"iQ0eM0mJ7uT0kV6kL5zY","wD2rP3lP9xF4mE1eC5jS","rG0lR2rZ5vM6mW5lM1rR",
"fO3kW1fE6eD0pU1kY7xK"
]

by_exact = defaultdict(list)
for st in strings:
    if st["s"] in exact_needles:
        by_exact[st["s"]].append(st)
    for k,v in known_dynamic.items():
        if st["s"] == v:
            by_exact[f"dyn[{k}]={v}"].append(st)
    for i,v in enumerate(static_salts):
        if st["s"] == v:
            by_exact[f"salt[{31+i}]={v}"].append(st)

hex20 = [st for st in strings if re.fullmatch(r"[0-9a-f]{20}", st["s"])]
interesting = []
rx = re.compile(r"(pak|decrypt|encrypt|decryption|encryption|sm4|aes|zstd|tcp|socket|recv|response|key)", re.I)
for st in strings:
    s=st["s"]
    if rx.search(s) and len(s) <= 180:
        score = sum(1 for w in ("pak","decrypt","encrypt","sm4","tcp","key","response") if w in s.lower())
        if score >= 1:
            interesting.append({**st,"score":score})
interesting.sort(key=lambda x:(-x["score"], len(x["s"])))
interesting = interesting[:600]

# Select target addresses for xref discovery
targets = {}
for name, arr in by_exact.items():
    for st in arr: targets[st["va"]] = name
for st in interesting[:250]:
    targets.setdefault(st["va"], st["s"])

md = Cs(CS_ARCH_ARM64, CS_MODE_LITTLE_ENDIAN)
md.detail = True
xrefs = defaultdict(list)
special = []
function_guess = None
recent = deque(maxlen=24)
regs = {}

def is_prologue(ins):
    # crude but useful function-start heuristic
    return ins.mnemonic == "stp" and "x29, x30" in ins.op_str and "[sp" in ins.op_str

def nearest_target(val):
    if val in targets: return val
    return None

special_imms = {1,2,4,16,17,18,19,31,39,41,42,43,44,47,49,50,52,222,0x1000000,0xff000000,0xffffff}

for seg in execs:
    blob = data[seg["offset"]:seg["offset"]+seg["filesz"]]
    regs.clear(); recent.clear(); function_guess=None
    for ins in md.disasm(blob, seg["vaddr"]):
        if is_prologue(ins):
            function_guess = ins.address
        recent.append((ins.address, ins.mnemonic, ins.op_str))
        ops = ins.operands
        try:
            # Resolve ADR/ADRP
            if ins.mnemonic in ("adr","adrp") and len(ops)>=2 and ops[0].type==ARM64_OP_REG and ops[1].type==ARM64_OP_IMM:
                regs[ops[0].reg] = int(ops[1].imm)
            elif ins.mnemonic == "add" and len(ops)>=3 and ops[0].type==ARM64_OP_REG and ops[1].type==ARM64_OP_REG and ops[2].type==ARM64_OP_IMM:
                if ops[1].reg in regs:
                    regs[ops[0].reg] = (regs[ops[1].reg] + int(ops[2].imm)) & 0xffffffffffffffff
                else:
                    regs.pop(ops[0].reg, None)
            elif ins.mnemonic == "mov" and len(ops)>=2 and ops[0].type==ARM64_OP_REG:
                if ops[1].type==ARM64_OP_REG and ops[1].reg in regs:
                    regs[ops[0].reg] = regs[ops[1].reg]
                elif ops[1].type==ARM64_OP_IMM:
                    regs[ops[0].reg] = int(ops[1].imm)
                else:
                    regs.pop(ops[0].reg, None)
            elif ins.mnemonic.startswith("ldr") and len(ops)>=2 and ops[0].type==ARM64_OP_REG and ops[1].type==ARM64_OP_MEM:
                b=ops[1].mem.base
                if b in regs:
                    mem=(regs[b] + int(ops[1].mem.disp)) & 0xffffffffffffffff
                    # Record direct data ref and pointer-indirect ref
                    if mem in targets:
                        xrefs[mem].append({"insn":ins.address,"func":function_guess,"kind":"mem","text":f"{ins.mnemonic} {ins.op_str}"})
                    if ins.mnemonic=="ldr":
                        ptr=read_u64_va(mem)
                        if ptr in targets:
                            xrefs[ptr].append({"insn":ins.address,"func":function_guess,"kind":"ptr","mem":mem,"text":f"{ins.mnemonic} {ins.op_str}"})
                        if ptr is not None:
                            regs[ops[0].reg]=ptr
                        else:
                            regs.pop(ops[0].reg,None)
                    else:
                        regs.pop(ops[0].reg,None)
            # resolved register values may point directly at strings
            for r,v in list(regs.items()):
                t=nearest_target(v)
                if t is not None and (not xrefs[t] or xrefs[t][-1].get("insn") != ins.address):
                    xrefs[t].append({"insn":ins.address,"func":function_guess,"kind":"reg","reg":ins.reg_name(r),"text":f"{ins.mnemonic} {ins.op_str}"})
            # special immediates / masks
            imms=[int(o.imm) for o in ops if o.type==ARM64_OP_IMM]
            if any((x & 0xffffffffffffffff) in special_imms for x in imms):
                special.append({
                    "address":ins.address,"func":function_guess,"mnemonic":ins.mnemonic,"op_str":ins.op_str,
                    "immediates":[hex(x & 0xffffffffffffffff) for x in imms],
                    "context":list(recent)
                })
            # Reset weak constant tracking at control-flow boundaries
            if ins.mnemonic in ("ret","br","blr") or ins.mnemonic.startswith("b."):
                regs.clear()
        except Exception:
            pass

# Group functions by interesting referenced strings
func_strings=defaultdict(set)
for va, refs in xrefs.items():
    for r in refs:
        if r.get("func"):
            func_strings[r["func"]].add(targets.get(va,hex(va)))

ranked_funcs=[]
for f, ss in func_strings.items():
    score=sum(3 if re.search(r"decrypt|encrypt|sm4|pak|key",s,re.I) else 1 for s in ss)
    if len(ss)>=2 or score>=3:
        ranked_funcs.append({"func":f,"score":score,"strings":sorted(ss)})
ranked_funcs.sort(key=lambda x:(-x["score"],-len(x["strings"])))

result={
    "file":str(SO),
    "size":len(data),
    "load_segments":loads,
    "exact_strings":dict(by_exact),
    "hex20_count":len(hex20),
    "hex20":hex20[:500],
    "interesting_strings":interesting,
    "xrefs":{hex(k):v for k,v in xrefs.items() if v},
    "ranked_functions":ranked_funcs[:200],
    "special_immediates":special[:5000]
}
(OUT/"static_scan.json").write_text(json.dumps(result,indent=2),encoding="utf-8")

# Human-readable grep-like string report
with (OUT/"strings_focus.txt").open("w",encoding="utf-8") as fp:
    for st in interesting:
        fp.write(f"0x{st['va']:x}\t{st['s']}\n")
    fp.write("\n=== 20hex candidates ===\n")
    for st in hex20:
        fp.write(f"0x{st['va']:x}\t{st['s']}\n")

# Capstone summaries around special dynamic-key checks
with (OUT/"dynamic_mask_candidates.txt").open("w",encoding="utf-8") as fp:
    for s in special:
        txt=(s["mnemonic"]+" "+s["op_str"]).lower()
        if any(k in txt for k in ("0xff000000","0x1000000","0xffffff","#0x18")) or any(v in s["immediates"] for v in ("0xff000000","0x1000000","0xffffff")):
            fp.write(f"\nFUNC~0x{(s['func'] or 0):x} @ 0x{s['address']:x}: {s['mnemonic']} {s['op_str']}\n")
            for c in s["context"]:
                fp.write(f"  0x{c[0]:x}: {c[1]} {c[2]}\n")

# Optional radare2 enrichment
r2_report={}
try:
    import r2pipe
    r2=r2pipe.open(str(SO), flags=["-2"])
    r2.cmd("e anal.timeout=180")
    r2.cmd("e anal.hasnext=true")
    r2.cmd("aa")
    query_addrs=set()
    for va, refs in xrefs.items():
        if refs and (targets.get(va,"").startswith("SetDecryptionKey") or re.search(r"decrypt|encrypt|sm4|48ea|c44d",targets.get(va,""),re.I)):
            query_addrs.add(va)
    for va in list(query_addrs)[:40]:
        refs=r2.cmdj(f"axtj @ {va}") or []
        rr=[]
        for ref in refs[:30]:
            frm=ref.get("from")
            fi=(r2.cmdj(f"afij @ {frm}") or [])
            if fi:
                faddr=fi[0].get("offset",frm)
                dis=r2.cmd(f"pd 100 @ {faddr}")
            else:
                faddr=frm; dis=r2.cmd(f"pd 50 @ {frm}")
            rr.append({"ref":ref,"function":fi[:1],"disasm":dis})
        r2_report[hex(va)]={"target":targets.get(va),"refs":rr}
    r2.quit()
except Exception as e:
    r2_report={"error":repr(e),"traceback":traceback.format_exc()}
(OUT/"r2_xrefs.json").write_text(json.dumps(r2_report,indent=2),encoding="utf-8")

# compact markdown
lines=["# PUBG 4.6 dynamic-key static scan","",f"- File: {SO.name}",f"- Size: {len(data)}",f"- 20-hex candidates: {len(hex20)}","",
"## Exact anchors"]
for name,arr in sorted(by_exact.items()):
    lines.append(f"- {name}: "+", ".join(f"0x{x['va']:x}" for x in arr))
lines += ["","## Top co-reference functions"]
for x in ranked_funcs[:50]:
    lines.append(f"- 0x{x['func']:x} score={x['score']}: " + " | ".join(x["strings"][:12]))
lines += ["","## Notes",
"- Missing dyn[39]/dyn[41] as plaintext is meaningful only if all other known dynamic salts are checked alongside it.",
"- dynamic_mask_candidates.txt lists code that manipulates 0xFF000000 / 0x01000000 / 0x00FFFFFF-style values.",
"- r2_xrefs.json is supplemental; capstone-derived references are in static_scan.json."
]
(OUT/"REPORT.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
print("analysis complete", OUT)
