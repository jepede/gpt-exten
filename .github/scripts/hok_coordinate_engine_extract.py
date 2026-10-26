#!/usr/bin/env python3
"""Selective Honor of Kings IL2CPP/Unity coordinate static audit using Tencent HTTP Range.
No full-APK download, no executable code run. CRC32 and SHA256 verified for each member.
"""
from pathlib import Path
import sys,os,re,hashlib,mmap,shutil,subprocess,json,zipfile
sys.path.insert(0,str(Path(__file__).resolve().parent))
from ace_range_from_tencent_apks import RangeFile,SOURCES
OUT=Path("reports/hok_20261026");OUT.mkdir(parents=True,exist_ok=True)
RAW=Path("out/hok_coord/raw");RAW.mkdir(parents=True,exist_ok=True)
PACK=Path("out/hok_coord/packs");PACK.mkdir(parents=True,exist_ok=True)
title,pkg,version,source_md5,total=SOURCES["hok"]
url=f"http://imtt.dd.qq.com/sjy.00022/sjy.00001/16891/apk/{source_md5}.apk?fsname={pkg}_{version}.apk"
members={
 "il2cpp":"lib/arm64-v8a/libil2cpp.so",
 "gamecore":"lib/arm64-v8a/libGameCore.so",
 "unity":"lib/arm64-v8a/libunity.so",
 "metadata":"assets/bin/Data/Managed/Metadata/global-metadata.dat"
}
terms=["Vector3","Vector2","Quaternion","Transform","GetPosition","SetPosition","WorldPosition","LocalPosition",
"m_Position","ActorPosition","ActorPos","HeroPos","HeroPosition","LogicPos","ClientPos","CurPos","TargetPos",
"Position","Coord","Coordinate","Location","ActorRoot","HeroActor","GameActor","BattleActor",
"PlayerCharacter","ActorManager","ActorComponent","MoveController","MoveDir","MoveSpeed","PlayerPosition",
"EncryptPosition","DecryptPosition","EncryptVector","EncVector","EncPos","bEncrypted","GetActorPos",
"FixedPoint","Fix64","LVector3","VInt3","FrameSync","SyncPosition","NetPosition","NetworkPosition",
"SkillCooldown","GameBattle"]
pat=re.compile(rb"[\x20-\x7e]{7,180}\x00")
interesting=re.compile(r"Actor|Hero|Position|Coord|Location|Vector|World|Transform|Move|Battle|Encrypt|Decrypt|FrameSync|Unity|GameSystem",re.I)
def digest(p):
 h=hashlib.sha256()
 with p.open("rb") as f:
  for b in iter(lambda:f.read(8<<20),b""):h.update(b)
 return h.hexdigest()
def run(args,timeout=100):
 try:
  p=subprocess.run(args,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=timeout,text=True,errors="replace")
  return {"rc":p.returncode,"output":p.stdout[:70000]}
 except Exception as e:return {"rc":-1,"output":str(e)}
def scan(path,label):
 entry={"size":path.stat().st_size,"sha256":digest(path)}
 with path.open("rb") as f:first=f.read(160)
 entry["magic128"]=first[:128].hex()
 entry["elf"]=first[:4]==b"\x7fELF"
 if entry["elf"]:
  entry["header"]=run(["readelf","-hW",str(path)])
  entry["program_headers"]=run(["readelf","-lW",str(path)])
  entry["sections"]=run(["readelf","-SW",str(path)])
  entry["dynamic"]=run(["readelf","-dW",str(path)])
  symbols=run(["readelf","-Ws",str(path)],timeout=150)["output"].splitlines()
  entry["symbol_filtered"]=[x.strip() for x in symbols if interesting.search(x)][:160]
 else:
  entry["metadata_magic"]=first[:4].hex()
  entry["metadata_version"]=int.from_bytes(first[4:8],"little")
  entry["standard_il2cpp_header"]=(first[:4]==bytes.fromhex("af1bb1fa"))
  entry["metadata_header_words"]=[int.from_bytes(first[i:i+4],"little") for i in range(0,128,4)]
 hits={}
 with path.open("rb") as f:
  mm=mmap.mmap(f.fileno(),0,access=mmap.ACCESS_READ)
  for term in terms:
   needle=term.encode()
   pos=0;count=0;examples=[]
   while count<180:
    at=mm.find(needle,pos)
    if at<0:break
    count+=1
    if len(examples)<6:
     context=mm[max(0,at-30):min(len(mm),at+len(needle)+80)]
     examples.append({"offset":hex(at),"preview":"".join(chr(x) if 32<=x<127 else "." for x in context)[:135]})
    pos=at+len(needle)
   if count:hits[term]={"at_least":count,"capped":count>=180,"examples":examples}
  sample=mm[:min(len(mm),96<<20)]
  decoded=[]
  for m in pat.finditer(sample):
   raw=m.group()[:-1]
   if interesting.search(raw.decode("latin1","replace")):
    decoded.append({"offset":hex(m.start()),"value":raw.decode("latin1","replace")[:180]})
    if len(decoded)>=800:break
  entry["names_sample"]=decoded
  entry["term_hits"]=hits
  mm.close()
 print("SCANNED",label,"size",entry["size"],"sha256",entry["sha256"],
       "magic",entry.get("metadata_magic"),"selected_counts",
       json.dumps({x:hits[x]["at_least"] for x in ("Vector3","WorldPosition","LogicPos","ActorPosition","EncVector","DecryptPosition","VInt3") if x in hits}),flush=True)
 return entry
