#!/usr/bin/env python3
"""Offline-focused static ACE/MRPCS SO extraction from verified, cached game APK artifacts.
Runs inside GitHub Actions; NEVER exports the complete APK or huge engine SO.
"""
import argparse
import csv
import hashlib
import json
import mmap
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile

REPO = os.environ["GITHUB_REPOSITORY"]
TOKEN = os.environ["GH_TOKEN"]
ROOT = Path.cwd()
PATTERNS = [
    "mrpcs", "vmrpcs", "MRPCS_ANDROID", "tss_sdk", "TssSDK", "TP2Sdk", "tp2_",
    "anogs", "anort", "tersafe", "tprt", "shellcode", "mprotect", "memfd_create",
    "dlopen", "dl_iterate_phdr", "ptrace"
]
FOCUS_NAME = re.compile(
    r"^lib(?:anogs[a-z0-9_]*|anort[a-z0-9_]*|tersafe[a-z0-9_]*|tprt[a-z0-9_]*|"
    r"turing[a-z0-9_]*|tss[a-z0-9_]*|tp2[a-z0-9_]*|anticheat[a-z0-9_]*|"
    r"ace[a-z0-9_]*|gamemaster[a-z0-9_]*)\.so$", re.I
)
LIMIT_RAW_SO = 70 * 1024 * 1024
MAX_PACK_RAW = 75 * 1024 * 1024

PUBG = {
    "id": "pubg",
    "game": "PUBG MOBILE Global",
    "version": "4.6.0 (21525)",
    "package": "com.tencent.ig",
    "source": "APKMirror / Level Infinite; base APK only, no OBB",
    "apk_name": "PUBG-MOBILE-Global-4.6.0-21525-arm64-v8a.apk",
    "apk_size": 107399819,
    "apk_sha256": "9e28aa526caa748fc650a2f7b86f1ef545acf94f09811a5fa41414ca818e8696",
    "apk_md5": "ac9ba3006c7c1dcdddf320f8e821f9c7",
    "artifacts": [{"id":11308584380,"zipsha":"677af3e93aa55b485613352eb58f9eec93ae4d79d0803a6431ba4c80d2b68e58"}]
}
NARUTO = {
    "id": "naruto",
    "game": "火影忍者 Android 国服",
    "version": "1.79.79.9",
    "package": "com.tencent.KiHan",
    "source": "Tencent MyApp official APK; existing GitHub cache",
    "apk_name": "naruto-1.79.79.9.apk",
    "apk_size": 1735650312,
    "apk_sha256": "5582bd1394f1438537829cb65bb486688ca2addc305c7a9717a7cf20b7eaa1b9",
    "apk_md5": "1ce28cdbbe7ae3ea5cdc9a083dfb9857",
    "artifacts": [
        {"id":11141309461,"zipsha":"75578e684a4b272f3caef7c0b3c6968c309886f4bb4d6953769a913460b4f8db","size":209715200,"rawsha":"7402956f782b944df43412e04ec71fac49814889e3fb65a9e09a227b710e0b59"},
        {"id":11142255606,"zipsha":"b96edbec2b96ab4f171f5c0d5bab63a58cefca7ededce959469dce3059e99a0c","size":209715200,"rawsha":"64c2848decf3b6ba34332afbb183e2d94010d02d8e277dfda7688c259bb137e7"},
        {"id":11141194843,"zipsha":"b2aab5dc4a597de3563b4e71f79b230dc7b7e4df4a0e6c1d084ab944dda4faf0","size":209715200,"rawsha":"37dc4782e2b849e5be00dd1d7d3bf444fc29592dfc8ffb6dc3bf3ec875bb2cd8"},
        {"id":11141184990,"zipsha":"d608d4a270eec97be7a755d2fb25b8ec8605ac3e7520988f9c721dde4952f2a3","size":209715200,"rawsha":"bdc87d7b20bebcbe882d3d70ce13ee24b75e2df27bb4a9380b9a2186a1e5221c"},
        {"id":11142245673,"zipsha":"52c00baa944d2fc7f86c435c83e335e9b684a49382726f906aba4854152c69df","size":209715200,"rawsha":"74bbd33c47b748b98d7d403d9c010cf5a85fb1a6a8a6bdbaaec05a267efb321f"},
        {"id":11142240675,"zipsha":"efedb270ad04a8358f1241c1d3fc87cb487acdadd1149a8fa45e3ea05f4f4ea5","size":209715200,"rawsha":"9721dc39f50c3db2189b8971c37e309d442ad9ce699836ee287e5a09ef6b79eb"},
        {"id":11142250687,"zipsha":"aacbf58beb6cf19e86c11a2005288c5f13167349ce463a773162d65056bf12bd","size":209715200,"rawsha":"354ad70526613bda0e60395c6fb50533e91a719f9a0d31537368ad346e34a280"},
        {"id":11142305362,"zipsha":"8c3ad5a3411dab2e7b4d1c59e94b0874b61180b2794b6feac58f7e52cbd3e017","size":209715200,"rawsha":"3a38a4533b382a3aceee7f323e713811055f088c6a5bd2d2261b6bd4fb78e238"},
        {"id":11142430023,"zipsha":"e673ac258915ba5289d219c27abb676fde73e206bbee74e273c42816b7c6675b","size":57928712,"rawsha":"2ef071f55491d919c8072ef68373b28c10b8116745ac66891c5981e6ca3b1b60"}
    ]
}

