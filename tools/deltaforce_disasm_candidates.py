#!/usr/bin/env python3
"""Bounded manual disassembly of candidate coordinate accessors and a historical offset."""
import argparse,re,subprocess,sys
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument("elf");p.add_argument("scan");p.add_argument("output");args=p.parse_args()
scan=Path(args.scan).read_text()
matches=[]
for line in scan.splitlines():
 if not line.startswith("CANDIDATE "):continue
 m=re.search(r"CANDIDATE\s+(\S+)\s+(0x[0-9a-f]+).*?off=0x([0-9a-f]+).*?fde=(0x[0-9a-f]+).*?next_fde=(0x[0-9a-f]+)",line)
 if not m:continue
 kind,addr,off,fde,end=m.groups()
 matches.append((kind,int(addr,16),int(off,16),int(fde,16),int(end,16)))
chosen=[(0x0d1fbb84,"historic old-version offset",60)]
used={0x0d1fbb84}
for kind,addr,off,start,end in matches:
 if len(chosen)>=17:break
 if addr in used:continue
 chosen.append((addr,f"{kind}, member offset +0x{off:x}, possible unwind entry 0x{start:x}",30))
 used.add(addr)
commands=["e scr.color=false","e asm.lines=false","e asm.bytes=true","e asm.comments=false"]
for addr,note,lines in chosen:
 # avoid invoking full-file aaa analysis on the large ELF
 commands.append(f"pd {lines} @ 0x{addr:x}")
commands.append("q")
process=subprocess.run(["r2","-q","-e","scr.color=false","-c",";".join(commands),args.elf],
  text=True,errors="replace",stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=220)
output="# Deep candidate r2 disassembly\n\n"
output+="No full-file analysis; disassembly at bounded candidate addresses only.\n\n"
output+="## Address manifest\n\n"
for addr,note,lines in chosen:output+=f"- 0x{addr:x}: {note}, requested {lines} instructions\n"
output+="\n## radare2 output\n\n"+process.stdout[:170000]+"\n"
Path(args.output).write_text(output)
print("RADARE2 rc:",process.returncode,"candidate_count:",len(chosen),flush=True)
print("RADARE2 output excerpt:\n",process.stdout[:20000],flush=True)
