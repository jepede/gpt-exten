#!/usr/bin/env python3
import sys
from pathlib import Path
from elftools.elf.elffile import ELFFile
from capstone import Cs,CS_ARCH_ARM64,CS_MODE_LITTLE_ENDIAN

P=Path(sys.argv[1]); raw=P.read_bytes()
names=[
"stub_decrypt_elf",
"ELF_HOOK_BRIDGE_UE4_FPakInfo_Serialize",
"ELF_HOOK_UE4_FPakInfo_Serialize",
"g_acf_array","g_aco_array","xxxxXXXXxxxx",
]
with P.open("rb") as f:
 e=ELFFile(f)
 segs=[]
 for s in e.iter_segments():
  if s["p_type"]=="PT_LOAD":
   segs.append((int(s["p_vaddr"]),int(s["p_offset"]),int(s["p_filesz"]),int(s["p_memsz"]),int(s["p_flags"])))
 def vaoff(va):
  for v,o,fs,ms,fl in segs:
   if v<=va<v+fs:return o+(va-v)
  return None
 md=Cs(CS_ARCH_ARM64,CS_MODE_LITTLE_ENDIAN)
 syms={}
 for secname in [".dynsym",".symtab"]:
  sec=e.get_section_by_name(secname)
  if not sec:continue
  for sym in sec.iter_symbols():
   if sym.name in names or any(x in sym.name for x in ("FPakInfo","decrypt_elf","acf_array","aco_array")):
    syms[(secname,sym.name)]=(int(sym["st_value"]),int(sym["st_size"]),sym["st_info"]["type"],sym["st_shndx"])
 print("== SYMBOLS ==")
 for k,v in sorted(syms.items(),key=lambda kv:kv[1][0]):
  print(k,v)
 print("\n== DISASM ==")
 seen=set()
 for (sec,name),(va,size,typ,sh) in sorted(syms.items(),key=lambda kv:kv[1][0]):
  if va==0 or va in seen:continue
  seen.add(va); off=vaoff(va)
  print(f"\n-- {name} sec={sec} va=0x{va:x} size=0x{size:x} off={off} type={typ} --")
  if off is None:continue
  n=max(size,0x300) if typ=="STT_FUNC" else min(max(size,0x80),0x400)
  n=min(n,0x1800)
  if typ=="STT_FUNC" or name.startswith("ELF_") or name=="stub_decrypt_elf":
   for ins in md.disasm(raw[off:off+n],va):
    print(f"0x{ins.address:x}: {ins.mnemonic:8s} {ins.op_str}")
  else:
   b=raw[off:off+n]
   print("hex",b.hex())
