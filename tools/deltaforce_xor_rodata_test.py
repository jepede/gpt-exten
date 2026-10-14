#!/usr/bin/env python3
"""Check whether XOR E2 also masks .rodata; compare raw and decoded names.
Read-only. Never infer coordinate encryption from string protection.
"""
import sys, json, mmap, struct, hashlib, collections, math
from pathlib import Path

SO=Path(sys.argv[1])
ROOT=Path("reports/deltaforce_rodata")
ROOT.mkdir(parents=True,exist_ok=True)
TERMS=[
"USceneComponent","AActor","UWorld","FVector","FTransform","FEncVector",
"FEncHandler","bEncrypted","SetRelativeLocation","GetActorLocation",
"SetActorLocation","K2_GetActorLocation","GetComponentLocation","ComponentToWorld",
"RelativeLocation","RelativeRotation","RelativeScale3D","ReplicatedMovement",
"NetSerialize","GWorld","/Script/Engine","/Script/CoreUObject",
"UObject","FName","FMatrix","FQuat","NC_BP_DFMCharacter_C",
"Encrypt","Decrypt","Location","Transform","PlayerController","SkeletalMesh",
"WorldPosition","ActorLocation","NetQuantize","xorshift","AES","SM4"
]
def hashbuf(x):
 return hashlib.sha256(x).hexdigest()
def stats(x):
 c=collections.Counter(x)
 return {"bytes":len(x),"top12":[[hex(k),v] for k,v in c.most_common(12)],
  "ascii_printable_ratio":round(sum(32<=v<=126 for v in x)/len(x),5),
  "zero_count":c.get(0,0),"e2_count":c.get(0xe2,0)}
def hits(hay,needle,limit=12):
 pos=0;result=[];total=0
 while True:
  i=hay.find(needle,pos)
  if i<0:break
  total+=1
  if len(result)<limit:
   left=max(0,i-16);right=min(len(hay),i+len(needle)+36)
   ctx=hay[left:right].replace(b"\x00",b"|").decode("ascii","backslashreplace")
   result.append({"section_offset":hex(i),"context":ctx[:150]})
  pos=i+max(1,len(needle))
 return {"count":total,"first":result}
def strings_sample(data):
 # ASCII \x20-\x7e at least 5, bounded to top 60 samples
 import re
 result=[]
 for m in re.finditer(rb"[\x20-\x7e]{8,}",data):
  val=m.group().decode("ascii","replace")
  if len(val)>400:val=val[:400]
  if len(result)<60:result.append({"off":hex(m.start()),"text":val[:200]})
  if len(result)==60:break
 return result
with SO.open("rb") as f:
 hdr=f.read(64)
 vals=struct.unpack("<16sHHIQQQIHHHHHH",hdr)
 ident,etype,machine,ev,entry,phoff,shoff,flags,ehsize,phentsize,phnum,shentsize,shnum,shstrndx=vals
 assert ident[:6]==b"\x7fELF\x02\x01" and machine==183
 secs=[]
 for i in range(shnum):
  f.seek(shoff+i*shentsize)
  nam,typ,sflags,addr,off,size,link,info,align,entsize=struct.unpack("<IIQQQQIIQQ",f.read(64))
  secs.append({"nameoff":nam,"addr":addr,"off":off,"size":size,"typ":typ})
 sh=secs[shstrndx];f.seek(sh["off"]);names=f.read(sh["size"])
 for s in secs:
  k=s["nameoff"]
  s["name"]=names[k:names.find(b"\0",k)].decode("utf8","replace") if k<len(names) else "?"
 mm=mmap.mmap(f.fileno(),0,access=mmap.ACCESS_READ)
 selected=[s for s in secs if s["name"] in (".rodata",".dynstr",".gcc_except_table",".data.rel.ro",".data")]
 result={}
 for s in selected:
  start=s["off"];sz=s["size"]
  blob=bytes(mm[start:start+sz])
  plain=blob.translate(bytes([i ^ 0xe2 for i in range(256)]))
  is_cand=s["name"]==".rodata"
  row={"section":s,"raw_sha256":hashbuf(blob),"e2_sha256":hashbuf(plain),
       "raw_stats":stats(blob),"xor_stats":stats(plain)}
  if is_cand:
   row["raw_term_counts"]={k:hits(blob,k.encode(),3) for k in TERMS}
   row["e2_term_counts"]={k:hits(plain,k.encode(),5) for k in TERMS}
   row["raw_utf16_terms"]={k:hits(blob,k.encode("utf-16le"),2) for k in TERMS}
   row["e2_utf16_terms"]={k:hits(plain,k.encode("utf-16le"),3) for k in TERMS}
   row["raw_ascii_sample"]=strings_sample(blob[:min(len(blob),5_000_000)])
   row["e2_ascii_sample"]=strings_sample(plain[:min(len(plain),5_000_000)])
   (ROOT/"rodata_xor_e2.bin").write_bytes(plain)
   print("RODATA_XOR_E2",{"unmasked_size":len(plain),
             "unmasked_sha256":row["e2_sha256"],
             "name_matches":{k:v["count"] for k,v in row["e2_term_counts"].items() if v["count"]>0},
             "first_ascii":row["e2_ascii_sample"][:12]},flush=True)
  result[s["name"]]=row
  print("SECTION_STATS",s["name"],{"raw":row["raw_stats"],"xor":row["xor_stats"]},flush=True)
 report={"name":SO.name,"sha256":hashbuf(mm),"hypothesis":"E2 static file code mask, rodata independent test","sections":result}
 (ROOT/"rodata_scan.json").write_text(json.dumps(report,indent=2,ensure_ascii=False))
 lines=["# Delta Force ARM64 .rodata mask verification",
   "libUE4 SHA256: "+report["sha256"],"",
   "## Section-level raw versus XOR E2 byte distributions"]
 for name,row in result.items():
  lines+=["### "+name,"Raw: "+json.dumps(row["raw_stats"]),
     "XOR E2: "+json.dumps(row["xor_stats"])]
 r=result.get(".rodata",{})
 if r:
  lines+=["","## Raw vs E2-decoded UE4 named strings"]
  for term in TERMS:
   a=r["raw_term_counts"][term]["count"]
   b=r["e2_term_counts"][term]["count"]
   ca=r["raw_utf16_terms"][term]["count"]
   cb=r["e2_utf16_terms"][term]["count"]
   lines.append(f"- {term}: raw ASCII={a}, XOR ASCII={b}, raw UTF16={ca}, XOR UTF16={cb}")
  lines+=["","## Decoded ASCII examples (first 60 in .rodata)"]
  for row in r["e2_ascii_sample"]: lines.append(row["off"]+" "+row["text"])
  lines+=["","## Coordinate target addresses (VA = .rodata VA + section offset)"]
  for k,v in r["e2_term_counts"].items():
   if v["count"]:
    for h in v["first"][:5]:
     va=r["section"]["addr"]+int(h["section_offset"],16)
     lines.append(f"- {k} @ {hex(va)} :: {h['context']}")
 (ROOT/"rodata_scan.md").write_text("\n".join(lines)+"\n")
 print("MASK_TEST_DONE",flush=True)
 mm.close()
