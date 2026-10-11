#!/usr/bin/env python3
import sys,struct,json,re
from pathlib import Path
from elftools.elf.elffile import ELFFile
from capstone import Cs,CS_ARCH_ARM64,CS_MODE_LITTLE_ENDIAN
P=Path(sys.argv[1]); raw=P.read_bytes()
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
 dyn=e.get_section_by_name(".dynsym")
 syms={}
 if dyn:
  for idx,s in enumerate(dyn.iter_symbols()):
   syms[idx]=(s.name,int(s["st_value"]),int(s["st_size"]),str(s["st_shndx"]),s["st_info"]["type"],s["st_info"]["bind"])
 targets={}
 for name in ("g_acf_array","g_aco_array"):
  for idx,v in syms.items():
   if v[0]==name: targets[name]=v
 print("FILE",P,"size",len(raw))
 print("TARGETS",targets)
 relocs=[]
 for sec in e.iter_sections():
  if sec["sh_type"] not in ("SHT_RELA","SHT_REL"):continue
  symtab=e.get_section(sec["sh_link"]) if sec["sh_link"] else None
  for rel in sec.iter_relocations():
   off=int(rel["r_offset"]); ridx=rel["r_info_sym"]; nm=""
   if symtab is not None and ridx:
    try:nm=symtab.get_symbol(ridx).name
    except:pass
   addend=int(rel["r_addend"]) if "r_addend" in rel.entry else None
   relocs.append((off,sec.name,rel["r_info_type"],ridx,nm,addend))
 md=Cs(CS_ARCH_ARM64,CS_MODE_LITTLE_ENDIAN)
 for name,(nm,va,size,shndx,typ,bind) in targets.items():
  print(f"\n== {name} va=0x{va:x} size=0x{size:x} slots={size//8} ==")
  o=vaoff(va)
  if o is not None:
   b=raw[o:o+size]
   for i in range(0,size,8):
    q=struct.unpack_from("<Q",b,i)[0] if i+8<=len(b) else 0
    rs=[r for r in relocs if r[0]==va+i]
    print(f"slot[{i//8:02d}] +0x{i:03x} va=0x{va+i:x} raw=0x{q:x} reloc={rs}")
  print("-- RELOCS RANGE --")
  for r in relocs:
   if va<=r[0]<va+size:print(r)

 # interesting exported/defined symbols
 print("\n== INTERESTING DYNAMIC SYMBOLS ==")
 for idx,(nm,va,size,sh,typ,bind) in syms.items():
  lo=nm.lower()
  if va and any(k in lo for k in ("acf","aco","elf","hook","decrypt","encrypt","protect","integrity","stub","syscall","report","tcp","key")):
   print(idx,nm,hex(va),hex(size),sh,typ,bind)

 print("\n== INTERESTING STRINGS ==")
 for m in re.finditer(rb"[ -~]{4,}",raw):
  s=m.group().decode("ascii","ignore"); lo=s.lower()
  if any(k in lo for k in ("decrypt","encrypt","hook","elf","mprotect","integrity","tcp","socket","pak","key","stub","report","acf","aco")) and len(s)<240:
   va=None
   for v,o,fs,ms,fl in segs:
    if o<=m.start()<o+fs:va=v+(m.start()-o);break
   print(hex(va) if va is not None else None, s)

 # Resolve relocation addends/values to executable code and dump unique targets
 candidates=set()
 for name,(nm,va,size,shndx,typ,bind) in targets.items():
  o=vaoff(va)
  if o is not None:
   b=raw[o:o+size]
   for i in range(0,size,8):
    if i+8<=len(b):
     q=struct.unpack_from("<Q",b,i)[0]
     for v,oo,fs,ms,fl in segs:
      if fl&1 and v<=q<v+fs:candidates.add(q)
  for r in relocs:
   if va<=r[0]<va+size and r[5]:
    q=r[5]
    for v,oo,fs,ms,fl in segs:
     if fl&1 and v<=q<v+fs:candidates.add(q)
 print("\n== CANDIDATE CODE TARGETS ==")
 for va in sorted(candidates):
  o=vaoff(va)
  print(f"\n-- target 0x{va:x} --")
  if o is None:continue
  for ins in md.disasm(raw[o:o+0x300],va):
   print(f"0x{ins.address:x}: {ins.mnemonic:8s} {ins.op_str}")
