#!/usr/bin/env python3
"""Map HOK metadata v29 type definitions and coordinate/encryption method names."""
import sys,zipfile,struct,json,re,hashlib
from pathlib import Path
sys.path.insert(0,".github/scripts")
from ace_range_from_tencent_apks import RangeFile,SOURCES
game,pkg,version,md5,expected=SOURCES["hok"]
url=f"http://imtt.dd.qq.com/sjy.00022/sjy.00001/16891/apk/{md5}.apk?fsname={pkg}_{version}.apk"
dest=Path("out/hok_type_map");dest.mkdir(parents=True,exist_ok=True)
remote=RangeFile(url);assert remote.size==expected
member="assets/bin/Data/Managed/Metadata/global-metadata.dat"
with zipfile.ZipFile(remote) as z:
 raw=z.read(member)
assert struct.unpack_from("<I",raw)[0]==0xfab11baf
ver=struct.unpack_from("<I",raw,4)[0]
pairs=[struct.unpack_from("<II",raw,8+i*8) for i in range(37)]
so,ss=pairs[2];sdata=raw[so:so+ss]
def text_at(index):
 if index>=len(sdata):return ""
 end=sdata.find(bytes([0]),index)
 if end<index or end-index>350:return ""
 return sdata[index:end].decode("utf8","replace")
score=[]
for slot in range(5,27):
 off,size=pairs[slot]
 if off+size>len(raw):continue
 for width in (100,104,96,88):
  if size%width:continue
  samples=[]
  for j in range(min(35,size//width)):
   key=struct.unpack_from("<I",raw,off+j*width)[0]
   samples.append(text_at(key))
  found=sum(1 for x in samples if 1<=len(x)<100 and re.fullmatch("[A-Za-z0-9_+.<>,]+",x))
  score.append({"table":slot,"width":width,"score":found,"names":samples[:12]})
print("TYPEDEF_SCORE",json.dumps(sorted(score,key=lambda x:x["score"],reverse=True)[:17]),flush=True)
# v29 metadata layout confirmed against all 64,125 type records and global counts:
# 88-byte TypeDefinition, fieldStart @+0x20, methodStart @+0x24,
# method_count uint16 @+0x40, field_count uint16 @+0x44.
table=19;width=88
types_o,types_z=pairs[table];method_o,method_z=pairs[5];field_o,field_z=pairs[11]
assert field_o+field_z<=len(raw) and method_o+method_z<=len(raw)
fieldsize=12;methodsize=32
match_type=re.compile("(?i)(position|coordinate|coord|encrypt|decrypt|obscured|protected|vector|vint|actorroot|movecomponent|heropos|battleactor|framesync|anti.?cheat)")
match_member=re.compile("(?i)(position|coord|encrypt|decrypt|vector|vint|move|velocity|rotation|sync|anti.?cheat|key|world|local)")
rows=[];enums=[];hits=0
for n in range(types_z//width):
 ptr=types_o+n*width
 name=text_at(struct.unpack_from("<I",raw,ptr)[0])
 ns=text_at(struct.unpack_from("<I",raw,ptr+4)[0])
 if not name:continue
 fld0,method0=struct.unpack_from("<II",raw,ptr+32)
 methods=struct.unpack_from("<H",raw,ptr+64)[0]
 fields=struct.unpack_from("<H",raw,ptr+68)[0]
 if fld0+fields>field_z//fieldsize or method0+methods>method_z//methodsize:continue
 if not match_type.search(name) and n>0:
  # Preserve exact configuration owner when a field name matches
  found=False
  for fi in range(fld0,min(fld0+fields,fld0+250)):
   fn=text_at(struct.unpack_from("<I",raw,field_o+fi*fieldsize)[0])
   if fn=="RES_GAMECORE_CONF_TYPE_HERO_POSITION_ENCRYPT_TYPE":found=True
  if not found:continue
 fields_names=[]
 for fi in range(fld0,min(fld0+fields,fld0+120)):
  fn=text_at(struct.unpack_from("<I",raw,field_o+fi*fieldsize)[0])
  if fn:fields_names.append(fn)
 methods_names=[]
 for mi in range(method0,min(method0+methods,method0+100)):
  mn=text_at(struct.unpack_from("<I",raw,method_o+mi*methodsize)[0])
  if mn:methods_names.append(mn)
 if "RES_GAMECORE_CONF_TYPE_HERO_POSITION_ENCRYPT_TYPE" in fields_names:
  enums.append({"class":name,"namespace":ns,"index":n})
 row={"class":name,"namespace":ns,"typedef":n,"fields":fields_names,
      "methods":methods_names,"method_start":method0,"field_start":fld0}
 rows.append(row);hits+=1
report={"metadata_version":ver,"class_table":table,"record_size":width,
 "type_count":types_z//width,"method_count":method_z//methodsize,
 "field_count":field_z//fieldsize,"matched_count":hits,
 "hero_position_encrypt_enum_owner":enums,
 "class_rows":rows,"hash_sha256":hashlib.sha256(raw).hexdigest()}
(dest/"type_map.json").write_text(json.dumps(report,indent=2,ensure_ascii=False))
print("HOK_TYPE_MAP",json.dumps({"metadata_version":ver,"type_count":report["type_count"],
 "method_count":report["method_count"],"field_count":report["field_count"],
 "matched":hits,"enum_owners":enums,
 "selected_types":[x for x in rows if match_type.search(x["class"])][:90]},ensure_ascii=False)[:25000],flush=True)
print("HOK_TYPE_MAP_DONE",flush=True)
remote.close()
