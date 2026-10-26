#!/usr/bin/env python3
"""Locate exact HOK IL2CPP metadata field owners and native-relevant coordinate/encryption types.
Static evidence only, read-only source APK byte-range access.
"""
import bisect,json,re,struct,sys,zipfile
from pathlib import Path
sys.path.insert(0,".github/scripts")
from ace_range_from_tencent_apks import RangeFile,SOURCES
_,pkg,version,md5,size=SOURCES["hok"]
url=f"http://imtt.dd.qq.com/sjy.00022/sjy.00001/16891/apk/{md5}.apk?fsname={pkg}_{version}.apk"
out=Path("out/hok_coord_owner");out.mkdir(parents=True,exist_ok=True)
r=RangeFile(url);assert r.size==size
with zipfile.ZipFile(r) as z:data=z.read("assets/bin/Data/Managed/Metadata/global-metadata.dat")
assert struct.unpack_from("<I",data,0)[0]==0xfab11baf
pairs=[struct.unpack_from("<II",data,8+i*8) for i in range(35)]
stringo,stringlen=pairs[2];strings=data[stringo:stringo+stringlen]
fieldo,fieldlen=pairs[11];typeo,typelen=pairs[19];methodo,methodlen=pairs[5]
assert typelen%88==0 and fieldlen%12==0 and methodlen%32==0
def getstr(i):
 if i<0 or i>=len(strings):return ""
 end=strings.find(b"\0",i)
 if end<0 or end-i>400:return ""
 return strings[i:end].decode("utf8","replace")
fields=[]
for i in range(fieldlen//12):
 nameidx=struct.unpack_from("<I",data,fieldo+i*12)[0]
 fields.append(getstr(nameidx))
types=[]
for i in range(typelen//88):
 off=typeo+i*88
 nameidx,nsidx=struct.unpack_from("<II",data,off)
 fstart,mstart=struct.unpack_from("<II",data,off+32)
 mcount,fcount=struct.unpack_from("<HH",data,off+64)
 types.append({"type_index":i,"name":getstr(nameidx),"namespace":getstr(nsidx),
               "field_start":fstart,"field_count":fcount,"method_start":mstart,"method_count":mcount})
by_name={q["name"]:q for q in types if q["name"]}
exact="RES_GAMECORE_CONF_TYPE_HERO_POSITION_ENCRYPT_TYPE"
targets=[i for i,x in enumerate(fields) if exact in x or re.search(r"(?i)(hero.*pos.*encrypt|position.*encrypt|encrypt.*position|encrypt.*coord|coord.*encrypt|position.*decryp|decrypt.*position)",x)]
def owners_for(index):
 return [q for q in types if q["field_start"]<=index<q["field_start"]+q["field_count"]]
owner_rows=[]
for fidx in targets:
 for typ in owners_for(fidx):
  a,b=typ["field_start"],typ["field_start"]+typ["field_count"]
  q=dict(typ);q["matched_field"]=fields[fidx];q["field_index"]=fidx
  q["other_matching_fields"]=[x for x in fields[a:b] if re.search(r"(?i)(encrypt|decrypt|position|coord|safe|guard|anti)",x)][:180]
  q["fields_neighbors"]=fields[max(a,fidx-10):min(b,fidx+11)]
  owner_rows.append(q)
regex=re.compile(r"(?i)(encrypt|decrypt|safevector|encvector|positioncrypt|positionencrypt|vec3|vint3|frame.*sync|mov(e|ement).*component|actor.*root|hero.*position)")
name_candidates=[]
for q in types:
 if regex.search(q["name"]):
  v=dict(q)
  a=q["field_start"];b=a+q["field_count"]
  v["fields"]=fields[a:min(b,a+70)] if a< len(fields) else []
  name_candidates.append(v)
summary={
 "IL2CPP_version":struct.unpack_from("<I",data,4)[0],
 "type_count":len(types),"field_count":len(fields),"method_count":methodlen//32,
 "exact_key":exact,"exact_string_occurrences_in_string_table":strings.count(exact.encode()),
 "matched_field_count":len(targets),"matching_field_indices":targets,
 "owners":owner_rows,"candidate_types":name_candidates[:900],
}
(out/"owner.json").write_text(json.dumps(summary,ensure_ascii=False,indent=2))
print("HOK_CONFIG_OWNER",json.dumps({"match_count":len(targets),"owners":owner_rows},ensure_ascii=False)[:19000],flush=True)
print("HOK_RELEVANT_TYPES",json.dumps(name_candidates[:120],ensure_ascii=False)[:21000],flush=True)
print("HOK_OWNER_SUCCESS",{"class_count":len(types),"matched":len(targets),"type_names_found":len(name_candidates)},flush=True)
r.close()
