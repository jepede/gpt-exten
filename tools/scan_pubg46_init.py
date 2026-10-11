#!/usr/bin/env python3
import sys,json
from pathlib import Path
from elftools.elf.elffile import ELFFile
from capstone import Cs,CS_ARCH_ARM64,CS_MODE_LITTLE_ENDIAN
from capstone.arm64 import *
P=Path(sys.argv[1]); raw=P.read_bytes()
with P.open("rb") as f:
 e=ELFFile(f)
 segs=[]
 for s in e.iter_segments():
  if s["p_type"]=="PT_LOAD":
   segs.append(dict(vaddr=int(s["p_vaddr"]),off=int(s["p_offset"]),filesz=int(s["p_filesz"]),memsz=int(s["p_memsz"]),flags=int(s["p_flags"]),align=int(s["p_align"])))
 init=None
 for s in e.iter_segments():
  if s["p_type"]=="PT_DYNAMIC":
   for t in s.iter_tags():
    if t.entry.d_tag=="DT_INIT": init=int(t.entry.d_val)
 print("PT_LOAD:")
 for x in segs: print(x)
 print("DT_INIT",hex(init) if init else None)
 dyn=[]
 ds=e.get_section_by_name(".dynsym")
 if ds:
  for sym in ds.iter_symbols():
   n=sym.name
   if any(k in n for k in ["mprotect","mmap","memcpy","memmove","cache","dlopen","dlsym","pthread","syscall"]):
    dyn.append((n,int(sym["st_value"])))
 print("DYNSYM",dyn)

def vaoff(va):
 for s in segs:
  if s["vaddr"]<=va<s["vaddr"]+s["filesz"]:return s["off"]+(va-s["vaddr"])
 return None
md=Cs(CS_ARCH_ARM64,CS_MODE_LITTLE_ENDIAN);md.detail=True
seen=set()
def dump(addr,size=0x500,depth=0):
 if addr in seen or depth>3:return
 seen.add(addr);o=vaoff(addr)
 if o is None:return
 print(f"\n== FUNC/CODE 0x{addr:x} depth={depth} ==")
 insns=list(md.disasm(raw[o:o+size],addr))
 calls=[]
 for i in insns:
  print(f"0x{i.address:x}: {i.mnemonic:8s} {i.op_str}")
  if i.mnemonic=="bl" and i.operands and i.operands[0].type==ARM64_OP_IMM:
   calls.append(i.operands[0].imm)
 # recurse only into high/private-looking callees and nearby ones
 for c in calls[:40]:
  if vaoff(c) is not None and (abs(c-addr)<0x200000 or c>0xe000000):
   dump(c,0x300,depth+1)
if init: dump(init,0x900,0)

# Search exact immediate bytes in raw for likely protector key/map constants (data only heuristic)
for b in [0xc8,0x71]:
 print("byte_count",hex(b),raw.count(bytes([b])))
