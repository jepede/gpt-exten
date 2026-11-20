import pathlib,urllib.request,urllib.parse,http.cookiejar,zipfile,json,gzip,hashlib,zlib,struct,os,shutil,re
out=pathlib.Path("inputs")
out.mkdir()
records=[]
errors=[]
def request(url,headers=None,data=None):
    return urllib.request.urlopen(urllib.request.Request(url,headers=headers or {"User-Agent":"EmberAssets/0.5"},data=data),timeout=75)
def fetch(url,path,session=None):
    path.parent.mkdir(parents=True,exist_ok=True)
    with (session.open(urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0"}),timeout=90) if session else request(url)) as r,path.open("wb") as f:
        shutil.copyfileobj(r,f)
    return path
def record(name,url,path,license):
    records.append({"name":name,"source":url,"path":str(path.relative_to(out)),"license":license,"size":path.stat().st_size,"sha256":hashlib.sha256(path.read_bytes()).hexdigest()})
api="https://api.github.com/repos/jepede/gpt-exten/actions/runs/44675490981"
headers={"Authorization":"Bearer "+os.environ["GH_TOKEN"],"Accept":"application/vnd.github+json"}
with request(api,headers) as r: previous=json.load(r)
reuse_hair=previous["status"]=="completed" and previous["conclusion"]=="success"
if not reuse_hair and previous["status"]!="completed":
    try:
        with request(api+"/cancel",headers,b"") as r: print("Cancelled incomplete whole-archive transfer",r.status)
    except urllib.error.HTTPError as error:
        if error.code!=409: raise
if reuse_hair:
    print("Previous hair artifact completed: reuse run 44675490981; no repeated upstream hair download")
else:
    source="https://files2.makehumancommunity.org/asset_packs/makehuman_system_assets/makehuman_system_assets_cc0.zip"
    entries=[{"name":"hair/short03/short03.thumb","offset":243543800,"size":38550,"method":8,"crc":3744815383,"raw_size":39414},{"name":"hair/short03/short03_diffuse.png","offset":243582434,"size":2379485,"method":8,"crc":4065313520,"raw_size":2392930},{"name":"hair/short03/short03.obj","offset":245962009,"size":27104,"method":8,"crc":2661580316,"raw_size":74766},{"name":"hair/short03/short03.mhclo","offset":245989195,"size":25622,"method":8,"crc":1860339413,"raw_size":69048},{"name":"hair/short03/short03.mhmat","offset":246014901,"size":634,"method":8,"crc":2108287408,"raw_size":1309},{"name":"hair/ponytail01/ponytail01.obj","offset":250564341,"size":87120,"method":8,"crc":2835480296,"raw_size":264384},{"name":"hair/ponytail01/ponytail01_diffuse.png","offset":250651549,"size":3906581,"method":8,"crc":3412443288,"raw_size":3910782},{"name":"hair/ponytail01/ponytail01.mhclo","offset":254558226,"size":82028,"method":8,"crc":1792184878,"raw_size":252080},{"name":"hair/ponytail01/ponytail01.thumb","offset":254640344,"size":47809,"method":8,"crc":3114122810,"raw_size":47981},{"name":"hair/ponytail01/ponytail01.mhmat","offset":254688243,"size":631,"method":8,"crc":1099673810,"raw_size":1305},{"name":"hair/short02/short02.thumb","offset":254689035,"size":40255,"method":8,"crc":1543425394,"raw_size":41127},{"name":"hair/short02/short02.obj","offset":254729374,"size":50161,"method":8,"crc":1005823987,"raw_size":139742},{"name":"hair/short02/short02.mhclo","offset":254779617,"size":43333,"method":8,"crc":377146603,"raw_size":119240},{"name":"hair/short02/short02.mhmat","offset":254823034,"size":644,"method":8,"crc":367839644,"raw_size":1323},{"name":"hair/short02/short02_diffuse.png","offset":254823762,"size":3526253,"method":8,"crc":1488863504,"raw_size":3553543},{"name":"hair/short02/short02_normal.png","offset":258350105,"size":1608604,"method":8,"crc":3449626045,"raw_size":1626745},{"name":"hair/short04/short04.mhmat","offset":265877064,"size":641,"method":8,"crc":937100313,"raw_size":1316},{"name":"hair/short04/short04.obj","offset":265877789,"size":20042,"method":8,"crc":485057326,"raw_size":55152},{"name":"hair/short04/short04.mhclo","offset":265897913,"size":20793,"method":8,"crc":4246018849,"raw_size":59195},{"name":"hair/short04/short04_diffuse.png","offset":265918790,"size":2294596,"method":8,"crc":1505717266,"raw_size":2308132},{"name":"hair/short04/short04.thumb","offset":268213476,"size":40914,"method":8,"crc":1516849492,"raw_size":41792}]
    def byte_range(start,end):
        with request(source,{"Range":"bytes=%d-%d"%(start,end),"User-Agent":"EmberAssetRanges/0.5"}) as r:
            if r.status!=206: raise RuntimeError("Upstream does not honor byte ranges")
            data=r.read()
        if len(data)!=end-start+1: raise RuntimeError("Incomplete range")
        return data
    for entry in entries:
        header=byte_range(entry["offset"],entry["offset"]+29)
        fields=struct.unpack("<4s5H3I2H",header)
        if fields[0]!=bytes([80,75,3,4]): raise RuntimeError("ZIP header mismatch")
        start=entry["offset"]+30+fields[-2]+fields[-1]
        packed=byte_range(start,start+entry["size"]-1)
        raw=zlib.decompress(packed,-15) if entry["method"]==8 else packed
        if len(raw)!=entry["raw_size"] or zlib.crc32(raw)&0xffffffff!=entry["crc"]: raise RuntimeError("Hair CRC mismatch")
        path=out/entry["name"]
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_bytes(raw)
        record(entry["name"],source,path,"CC0 MakeHuman system assets")
    print("Selected hair data complete")
base="https://huggingface.co/datasets/allenai/objaverse/resolve/main/"
uid="48141819356643559761da09dd9e7841"
model=fetch(base+"glbs/000-123/"+uid+".glb",out/"scar_detailed/model.glb")
record("SCAR L by Daniel Abeleira",base+"glbs/000-123/"+uid+".glb",model,"Verify embedded CC-BY and annotation")
meta=fetch(base+"metadata/000-123.json.gz",out/"scar_detailed/source-metadata.json.gz")
annotation=json.loads(gzip.decompress(meta.read_bytes()))[uid]
(out/"scar_detailed/annotation.json").write_text(json.dumps(annotation,indent=2))
page="https://hamsunqiu.itch.io/modern-military-weapons-sound-pack-38-wav-cc0"
try:
    session=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
    html_file=fetch(page,out/"audio/source-page.html",session)
    html=html_file.read_text()
    ids=re.findall('data-upload_id="([0-9]+)"',html)
    csrf_match=re.search('name="csrf_token"[^>]*(?:value|content)="([^"]+)"',html)
    csrf=csrf_match.group(1) if csrf_match else ""
    if not ids: raise RuntimeError("Public audio upload ID missing")
    upload="20022029" if "20022029" in ids else ids[0]
    endpoint=page+"/file/"+upload+"?source=view_game&as_props=1"
    req=urllib.request.Request(endpoint,data=urllib.parse.urlencode({"csrf_token":csrf}).encode(),headers={"Referer":page,"X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0"})
    with session.open(req,timeout=75) as r: result=json.load(r)
    if not result.get("url"): raise RuntimeError("No public audio download URL; keys "+str(list(result)))
    audio=fetch(result["url"],out/"audio/military_sfx_pack_v0.2.zip",session)
    with zipfile.ZipFile(audio) as z:
        if z.testzip() is not None: raise RuntimeError("Audio CRC mismatch")
    record("Modern Military Weapons Sound Pack v0.2",page,audio,"CC0; SOURCES_CC0.txt included")
except Exception as error:
    errors.append({"name":"sound pack","error":str(error)})
manifest={"version":"ember-realism-inputs-v05-20261120","hair_reuse_previous_run":reuse_hair,"records":records,"errors":errors}
(out/"manifest.json").write_text(json.dumps(manifest,indent=2))
bundle=pathlib.Path("ember-realism-inputs-v05.zip")
with zipfile.ZipFile(bundle,"w",zipfile.ZIP_DEFLATED) as z:
    for p in sorted(out.rglob("*")):
        if p.is_file(): z.write(p,p.relative_to(out))
if bundle.stat().st_size>=90*1024*1024: raise RuntimeError("Bundle requires part splitting")
summary={"file":bundle.name,"size":bundle.stat().st_size,"sha256":hashlib.sha256(bundle.read_bytes()).hexdigest(),**manifest}
pathlib.Path("input-manifest.json").write_text(json.dumps(summary,indent=2))
print(json.dumps({"size":summary["size"],"sha256":summary["sha256"],"files":len(records),"errors":errors,"hair_reused":reuse_hair}))