def digest(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(8*1024*1024), b""):
            h.update(block)
    return h.hexdigest()

def download_artifact(artifact, dest):
    aid = artifact["id"]
    print("DOWNLOAD CACHE ARTIFACT", aid, flush=True)
    url = f"https://api.github.com/repos/{REPO}/actions/artifacts/{aid}/zip"
    args = [
        "curl", "--fail", "--location", "--silent", "--show-error",
        "--retry", "6", "--retry-all-errors", "--retry-delay", "3",
        "--connect-timeout", "30", "--max-time", "1000",
        "-H", f"Authorization: Bearer {TOKEN}",
        "-H", "Accept: application/vnd.github+json", "-o", str(dest), url
    ]
    subprocess.run(args, check=True)
    sha = digest(dest)
    assert sha == artifact["zipsha"], f"Artifact ZIP SHA mismatch {aid}: {sha}"

def reconstruct(conf, tmp):
    apk = tmp / conf["apk_name"]
    fullsha, fullmd5 = hashlib.sha256(), hashlib.md5()
    written = 0
    with open(apk, "wb") as dst:
        for i, artifact in enumerate(conf["artifacts"]):
            z = tmp / f"cache_{i:02d}.zip"
            download_artifact(artifact, z)
            with zipfile.ZipFile(z) as archive:
                files = [x for x in archive.infolist() if x.filename.endswith(".apk") or re.search(r"\.apk\.part-(\d+)$",x.filename)]
                if not files:
                    files = [x for x in archive.infolist() if x.filename.endswith(f"part-{i:02d}") or x.filename.endswith(f".part.{i:02d}")]
                if len(files) != 1:
                    raise ValueError(f"Expected a single APK or APK part in {artifact['id']}; got {[x.filename for x in files]}")
                info = files[0]
                if conf["id"]=="pubg":
                    assert info.filename.endswith(".apk"), info.filename
                else:
                    assert info.filename.endswith(f"part-{i:02d}") or info.filename.endswith(f".part.{i:02d}"), info.filename
                segmentsha = hashlib.sha256()
                partlen = 0
                with archive.open(info) as src:
                    for block in iter(lambda: src.read(8*1024*1024), b""):
                        dst.write(block)
                        fullsha.update(block)
                        fullmd5.update(block)
                        segmentsha.update(block)
                        partlen += len(block)
                if "size" in artifact:
                    assert partlen == artifact["size"], (i,partlen,artifact["size"])
                    assert segmentsha.hexdigest() == artifact["rawsha"], (i,segmentsha.hexdigest())
                written += partlen
            z.unlink()
            print("VERIFIED ARTIFACT PART", i, "size", partlen, flush=True)
    assert written == conf["apk_size"], f"APK length {written} != {conf['apk_size']}"
    assert fullsha.hexdigest() == conf["apk_sha256"], "Whole APK SHA256 mismatch"
    assert fullmd5.hexdigest() == conf["apk_md5"], "Whole APK MD5 mismatch"
    print("APK FULL SHA256 VERIFIED", fullsha.hexdigest(), flush=True)
    return apk

