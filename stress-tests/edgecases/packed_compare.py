#!/usr/bin/env python3
"""Compare original and packed Android AArch64 ELF edge fixtures under Bionic.
Runs locally only; NEVER uploads private packer/shell/ELFs.
"""
import argparse
import concurrent.futures
import datetime
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time

CASES=("needed72","host_reverse","host_tls","long_runpath","stripped_main","huge_tls")
IGNORE=("linker: Warning:","WARNING: linker:","[LINKER]","[SHELL]")
EXPECT={
    "needed72":"EDGE_NEEDED72=2628",
    "host_reverse":"EDGE_HOST_EXPORT=42",
    "host_tls":"EDGE_HOST_TLS=12",
    "long_runpath":"EDGE_LONG_RUNPATH=2718",
    "stripped_main":"EDGE_STRIPPED_MAIN=12345",
    "huge_tls":"EDGE_HUGE_TLS=163200",
}

def sha256(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024*1024), b""):h.update(chunk)
    return h.hexdigest()

def run(cmd, env, timeout):
    t=time.monotonic()
    try:
        p=subprocess.run([str(i) for i in cmd],env=env,capture_output=True,text=True,
                         errors="replace",timeout=timeout)
        return {"cmd":list(map(str,cmd)),"rc":p.returncode,"stdout":p.stdout,"stderr":p.stderr,
                "elapsed":round(time.monotonic()-t,3),"timed_out":False}
    except subprocess.TimeoutExpired as e:
        def decode(x):
            if x is None:return ""
            return x.decode("utf-8","replace") if isinstance(x,bytes) else x
        return {"cmd":list(map(str,cmd)),"rc":124,"stdout":decode(e.stdout),
                "stderr":decode(e.stderr)+"\nTIMEOUT\n","elapsed":round(time.monotonic()-t,3),"timed_out":True}

def norm(text):
    return "\n".join(s for s in text.splitlines() if not s.startswith(IGNORE)).strip()

