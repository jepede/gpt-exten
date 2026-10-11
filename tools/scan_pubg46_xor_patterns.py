#!/usr/bin/env python3
import sys,json,hashlib,struct
from pathlib import Path
import numpy as np
from elftools.elf.elffile import ELFFile

P=Path(sys.argv[1]); OUT=Path(sys.argv[2]); OUT.mkdir(parents=True,exist_ok=True)
raw=P.read_bytes(); a=np.frombuffer(raw,dtype=np.uint8)
# Adjacent XOR is invariant under per-region single-byte XOR.
diff=np.bitwise_xor(a[:-1],a[1:]).tobytes()

patterns={
"static0":b"xG2qW5lP7lV2iN5fN5pG",
"static16":b"rT6aQ6oZ1yM0gO5tO1aN",
"static19_method50":b"wD2rP3lP9xF4mE1eC5jS",
"static20":b"rG0lR2rZ5vM6mW5lM1rR",
"static21":b"fO3kW1fE6eD0pU1kY7xK",
"dyn37":b"46e490567d02cdb312b3",
"dyn38":b"f838b560ec26d4ba67fd",
"dyn42":b"56eed0401753d9e5ee86",
"dyn43":b"5412cc837199fa08d229",
"dyn44":b"48750e47caff0540e2ee",
"global":b"48ea7d82db9995f2",
"alt19":b"c44d833f54ba436f",
}
# SM4 SBOX prefix enough to identify a page-XOR copy.
patterns["sm4_sbox32"]=bytes([
0x34,0x66,0x25,0x74,0x89,0x78,0xE4,0xA9,0x5A,0x41,0xBC,0x7A,0xD6,0x16,0x21,0x23,
0x4D,0x61,0xDA,0x94,0x9B,0xDF,0x13,0x3C,0x69,0x3A,0x31,0x0A,0x5F,0xD7,0x99,0x95])
CK=[
0x000EB92B,0x3A0AE783,0x9E3B5C67,0xADDBDABF,0x7B7484CB,0x49156C63,0xC79AB5E7,0x79EC9CFF,
0x1725BEAB,0x2FB89CA3,0x24808AD7,0xDDD28B1F,0x4740DA4B,0xBBC3EA73,0x247B30E7,0x91BE385F]
patterns["sm4_ck64_le"]=b"".join(struct.pack("<I",x) for x in CK)
patterns["sm4_ck64_be"]=b"".join(struct.pack(">I",x) for x in CK)

with P.open("rb") as f:
 e=ELFFile(f); segs=[]
 for s in e.iter_segments():
  if s["p_type"]=="PT_LOAD":
   segs.append((int(s["p_offset"]),int(s["p_filesz"]),int(s["p_vaddr"]),int(s["p_flags"])))
def off2va(o):
 for off,sz,va,fl in segs:
  if off<=o<off+sz:return va+(o-off)
 return None

def find_invariant(pat):
 d=bytes([pat[i]^pat[i+1] for i in range(len(pat)-1)])
 hits=[]; pos=0
 while True:
  i=diff.find(d,pos)
  if i<0:break
  k=raw[i]^pat[0]
  enc=raw[i:i+len(pat)]
  if bytes(x^k for x in enc)==pat:
   hits.append({"off":i,"va":off2va(i),"xor":k,"enc_hex":enc.hex()})
  pos=i+1
  if len(hits)>=200:break
 return hits

res={}
for name,p in patterns.items():
 res[name]=find_invariant(p)

# For any hit, dump an aligned neighborhood both raw and XOR-decoded by hit key.
neighborhoods=[]
for name,hits in res.items():
 for h in hits[:30]:
  off=h["off"]; k=h["xor"]; base=off & ~0xfff
  lo=max(0,off-0x200); hi=min(len(raw),off+0x400)
  dec=bytes(x^k for x in raw[lo:hi])
  printable="".join(chr(x) if 32<=x<127 else "." for x in dec)
  neighborhoods.append({
   "name":name,"off":off,"va":h["va"],"xor":k,"page_off":base,
   "context_lo":lo,"decoded_hex":dec.hex(),"decoded_ascii":printable
  })

# Aggregate hit keys/pages: useful for whole-page protector inference.
key_counts={}
page_counts={}
for name,hits in res.items():
 for h in hits:
  key_counts[str(h["xor"])]=key_counts.get(str(h["xor"]),0)+1
  page=f"0x{h['off']&~0xfff:x}:xor=0x{h['xor']:02x}"
  page_counts[page]=page_counts.get(page,0)+1

out={"sha256":hashlib.sha256(raw).hexdigest(),"patterns":res,"key_counts":key_counts,"page_counts":page_counts,"neighborhoods":neighborhoods}
(OUT/"xor_scan.json").write_text(json.dumps(out,indent=2),encoding="utf-8")
with (OUT/"xor_report.txt").open("w",encoding="utf-8") as w:
 w.write(f"sha256={out['sha256']}\n")
 w.write("== HITS ==\n")
 for n,h in res.items():w.write(f"{n}: {h}\n")
 w.write("\n== XOR KEY COUNTS ==\n"+json.dumps(key_counts,indent=2)+"\n")
 w.write("\n== PAGE COUNTS ==\n"+json.dumps(page_counts,indent=2)+"\n")
 w.write("\n== DECODED CONTEXTS ==\n")
 for n in neighborhoods:
  w.write(f"\n-- {n['name']} off=0x{n['off']:x} va={n['va']} xor=0x{n['xor']:02x} --\n")
  w.write(n["decoded_ascii"]+"\n")
print("done")
