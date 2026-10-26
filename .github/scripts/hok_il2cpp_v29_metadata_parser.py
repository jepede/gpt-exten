#!/usr/bin/env python3
"""Metadata v29 type/method/field recovery (layout from Perfare/Il2CppDumper MetadataClass.cs).
Does not infer native method RVA or field byte offsets without protected runtime registration.
"""
from pathlib import Path
import json,struct,re
root=Path("reports/hok_20261026/metadata_v29")
root.mkdir(parents=True,exist_ok=True)
p=Path("work/hok_native/assets/bin/Data/Managed/Metadata/global-metadata.dat")
data=p.read_bytes()
u32=lambda x:struct.unpack_from("<I",data,x)[0]
assert u32(0)==0xfab11baf and u32(4)==29
tags=[
 "stringLiteral","stringLiteralData","string","events","properties","methods","parameterDefaultValues",
 "fieldDefaultValues","fieldAndParameterDefaultValueData","fieldMarshaledSizes","parameters","fields",
 "genericParameters","genericParameterConstraints","genericContainers","nestedTypes","interfaces",
 "vtableMethods","interfaceOffsets","typeDefinitions","images","assemblies","fieldRefs","referencedAssemblies",
 "attributeData","attributeDataRange","unresolvedVirtualCallParameterTypes",
 "unresolvedVirtualCallParameterRanges","windowsRuntimeTypeNames","windowsRuntimeStrings",
 "exportedTypeDefinitions"
]
assert len(tags)==31 and u32(8)==256
sec={}
for i,t in enumerate(tags):
 o,s=struct.unpack_from("<II",data,8+i*8)
 assert o+s<=len(data) and s>=0
 sec[t]=(o,s)
string_base,string_size=sec["string"]
def text(index):
 if not 0<=index<string_size:return "<invalid>"
 start=string_base+index
 end=data.find(b"\x00",start,string_base+string_size)
 return data[start:end].decode("utf8","replace") if end>=start else "<invalid>"
def table(tag,fmt,keys):
 off,size=sec[tag];width=struct.calcsize(fmt)
 assert size%width==0,(tag,size,width)
 return [dict(zip(keys,struct.unpack_from(fmt,data,off+i*width))) for i in range(size//width)]
T=table("typeDefinitions","<IIiiiiiIiiiiiiiiHHHHHHHHII",[
 "nameIndex","namespaceIndex","byvalTypeIndex","declaringTypeIndex","parentIndex",
 "elementTypeIndex","genericContainerIndex","flags","fieldStart","methodStart",
 "eventStart","propertyStart","nestedTypesStart","interfacesStart","vtableStart",
 "interfaceOffsetsStart","method_count","property_count","field_count","event_count",
 "nested_type_count","vtable_count","interfaces_count","interface_offsets_count",
 "bitfield","token"])
M=table("methods","<IiiiiIHHHH",["nameIndex","declaringType","returnType",
"parameterStart","genericContainerIndex","token","flags","iflags","slot","parameterCount"])
F=table("fields","<IiI",["nameIndex","typeIndex","token"])
I=table("images","<IiiIiIiIiI",["nameIndex","assemblyIndex","typeStart",
"typeCount","exportedTypeStart","exportedTypeCount","entryPointIndex","token",
"customAttributeStart","customAttributeCount"])
print("METADATA_29_COUNTS",json.dumps({"types":len(T),"methods":len(M),"fields":len(F),"images":len(I)}),flush=True)
for x in T:
 x["name"]=text(x["nameIndex"]);x["namespace"]=text(x["namespaceIndex"])
 assert x["field_count"]==0 or (0<=x["fieldStart"]<=len(F) and x["fieldStart"]+x["field_count"]<=len(F)),x
 assert x["method_count"]==0 or (0<=x["methodStart"]<=len(M) and x["methodStart"]+x["method_count"]<=len(M)),x
for x in F:x["name"]=text(x["nameIndex"])
for x in M:x["name"]=text(x["nameIndex"])
for x in I:x["name"]=text(x["nameIndex"])
narrow=re.compile(r"VInt3|Actor|Hero|LogicPos|Move|Battle|Position|Coord|Vector|FrameSync|Encrypt|Decrypt|Fog|Visible|World|Transform|NetPos",re.I)
rank=re.compile(r"GetActorLogicPos|SetActorLogicPos|LogicPos|Position|VInt3|Coordinate|Invisible|Fog|Encrypt|Decrypt|ActorRoot|HeroActor",re.I)
rows=[]
members=[]
for i,t in enumerate(T):
 if not narrow.search(t["name"]+" "+t["namespace"]):continue
 fs=[{"name":f["name"],"field_index":t["fieldStart"]+j,"type_index":f["typeIndex"],
      "token":hex(f["token"])} for j,f in enumerate((F[t["fieldStart"]:t["fieldStart"]+t["field_count"]] if t["field_count"] else []))]
 ms=[{"name":m["name"],"method_index":t["methodStart"]+j,"token":hex(m["token"]),
      "parameter_count":m["parameterCount"]} for j,m in enumerate((M[t["methodStart"]:t["methodStart"]+t["method_count"]] if t["method_count"] else []))]
 row={"type_index":i,"type":t["name"],"namespace":t["namespace"],
      "is_value_type":bool(t["bitfield"]&1),"fields":fs,"methods":ms}
 rows.append(row)
 for kind,vv in (("field",fs),("method",ms)):
  for member in vv:
   if rank.search(member["name"]):
    members.append({"class":row["namespace"]+"."+row["type"],"kind":kind,"member":member})
rows.sort(key=lambda x:(0 if rank.search(x["type"]) else 1,
                        0 if "Actor" in x["type"] or "Logic" in x["type"] else 1,
                        x["namespace"],x["type"]))
(root/"types.json").write_text(json.dumps({"metadata_version":29,"total_types":len(T),
 "total_fields":len(F),"total_methods":len(M),"matched_type_count":len(rows),
 "image_count":len(I),"images":[{"name":x["name"],"start":x["typeStart"],
 "count":x["typeCount"]} for x in I],"types":rows[:650]},indent=2,ensure_ascii=False))
(root/"position_members.json").write_text(json.dumps({"total":len(members),
"members":members[:6000]},indent=2,ensure_ascii=False))
print("META_TYPES_HIGHLIGHTS",json.dumps({"matched_types":len(rows),"matched_members":len(members),
"types":[{"name":x["namespace"]+"."+x["type"],"field_count":len(x["fields"]),
"method_count":len(x["methods"])} for x in rows[:100]],
"members":[{"class":x["class"],"kind":x["kind"],"name":x["member"]["name"]} for x in members[:100]]},
ensure_ascii=False),flush=True)
report=["# HoK 12.1.1.1 IL2CPP version 29 recovered coordinate types",
f"Types: {len(T)}; methods: {len(M)}; fields: {len(F)}.",
"Exact runtime field offsets and native method addresses are NOT determined by metadata alone.",
"","## Type definitions"]
for t in rows[:250]:
 if not rank.search(t["type"]):continue
 report+=["","### "+t["namespace"]+"."+t["type"]+" ["+str(t["type_index"])+"]"]
 for f in t["fields"][:40]:report.append("FIELD "+f["name"]+" token="+f["token"])
 for m in t["methods"][:55]:report.append("METHOD "+m["name"]+" token="+m["token"])
report+=["","## Position members"]
for x in members[:450]:
 report.append(x["class"]+" "+x["kind"]+" "+x["member"]["name"])
(root/"coordinate_types.md").write_text("\n".join(report)+"\n")
print("METADATA_V29_PARSE_COMPLETE",flush=True)
