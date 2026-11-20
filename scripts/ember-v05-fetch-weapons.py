import pathlib, urllib.request, urllib.parse, http.cookiejar, zipfile, gzip, json, hashlib, re, shutil
root = pathlib.Path("weapon-candidates")
root.mkdir()
records = []
errors = []
def fetch(url, target, session=None):
    target = pathlib.Path(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent":"EmberAssetResearch/0.5"})
    with (session.open(req,timeout=90) if session else urllib.request.urlopen(req,timeout=90)) as response, target.open("wb") as out:
        shutil.copyfileobj(response,out)
    return target
def record(name, url, path, license):
    records.append({"name":name,"source":url,"path":str(path.relative_to(root)),"license":license,"size":path.stat().st_size,"sha256":hashlib.sha256(path.read_bytes()).hexdigest()})
direct = [
 ("SCAR-L","https://raw.githubusercontent.com/AetherRadar/operation-steel-tide/main/assets/models/steel_tide_scarl/scarl_reloadable.glb","scar/scarl_reloadable.glb","CC BY 3.0"),
 ("SCAR-L credits","https://raw.githubusercontent.com/AetherRadar/operation-steel-tide/main/assets/models/steel_tide_scarl/LICENSE.md","scar/LICENSE.md","CC BY 3.0"),
 ("AK47","https://raw.githubusercontent.com/AetherRadar/operation-steel-tide/main/assets/models/steel_tide_ak74/ak47_reloadable_world.glb","ak47/ak47_reloadable.glb","CC0 geometry; MIT replacement textures"),
 ("AK47 credits","https://raw.githubusercontent.com/AetherRadar/operation-steel-tide/main/assets/models/steel_tide_ak74/LICENSE.md","ak47/LICENSE.md","CC0 + MIT"),
 ("Derivative source license","https://raw.githubusercontent.com/AetherRadar/operation-steel-tide/main/LICENSE","source-LICENSE","MIT"),
]
for name,url,relative,license in direct:
    try:
        path=fetch(url,root/relative)
        record(name,url,path,license)
    except Exception as error:
        errors.append({"name":name,"error":str(error)})
uids = {
 "059e968f6f764357880807c62c117ab7":"hk416_tastytony",
 "a16768f0ffa24737a4fe324a411cfbd9":"hk416_a7_r4m",
 "9c05037d7d114ff28a82d8a83003b2bd":"hk416_a7_burner",
 "0e3c0c7f6c6b4f98bc278b3b310d234b":"kar98_berk",
 "d1b203a857e645fdbf086244e73fa258":"kar98_danscrivy",
}
base="https://huggingface.co/datasets/allenai/objaverse/resolve/main/"
mapping_path=fetch(base+"object-paths.json.gz",root/"object-paths.json.gz")
mapping=json.loads(gzip.decompress(mapping_path.read_bytes()))
matched={}
metadata={}
for uid,name in uids.items():
    path=mapping.get(uid)
    if not path:
        errors.append({"name":name,"error":"UID absent from Objaverse archive"})
        continue
    matched[uid]=path
    try:
        target=fetch(base+path,root/name/"model.glb")
        record(name,base+path,target,"Verify corresponding annotation before use")
        group=path.split("/")[-2]
        if group not in metadata:
            meta_path=fetch(base+"metadata/"+group+".json.gz",root/"metadata"/(group+".json.gz"))
            metadata[group]=json.loads(gzip.decompress(meta_path.read_bytes()))
        annotation=metadata[group].get(uid)
        if annotation is not None:
            (root/name/"annotation.json").write_text(json.dumps(annotation,indent=2))
    except Exception as error:
        errors.append({"name":name,"error":str(error)})
(root/"objaverse-matches.json").write_text(json.dumps(matched,indent=2))
page="https://hamsunqiu.itch.io/modern-military-weapons-sound-pack-38-wav-cc0"
try:
    session=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
    html_path=fetch(page,root/"sound-pack-page.html",session)
    html=html_path.read_text()
    uploads=list(dict.fromkeys(re.findall(r'data-upload_id=["\\\'](\\d+)',html)))
    csrf_match=re.search(r'name=["\\\']csrf_token["\\\'][^>]*value=["\\\']([^"\\\']+)',html)
    csrf=csrf_match.group(1) if csrf_match else ""
    if not uploads:
        raise RuntimeError("No public download upload_id in author page")
    success=False
    for upload in uploads:
        endpoint=page+"/file/"+upload+"?source=view_game&as_props=1"
        request=urllib.request.Request(endpoint,data=urllib.parse.urlencode({"csrf_token":csrf}).encode(),headers={"Referer":page,"X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0"})
        with session.open(request,timeout=60) as response:
            answer=json.loads(response.read())
        url=answer.get("url")
        if not url:
            continue
        target=fetch(url,root/"audio/military_sfx_pack_v0.2.zip",session)
        with zipfile.ZipFile(target) as z:
            if z.testzip() is not None:
                raise RuntimeError("Sound pack ZIP CRC failure")
        record("Modern Military Weapons Sound Pack v0.2",page,target,"CC0; inspect SOURCES_CC0.txt")
        success=True
        break
    if not success:
        raise RuntimeError("Public download endpoint did not return a ZIP URL")
except Exception as error:
    errors.append({"name":"military_sfx_pack_v0.2","error":str(error)})
(root/"manifest.json").write_text(json.dumps({"records":records,"errors":errors},indent=2))
bundle=pathlib.Path("ember-weapon-candidates-v05.zip")
with zipfile.ZipFile(bundle,"w",zipfile.ZIP_DEFLATED) as z:
    for path in sorted(root.rglob("*")):
        if path.is_file():
            z.write(path,path.relative_to(root))
parts=pathlib.Path("parts")
parts.mkdir()
chunk=90*1024*1024
with bundle.open("rb") as source:
    index=0
    while True:
        data=source.read(chunk)
        if not data: break
        (parts/("bundle.part%02d"%index)).write_bytes(data)
        index+=1
if index>8: raise RuntimeError("Bundle exceeds declared part capacity")
summary={"file":bundle.name,"size":bundle.stat().st_size,"sha256":hashlib.sha256(bundle.read_bytes()).hexdigest(),"parts":[{"file":p.name,"size":p.stat().st_size,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(parts.iterdir())],"records":records,"errors":errors}
pathlib.Path("bundle-manifest.json").write_text(json.dumps(summary,indent=2))
print(json.dumps(summary,indent=2))