def safe_run(args, limit=110):
    result = subprocess.run(args, capture_output=True, text=True, errors="replace", timeout=limit)
    return result.stdout if result.returncode==0 else ""

def extract_hits(path):
    hits = {}
    if path.stat().st_size == 0:
        return hits
    with open(path,"rb") as f, mmap.mmap(f.fileno(),0,access=mmap.ACCESS_READ) as mm:
        for term in PATTERNS:
            pattern = re.compile(re.escape(term.encode("ascii")),re.I)
            sampled=[]
            count=0
            for m in pattern.finditer(mm):
                count+=1
                if len(sampled)<6:
                    context=bytes(mm[max(0,m.start()-38):min(len(mm),m.end()+64)])
                    preview="".join(chr(c) if 32<=c<=126 else "." for c in context)
                    sampled.append({"file_offset":hex(m.start()),"context":preview})
            if count:
                hits[term]={"count":count,"samples":sampled}
    return hits

def inspect_lib(p, entry):
    data=p.open("rb").read(64)
    is_arm64=(data[:4]==b"\x7fELF" and data[4]==2 and int.from_bytes(data[18:20],"little")==183)
    entry["elf_aarch64"]=is_arm64
    entry["sha256"]=digest(p)
    entry["static_hits"]=extract_hits(p)
    if is_arm64:
        output=safe_run(["readelf","-dW",str(p)])
        entry["dt_needed"]=re.findall(r"\(NEEDED\).*?\[(.*?)\]", output)
        entry["soname"]=re.findall(r"\(SONAME\).*?\[(.*?)\]", output)
        hdr=safe_run(["readelf","-hW",str(p)])
        entry["entry_point"]= (re.findall(r"Entry point address:\s*(\S+)",hdr)or[""])[0]
        symbols=safe_run(["readelf","-Ws",str(p)],limit=180)
        entry["relevant_dynamic_symbols"]=[line.strip()[:300] for line in symbols.splitlines()
             if re.search(r"mrpcs|TssSDK|TP2|tss_sdk|tp2_|anogs|anort|tersafe|JNI_OnLoad",line,re.I)][:90]
        build=safe_run(["readelf","-nW",str(p)],limit=80)
        entry["build_id"]=(re.findall(r"Build ID:\s*(\S+)",build)or[None])[0]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--game",choices=["pubg","naruto"],required=True)
    args=ap.parse_args()
    conf={"pubg":PUBG,"naruto":NARUTO}[args.game]
    base=ROOT/"out"/conf["id"]
    rep=base/"reports"
    packdir=base/"packs"
    rep.mkdir(parents=True,exist_ok=True)
    packdir.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=f"ace_{conf['id']}_") as t:
        tmp=Path(t)
        apk=reconstruct(conf,tmp)
        with zipfile.ZipFile(apk) as zf:
            all_so=[x for x in zf.infolist() if re.fullmatch(r"lib/[^/]+/[^/]+\.so",x.filename,re.I)]
            catalog=[{"path":x.filename,"bytes":x.file_size,"compressed_bytes":x.compress_size,
                      "is_focus":bool(FOCUS_NAME.match(Path(x.filename).name))}
                     for x in all_so]
            focus=[x for x in all_so if FOCUS_NAME.match(Path(x.filename).name)]
            tracked_assets=[{"file":x.filename,"bytes":x.file_size} for x in zf.infolist()
                if re.search(r"mrpcs|vmrpcs|tersafe|anogs|anort|tprt|ace_shell",x.filename,re.I)][:100]
            result={"game":conf["game"],"version":conf["version"],"package":conf["package"],
                    "source":conf["source"],"apk_sha256":conf["apk_sha256"],
                    "apk_size":conf["apk_size"],"is_base_apk":args.game=="pubg",
                    "abis":sorted({x.filename.split("/")[1] for x in all_so}),
                    "lib_count":len(all_so),"so_catalog":catalog,
                    "focus":[],"asset_path_hits":tracked_assets,
                    "notes":["This is APK-only static evidence; OBB, online updates and runtime libraries were not examined.",
                            "Code or rule strings do not by themselves establish a cloud-delivered coordinate-decryption shellcode."]}
            extracted=[]
            for info in focus:
                entry={"apk_path":info.filename,"file":Path(info.filename).name,
                       "abi":info.filename.split("/")[1],"bytes":info.file_size,
                       "compressed_bytes":info.compress_size}
                if info.file_size>LIMIT_RAW_SO:
                    entry["omitted_binary"]="Over 70 MiB raw; not uploaded by design"
                else:
                    p=tmp / f"{entry['abi']}_{entry['file']}"
                    with zf.open(info) as src, open(p,"wb") as dst:
                        shutil.copyfileobj(src,dst,8*1024*1024)
                    inspect_lib(p,entry)
                    extracted.append((entry,p))
                result["focus"].append(entry)
                print("SECURITY LIB",entry["apk_path"],"bytes",entry["bytes"],
                      "MRPCS",entry.get("static_hits",{}).get("mrpcs",{}).get("count",0),
                      "sha256",entry.get("sha256","not exported"),flush=True)
            with open(rep/"SO_CATALOG.csv","w",newline="") as f:
                writer=csv.DictWriter(f,fieldnames=["path","bytes","compressed_bytes","is_focus"])
                writer.writeheader()
                writer.writerows(catalog)
            (rep/"analysis.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
            lines=[f"# {conf['game']} ACE / MRPCS APK 静态分析",
                   f"- 版本：{conf['version']}",
                   f"- 包名：{conf['package']}",
                   f"- APK SHA256：\`{conf['apk_sha256']}\`",
                   f"- APK 大小：{conf['apk_size']} bytes",
                   f"- 原始库条目：{len(all_so)}",
                   f"- ABI：{', '.join(result['abis'])}",
                   f"- 目标安全库：{len(focus)}",
                   "", "| 库（路径） | bytes | SHA256 | MRPCS hits | 相关字符串 |",
                   "|---|---:|---|---:|---|"]
            for e in result["focus"]:
                h=e.get("static_hits",{})
                lines.append("| " + " | ".join([
                    e["apk_path"],str(e["bytes"]),e.get("sha256","omitted"),
                    str(h.get("mrpcs",{}).get("count",0)),
                    ", ".join(k for k in h if k.lower() in ("mrpcs","vmrpcs","anogs","anort","tersafe","tprt","shellcode"))
                ]) + " |")
            lines += ["","## 证据边界",
                      "本次仅静态读取 Base APK/APK 的目录、ELF 动态表、导出符号和明文字符串。",
                      "没有检查热更新、OBB、动态解密页面、匿名执行映射及服务端资源。",
                      "MRPCS/VMRPCS 或 shellcode 命名文本的存在不等于确证坐标加密云下发实现。",
                      f"APK SHA256 和缓存 Artifact SHA256 均已在 Actions 校验。"]
            (rep/"REPORT.md").write_text("\n".join(lines)+"\n")
            # Make individually small, validated transport packages.
            packs=[]
            total_raw=0
            pack_no=0
            archive=None
            for entry,p in extracted:
                if archive is None or total_raw + p.stat().st_size > MAX_PACK_RAW:
                    if archive:
                        archive.close()
                    dest=packdir/f"ace-libs-{pack_no:02d}.zip"
                    archive=zipfile.ZipFile(dest,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=5)
                    packs.append(dest)
                    pack_no+=1
                    total_raw=0
                archive.write(p,arcname=f"lib/{entry['abi']}/{entry['file']}")
                total_raw+=p.stat().st_size
            if archive:
                archive.close()
            man={"game":conf["game"],"apk_sha256":conf["apk_sha256"],
                 "packs":[{"filename":p.name,"size":p.stat().st_size,"sha256":digest(p)} for p in packs],
                 "files":[{"path":e["apk_path"],"sha256":e["sha256"],"size":e["bytes"]} for e,p in extracted]}
            assert all(p.stat().st_size < 95*1024*1024 for p in packs)
            (rep/"PACK_MANIFEST.json").write_text(json.dumps(man,indent=2,ensure_ascii=False)+"\n")
            print("FINAL",args.game,"focus_count",len(focus),"packs",json.dumps(man["packs"]),flush=True)

if __name__=="__main__":
    main()
