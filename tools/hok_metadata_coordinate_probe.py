#!/usr/bin/env python3
"""Inspect standard Unity IL2CPP metadata from the existing official HOK APK URL."""
import sys,json,re,zipfile,hashlib,struct
from pathlib import Path
sys.path.insert(0,".github/scripts")
from ace_range_from_tencent_apks import RangeFile,SOURCES

title,pkg,version,md5,total=SOURCES["hok"]
url=f"http://imtt.dd.qq.com/sjy.00022/sjy.00001/16891/apk/{md5}.apk?fsname={pkg}_{version}.apk"
member="assets/bin/Data/Managed/Metadata/global-metadata.dat"
dest=Path("out/hok_metadata")
dest.mkdir(parents=True,exist_ok=True)
remote=RangeFile(url)
assert remote.size==total
with zipfile.ZipFile(remote) as z:
 info=z.getinfo(member)
 file=dest/"global-metadata.dat"
 h=hashlib.sha256()
 with z.open(info) as inp,file.open("wb") as out:
  for block in iter(lambda:inp.read(4<<20),b""):
   out.write(block);h.update(block)
 assert file.stat().st_size==info.file_size
 data=file.read_bytes()
magic,version_id=struct.unpack_from("<II",data,0)
report={"package":pkg,"version":version,"metadata_bytes":len(data),
  "sha256":h.hexdigest(),"crc32":format(info.CRC,"08x"),"magic":hex(magic),
  "il2cpp_version":version_id,"standard_metadata":magic==0xfab11baf}
queries=["Vector3","Transform","Position","GetPosition","SetPosition",
  "MoveComponent","Actor","Hero","Battle","Sync","Coordinate","Encrypt",
  "Decrypt","Obscured","SafeVector","AntiCheat","LocalPosition",
  "Network","Velocity","Rotation","Player","Movement"]
if magic==0xfab11baf:
 string_offset,string_size=struct.unpack_from("<II",data,24)
 report["string_table"]={"offset":string_offset,"bytes":string_size,
    "valid":string_offset+string_size<=len(data)}
 if string_offset+string_size<=len(data):
  strings=data[string_offset:string_offset+string_size]
  name_list=[(i,x.decode("utf8","replace")) for i,x in enumerate(strings.split(bytes([0])))]
  selected={}
  for term in queries:
   names=[v for _,v in name_list if term.lower() in v.lower()]
   selected[term]={"count":len(names),"samples":names[:85]}
  report["strings"]=selected
else:
 report["note"]="Nonstandard metadata header: requires format inspection before interpreting type layout."
 report["ascii_samples"]=[x.decode("ascii","replace") for x in re.findall(rb"[\x20-\x7e]{8,}",data[:4<<20])[:60]]
report["range_calls"]=remote.calls
report["range_bytes"]=remote.received
(dest/"metadata_findings.json").write_text(json.dumps(report,indent=2,ensure_ascii=False))
summary={k:{"count":v["count"],"samples":v["samples"][:25]} for k,v in report.get("strings",{}).items()}
print("METADATA_RESULT",json.dumps({"magic":report["magic"],"version":version_id,
   "sha256":report["sha256"],"bytes":len(data),"hits":summary},ensure_ascii=False)[:22000],flush=True)
remote.close()
file.unlink()
