#!/usr/bin/env python3
"""Recover ARM64 string address references in an ELF; read-only."""
import struct,mmap,json,sys,collections
from pathlib import Path
p=Path(sys.argv[1]); o=Path("reports/hok")
o.mkdir(parents=True,exist_ok=True)
terms=["VInt3","VInt2","PositionRecorderUnit","SyncPositionMoveCmd","GameGridFow","Vector3Serializer","Position","Transform","FrameSync","main_hero_location","Fixed"]
with p.open("rb") as f:
 m=mmap.mmap(f.fileno(),0,access=mmap.ACCESS_READ)
 h=struct.unpack_from("<16sHHIQQQIHHHHHH",m)
 _,_,_,_,_,_,shoff,_,_,_,_,sz,n,stridx=h
 s=[struct.unpack_from("<IIQQQQIIQQ",m,shoff+i*sz) for i in range(n)]
 ns=s[stridx];names=m[ns[4]:ns[4]+ns[5]]
 sections={names[q[0]:names.find(b"\0",q[0])].decode("ascii","replace"):q for q in s}
 txt,ro=sections[".text"],sections[".rodata"]
 data=m[ro[4]:ro[4]+ro[5]]
 pag=collections.defaultdict(list); string_addresses={}
 for k in terms:
  x=k.encode();hits=[];at=0
  while len(hits)<120:
   idx=data.find(x,at)
   if idx<0:break
   va=ro[3]+idx
   hits.append(va);pag[va&~4095].append((va,k))
   at=idx+len(x)
  string_addresses[k]=[hex(i) for i in hits]
 refs=[];seen=set()
 def sx(v,b):return v-(1<<b) if v&(1<<(b-1)) else v
 inst=memoryview(m)[txt[4]:txt[4]+txt[5]]
 for i in range(0,len(inst)-64,4):
  w=struct.unpack_from("<I",inst,i)[0];pc=txt[3]+i
  if w&0x9f000000!=0x90000000:continue
  imm=(((w>>5)&0x7ffff)<<2)|((w>>29)&3)
  pg=(pc&~4095)+(sx(imm,21)<<12)
  opts=pag.get(pg)
  if not opts:continue
  reg=w&31
  for j in range(i+4,i+52,4):
   q=struct.unpack_from("<I",inst,j)[0];v=None;kind=""
   if q&0xff000000==0x91000000 and ((q>>5)&31)==reg:
    v=pg+(((q>>10)&4095)<<(12 if q&(1<<22) else 0));kind="add"
   elif q&0xffc00000==0xf9400000 and ((q>>5)&31)==reg:
    v=pg+(((q>>10)&4095)<<3);kind="ldr"
   if v is not None:
    for adr,k in opts:
     key=(pc,j,v,k)
     if adr==v and key not in seen:
      refs.append({"pc":hex(pc),"use":hex(txt[3]+j),"name":k,"target":hex(v),"kind":kind})
      seen.add(key)
   if q&0xfc000000==0x14000000 or q&0xfffffc1f==0xd65f0000:break
 inst.release();m.close()
report={"rodata_start":hex(ro[3]),"text_start":hex(txt[3]),"names":string_addresses,"xref_count":len(refs),"xrefs":refs[:2000]}
(o/"coordinate_xref.json").write_text(json.dumps(report,indent=2))
print("XREF_RESULT",json.dumps({"name_hits":{k:len(v) for k,v in string_addresses.items()},"ref_counts":dict(collections.Counter(v['name'] for v in refs)),"examples":refs[:65]}),flush=True)
