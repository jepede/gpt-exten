#!/usr/bin/env python3
"""Validate version-29 Il2Cpp type layout using field and method count invariants."""
import sys,struct,zipfile,json
from pathlib import Path
sys.path.insert(0,".github/scripts")
from ace_range_from_tencent_apks import RangeFile,SOURCES
_,pkg,ver,md5,size=SOURCES["hok"]
u=f"http://imtt.dd.qq.com/sjy.00022/sjy.00001/16891/apk/{md5}.apk?fsname={pkg}_{ver}.apk"
out=Path("out/hok_layout");out.mkdir(parents=True,exist_ok=True)
r=RangeFile(u);assert r.size==size
with zipfile.ZipFile(r) as z:data=z.read("assets/bin/Data/Managed/Metadata/global-metadata.dat")
assert struct.unpack_from("<I",data,0)[0]==0xfab11baf
pairs=[struct.unpack_from("<II",data,8+i*8) for i in range(35)]
st,sz=pairs[2];s=data[st:st+sz]
def getstr(idx):
 if idx>=len(s):return ""
 p=s.find(b"\0",idx)
 return s[idx:p].decode("utf8","replace") if p>=idx and p-idx<350 else ""
t,ts=pairs[19]
f,fs=pairs[11]
m,ms=pairs[5]
n=ts//88
print("TYPE_TABLE",{"type_off":t,"type_bytes":ts,"types":n,
"fields":fs//12,"methods":ms//32,"remainder":ts%88},flush=True)
print("SAMPLE_NAMES",[getstr(struct.unpack_from("<I",data,t+i*88)[0]) for i in range(min(n,35))],flush=True)
totals=[]
for off in range(36,84,2):
 values=[struct.unpack_from("<H",data,t+i*88+off)[0] for i in range(n)]
 count=sum(values)
 if count>1000000:continue
 totals.append({"offset":off,"total":count,"max":max(values),"nonzero":sum(x>0 for x in values)})
totals.sort(key=lambda x:min(abs(x["total"]-fs//12),abs(x["total"]-ms//32)))
print("COUNT_COLUMNS",json.dumps(totals[:20]),flush=True)
starts=[]
for off in range(12,73,4):
 values=[struct.unpack_from("<I",data,t+i*88+off)[0] for i in range(n)]
 good=sum(v<=max(fs//12,ms//32) for v in values)
 monotonic=sum(values[i]<=values[i+1] for i in range(len(values)-1))/max(1,len(values)-1)
 starts.append({"offset":off,"in_range":good,"nondecreasing":round(monotonic,5),
                "start":values[:8],"end":values[-5:]})
starts.sort(key=lambda x:(x["in_range"],x["nondecreasing"]),reverse=True)
print("START_COLUMNS",json.dumps(starts[:22]),flush=True)
(out/"layout.json").write_text(json.dumps({"types":n,"fields":fs//12,"methods":ms//32,
"count_columns":totals,"start_columns":starts},indent=2))
r.close()
