#!/usr/bin/env python3
"""Read-only exact HOK v29 IL2CPP names and member ranges for movement/coord.
Exact native code addresses require separate CodeRegistration analysis.
"""
import json,struct,sys,zipfile
from pathlib import Path
sys.path.insert(0,".github/scripts")
from ace_range_from_tencent_apks import RangeFile,SOURCES
_,pkg,ver,md5,size=SOURCES["hok"]
u=f"http://imtt.dd.qq.com/sjy.00022/sjy.00001/16891/apk/{md5}.apk?fsname={pkg}_{ver}.apk"
out=Path("out/hok_move_members");out.mkdir(parents=True,exist_ok=True)
cache=Path("work/hok_cached/global-metadata.dat")
assert cache.exists(), "Missing verified cached metadata; restore artifact first"
data=cache.read_bytes()
pairs=[struct.unpack_from("<II",data,8+i*8) for i in range(32)]
st,ss=pairs[2];string_data=data[st:st+ss]
def S(i):
 if i<0 or i>=len(string_data):return ""
 j=string_data.find(b"\0",i)
 return string_data[i:j].decode("utf8","replace") if j>=i and j-i<400 else ""
fo,fl=pairs[11];mo,ml=pairs[5];to,tl=pairs[19]
assert tl%88==0 and fl%12==0 and ml%32==0
interest={
 ("Assets.Scripts.GameLogic","MoveComponent"),
 ("","VInt3"),
 ("BluePrint.UGC.UI.Core","VInt3"),
 ("Assets.Scripts.Framework","FrameSynchr"),
 ("Assets.Scripts.GameLogic.Dimension","DimensionMoveComponent"),
 ("CSProtocolWrapper","FRAMEDT_VECTOR3"),
 ("CSProtocol","COMDT_VECTOR3"),
 ("CSProtocol","COMDT_COORDINATE"),
 ("CSProtocol","COMDT_IN_GAME_COORDINATE"),
 ("Assets.Scripts.GameLogic","GameCommonVInt3Param"),
 ("CSProtocol","COMDT_DIMENSION_MAP_ANTI_CHEAT_INFO"),
}
types=[]
for i in range(tl//88):
 p=to+88*i
 name=S(struct.unpack_from("<I",data,p)[0])
 ns=S(struct.unpack_from("<I",data,p+4)[0])
 fieldstart,methodstart=struct.unpack_from("<II",data,p+32)
 methodcount=struct.unpack_from("<H",data,p+64)[0]
 fieldcount=struct.unpack_from("<H",data,p+68)[0]
 if (ns,name) not in interest:continue
 rows={"index":i,"namespace":ns,"name":name,"method_start":methodstart,"field_start":fieldstart,
       "method_count":methodcount,"field_count":fieldcount,
       "fields":[],"methods":[]}
 if fieldstart!=0xffffffff:
  for j in range(fieldstart,min(fieldstart+fieldcount,fl//12)):
   fp=fo+j*12
   fname=S(struct.unpack_from("<I",data,fp)[0])
   typeindex=struct.unpack_from("<i",data,fp+4)[0]
   rows["fields"].append({"field_index":j,"name":fname,"type_index":typeindex})
 if methodstart!=0xffffffff:
  for j in range(methodstart,min(methodstart+methodcount,ml//32)):
   mp=mo+j*32
   mname=S(struct.unpack_from("<I",data,mp)[0])
   # declaringType pointer is not a process pointer; this is metadata method definition only
   declaring=struct.unpack_from("<i",data,mp+4)[0]
   ret_type=struct.unpack_from("<i",data,mp+8)[0]
   pstart=struct.unpack_from("<i",data,mp+12)[0]
   token=struct.unpack_from("<I",data,mp+20)[0]
   rows["methods"].append({"method_index":j,"name":mname,"declaring_type_index":declaring,
      "return_type_index":ret_type,"parameter_start":pstart,"token":hex(token)})
 types.append(rows)
# Gather global method names hinting actual position crypto, not unrelated AES/TEA packets
patterns=["PositionEncrypt","EncryptPosition","DecryptPosition","PositionDecrypt",
          "GetGameLogicPosition","GetHeroPos","GetActorPos","GetCurPosition",
          "GetRemotePosition","SetCurPosition","SetRemotePosition",
          "VInt3ToVector3","ConvertVInt3","ToVector3","GetPosition",
          "GetForward","SetPosition","GetGlobalConf"]
methods_hits={}
for needle in patterns:
 arr=[]
 for j in range(ml//32):
  idx=struct.unpack_from("<I",data,mo+j*32)[0]
  name=S(idx)
  if needle.lower() in name.lower():
   if len(arr)<65:arr.append({"method_index":j,"method":name})
 methods_hits[needle]={"at_least":len(arr),"samples":arr}
(out/"members.json").write_text(json.dumps({"source_meta_version":29,"types":types,"search_methods":methods_hits},ensure_ascii=False,indent=2))
for typ in types:
 print("TYPE",json.dumps(typ,ensure_ascii=False)[:8500],flush=True)
print("METHODS",json.dumps(methods_hits,ensure_ascii=False)[:13000],flush=True)
print("HOK_MEMBERS_DONE",len(types),flush=True)
