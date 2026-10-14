#!/usr/bin/env python3
"""Generate exact decoded .rodata C-string and substring VA targets for ARM64 XREF."""
import json, mmap, re, struct, sys, hashlib
from pathlib import Path
SO=Path(sys.argv[1]); ROOT=Path("reports/deltaforce_ref_xrefs");ROOT.mkdir(parents=True,exist_ok=True)
search=[
  "FEncVector","FEncHandler","bEncrypted","EncLocation","EncRotation","EncScale",
  "RelativeLocation","GetActorLocation","GetComponentLocation",
  "SetRelativeLocation","SetActorLocation","ComponentToWorld",
  "SetWorldLocation","GetWorldLocation","GetRelativeLocation",
  "NetSerialize","K2_GetActorLocation","DecryptPosition","CoordDecrypt"
]
with SO.open("rb") as fd:
 vals=struct.unpack("<16sHHIQQQIHHHHHH",fd.read(64))
 ident,etype,machine,version,entry,phoff,shoff,flags,ehsize,phentsize,phnum,shentsize,shnum,shstrndx=vals
 assert ident[:6]==b"\x7fELF\x02\x01" and machine==183
 sh=[]
 for i in range(shnum):
  fd.seek(shoff+i*shentsize)
  n,t,flags,va,off,size,lk,inf,align,entsize=struct.unpack_from("<IIQQQQIIQQ",fd.read(shentsize))
  sh.append((n,va,off,size))
 n,va,off,size=sh[shstrndx];fd.seek(off);strtab=fd.read(size)
 sec={}
 for no,address,offs,ssize in sh:
  name=strtab[no:strtab.find(b"\0",no)].decode("ascii","replace")
  sec[name]=(address,offs,ssize)
 rva,roff,rsize=sec[".rodata"]
 fd.seek(roff);raw=fd.read(rsize)
 data=raw.translate(bytes(i^0xe2 for i in range(256)))
 matches=[]
 for hit in re.finditer(rb"[\x20-\x7e]{5,}\x00",data):
  val=hit.group()[:-1].decode("ascii","replace")
  keywords=[x for x in search if x.lower() in val.lower()]
  if not keywords:continue
  if len(val)>1200:continue
  offset=hit.start()
  matches.append({"va":hex(rva+offset),"section_offset":hex(offset),
    "text":val,"keywords":keywords})
 # Search any hit regardless of Cstring framing; compiled code may contain merged/suffix symbols.
 for needle in search:
  encoded=needle.encode()
  cur=0
  while True:
   i=data.find(encoded,cur)
   if i<0:break
   # no extra row if this address is already the start of an existing string
   matches.append({"va":hex(rva+i),"section_offset":hex(i),
      "text":"SUBSTR:"+needle,"keywords":[needle]})
   cur=i+len(encoded)
 unique={}
 for item in matches:
  k=item["va"]
  if k in unique:
   old=unique[k]
   old["keywords"]=list(dict.fromkeys(old["keywords"]+item["keywords"]))
  else:unique[k]=item
 matches=sorted(unique.values(),key=lambda x:int(x["va"],16))
 with (ROOT/"target_strings.tsv").open("w") as out:
  for row in matches:
   label=",".join(row["keywords"])+" "+row["text"].replace("\t"," ").replace("\n"," ")[:220]
   out.write(row["va"]+"\t"+label+"\n")
 (ROOT/"target_strings.json").write_text(json.dumps({"rodata_va":hex(rva),"rodata_size":rsize,
   "mask":hex(0xe2),"target_count":len(matches),"strings":matches[:4000]},indent=2,ensure_ascii=False))
 print("RODATA_CSTRING_TARGETS",len(matches),flush=True)
 for k in ["FEncVector","FEncHandler","bEncrypted","EncLocation","GetActorLocation"]:
  rows=[x for x in matches if k in x["keywords"] and not x["text"].startswith("SUBSTR:")]
  print("TARGETS",k,json.dumps(rows[:30],ensure_ascii=False),flush=True)
