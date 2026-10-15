#!/usr/bin/env python3
"""Delta Force UE4 ARM64: recover Android APS2 relocations and cross-reference masked UE metadata.
Read-only. Addresses are ELF relative VAs, not runtime ASLR addresses.
"""
import bisect,collections,hashlib,json,mmap,struct,sys,time,zipfile
from pathlib import Path
APK=Path(sys.argv[1])
ROOT=Path("reports/deltaforce_aps2");ROOT.mkdir(parents=True,exist_ok=True)
SO=Path("work/research/libUE4.so")
SO.parent.mkdir(parents=True,exist_ok=True)
NAME="lib/arm64-v8a/libUE4.so"
EXPECT="387cd911a67eca1069bd5e4c874bce5dfb14823ca75f55f1ae7c43a09f2f1441"
if not SO.exists() or SO.stat().st_size!=566193496:
 with zipfile.ZipFile(APK) as z:
  assert NAME in z.namelist()
  with z.open(NAME) as fi,SO.open("wb") as fo:
   for b in iter(lambda:fi.read(8<<20),b""):fo.write(b)
h=hashlib.sha256()
with SO.open("rb") as fd:
 for b in iter(lambda:fd.read(16<<20),b""):h.update(b)
assert h.hexdigest()==EXPECT,(h.hexdigest(),EXPECT)
print("LIBUE4_VERIFIED",EXPECT,flush=True)
def parse_sections(mm):
 head=struct.unpack_from("<16sHHIQQQIHHHHHH",mm,0)
 ident,etype,machine,version,entry,phoff,shoff,flags,ehsize,phentsize,phnum,shentsize,shnum,shstrndx=head
 assert ident[:6]==b"\x7fELF\x02\x01" and machine==183
 sh=[]
 for i in range(shnum):
  n,t,f,va,off,size,l,inf,al,es=struct.unpack_from("<IIQQQQIIQQ",mm,shoff+i*shentsize)
  sh.append(dict(nameoff=n,type=t,flags=f,va=va,off=off,size=size))
 meta=sh[shstrndx]
 names=mm[meta["off"]:meta["off"]+meta["size"]]
 for s in sh:
  p=s["nameoff"]
  s["name"]=names[p:names.find(b"\x00",p)].decode("ascii","replace")
 ph=[]
 for i in range(phnum):
  typ,f,off,va,paddr,fs,ms,al=struct.unpack_from("<IIQQQQQQ",mm,phoff+i*phentsize)
  if typ==1:ph.append(dict(va=va,off=off,filesz=fs,flags=f))
 return {s["name"]:s for s in sh},ph
def uleb_signed(src,start):
 shift=0;n=0
 for i in range(10):
  b=src[start+i]
  n|=(b&127)<<shift;shift+=7
  if not b&128:
   if b&64:n-=1<<shift
   return n,start+i+1
 raise RuntimeError("SLEB128 >10 bytes")
def info_va(va,ph):
 for q in ph:
  if q["va"]<=va<q["va"]+q["filesz"]:
   return q["off"]+va-q["va"]
 return None
