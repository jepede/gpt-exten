#!/usr/bin/env python3
"""HOK libGameCore.so AArch64 strict PC-relative code/string XREF.
No disassembly dependency for full scan. ADRP+ADD and ADRP+LDR/STR validated.
Source is the SHA256-pinned GameCore ELF extracted from existing cached Artifact.
"""
from pathlib import Path
import bisect,collections,json,mmap,struct,subprocess
p=Path("work/hok_cached/libGameCore.so"); assert p.exists()
out=Path("out/hok_gamecore_xref");out.mkdir(parents=True,exist_ok=True)
terms=[
 "ModifyEnemyInvisibleHeroPositionByTimeDynamic",
 "ModifyEnemyInvisibleHeroPosition","GetActorLogicPos","SetActorLogicPos",
 "real_location","modified_location","HeroPosition","GetHeroPosition",
 "ActorRoot","ActorPos","MoveDir","SyncPosition","CheckActorPos","HeroPos",
 "invisible_value_location","invisible2visible","HERO_POSITION_ENCRYPT_TYPE",
]
with p.open("rb") as f:
 m=mmap.mmap(f.fileno(),0,access=mmap.ACCESS_READ)
 h=struct.unpack_from("<16sHHIQQQIHHHHHH",m,0)
 assert h[0][:6]==b"\x7fELF\x02\x01" and h[2]==183
 shoff,shsize,shnum,shstr=h[6],h[11],h[12],h[13]
 headers=[]
 for j in range(shnum):
  z=struct.unpack_from("<IIQQQQIIQQ",m,shoff+j*shsize)
  headers.append({"nameoff":z[0],"type":z[1],"va":z[3],"off":z[4],"size":z[5]})
 st=headers[shstr]; stdata=m[st["off"]:st["off"]+st["size"]]
 for z in headers:
  i=z["nameoff"];e=stdata.find(b"\0",i)
  if i<len(stdata) and e>=i:z["name"]=stdata[i:e].decode("ascii","replace")
 sec={q["name"]:q for q in headers if "name" in q}
 code=sec[".text"];r=sec[".rodata"];eh=sec[".eh_frame_hdr"]
 start=code["off"];size=code["size"];vbase=code["va"]
 ro=m[r["off"]:r["off"]+r["size"]]
 targets={};by_page=collections.defaultdict(dict)
 for term in terms:
  needle=term.encode();pos=0
  while True:
   i=ro.find(needle,pos)
   if i<0:break
   string_start=ro.rfind(b"\0",max(0,i-350),i)+1
   end=ro.find(b"\0",i)
   if end<0 or end-string_start>480 or string_start>i:
    string_start=i;end=min(len(ro),i+len(needle)+150)
   s=ro[string_start:end]
   if sum(32<=x<127 for x in s)/max(1,len(s))>=0.77:
    val=s.decode("utf8","replace")
    for k in (string_start,i):
     va=r["va"]+k
     if va not in targets:targets[va]={"name":val,"terms":[]}
     if term not in targets[va]["terms"]:targets[va]["terms"].append(term)
     by_page[va&~4095][va]=targets[va]
   pos=i+len(needle)
 print("TARGET_COUNT",len(targets),"PAGES",len(by_page),flush=True)
 starts=[]
 hdr=m[eh["off"]:eh["off"]+12]
 if hdr[:4]==b"\x01\x1b\x03\x3b":
  count=struct.unpack_from("<I",hdr,8)[0]
  if 0<count<1600000:
   for j in range(count):
    d=struct.unpack_from("<i",m,eh["off"]+12+8*j)[0]
    x=eh["va"]+d
    if vbase<=x<vbase+size:starts.append(x)
 starts=sorted(set(starts))
 def fn(pc):
  i=bisect.bisect_right(starts,pc)-1
  if i>=0:return [hex(starts[i]),hex(starts[i+1]) if i+1<len(starts) else None]
  return []
 def sext(x,b):return x-(1<<b) if x>>(b-1) else x
 candidates=[]
 candidates_per_term=collections.Counter()
 cand_cap=2000
 counts={"raw":0,"xor_e2":0}
 for mode,mask in [("raw",0),("xor_e2",0xe2e2e2e2)]:
  for i in range(0,size-size%4,4):
   w=struct.unpack_from("<I",m,start+i)[0]^mask
   pc=vbase+i
   if (w&0x9f000000)==0x90000000:
    imm=((((w>>5)&0x7ffff)<<2)|((w>>29)&3))
    page=(pc&~4095)+(sext(imm,21)<<12)
    page_targets=by_page.get(page)
    if not page_targets:continue
    counts[mode]+=1
    reg=w&31
    for j in range(i+4,min(i+4*17,size-size%4),4):
     next_w=struct.unpack_from("<I",m,start+j)[0]^mask
     typ="";target=None
     if (next_w&0xff000000)==0x91000000 and ((next_w>>5)&31)==reg:
      offset=((next_w>>10)&4095)<<(12 if (next_w>>22)&1 else 0)
      target=page+offset
      typ="ADRP+ADD"
     elif (next_w&0xffc00000) in (0xf9400000,0xf9000000) and ((next_w>>5)&31)==reg:
      offset=((next_w>>10)&4095)<<3
      target=page+offset;typ="ADRP+LDR/STR_X"
     if target in page_targets:
      name=page_targets[target]["name"]
      candidates_per_term[tuple(page_targets[target]["terms"])]+=1
      if len(candidates)<cand_cap:
       candidates.append({"mode":mode,"start_pc":hex(pc),"use_pc":hex(vbase+j),"kind":typ,
                          "reg":reg,"target_va":hex(target),"name":name,"terms":page_targets[target]["terms"],"FDE":fn(pc)})
     if next_w&0xfc000000==0x14000000 or next_w&0xfffffc1f==0xd65f0000:break
   elif (w&0x9f000000)==0x10000000:
    imm=((((w>>5)&0x7ffff)<<2)|((w>>29)&3))
    addr=pc+sext(imm,21)
    if addr in targets:
     name=targets[addr]["name"]
     if len(candidates)<cand_cap:
      candidates.append({"mode":mode,"start_pc":hex(pc),"use_pc":hex(pc),"kind":"ADR",
                         "target_va":hex(addr),"name":name,"terms":targets[addr]["terms"],"FDE":fn(pc)})
     candidates_per_term[tuple(targets[addr]["terms"])]+=1
  print("MODE_DONE",mode,"PAGES",counts[mode],"CANDIDATES",len(candidates),flush=True)
 # Avoid claiming strings to be code if no XREF. Need snippets for functions if available.
 seen=set();snippets=[]
 for x in candidates:
  fd=x["FDE"]
  if not fd:continue
  fnva=int(fd[0],16)
  if fnva in seen:continue
  seen.add(fnva)
  if len(snippets)>=35:break
  upper=min(int(fd[1],16) if fd[1] else fnva+512,fnva+800)
  cmd=["r2","-2","-q","-e","scr.color=false","-c","pd 130 @ "+hex(fnva),str(p)]
  try:
   z=subprocess.run(cmd,capture_output=True,text=True,errors="replace",timeout=55)
   snippets.append({"fde_start":hex(fnva),"fde_end":hex(upper),"terms":x["terms"],
                   "disassembly":(z.stdout+z.stderr)[:17500]})
  except Exception as e:snippets.append({"fde_start":hex(fnva),"error":str(e)})
 report={"engine":"HOK 12.1.1.1 GameCore raw and potential E2 mask",
         "FDE":len(starts),"text":{"VA":hex(vbase),"size":size},
         "candidate_terms":[{"va":hex(k),**v} for k,v in targets.items()],
         "address_page_matches":counts,
         "crossrefs":candidates,"term_count":{",".join(k):v for k,v in candidates_per_term.items()},
         "disassembly":snippets,
         "limits":"ADRP matches require manual local dataflow validation; no runtime actual-coordinate evidence."}
 (out/"xref_results.json").write_text(json.dumps(report,indent=2,ensure_ascii=False))
 print("XREF_SUMMARY",json.dumps({"count":len(candidates),"by_keyword":report["term_count"],
              "first":candidates[:40],"FDE":len(starts)},ensure_ascii=False)[:13500],flush=True)
 m.close()
