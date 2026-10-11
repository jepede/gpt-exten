#!/usr/bin/env python3
import sys, json
from pathlib import Path
from elftools.elf.elffile import ELFFile
P=Path(sys.argv[1])
slots=set(range(0xF74F7A0,0xF74F880,8))
with P.open('rb') as f:
    e=ELFFile(f)
    print("ELF",P)
    print("== RELOCATIONS IN PROTECTOR GOT RANGE ==")
    for sec in e.iter_sections():
        if sec['sh_type'] not in ('SHT_RELA','SHT_REL'):
            continue
        symtab=e.get_section(sec['sh_link']) if sec['sh_link'] else None
        for rel in sec.iter_relocations():
            off=int(rel['r_offset'])
            if not (0xF74F700 <= off < 0xF750000):
                continue
            symidx=rel['r_info_sym']
            name=''
            if symtab is not None and symidx:
                try: name=symtab.get_symbol(symidx).name
                except Exception: pass
            print(f"{sec.name}: off=0x{off:x} type={rel['r_info_type']} sym={symidx} name={name}")
    print("\n== ALL TARGET SLOTS EXACT ==")
    found={}
    for sec in e.iter_sections():
        if sec['sh_type'] not in ('SHT_RELA','SHT_REL'):
            continue
        symtab=e.get_section(sec['sh_link']) if sec['sh_link'] else None
        for rel in sec.iter_relocations():
            off=int(rel['r_offset'])
            if off in slots:
                symidx=rel['r_info_sym']; name=''
                if symtab is not None and symidx:
                    try:name=symtab.get_symbol(symidx).name
                    except:pass
                found[off]=(sec.name,rel['r_info_type'],name)
    for off in sorted(slots):
        print(f"0x{off:x}: {found.get(off)}")

    print("\n== DYNAMIC TAGS ==")
    for s in e.iter_segments():
        if s['p_type']=='PT_DYNAMIC':
            for t in s.iter_tags():
                if t.entry.d_tag in ('DT_INIT','DT_JMPREL','DT_PLTRELSZ','DT_PLTREL','DT_SYMTAB','DT_STRTAB','DT_RELA','DT_RELASZ'):
                    print(t.entry.d_tag, hex(int(t.entry.d_val)) if isinstance(t.entry.d_val,int) else t.entry.d_val)