r=RangeFile(url)
try:
 assert r.size==total,(r.size,total)
 with zipfile.ZipFile(r) as z:
  report={"game":title,"version":version,"package":pkg,"source":url,
          "source_apk_bytes":r.size,"whole_apk_sha256_verified":False,"members":{}}
  for label,source_name in members.items():
   info=z.getinfo(source_name)
   path=RAW/Path(source_name).name
   with z.open(info) as src,path.open("wb") as dst:shutil.copyfileobj(src,dst,8<<20)
   assert path.stat().st_size==info.file_size
   entry=scan(path,label)
   entry.update({"path":source_name,"crc32":format(info.CRC,"08x"),"zip_member_crc_checked":True,"compressed_size":info.compress_size})
   archive=PACK/("hok-12.1.1.1-"+label+".zip")
   with zipfile.ZipFile(archive,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=6) as zz:
    zz.write(path,arcname=source_name)
   entry["portable_archive"]=archive.name
   entry["archive_bytes"]=archive.stat().st_size
   entry["archive_sha256"]=digest(archive)
   assert archive.stat().st_size<97000000,(label,archive.stat().st_size)
   report["members"][label]=entry
   print("PACKAGED",label,"raw",entry["size"],"zip",entry["archive_bytes"],"hash",entry["sha256"],flush=True)
  report["range_calls"]=r.calls
  report["source_bytes_fetched"]=r.received
  (OUT/"coordinate_engine_analysis.json").write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n")
  manifest={"name":"HoK coordinate static ELF and IL2CPP metadata","version":version,
            "platform":"Android","architecture":"arm64-v8a",
            "files":[{k:e[k] for k in ("path","size","sha256","portable_archive","archive_bytes","archive_sha256","crc32")}
                     for e in report["members"].values()]}
  (OUT/"portable_archive_manifest.json").write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+"\n")
  md=["# 王者荣耀 12.1.1.1：核心坐标模块静态逆向","",
   "源 APK 按 HTTP Range 读取；只提取必要成员，逐一验证 ZIP CRC32 和 SHA256。未验证整个 APK 的 MD5/SHA256。",
   "","## 实际导出文件","",
   "| 文件 | 字节数 | SHA256 | ZIP 大小 |","|---|---:|---|---:|"]
  for lab,e in report["members"].items():
   md.append("| "+e["path"]+" | "+str(e["size"])+" | "+e["sha256"]+" | "+str(e["archive_bytes"])+" |")
  e=report["members"]["metadata"]
  md+=["","## IL2CPP 元数据","",
       "Magic: "+e.get("metadata_magic","?"),
       "Version: "+str(e.get("metadata_version","?")),
       "Standard metadata: "+str(e.get("standard_il2cpp_header","?")),
       "","## 字符串证据（仅做定位，不等于确认加密）",""]
  for lab,e in report["members"].items():
   md.append("### "+lab)
   for term,x in e["term_hits"].items():
    if interesting.search(term):md.append("- "+term+": "+str(x["at_least"])+("+" if x["capped"] else ""))
  md+=["","## 分析限制","查到 Vector3、Position 或 Encrypt 字符串，不代表它们之间存在真实调用或坐标加密。需要继续做 IL2CPP 类型/方法解析、ARM64 控制流和真实样本回归。"]
  (OUT/"coordinate_engine_analysis.md").write_text("\n".join(md)+"\n")
  print("ENGINE_AUDIT_COMPLETE",json.dumps({"downloaded":r.received,"range_calls":r.calls,"files":{k:{"size":e["size"],"zip":e["archive_bytes"],"sha256":e["sha256"]} for k,e in report["members"].items()}},ensure_ascii=False),flush=True)
finally:
 r.close()
