#!/usr/bin/env python3
import sys, json, struct, mmap, hashlib, subprocess, bisect, collections
from pathlib import Path

TARGET = 0x0D1FBB60
KEY = 0xE2
SO = Path(sys.argv[1])
OUT = Path("reports/deltaforce_xor_e2")
OUT.mkdir(parents=True, exist_ok=True)

def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda: f.read(16 << 20), b""):
            h.update(b)
    return h.hexdigest()

def prolog(w):
    if (w & 0xff8003ff) == 0xd10003ff: return "SUB_SP"
    if w in (0xd503233f,0xd50323bf,0xd503245f,0xd503241f): return "PAC_BTI"
    if (w & 0xffc003e0) in (0xa98003e0,0xa90003e0,0xa88003e0): return "STP_SP"
    if (w & 0xffc003e0) == 0xf90003e0: return "STR_SP"
    if (w & 0xfffffc1f) == 0xd65f0000: return "RET"
    return None

def radare2(path):
    try:
        p = subprocess.run(["r2","-2","-q","-n","-a","arm","-b","64",
                            "-c","e scr.color=false;pd 52 @ 0",str(path)],
                           capture_output=True,text=True,errors="replace",timeout=90)
        return {"rc":p.returncode,"output":(p.stdout+p.stderr)[-11000:]}
    except Exception as exc:
        return {"rc":-1,"output":str(exc)}

