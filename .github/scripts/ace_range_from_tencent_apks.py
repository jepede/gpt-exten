#!/usr/bin/env python3
"""Tencent APK HTTP Range ZIP extraction: only ACE focused SO, no whole APK download.
ZIP member CRC32 is verified, plus independent extracted-file SHA256.
"""
import argparse, collections, hashlib, io, json, re, shutil, tempfile, zipfile, os
os.environ.setdefault('GH_TOKEN', '')  # Reuse static ELF helpers only; no artifact token needed here.
from pathlib import Path
import requests
import ace_extract_cached_game_apks as core

SOURCES={
 "hok":("王者荣耀","com.tencent.tmgp.sgame","12.1.1.1","23516462AE86013BEC0F3E902B8CD638",1748020376),
 "peace":("和平精英","com.tencent.tmgp.pubgmhd","1.38.12","30E4261077A0A4BB39096ACD970118EB",2097992146),
 "cf":("穿越火线-枪战王者","com.tencent.tmgp.cf","1.0.580.880","DBF52408309F14C4DC3F7EE63F797686",2136799531)
}
BLOCK=2*1024*1024
LIMIT_RAW=70*1024*1024
LIMIT_PACK=80*1024*1024

class RangeFile(io.RawIOBase):
 def __init__(self,url):
  self.url=url
  self.session=requests.Session()
  self.session.headers.update({"User-Agent":"Mozilla/5.0 (Linux; Android 16; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36","Accept-Encoding":"identity"})
  self.pos=0
  self.size=None
  self.cache=collections.OrderedDict()
  self.calls=0
  self.received=0
  magic=self.fetch(0,3)
  if magic!=b"PK\x03\x04":raise ValueError("Not an APK ZIP file!")
 def fetch(self,a,b):
  with self.session.get(self.url,headers={"Range":f"bytes={a}-{b}"},stream=True,timeout=(20,115),allow_redirects=True) as resp:
   if resp.status_code!=206:
    raise ValueError(f"Server does not honor HTTP Range: {resp.status_code} final={resp.url}")
   cr=resp.headers.get("Content-Range","")
   m=re.fullmatch(r"bytes (\d+)-(\d+)/(\d+)",cr)
   if not m or int(m[1])!=a or int(m[2])!=b:
    raise ValueError(f"Unexpected Content-Range {cr}")
   n=int(m[3])
   if self.size is not None and n!=self.size:
    raise ValueError("Source changed size during extraction")
   self.size=n
   payload=resp.raw.read(b-a+1)
   if len(payload)!=b-a+1:
    raise ValueError("Incomplete range response")
   self.calls+=1
   self.received+=len(payload)
   return payload
 def seekable(self):return True
 def readable(self):return True
 def tell(self):return self.pos
 def seek(self,offset,whence=0):
  self.pos=offset if whence==0 else self.pos+offset if whence==1 else self.size+offset if whence==2 else None
  if self.pos is None or self.pos<0:raise ValueError("Bad file seek")
  return self.pos
 def block(self,idx):
  if idx in self.cache:
   self.cache.move_to_end(idx)
   return self.cache[idx]
  a=idx*BLOCK;b=min(self.size,a+BLOCK)-1
  chunk=self.fetch(a,b)
  self.cache[idx]=chunk
  while len(self.cache)>16:self.cache.popitem(last=False)
  return chunk
 def read(self,n=-1):
  if self.pos>=self.size:return b""
  if n is None or n<0:n=self.size-self.pos
  n=min(n,self.size-self.pos)
  out=[]
  while n>0:
   idx,delta=divmod(self.pos,BLOCK)
   block=self.block(idx)
   item=block[delta:delta+n]
   if not item:raise ValueError("Remote ZIP read failure")
   self.pos+=len(item);n-=len(item);out.append(item)
  return b"".join(out)
 def close(self):
  self.session.close()
  super().close()

