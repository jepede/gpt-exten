#!/usr/bin/env python3
"""Offline Niagram source triage: never executes target code."""
import re,json,collections,subprocess,tarfile
from pathlib import Path
from urllib.parse import urlsplit
ROOT=Path("niagram-src"); OUT=Path("audit-out"); OUT.mkdir(exist_ok=True)
exts={".java",".kt",".xml",".gradle",".properties",".groovy",".yml",".yaml",".sh",".py",".c",".cc",".cpp",".h",".hpp",".cmake",".txt",".md"}
def git(*a,limit=12000000):
    try:
        p=subprocess.run(["git","-C",str(ROOT),*a],capture_output=True,text=True,timeout=180)
        return p.stdout[:limit] if p.returncode==0 else "ERROR "+p.stderr[:1000]
    except Exception as e:return "ERROR "+repr(e)
def save(name,s): (OUT/name).write_text(s,encoding="utf-8")
rules={
 "EXEC":r"Runtime\.getRuntime\s*\(\s*\)\.exec|ProcessBuilder\s*\(|\bsystem\s*\(\s*\"|popen\s*\(",
 "DYNAMIC_CODE":r"DexClassLoader|InMemoryDexClassLoader|DexFile\.loadDex|System\.load\s*\(|System\.loadLibrary|dlopen\s*\(",
 "SENSITIVE":r"getAuthKey|auth_key|session.*(?:upload|send|export)|ContactsContract|READ_SMS|READ_CONTACTS|AccessibilityService|READ_PHONE_STATE|TelephonyManager|getInstalledPackages|NotificationListenerService",
 "NETWORK":r"https?://|OkHttpClient|HttpURLConnection|Retrofit|WebSocket|Firebase|Crashlytics|firebase_analytics",
 "UPDATE":r"update.*apk|apk.*update|apksigner|verify.*signature|signingInfo|GET_SIGNING_CERTIFICATES|PackageInstaller|ACTION_INSTALL_PACKAGE|REQUEST_INSTALL_PACKAGES",
 "CRYPTO":r"TrustManager|X509TrustManager|HostnameVerifier|onReceivedSslError|setJavaScriptEnabled|addJavascriptInterface|checkServerTrusted",
 "AUTOMATION":r"curl\s|wget\s|base64\s+-d|bash\s+-c|sh\s+-c|pip\s+install|git\s+clone|secrets\.",
}
regex={k:re.compile(v,re.I) for k,v in rules.items()}
url_re=re.compile(r'https?://[a-z0-9._~:/?#\[\]@!$&()*+,;=%-]{5,200}',re.I)
records=[]; domains=collections.defaultdict(set); scanned=0; lines=0
paths=git("ls-files","-z").split("\0")
for path in paths:
    fp=ROOT/path
    if not path or fp.suffix.lower() not in exts or not fp.is_file() or fp.stat().st_size>2000000:continue
    scanned+=1
    try:s=fp.read_text("utf-8",errors="replace")
    except:continue
    for i,line in enumerate(s.splitlines(),1):
        lines+=1
        for name,rx in regex.items():
            if rx.search(line):records.append((name,path,i,line.strip()[:280]))
        for link in url_re.findall(line):
            d=urlsplit(link).hostname
            if d:domains[d.lower()].add(path)
def score(x):
    p=x[1].lower()
    return 0 if any(w in p for w in ("niagram","nya","neko","update","analytics","github","proxy","secret","build.gradle",".github/")) else 1
records.sort(key=lambda x:(score(x),x[0],x[1],x[2]))
save("signals.tsv","type\tfile\tline\tcode\n"+"\n".join("\t".join(map(str,x)) for x in records[:22000]))
save("domains.tsv","domain\tfile_count\tpaths\n"+"\n".join(d+"\t"+str(len(p))+"\t"+", ".join(sorted(p)[:15]) for d,p in sorted(domains.items(),key=lambda x:(-len(x[1]),x[0]))))
for v,a,b in [("release","1270","1273"),("dev","1273","origin/dev")]:
    save("diff-"+v+"-stats.txt",git("diff","--stat",a,b))
    save("diff-"+v+"-files.txt",git("diff","--name-status",a,b))
    save("diff-"+v+".patch",git("diff","--unified=2",a,b,limit=14000000))
save("gitmodules.txt",(ROOT/".gitmodules").read_text(errors="replace") if (ROOT/".gitmodules").exists() else "")
save("git-refs.txt",git("log","-1","--format=%H %aI %s","1273")+"\nDEV\n"+git("log","-1","--format=%H %aI %s","origin/dev"))
save("scope.json",json.dumps({"tracked":len(paths)-1,"scanned_files":scanned,"lines":lines,"pattern_hits":len(records),"unique_domains":len(domains)},indent=2))
report=["# Niagram automated preliminary static triage", "","Target: HSSkyBoy/Niagram tag 1273, compare tag 1270 and dev.","Not proof of malware; regex hits require manual context. No source-to-APK reproducibility verified.","",f"Scanned {scanned} text files / {lines} lines, {len(records)} signal matches, {len(domains)} domains.","","## Release / dev refs",git("log","-1","--format=%H %aI %s","1273"),git("log","-1","--format=%H %aI %s","origin/dev"),"","## 1270 to 1273 changes",git("diff","--stat","1270","1273",limit=14000),"","## 1273 to dev changes",git("diff","--stat","1273","origin/dev",limit=14000),"","## Interesting code (first 220)"]
for name,p,i,line in records[:220]:report.append(f"- {name}: {p}:{i} :: {line[:160]}")
report+=["","## Domains (first 100)"]
for d,p in sorted(domains.items(),key=lambda x:(-len(x[1]),x[0]))[:100]:report.append(f"- {d} ({len(p)} files) "+", ".join(sorted(p)[:4]))
save("report.md","\n".join(report))
interesting=[]
for p in paths:
    if re.search(r"update|signature|sign|github|analytics|crash|firebase|privacy|proxy|tcp2ws|webview|network|manifest|secret|login|auth|session|credentials|translate",p,re.I):
        f=ROOT/p
        if f.is_file() and f.suffix.lower() in exts and f.stat().st_size<=500000:interesting.append(p)
save("interesting-files.txt","\n".join(interesting))
with tarfile.open(OUT/"sensitive-sources.tar.gz","w:gz",compresslevel=4) as t:
    for p in sorted(set(interesting))[:1800]:t.add(ROOT/p,arcname=p,recursive=False)
