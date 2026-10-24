#!/usr/bin/env python3
"""Probe Tencent MyApp landing pages for official APK links; do not download installers."""
import json,re,html,concurrent.futures
import requests
APPS={
 "arena":("暗区突围","com.tencent.mf.uam"),
 "cod":("使命召唤手游","com.tencent.tmgp.cod"),
 "lolm":("英雄联盟手游","com.tencent.lolm"),
 "speed":("QQ飞车手游","com.tencent.tmgp.speedmobile"),
 "jcc":("金铲铲之战","com.tencent.jkchess"),
 "codev":("无畏契约手游","com.tencent.tmgp.codev")
}
def probe(k,v):
 name,pkg=v
 url="https://a.app.qq.com/o/simple.jsp?pkgname="+pkg
 ans={"game":k,"title":name,"pkg":pkg,"url":url}
 try:
  r=requests.get(url,headers={"User-Agent":"Mozilla/5.0 (Linux; Android 16; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Mobile Safari/537.36"},timeout=(20,60))
  r.raise_for_status()
  t=html.unescape(r.text).replace("\\/","/")
  ans["html_size"]=len(t)
  hits=re.findall(r'https?://imtt\.dd\.qq\.com/[^\s"\\<>]+?\.apk\?fsname=[^"\\<>\s]+',t,re.I)
  ans["apk_urls"]=list(dict.fromkeys(hits))[:5]
  ans["versions"]=list(dict.fromkeys(re.findall(r'"versionName"\s*:\s*"([^"]+)"',t)))[:10]
  ans["apkUrls"]=list(dict.fromkeys(re.findall(r'"apkUrl(?:64)?"\s*:\s*"([^"]+)"',t)))[:5]
  ans["fileSizes"]=list(dict.fromkeys(re.findall(r'"fileSize"\s*:\s*\{\s*"bytes"\s*:\s*"(\d+)"',t)))[:10]
  ans["page_title"]=(re.findall(r"<title>(.*?)</title>",t,re.I|re.S)or[""])[0][:100]
 except Exception as e:
  ans["error"]=str(e)[:400]
 return ans
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
 out=list(ex.map(lambda kv:probe(*kv),APPS.items()))
for o in out: print(json.dumps(o,ensure_ascii=False),flush=True)
with open("game_sources_ace_20261024.json","w") as f:json.dump(out,f,ensure_ascii=False,indent=2)