def main():
 parser=argparse.ArgumentParser()
 parser.add_argument("--game",required=True,choices=sorted(SOURCES))
 a=parser.parse_args()
 title,pkg,version,md5_expected,size_expected=SOURCES[a.game]
 source=f"http://imtt.dd.qq.com/sjy.00022/sjy.00001/16891/apk/{md5_expected}.apk?fsname={pkg}_{version}.apk"
 output=Path("out")/a.game
 report=output/"reports"
 packdir=output/"packs"
 report.mkdir(parents=True,exist_ok=True)
 packdir.mkdir(parents=True,exist_ok=True)
 remote=RangeFile(source)
 assert remote.size==size_expected,(remote.size,size_expected)
 result={"game":title,"version":version,"package":pkg,"source_url":source,
  "source_apk_bytes":remote.size,"unverified_apk_whole_md5_from_download_url":md5_expected,
  "verification":"HTTP byte-range and ZIP CRC32 of extracted members, plus SHA256 of each SO; full APK MD5 not checked",
  "catalog":[],"focus":[],"interesting_assets":[],"notes":[
   "Static analysis only: no dynamic download, no direct evidence of coordinate-encryption shellcode",
   "Absence in the APK does not exclude runtime hot updates or split APKs"]}
 with zipfile.ZipFile(remote) as z:
  items=z.infolist()
  allso=[x for x in items if re.fullmatch(r"lib/[^/]+/[^/]+\.so",x.filename,re.I)]
  result["total_entries"]=len(items)
  result["so_count"]=len(allso)
  result["abis"]=sorted({x.filename.split("/")[1] for x in allso})
  result["interesting_assets"]=[{"path":x.filename,"bytes":x.file_size} for x in items
    if re.search(r"mrpcs|vmrpcs|tersafe|anogs|anort|tprt|ace_shell",x.filename,re.I)][:150]
  for x in allso:
   result["catalog"].append({"path":x.filename,"size":x.file_size,"compressed":x.compress_size,
      "crc32":format(x.CRC,"08x"),"focus":bool(core.FOCUS_NAME.match(Path(x.filename).name))})
  try:
   manifest=z.read("AndroidManifest.xml")
   result["manifest_sha256"]=hashlib.sha256(manifest).hexdigest()
   result["manifest_contains_package_utf16"]=pkg.encode("utf-16le") in manifest
  except Exception as e:
   result["manifest_error"]=str(e)
  small_libs=[]
  with tempfile.TemporaryDirectory() as dirname:
   tmp=Path(dirname)
   for info in allso:
    if not core.FOCUS_NAME.match(Path(info.filename).name):continue
    entry={"path":info.filename,"bytes":info.file_size,"compressed":info.compress_size,"crc32":format(info.CRC,"08x")}
    if info.file_size>LIMIT_RAW:
     entry["omitted"]="Exceeds max single SO safe transport size 70MiB"
    else:
     saved=tmp/(info.filename.split("/")[1]+"_"+Path(info.filename).name)
     with z.open(info) as src,saved.open("wb") as dst:
      shutil.copyfileobj(src,dst,1024*1024)
     assert saved.stat().st_size==info.file_size
     core.inspect_lib(saved,entry)
     small_libs.append((info.filename,saved,entry))
    result["focus"].append(entry)
    print("LIB",info.filename,info.file_size,"MRPCS",entry.get("static_hits",{}).get("mrpcs",{}).get("count",0),flush=True)
   pack_index=0
   package=None
   rawbytes=0
   packages=[]
   for name,p,entry in small_libs:
    if package is None or rawbytes+p.stat().st_size>LIMIT_PACK:
     if package:package.close()
     dst=packdir/f"ace-libs-{pack_index:02d}.zip"
     package=zipfile.ZipFile(dst,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=5)
     packages.append(dst)
     rawbytes=0
     pack_index+=1
    package.write(p,arcname=name)
    rawbytes+=p.stat().st_size
   if package:package.close()
   assert all(x.stat().st_size<95*1024*1024 for x in packages)
   result["packs"]=[{"file":x.name,"bytes":x.stat().st_size,"sha256":core.digest(x)} for x in packages]
  result["http_range_calls"]=remote.calls
  result["http_bytes_downloaded"]=remote.received
  print("COMPLETE",a.game,"SO",len(allso),"focus",len(result["focus"]),"ranges",remote.calls,"transferred",remote.received,flush=True)
 remote.close()
 (report/"analysis.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
 with (report/"SO_CATALOG.tsv").open("w") as f:
  f.write("path\tsize\tcompressed\tcrc32\tfocus\n")
  for x in result["catalog"]:
   f.write(f"{x['path']}\t{x['size']}\t{x['compressed']}\t{x['crc32']}\t{x['focus']}\n")
 lines=[f"# {title} 官方 APK 安全库静态分析",f"- 版本：{version}",f"- 包名：{pkg}",
 f"- 官方 CDN APK 字节数：{remote.size}",f"- HTTP Range 读取量：{remote.received}",
 f"- 原生 SO：{len(allso)}",f"- Focus SO：{len(result['focus'])}",
 "",
 "| SO | 文件大小 | SHA256 | MRPCS 命中 | VMRPCS 命中 |",
 "|---|---:|---|---:|---:|"]
 for x in result["focus"]:
  hits=x.get("static_hits",{})
  lines.append(f"| {x['path']} | {x['bytes']} | {x.get('sha256','skipped')} | {hits.get('mrpcs',{}).get('count',0)} | {hits.get('vmrpcs',{}).get('count',0)} |")
 lines += ["","本次直接从腾讯 CDN 的远端 APK 按 HTTP Range 读取 ZIP 目录与必要 SO，ZIP CRC32 验证通过；仅对提取后的 SO 计算 SHA256。",
 "没有下载整个 APK，因此未验证官方 URL 中 MD5 对整个文件的正确性。",
 "静态字符串/符号不足以证明云下发 Shellcode 或坐标加密实现，亦不能排除游戏启动后热更新其他库。"]
 (report/"REPORT.md").write_text("\n".join(lines)+"\n")
if __name__=="__main__":main()
