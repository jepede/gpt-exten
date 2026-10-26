#!/usr/bin/env python3
"""Inspect HOK IL2CPP and GameCore ELF layout and coordinate references, read-only."""
import hashlib,json,mmap,struct,sys,zipfile
from pathlib import Path
sys.path.insert(0,".github/scripts")
from ace_range_from_tencent_apks import RangeFile,SOURCES
title,pkg,version,md5,expected=SOURCES["hok"]
url=f"http://imtt.dd.qq.com/sjy.00022/sjy.00001/16891/apk/{md5}.apk?fsname={pkg}_{version}.apk"
out=Path("out/hok_coordinate_elf");out.mkdir(parents=True,exist_ok=True)
names=["lib/arm64-v8a/libil2cpp.so","lib/arm64-v8a/libGameCore.so","lib/arm64-v8a/libunity.so"]
words=["Vector3","VInt3","Position","position","Transform","MoveComponent","FrameSync",
       "Hero","Actor","Encrypt","Decrypt","Coordinate","HERO_POSITION_ENCRYPT",
       "SetPosition","GetPosition","Velocity","TssSDK","Obscured"]
remote=RangeFile(url)
assert remote.size==expected
reports=[]
with zipfile.ZipFile(remote) as z:
 for name in names:
  entry=z.getinfo(name)
  target=out/(Path(name).name)
  digest=hashlib.sha256()
  with z.open(entry) as src,target.open("wb") as dst:
   for buf in iter(lambda:src.read(8<<20),b""):
    digest.update(buf);dst.write(buf)
  assert target.stat().st_size==entry.file_size
  with target.open("rb") as f:
   m=mmap.mmap(f.fileno(),0,access=mmap.ACCESS_READ)
   assert m[:4]==b"\x7fELF"
   eh=struct.unpack_from("<16sHHIQQQIHHHHHH",m,0)
   phoff=eh[5];phsz=eh[9];phnum=eh[10]
   regions=[]
   for i in range(phnum):
    tp,flags,offset,va,pa,fs,ms,align=struct.unpack_from("<IIQQQQQQ",m,phoff+i*phsz)
    regions.append({"type":tp,"flags":flags,"offset":offset,"va":hex(va),"filesz":fs,"memsz":ms})
   hits={}
   for word in words:
    indices=[];p=0
    while len(indices)<25:
     idx=m.find(word.encode(),p)
     if idx<0:break
     indices.append(hex(idx));p=idx+len(word)
    if indices:hits[word]=indices
   report={"path":name,"size":entry.file_size,"sha256":digest.hexdigest(),
           "crc32":format(entry.CRC,"08x"),"arch":eh[2],"shnum":eh[12],
           "segments":regions,"literal_first25":hits}
   reports.append(report)
   print("ENGINE_ELF",json.dumps(report,ensure_ascii=False)[:16000],flush=True)
   m.close()
  target.unlink()
(out/"engine_elf_evidence.json").write_text(json.dumps({"members":reports,"partial_range":True},indent=2,ensure_ascii=False))
print("HOK_ENGINE_ELF_DONE",remote.received,flush=True)
remote.close()
