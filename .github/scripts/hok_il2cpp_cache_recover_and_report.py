#!/usr/bin/env python3
"""Restore already-verified HoK native archives from GitHub Artifacts, run IL2CPP Dumper
outside this script, then generate deterministic coordinate method summary.
"""
import sys,os,re,json,hashlib,subprocess,zipfile,shutil,collections
from pathlib import Path
ROOT=Path("work/hok_native");ROOT.mkdir(parents=True,exist_ok=True)
REPO=os.environ.get("GITHUB_REPOSITORY","jepede/gpt-exten")
REC=json.loads(Path("reports/hok_20261026/artifact_cache_index.json").read_text())
MAN=json.loads(Path("reports/hok_20261026/portable_archive_manifest.json").read_text())
def digest(path):
 h=hashlib.sha256()
 with open(path,"rb") as f:
  for b in iter(lambda:f.read(8<<20),b""):h.update(b)
 return h.hexdigest()
def download_cached(selected=None):
 for key,record in REC.items():
  if key=="report" or (selected is not None and key not in selected):continue
  member=next(x for x in MAN["files"] if x["portable_archive"].endswith("-"+key+".zip"))
  orig=ROOT/member["path"]
  if orig.is_file() and orig.stat().st_size==member["size"] and digest(orig)==member["sha256"]:
   print("REUSE_LOCAL",member["path"],flush=True);continue
  orig.parent.mkdir(parents=True,exist_ok=True)
  zipout=ROOT/("outer_"+key+".zip")
  url=f"https://api.github.com/repos/{REPO}/actions/artifacts/{record['id']}/zip"
  p=subprocess.run(["curl","--fail","--location","--retry","5","--retry-all-errors",
                    "--connect-timeout","30","--max-time","1000","--silent","--show-error",
                    "-H","Authorization: Bearer "+os.environ["GH_TOKEN"],
                    "-H","Accept: application/vnd.github+json","-o",str(zipout),url])
  assert p.returncode==0,("HTTP transport",key,p.returncode)
  required=record["digest"].split(":",1)[-1]
  assert digest(zipout)==required,("outer SHA mismatch",key)
  with zipfile.ZipFile(zipout) as container:
   infos=[x for x in container.infolist() if x.filename.endswith(member["portable_archive"])]
   assert len(infos)==1,(key,[x.filename for x in container.infolist()])
   inner=ROOT/member["portable_archive"]
   with container.open(infos[0]) as src,inner.open("wb") as dest:
    shutil.copyfileobj(src,dest,8<<20)
  assert digest(inner)==member["archive_sha256"],("inner SHA",key)
  with zipfile.ZipFile(inner) as z:
   info=z.getinfo(member["path"])
   assert format(info.CRC,"08x")==member["crc32"]
   with z.open(info) as fi,orig.open("wb") as fo:shutil.copyfileobj(fi,fo,8<<20)
  assert orig.stat().st_size==member["size"] and digest(orig)==member["sha256"]
  print("CACHE_RESTORED_VERIFIED",key,str(orig),orig.stat().st_size,member["sha256"],flush=True)
  zipout.unlink();inner.unlink()
