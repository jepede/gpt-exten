#!/usr/bin/env python3
"""Validate fixed XOR byte mask E2 on original ARM64 code and encoded UE4 strings.
This is static analysis only. No app execution, no memory modification in processes.
"""
import bisect,collections,json,math,mmap,re,struct,subprocess,sys
from pathlib import Path
elf=Path(sys.argv[1]);outdir=Path(sys.argv[2]);outdir.mkdir(parents=True,exist_ok=True)
with elf.open("rb") as f:
 m=mmap.mmap(f.fileno(),0,access=mmap.ACCESS_READ)
 _,_,machine,_,_,phoff,shoff,_,_,phentsize,phnum,shentsize,shnum,shidx=struct.unpack_from("<16sHHIQQQIHHHHHH",m,0)
 assert machine==183
 secs=[]
 for i in range(shnum):
  sh=struct.unpack_from("<IIQQQQIIQQ",m,shoff+i*shentsize)
  secs.append(dict(idx=i,n=sh[0],type=sh[1],flags=sh[2],va=sh[3],foff=sh[4],size=sh[5]))
 shstr=secs[shidx];names=m[shstr["foff"]:shstr["foff"]+shstr["size"]]
 for s in secs:
  i=s["n"];j=names.find(b"\0",i)
  s["name"]=names[i:j].decode("ascii","replace") if j>i else ""
 text=next(s for s in secs if s["name"]==".text")
 eh=next(s for s in secs if s["name"]==".eh_frame_hdr")
 assert m[eh["foff"]:eh["foff"]+4]==b"\x01\x1b\x03\x3b"
 n=struct.unpack_from("<I",m,eh["foff"]+8)[0]
 starts=[eh["va"]+struct.unpack_from("<i",m,eh["foff"]+12+8*i)[0] for i in range(n)]
 assert starts==sorted(starts)
 poses=[]
 for v in [text["va"],text["va"]+0x20,text["va"]+0xA48,0xd1fbb60,0xd1fbb84]:
  poses.append((v,"manual"))
 for d in range(0,2*1024*1024,32768):
  v=text["va"]+d
  i=bisect.bisect_left(starts,v)
  if i<len(starts):poses.append((starts[i],f"early-{d//32768}"))
 for i in range(48):
  v=text["va"]+(i*text["size"])//48
  j=bisect.bisect_left(starts,v)
  if j<len(starts):poses.append((starts[j],f"spread-{i}"))
 poses=sorted(set(poses))
 payloads={0:bytearray(),0xe2:bytearray()}
 stride=256
 for addr,tag in poses:
  pos=text["foff"]+addr-text["va"]
  assert 0<=pos<len(m)-128
  data=bytes(m[pos:pos+128])
  payloads[0].extend(data+bytes(stride-len(data)))
  payloads[0xe2].extend(bytes(x^0xe2 for x in data)+bytes(stride-len(data)))
 for mask,data in payloads.items():
  (outdir/f"sample_{mask:02x}.bin").write_bytes(data)
 def decode(mask):
  commands=["e scr.color=false","e asm.lines=false"]
  for i in range(len(poses)):
   commands.append(f"pdj 32 @ 0x{i*stride:x}")
  commands.append("q")
  cmd=["r2","-q","-a","arm","-b","64","-e","scr.color=false","-c",";".join(commands),str(outdir/f"sample_{mask:02x}.bin")]
  p=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,encoding="utf8",errors="replace",timeout=360)
  arrays=[]
  for line in p.stdout.splitlines():
   line=line.strip()
   if line.startswith("["):
    try:
     j=json.loads(line)
     if isinstance(j,list):arrays.append(j)
    except:pass
  return p,arrays
 all_results={}
 for mask in [0,0xe2]:
  p,rows=decode(mask)
  all_results[mask]=(p,rows)
  print("BATCH",hex(mask),"rc",p.returncode,"windows",len(rows),flush=True)
 def ratio(arr):
  if not arr:return [0,0]
  bad=sum(1 for v in arr if "invalid" in str(v.get("opcode","")).lower() or v.get("type")=="ill")
  return [bad,len(arr)]
 result={"file":elf.name,"section":text,"eh_frame_hdr_count":n,"mask":0xe2,"window_count":len(poses),"samples":[],"string_search":{}}
 cnt=collections.Counter()
 for i,(addr,tag) in enumerate(poses):
  origin=all_results[0][1][i] if i<len(all_results[0][1]) else []
  decoded=all_results[0xe2][1][i] if i<len(all_results[0xe2][1]) else []
  bad0,n0=ratio(origin);bad1,n1=ratio(decoded)
  if bad1<=2 and bad0>=20: cls="xor_e2"
  elif bad0<=2 and bad1>=20: cls="plaintext"
  else:cls="mixed_or_unknown"
  cnt[cls]+=1
  row={"address":hex(addr),"tag":tag,"status":cls,"invalid_original":f"{bad0}/{n0}","invalid_xor_e2":f"{bad1}/{n1}"}
  if tag=="manual":
   row["original_first"]=[x.get("opcode") for x in origin[:10]]
   row["xor_e2_first"]=[x.get("opcode") for x in decoded[:14]]
  result["samples"].append(row)
  if tag=="manual" or i%5==0:
   print("XOR_TEST",row,flush=True)
 print("SUMMARY",dict(cnt),flush=True)
 for s in secs:
  if s["name"] not in (".text",".rodata",".dynstr",".data.rel.ro"):continue
  start=s["foff"];end=min(start+s["size"],len(m))
  if start>=end:continue
  sample=m[start:min(end,start+131072)]
  count=collections.Counter(sample)
  name=s["name"]
  result["string_search"][name]={"most_common_bytes":count.most_common(10),"searches":{}}
  print("SECTION",name,"freq",count.most_common(7),flush=True)
  for name_token in ("FVector","FTransform","RelativeLocation","ComponentToWorld","USceneComponent",
        "GetActorLocation","SetActorLocation","GWorld","bEncrypted","FEncVector","/Script/Engine",
        "NC_BP_DFMCharacter_C","Decrypt","Encrypt","UObject","Actor"):
   raw=name_token.encode(); enc=bytes(b^0xe2 for b in raw)
   matched=[]
   for label,token in [("plain",raw),("xor_e2",enc)]:
    i=m.find(token,start,end); hits=[]
    while i>=0 and len(hits)<12:
     hits.append(hex(i));i=m.find(token,i+len(token),end)
    matched.append((label,hits))
   result["string_search"][s["name"]]["searches"][name_token]={k:v for k,v in matched}
   if matched[1][1]:print("XOR_STRING",s["name"],name_token,matched[1][1],flush=True)
 (outdir/"xor_e2_probe.json").write_text(json.dumps(result,indent=2,ensure_ascii=False))
 m.close()
