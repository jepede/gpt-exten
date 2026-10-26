#!/usr/bin/env python3
"""Inventory Tencent MyApp Honor of Kings APK ZIP directory via HTTP Range.
This is directory/metadata only. No whole APK download and no binary execution.
"""
import sys,os,zipfile,json,hashlib,re
from pathlib import Path
sys.path.insert(0, ".github/scripts")
from ace_range_from_tencent_apks import RangeFile,SOURCES
game="hok"
title,pkg,version,url_md5,expected_bytes=SOURCES[game]
url=f"http://imtt.dd.qq.com/sjy.00022/sjy.00001/16891/apk/{url_md5}.apk?fsname={pkg}_{version}.apk"
output=Path("out/hok_coord_inventory");output.mkdir(parents=True,exist_ok=True)
remote=RangeFile(url)
assert remote.size==expected_bytes,(remote.size,expected_bytes)
def to_row(x):
 return dict(path=x.filename,bytes=x.file_size,compressed=x.compress_size,method=x.compress_type,
             crc32=f"{x.CRC:08x}",offset=x.header_offset,flag_bits=x.flag_bits)
try:
 with zipfile.ZipFile(remote) as z:
  entries=z.infolist()
  libraries=[x for x in entries if x.filename.startswith("lib/") and x.filename.endswith(".so")]
  major=sorted(libraries,key=lambda x:-x.file_size)
  candidate_regex=re.compile(r"(?:lib(?:UE4|Unreal|unity|il2cpp|GameCore|gamecore|Game|cocos2dcpp|engine|client|logic|sgame|tersafe|tprt|gamemaster|turinggame|il2cpp|Lua|xlua)[a-z0-9_.-]*\.so)$",re.I)
  targets=[x for x in libraries if candidate_regex.search(x.filename)]
  asset_keys=re.compile(r"(?i)(?:global-metadata\.dat|assetbundles?|unity|lua|il2cpp|GameData|script|schema|config|proto|\.pak$|\.ucas$|\.utoc$)")
  chosen_assets=[x for x in entries if asset_keys.search(x.filename)]
  data=dict(game=title,pkg=pkg,version=version,expected_apk_size=expected_bytes,source_url=url,
            total_entries=len(entries),so_count=len(libraries),abis=sorted(set(x.filename.split("/")[1] for x in libraries)),
            largest_native=[to_row(x) for x in major[:55]],
            native_catalog=[to_row(x) for x in libraries],
            engine_candidates=[to_row(x) for x in targets],
            asset_candidates=[to_row(x) for x in chosen_assets[:200]],
            other_top_entries=[to_row(x) for x in sorted(entries,key=lambda x:-x.file_size)[:40]],
            range_count=remote.calls,received_bytes=remote.received,
            apk_whole_md5_verified=False, notes="Listed using remote ZIP central directory and source size; full APK bytes/hash not verified")
  assert any(x.filename=="AndroidManifest.xml" for x in entries)
  (output/"inventory.json").write_text(json.dumps(data,indent=2,ensure_ascii=False))
  rows=["# Honor of Kings Tencent APK native library inventory","",
   f"- Version: {version}",f"- Package: {pkg}",
   f"- Remote official APK length: {expected_bytes}",
   f"- Native SO count: {len(libraries)}",
   f"- Total ZIP entries: {len(entries)}",
   f"- Source whole-file MD5 not verified (partial download)",
   "","## Largest native SO files","",
   "| Path | Bytes | Compressed |","|---|---:|---:|"]
  for x in major[:70]:
   rows.append(f"| {x.filename} | {x.file_size} | {x.compress_size} |")
  rows+=["","## Engine and anti-cheat candidates"]
  for x in targets:rows.append(f"- {x.filename} ({x.file_size} bytes)")
  rows+=["","## Relevant assets (first 80)"]
  for x in chosen_assets[:80]:rows.append(f"- {x.filename} ({x.file_size} bytes)")
  (output/"inventory.md").write_text("\n".join(rows)+"\n")
  print("HOK_INVENTORY_DONE",json.dumps({"game":title,"version":version,"size":expected_bytes,
        "entries":len(entries),"native":len(libraries),
        "biggest":data["largest_native"][:32],"candidate_engines":data["engine_candidates"],
        "range_bytes":remote.received},ensure_ascii=False),flush=True)
finally:
 remote.close()