def report_dumper():
 folder=Path("work/il2cppdump")
 dest=Path("reports/hok_20261026/il2cpp")
 dest.mkdir(parents=True,exist_ok=True)
 errors=[]
 output=folder/"dump.cs"
 if not output.exists():
  errors.append("Il2CppDumper dump.cs missing: binary code registration may be protected.")
 else:
  text=output.read_text("utf8","replace")
  lines=text.splitlines()
  relevant=[]
  groups=[]
  rclass=re.compile(r"\b(?:class|struct|enum|interface)\s+(\w+)")
  keys=re.compile(r"Actor|Hero|Battle|Position|Vector|Coord|Move|FrameSync|ViewManager|FogOfWar|Encrypt|Decrypt|Fixed|LogicPos|WorldPos|NetPos|Skill",re.I)
  namespace=""
  buf=[]
  current=""
  def flush():
   if buf and (keys.search(current) or keys.search(namespace)):
    # filter within known large namespaces; prioritize class names.
    if keys.search(current):
     groups.append({"namespace":namespace,"name":current,"sample":buf[:250]})
  for line in lines:
   if line.startswith("// Namespace:"):
    flush();buf=[];namespace=line.split(":",1)[-1].strip();current=""
   elif line.lstrip().startswith("public class ") or line.lstrip().startswith("public struct ") or line.lstrip().startswith("public sealed class ") or line.lstrip().startswith("public enum ") or line.lstrip().startswith("internal class ") or line.lstrip().startswith("internal struct "):
    flush();buf=[];m=rclass.search(line);current=m.group(1) if m else line.strip()[:90]
   elif current:
    if len(buf)<300:buf.append(line)
  flush()
  groups.sort(key=lambda v:(0 if re.search(r"(?:Position|Coord|Encrypt|Decrypt|VInt3|ActorRoot|ViewManager|Logic)",v["name"],re.I) else 1, v["name"]))
  top=groups[:500]
  (dest/"coordinate_recovered_classes.json").write_text(json.dumps(top,ensure_ascii=False,indent=2))
  linesout=["# Recovered HoK IL2CPP coordinate/actor type subsets","",
    f"Full dump.cs length: {len(lines):,} lines, {len(text):,} chars",
    f"Candidate classes: {len(groups)}. Showing {len(top)} most relevant.",
    "Class names and method RVAs extracted from Il2CppDumper; method bodies still require ARM64 analysis.",
    ""]
  for item in top[:220]:
   linesout+=["","## "+item["namespace"]+"::"+item["name"],"~~~csharp"]
   linesout.extend(item["sample"][:100])
   linesout+=["~~~"]
  (dest/"coordinate_recovered_classes.md").write_text("\n".join(linesout)+"\n")
  print("DUMP_PARSED",len(lines),"classes",len(groups),"selected",len(top),flush=True)
  # keep full dump.cs as a compressed source-reference artifact; user gets it even if this chat sandbox fails
  zipped=Path("out/hok_coord/il2cpp_reconstructed.zip")
  zipped.parent.mkdir(parents=True,exist_ok=True)
  with zipfile.ZipFile(zipped,"w",zipfile.ZIP_DEFLATED,compresslevel=6) as z:
   for p in [output,folder/"script.json",folder/"stringliteral.json"]:
    if p.exists():z.write(p,arcname=p.name)
  print("IL2CPP_REFERENCE_BUNDLE",str(zipped),zipped.stat().st_size,flush=True)
  assert zipped.stat().st_size<95000000
 (dest/"limitations.json").write_text(json.dumps({"warnings":errors,"full_dump_present":output.exists()},indent=2))
def plain_metadata_summary():
 dst=Path("reports/hok_20261026/il2cpp");dst.mkdir(parents=True,exist_ok=True)
 p=ROOT/"assets/bin/Data/Managed/Metadata/global-metadata.dat"
 b=p.read_bytes()
 sanity=int.from_bytes(b[:4],"little");version=int.from_bytes(b[4:8],"little")
 assert sanity==0xfab11baf and version==29
 import re
 needle=re.compile(rb"[\x20-\x7e]{4,165}\x00")
 keys=re.compile(rb"Actor|Hero|Logic|Pos|Coord|Vector|Move|Battle|Sync|Encrypt|Decrypt|Fow|ViewManager|Transform",re.I)
 hits=[]
 for x in needle.finditer(b):
  value=x.group()[:-1]
  if keys.search(value):
   hits.append({"offset":hex(x.start()),"text":value.decode("utf8","replace")})
 # Keep de-duplicated names without declaring that all are types
 unique={}
 for x in hits:unique.setdefault(x["text"],x)
 (dst/"metadata_symbol_candidates.json").write_text(json.dumps({"magic":hex(sanity),"version":version,"all_hits":len(hits),
  "unique":len(unique),"candidates":list(unique.values())[:4500]},ensure_ascii=False,indent=2))
 keys2=["GetActorLogicPos","SetActorLogicPos","VInt3","Position","WorldPosition","FogOfWar","ViewManager","MoveDir","Coordinate","EncryptPosition","DecryptPosition"]
 print("METADATA_CANDIDATES",json.dumps({k:sum(k.lower() in x.lower() for x in unique) for k in keys2}),flush=True)
if __name__=="__main__":
 mode=sys.argv[1]
 if mode=="download":download_cached(set(sys.argv[2:]) if len(sys.argv)>2 else None)
 elif mode=="report":report_dumper();plain_metadata_summary()
 else:raise SystemExit("expected download|report")