with SO.open("rb") as f:
    hdr = f.read(64)
    vals = struct.unpack("<16sHHIQQQIHHHHHH", hdr)
    ident,etype,machine,ev,entry,phoff,shoff,flags,ehsize,phentsize,phnum,shentsize,shnum,shstrndx=vals
    assert ident[:6]==b"\x7fELF\x02\x01" and machine==183
    sections=[]
    for i in range(shnum):
        f.seek(shoff+i*shentsize)
        (name,typ,sflags,addr,off,size,link,info,align,entsize)=struct.unpack_from("<IIQQQQIIQQ",f.read(shentsize))
        sections.append(dict(nameno=name,addr=addr,offset=off,size=size,typ=typ))
    sh=sections[shstrndx]
    f.seek(sh["offset"]); names=f.read(sh["size"])
    for sec in sections:
        k=sec["nameno"]
        sec["name"]=names[k:names.find(b"\0",k)].decode("ascii","replace") if k<len(names) else "?"
    text=next(s for s in sections if s["name"]==".text")
    eh=next(s for s in sections if s["name"]==".eh_frame_hdr")
    mm=mmap.mmap(f.fileno(),0,access=mmap.ACCESS_READ)
    def fileoff(va):
        assert text["addr"]<=va<text["addr"]+text["size"]
        return text["offset"]+(va-text["addr"])
    def bytes_at(va,n):
        off=fileoff(va)
        return mm[off:off+min(n, text["size"]-(va-text["addr"]))]
    def word(va):
        return struct.unpack_from("<I", mm, fileoff(va))[0]
    def window(va, length=0x240):
        a=bytes_at(va,length)
        d=bytes(x^KEY for x in a)
        p1=OUT/("raw_%x.bin"%va);p2=OUT/("xor_%x.bin"%va)
        p1.write_bytes(a);p2.write_bytes(d)
        cnt=min(12,len(a)//4)
        words=list(struct.unpack_from("<"+"I"*cnt,a))
        return {"va":hex(va),"raw_hex":a[:72].hex(),"xor_hex":d[:72].hex(),
                "raw_words":[hex(x) for x in words],
                "xor_words":[hex(x^0xe2e2e2e2) for x in words],
                "raw_disasm":radare2(p1),"xor_disasm":radare2(p2)}

    eh_off=eh["offset"]
    e_version,ptr_enc,count_enc,table_enc=mm[eh_off:eh_off+4]
    count=struct.unpack_from("<I",mm,eh_off+8)[0] if count_enc==3 else 0
    starts=[]
    if (e_version,ptr_enc,count_enc,table_enc)==(1,0x1b,3,0x3b) and count<5000000 and eh["size"]>=12+count*8:
        for i in range(count):
            delta,fde=struct.unpack_from("<ii",mm,eh_off+12+8*i)
            va=eh["addr"]+delta
            if text["addr"]<=va<text["addr"]+text["size"] and va%4==0:
                starts.append(va)
    starts=sorted(set(starts))
    idx=bisect.bisect_left(starts,TARGET)
    sample=starts[::max(1,len(starts)//30000)]
    cc=collections.Counter()
    enc_example=[]; plain_example=[]
    for va in sample:
        w=word(va); orig=prolog(w); dec=prolog(w^0xe2e2e2e2)
        cc[("R" if orig else "-")+("X" if dec else "-")]+=1
        if orig and len(plain_example)<20:
            plain_example.append({"va":hex(va),"word":hex(w),"class":orig})
        if dec and not orig and len(enc_example)<20:
            enc_example.append({"va":hex(va),"word":hex(w),"xor":hex(w^0xe2e2e2e2),"class":dec})
    near=[]
    for va in starts[max(0,bisect.bisect_left(starts,TARGET-0x3000)):bisect.bisect_right(starts,TARGET+0x3000)]:
        w=word(va)
        near.append({"va":hex(va),"word":hex(w),"xor":hex(w^0xe2e2e2e2),
                     "raw_prolog":prolog(w),"xor_prolog":prolog(w^0xe2e2e2e2)})
    bins={}
    for left in range(TARGET-0x20000,TARGET+0x20000,0x8000):
        region=starts[bisect.bisect_left(starts,left):bisect.bisect_left(starts,left+0x8000)]
        c=collections.Counter()
        for va in region:
            w=word(va)
            c["functions"]+=1
            c["raw"]+=bool(prolog(w))
            c["xor"]+=bool(prolog(w^0xe2e2e2e2))
        bins[hex(left)]=dict(c)
    observed=["%08x"%w for w in struct.unpack("<6I",bytes_at(TARGET,24))]
    expected=["33e0211d","1be2d11b","4be5bd1a","4beab514","4bebad16","4be8991f"]
    checks=[a==b for a,b in zip(observed,expected)]
    t=window(TARGET)
    mid=window(TARGET+0x38)
    beginning=window(text["addr"],0x120)
    record={"library":"libUE4.so","sha256":sha256(SO),"target_va":hex(TARGET),
            "text":text,"eh_frame_hdr":eh,
            "fde_count":count,"decoded_fde_entries":len(starts),
            "previous_claim":{"expected_raw_words":expected,"actual_raw_words":observed,"matches":checks},
            "near_function_entries":near[:500],"sampled_entries":len(sample),
            "sampled_prologue_counts":dict(cc),"plain_examples":plain_example,
            "xor_examples":enc_example,"bins":bins,
            "target_disassembly":t,"plus_0x38_disassembly":mid,
            "plain_text_disassembly":beginning}
    (OUT/"xor_e2_report.json").write_text(json.dumps(record,indent=2,ensure_ascii=False))
    lines=["# libUE4.so XOR E2 independent test",
           "library SHA256: "+record["sha256"],
           "target: "+hex(TARGET),
           "FDE entries: "+str(len(starts)),
           "previous raw words: "+str(expected),
           "observed raw words: "+str(observed),
           "exact matches: "+str(checks),
           "function entry sample count: "+str(len(sample)),
           "prologue class counts: "+str(dict(cc)),
           "",
           "## Raw ARM64 disassembly",
           t["raw_disasm"]["output"],
           "",
           "## XOR E2 decoded ARM64 disassembly",
           t["xor_disasm"]["output"],
           "",
           "## XOR E2 decoded at target+0x38",
           mid["xor_disasm"]["output"],
           "",
           "## Plain .text entry sample",
           beginning["raw_disasm"]["output"],
           "",
           "## Entries within target +/- 0x3000"]
    for r in near[:150]:
        lines.append(str(r))
    lines.extend(["","## Function prologue classification bins"])
    for a,b in bins.items():lines.append(a+" "+str(b))
    lines.extend(["","## Caveat",
                  "The E2 mask is a candidate. Sustained valid instructions and independently verified control flow are needed.",
                  "Code byte protection is NOT the same as coordinate-value encryption.",
                  "PAC/AUT/BTI and virtual branch dispatch are not OLLVM evidence."])
    (OUT/"xor_e2_report.md").write_text("\n".join(lines)+"\n")
    print("PREVIOUS_WORDS_CHECK",json.dumps(record["previous_claim"]),flush=True)
    print("FDE_COUNT",count,"VALID_FDE",len(starts),"SAMPLED",len(sample),"PROLOG_STATS",dict(cc),flush=True)
    print("TARGET_PLUS_MINUS_NEAR",json.dumps(near[:30]),flush=True)
    print("BINS",json.dumps(bins),flush=True)
    print("DECODED_TARGET",t["xor_disasm"]["output"][:10000],flush=True)
    print("RAW_TARGET",t["raw_disasm"]["output"][:5500],flush=True)
    print("PLAIN_TEXT_START",beginning["raw_disasm"]["output"][:4000],flush=True)
    mm.close()
