#!/usr/bin/env python3
import sys
from pathlib import Path
from elftools.elf.elffile import ELFFile
from capstone import Cs,CS_ARCH_ARM64,CS_MODE_LITTLE_ENDIAN
from capstone.arm64 import ARM64_OP_IMM

P=Path(sys.argv[1]); raw=P.read_bytes()
targets=[0x3802c,0x38414,0x39e60,0x3e62c,0x156a5c,0x39400,
         0x13ff1c,0x1424cc,0x131384,0x13ce6c,0x108aec,0x10e3f0,0x13feb0]
with P.open("rb") as f:
 e=ELFFile(f)
 segs=[(int(s["p_vaddr"]),int(s["p_offset"]),int(s["p_filesz"]),int(s["p_flags"])) for s in e.iter_segments() if s["p_type"]=="PT_LOAD"]
 def vaoff(va):
  for v,o,fs,fl in segs:
   if v<=va<v+fs:return o+va-v
  return None
 dyn=e.get_section_by_name(".dynsym")
 syms=[]
 if dyn:
  for s in dyn.iter_symbols():
   if s.name and int(s["st_value"]):
    syms.append((int(s["st_value"]),int(s["st_size"]),s.name))
 # plt map
 plt=e.get_section_by_name(".plt"); rela=e.get_section_by_name(".rela.plt")
 pltmap={}
 if plt and rela:
  # AArch64: PLT0 is 32 bytes, each subsequent stub 16 bytes in relocation order.
  base=int(plt["sh_addr"])+0x20
  symtab=e.get_section(rela["sh_link"])
  for idx,r in enumerate(rela.iter_relocations()):
   nm=symtab.get_symbol(r["r_info_sym"]).name if r["r_info_sym"] else ""
   pltmap[base+idx*0x10]=nm
 print("PLT",hex(int(plt["sh_addr"])) if plt else None,"entries",len(pltmap))
 md=Cs(CS_ARCH_ARM64,CS_MODE_LITTLE_ENDIAN); md.detail=True
 def nearest(va):
  cand=[x for x in syms if x[0]<=va and (x[1]==0 or va<x[0]+x[1])]
  if cand:
   return max(cand,key=lambda x:x[0])
  return None
 for t in targets:
  o=vaoff(t); print(f"\n===== TARGET 0x{t:x} off={o} sym={nearest(t)} =====")
  if o is None:continue
  insns=list(md.disasm(raw[o:o+0x1000],t))
  # stop after ~0x800 or first RET after 0x40
  for ins in insns:
   print(f"0x{ins.address:x}: {ins.mnemonic:8s} {ins.op_str}")
   if ins.mnemonic=="bl" and ins.operands and ins.operands[0].type==ARM64_OP_IMM:
    c=ins.operands[0].imm
    print(f"    ; CALL -> 0x{c:x} plt={pltmap.get(c)} sym={nearest(c)}")
   if ins.mnemonic=="ret" and ins.address>t+0x40:break
