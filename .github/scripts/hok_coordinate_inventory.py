#!/usr/bin/env python3
"""Read-only inventory of cached known Tencent Honor of Kings 12.1.1.1 APK source via HTTP Range.
No full game APK download, no execution/instrumentation, no privilege changes.
"""
import os,sys,json,re,hashlib,zipfile,collections,time,subprocess,tempfile,shutil
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from ace_range_from_tencent_apks import RangeFile,SOURCES
OUT=Path("reports/hok_20261026");OUT.mkdir(parents=True,exist_ok=True)
title,pkg,version,md5,expected_size=SOURCES["hok"]
source=f"http://imtt.dd.qq.com/sjy.00022/sjy.00001/16891/apk/{md5}.apk?fsname={pkg}_{version}.apk"
remote=RangeFile(source)
try:
 assert remote.size==expected_size,(remote.size,expected_size)
 with zipfile.ZipFile(remote) as z:
  infos=z.infolist()
  libs=[i for i in infos if re.fullmatch(r"lib/[^/]+/[^/]+\.so",i.filename,re.I)]
  assets=[i for i in infos if re.search(r"unity|engine|il2cpp|gamecore|gamedata|assembl|global-metadata|libue4|coord|position|world|hero|actor|geometry|framework|lua|script|catalog|assetbundle",i.filename,re.I)][:350]
  result={
    "game":title,"version":version,"package":pkg,"apk_expected_size":expected_size,
    "url_md5_from_source_unverified":md5.lower(),"source":source,
    "apk_zip_entries":len(infos),"so_entries":len(libs),"abis":sorted({x.filename.split("/")[1] for x in libs}),
    "libs":sorted([dict(name=x.filename,size=x.file_size,packed=x.compress_size,crc32=format(x.CRC,"08x"),compression=x.compress_type) for x in libs],key=lambda a:-a["size"]),
    "relevant_asset_names":[dict(name=x.filename,size=x.file_size) for x in assets],
    "remote_bytes":remote.received,"range_calls":remote.calls,
    "notes":["Remote ZIP members enumerated over HTTP Range; original full-APK MD5 not verified.",
             "The listing alone cannot prove game coordinate encryption or concrete field layout."]
   }
 print("APK_META",json.dumps({k:v for k,v in result.items() if k not in ("libs","relevant_asset_names")},ensure_ascii=False),flush=True)
 print("TOP_LIBRARIES",json.dumps(result["libs"][:80],ensure_ascii=False),flush=True)
 print("RELEVANT_ASSETS",json.dumps(result["relevant_asset_names"][:150],ensure_ascii=False),flush=True)
 (OUT/"apk_native_inventory.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
 lines=["# 王者荣耀 APK 核心坐标逆向：原生模块与资源盘点","",
 f"Source: Honor of Kings CN {version} / {pkg}",f"ZIP entries {len(infos)}; SO entries {len(libs)}; ABIs {result['abis']}.",
 "Note: full APK SHA256/MD5 not yet verified, member inventory only.",
 "","## ARM native libraries (descending uncompressed size)","",
 "| Path | Size | Packed | CRC32 |","|---|---:|---:|---|"]
 for x in result["libs"]:lines.append(f"| {x['name']} | {x['size']:,} | {x['packed']:,} | {x['crc32']} |")
 lines+=["","## Potential gameplay metadata/assets",""]
 for x in result["relevant_asset_names"]:lines.append(f"- {x['name']} ({x['size']:,} bytes)")
 (OUT/"inventory.md").write_text("\n".join(lines)+"\n")
 print("INVENTORY_FINISHED",OUT,flush=True)
finally:
 remote.close()