def save_log(path,rec):
    path.write_text(json.dumps(rec,indent=2,ensure_ascii=False))

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--fixtures-dir",type=Path,required=True,
                    help="Extracted android-arm64-edgecases-20261015.tar.gz directory")
    ap.add_argument("--packer",type=Path,required=True)
    ap.add_argument("--shell",type=Path,required=True)
    ap.add_argument("--qemu",type=Path,required=True)
    ap.add_argument("--sysroot",type=Path,required=True)
    ap.add_argument("--out",type=Path,required=True)
    ap.add_argument("--repeats",type=int,default=2)
    ap.add_argument("--concurrent",type=int,default=0)
    ap.add_argument("--timeout",type=int,default=50)
    args=ap.parse_args()
    if not (1<=args.repeats<=20 and 0<=args.concurrent<=16 and 1<=args.timeout<=300):
        ap.error("invalid repeats/concurrent/timeout")
    args.out=args.out.resolve()
    args.out.mkdir(parents=True,exist_ok=True)
    paths=(args.packer,args.shell,args.qemu,args.sysroot/"system/bin/linker64",
           args.sysroot/"system/lib64/libc.so")
    for p in paths:
        if not p.is_file():ap.error("missing input "+str(p))
    logs=args.out/"logs"
    logs.mkdir(exist_ok=True)
    work=args.out/"fixtures"
    work.mkdir(exist_ok=True)
    for f in args.fixtures_dir.iterdir():
        if f.is_file() and (f.suffix==".so" or f.name in CASES):
            shutil.copy2(f,work/f.name)
        if f.is_dir() and f.name=="edgefar":
            shutil.copytree(f,work/f.name,dirs_exist_ok=True)
    for case in CASES:
        if not (work/case).is_file():ap.error("missing fixture "+case)
        (work/case).chmod(0o755)

    env=os.environ.copy()
    env.pop("LD_PRELOAD",None)
    env["ANDROID_ROOT"]="/system"
    env["ANDROID_DATA"]="/data"
    env["LD_LIBRARY_PATH"]=str(work)+":/system/lib64:/apex/com.android.runtime/lib64:/apex/com.android.runtime/lib64/bionic"
    pack_results=[]
    for case in CASES:
        packed=work/(case+".packed")
        r=run([args.packer,args.shell,work/case,packed],env,args.timeout)
        save_log(logs/(case+".packer.json"),r)
        pack_results.append({"case":case,"rc":r["rc"],"packed_exists":packed.exists()})
        print("PACK",case,r["rc"],packed.exists(),flush=True)
    
    def eval_one(case,ps,rep):
        q=[args.qemu]
        if ps==16384:q+=["-p","16384"]
        q+=["-L",args.sysroot]
        native=run([*q,work/case],env,args.timeout)
        if not (work/(case+".packed")).exists():
            packed={"rc":127,"stdout":"","stderr":"NO_PACKED_OUTPUT","timed_out":False}
        else:
            packed=run([*q,work/(case+".packed")],env,args.timeout)
        prefix=f"{ps}_{case}_{rep}"
        save_log(logs/(prefix+".native.json"),native)
        save_log(logs/(prefix+".packed.json"),packed)
        nstdout=norm(native["stdout"])
        pstdout=norm(packed["stdout"])
        nstderr=norm(native["stderr"])
        pstderr=norm(packed["stderr"])
        is_native_ok=(native["rc"]==0 and nstdout==EXPECT[case])
        same_out=(nstdout==pstdout)
        same_err=(nstderr==pstderr)
        is_pass=(is_native_ok and packed["rc"]==0 and same_out and same_err)
        reason=("pass" if is_pass else "native_baseline_failed" if not is_native_ok
                else "packer_failed" if packed["rc"]==127
                else "packed_timeout" if packed.get("timed_out")
                else "packed_signal" if packed["rc"]<0 or packed["rc"]>=128
                else "packed_exit" if packed["rc"]!=0
                else "output_mismatch")
        return {"case":case,"guest_page":ps,"iteration":rep,
                "native_rc":native["rc"],"packed_rc":packed["rc"],
                "native_stdout":nstdout,"packed_stdout":pstdout,
                "packed_stderr":pstderr[-1200:],
                "same_stdout":same_out,"same_stderr":same_err,
                "native_ok":is_native_ok,"passed":is_pass,"failure_class":reason}
    todo=[(case,ps,rep) for ps in (4096,16384) for case in CASES
          for rep in range(args.repeats)]
    if args.concurrent:
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.concurrent) as pool:
            rec=list(pool.map(lambda triple:eval_one(*triple),todo))
    else:
        rec=[eval_one(*x) for x in todo]
    for x in rec:
        print("PASS" if x["passed"] else "FAIL",x["guest_page"],x["case"],
              x["iteration"],"native",x["native_rc"],"packed",x["packed_rc"],
              x["failure_class"],flush=True)
    result={"utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "sha256":{"packer":sha256(args.packer),"shell":sha256(args.shell),
                      "qemu":sha256(args.qemu),
                      "linker64":sha256(args.sysroot/"system/bin/linker64"),
                      "libc":sha256(args.sysroot/"system/lib64/libc.so")},
            "pack_results":pack_results,"cases":rec,
            "counts":{"native":sum(x["native_ok"] for x in rec),"total":len(rec),
                      "packed":sum(x["passed"] for x in rec)}}
    (args.out/"edgecase-results.json").write_text(json.dumps(result,indent=2,ensure_ascii=False))
    with (args.out/"edgecase-results.tsv").open("w") as f:
        f.write("page\tcase\titeration\tnative_rc\tpacked_rc\tpass\treason\n")
        for x in rec:f.write(f"{x['guest_page']}\t{x['case']}\t{x['iteration']}\t{x['native_rc']}\t{x['packed_rc']}\t{x['passed']}\t{x['failure_class']}\n")
    print("EDGECASE_RESULT",result["counts"],flush=True)
    return 0 if result["counts"]["packed"]==result["counts"]["total"] else 1

if __name__=="__main__":
    sys.exit(main())