with SO.open("rb") as fd:
 mm=mmap.mmap(fd.fileno(),0,access=mmap.ACCESS_READ)
 sect,ph=parse_sections(mm)
 r=sect[".rodata"]
 decode=mm[r["off"]:r["off"]+r["size"]].translate(bytes(i^0xe2 for i in range(256)))
 key_terms=["FEncVector","FEncHandler","bEncrypted","GetActorEncLocation","GetComponentEncLocation","HasSameInfoWithEncLocation","LastFrameEncLocation","RelativeLocation","GetActorLocation","GetComponentLocation","ComponentToWorld"]
 names={}
 labels=collections.defaultdict(list)
 for term in key_terms:
  x=term.encode();p=0;found=[]
  while len(found)<160:
   at=decode.find(x,p)
   if at<0:break
   va=r["va"]+at
   found.append(va);labels[va].append(term)
   p=at+len(x)
  names[term]=[hex(x) for x in found]
 all_targets=set(labels)
 print("TARGET_STRINGS",json.dumps({k:{"count":len(v),"sample":v[:8]} for k,v in names.items()}),flush=True)
 aps=sect[".rela.dyn"];raw=mm[aps["off"]:aps["off"]+aps["size"]]
 print("PACKED_RELA",aps,"FIRST16",raw[:16].hex(),flush=True)
 report={"ELF_sha256":EXPECT,"sections":{k:sect[k] for k in (".text",".rodata",".rela.dyn",".data.rel.ro",".data",".dynamic")},
         "targets":names,"APS2_magic":raw[:4].hex(),"APS2_prefix":raw[:36].hex()}
 # raw 8-byte VA references; null if stored by reloc only
 rawrefs=[]
 for term in key_terms[:7]:
  for va in [int(x,16) for x in names[term]][:8]:
   pat=struct.pack("<Q",va)
   p=0
   while len(rawrefs)<1000:
    at=mm.find(pat,p)
    if at<0:break
    rawrefs.append(dict(name=term,target_va=hex(va),raw_file_offset=hex(at)))
    p=at+8
 report["raw_pointer_occurrences"]=rawrefs
 summary=collections.Counter();group_types=collections.Counter();hit=[];saved=[]
 prefix_ok=(raw[:4]==b"APS2")
 if prefix_ok:
  pos=4
  try:
   count,pos=uleb_signed(raw,pos)
   off,pos=uleb_signed(raw,pos)
   addend=0;info=0;scanned=0;limit=17000000
   prev_off=off
   last_bump=0
   while scanned<count and scanned<limit:
    grsz,pos=uleb_signed(raw,pos)
    flags,pos=uleb_signed(raw,pos)
    if grsz<=0 or grsz>count-scanned or flags<0 or flags>15:raise ValueError("Invalid group size/flags "+str((grsz,flags,scanned,pos)))
    group_types[flags]+=1
    if flags&2:delta,pos=uleb_signed(raw,pos)
    if flags&1:info,pos=uleb_signed(raw,pos)
    if flags&8 and flags&4: d,pos=uleb_signed(raw,pos);addend+=d
    for j in range(grsz):
     if flags&2:off+=delta
     else:d,pos=uleb_signed(raw,pos);off+=d
     if not flags&1:info,pos=uleb_signed(raw,pos)
     if flags&8:
      if not flags&4: d,pos=uleb_signed(raw,pos);addend+=d
     else:addend=0
     info64=info&0xffffffffffffffff
     typ=info64&0xffffffff
     sym=info64>>32
     summary[typ]+=1
     if (len(saved)<24):saved.append(dict(offset=hex(off),type=typ,sym=sym,addend=hex(addend&0xffffffffffffffff)))
     if typ==1027 and addend in all_targets:
      hit.append(dict(place_va=hex(off),data_va=hex(addend),label=labels[addend],rtype=typ,sym=sym,group_flag=flags))
     if off<prev_off and len(hit)<100:hit.append({"WARNING":"non-monotonic offset","off":hex(off)})
     prev_off=off
     scanned+=1
   report["APS2"]={"total_encoded":count,"parsed":scanned,"consumed_bytes":pos,"of_bytes":len(raw),"last_offset":hex(off),
      "types":dict(summary),"group_flags":dict(group_types),"first_relocs":saved,"string_pointer_hits":hit[:2000]}
  except Exception as e:
   report["APS2_error"]=str(e);print("APS2_PARSE_ERROR",str(e),flush=True)
 else:
  report["APS2_error"]="Non APS2 header, cannot parse with APS2 decoder"
 print("APS2_RESULTS",json.dumps(report.get("APS2",{}))[:17000],flush=True)
 # Gather nearest relocation addresses around target hits to identify registrar entries.
 if "APS2" in report and hit:
  target_place=[int(x["place_va"],16) for x in hit if "place_va" in x]
  bucket=set()
  for x in target_place:
   for t in range((x-0xa0)&~7,x+0xa8,8):bucket.add(t)
  rels=[]
  pos=4;count,pos=uleb_signed(raw,pos);off,pos=uleb_signed(raw,pos);addend=0;info=0;done=0
  while done<count and done<17000000:
   n,pos=uleb_signed(raw,pos);flags,pos=uleb_signed(raw,pos)
   if flags&2:delta,pos=uleb_signed(raw,pos)
   if flags&1:info,pos=uleb_signed(raw,pos)
   if flags&8 and flags&4:d,pos=uleb_signed(raw,pos);addend+=d
   for _ in range(n):
    if flags&2:off+=delta
    else:d,pos=uleb_signed(raw,pos);off+=d
    if not flags&1:info,pos=uleb_signed(raw,pos)
    if flags&8:
     if not flags&4:d,pos=uleb_signed(raw,pos);addend+=d
    else:addend=0
    if off in bucket:
     loc=info_va(off,ph)
     rels.append(dict(place=hex(off),rtype=int(info&0xffffffff),pointsto=hex(addend&0xffffffffffffffff),
          target_strings=labels.get(addend,[]),on_disk_word=mm[loc:loc+8].hex() if loc is not None else None))
    done+=1
  report["reloc_near_string_hits"]=rels[:5000]
  print("NEARBY_RELOCATIONS",json.dumps(rels[:160]),flush=True)
 # Scan static sorted data sections for VA fragments; may be represented as masking or packed small ints.
 for name in (".data.rel.ro",".data"):
  s=sect[name]
  data=mm[s["off"]:s["off"]+s["size"]]
  results=[]
  for term in key_terms[:7]:
   for tgt in names[term][:4]:
    addr=int(tgt,16);value=struct.pack("<Q",addr)
    p=0
    while len(results)<250:
     i=data.find(value,p)
     if i<0:break
     results.append({"name":term,"place_va":hex(s["va"]+i),"pointer_value":tgt})
     p=i+8
  report["raw_data_references_"+name]=results
 mm.close()
(ROOT/"relocation_evidence.json").write_text(json.dumps(report,indent=2,ensure_ascii=False))
 lines=["# Delta Force libUE4 relocated metadata pointers","","ELF SHA256: "+EXPECT,
  "Source: APK original verified; no target process memory is accessed.",
  "Android packed relocation magic: "+report["APS2_magic"],"",
  "## Decoded metadata targets"]
 for k,v in names.items():lines.append("* "+k+": "+str(len(v))+" -> "+", ".join(v[:20]))
 lines+=["","## APS2 relocation summary","",json.dumps(report.get("APS2",{"error":report.get("APS2_error","?")}),indent=2)[:19000]]
 lines+=["","## Nearby relocation records","",json.dumps(report.get("reloc_near_string_hits",[]),indent=2)[:33000]]
 (ROOT/"relocation_evidence.md").write_text("\n".join(lines)+"\n")
 print("RELO_ANALYSIS_COMPLETE",str(ROOT),flush=True)
