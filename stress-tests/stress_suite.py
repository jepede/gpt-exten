#!/usr/bin/env python3
"""Reproducible Android ARM64 high-pressure linker regression suite.

Use real Bionic runtime with qemu-aarch64. Native and packed executables
are compared on exit status and deterministic semantic output. Build-only
results are never counted as packed-runtime passes.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import struct
import subprocess
import sys
import time

def run(cmd, *, env=None, timeout=120):
    try:
        p = subprocess.run([str(x) for x in cmd], capture_output=True,
                           text=True, errors="replace", env=env,
                           timeout=timeout)
        return {"rc": p.returncode, "stdout": p.stdout, "stderr": p.stderr,
                "cmd": [str(x) for x in cmd]}
    except subprocess.TimeoutExpired as exc:
        def decode(x):
            return x.decode("utf-8", "replace") if isinstance(x, bytes) else (x or "")
        return {"rc": 124, "stdout": decode(exc.stdout),
                "stderr": decode(exc.stderr) + "\nTIMEOUT\n",
                "cmd": [str(x) for x in cmd]}

def save_log(dest, result):
    dest.write_text("CMD: " + " ".join(result["cmd"]) + "\nRC: " +
                    str(result["rc"]) + "\nSTDOUT:\n" + result["stdout"] +
                    "\nSTDERR:\n" + result["stderr"], encoding="utf-8")

def src_write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path

def generate(src, scale):
    count = 8192 * scale
    refs = ",".join("&cells[" + str(i % 64) + "]" for i in range(count))
    src_write(src/"relocs.c", """
#include <stdint.h>
#include <stdio.h>
static uint64_t cells[64];
static volatile uint64_t *volatile ptrs[] = {""" + refs + """};
int main(void) {
  uint64_t ok=0; const unsigned n=sizeof(ptrs)/sizeof(ptrs[0]);
  for (unsigned i=0;i<n;i++) {
    if (ptrs[i]==&cells[i%64]) ++ok;
    else return 19;
  }
  printf("RELOC count=%u ok=%llu\\n",n,(unsigned long long)ok);
  return ok==n?0:20;
}
""")
    src_write(src/"thread_tls.c", r"""
#include <pthread.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#define NT 24
#define LOOPS 8192
static __thread uint64_t tls_slot;
static void *thread_main(void *arg) {
  uintptr_t id=(uintptr_t)arg+1;
  tls_slot=0xcbf29ce484222325ULL ^ id;
  uint64_t expected=tls_slot;
  for (int i=0;i<LOOPS;i++) {
    tls_slot = (tls_slot ^ (id+i)) * 1099511628211ULL;
    expected = (expected ^ (id+i)) * 1099511628211ULL;
  }
  if (tls_slot!=expected) return (void *)1;
  return NULL;
}
int main(void) {
  pthread_t t[NT];
  for (uintptr_t i=0;i<NT;i++) if(pthread_create(&t[i],NULL,thread_main,(void*)i)) return 21;
  for (int i=0;i<NT;i++) {
    void *ret=(void*)1;
    if(pthread_join(t[i],&ret)||ret) return 22;
  }
  puts("THREAD_TLS threads=24 loops=8192 PASS");
  return 0;
}
""")
    src_write(src/"big_bss.c", r"""
#include <stdint.h>
#include <stdio.h>
static volatile unsigned char arena[32*1024*1024];
int main(void) {
  unsigned checksum=0;
  for(size_t i=0;i<sizeof(arena);i+=4096) { arena[i]=(unsigned char)((i/4096)%251+1); }
  unsigned expected=0;
  for(size_t i=0;i<sizeof(arena);i+=4096) {
    checksum+=arena[i];
    expected+=(unsigned)((i/4096)%251+1);
  }
  printf("BIG_BSS pages=%zu checksum=%u\n",sizeof(arena)/4096,checksum);
  return checksum==expected?0:81;
}
""")
    src_write(src/"dlopen_repeat.c", r"""
#include <dlfcn.h>
#include <stdio.h>
typedef int (*entry)(int);
int main(void) {
  unsigned long checksum=0;
  for(int i=0;i<256;i++) {
    void *h=dlopen("libstress_plugin.so",RTLD_NOW|RTLD_LOCAL);
    if(!h) {fprintf(stderr,"dlopen error: %s\n",dlerror());return 30;}
    entry f=(entry)dlsym(h,"stress_entry");
    if(!f) return 31;
    checksum+=(unsigned)f(i);
    if(dlclose(h)) return 32;
  }
  printf("DLOPEN loops=256 checksum=%lu\n",checksum);
  return 0;
}
""")
    src_write(src/"plugin.c", r"""
static __thread int calls=7;
int stress_entry(int value) { ++calls; return value * 3 + calls; }
""")
    src_write(src/"leaf.c", r"""
int leaf(int x) {return x*3+17;}
""")
    src_write(src/"mid.c", r"""
extern int leaf(int);
int mid(int x) {return leaf(x)+5;}
""")
    src_write(src/"top.c", r"""
extern int mid(int);
int top(int x) {return mid(x)+11;}
""")
    src_write(src/"needed_chain.c", r"""
#include <stdio.h>
extern int top(int);
int main(void) {
  long total=0;
  for(int i=0;i<16384;i++) total+=top(i);
  printf("NEEDED depth=3 count=16384 sum=%ld\n",total);
  return 0;
}
""")
    constructors = "\n".join(
        "static void __attribute__((constructor)) ctor_%d(void){ctor_count++;}" % i
        for i in range(256*scale))
    src_write(src/"constructors.c", """
#include <stdio.h>
static volatile unsigned ctor_count;
static volatile unsigned dtor_count;
""" + constructors + """
static void __attribute__((destructor)) destructor_summary(void) {
  dtor_count++; printf("DESTRUCTOR count=%u\\n",dtor_count);
}
int main(void) {
  printf("CONSTRUCTOR count=%u\\n", ctor_count);
  return ctor_count==""" + str(256*scale) + """?0:41;
}
""")
    src_write(src/"ifunc_weak.c", r"""
#include <stdio.h>
extern int optional_function(void) __attribute__((weak));
static int implementation(int x){ return 42+x; }
static void *selector(void){return (void*)implementation;}
int dispatcher(int) __attribute__((ifunc("selector")));
int main(void) {
  int got=dispatcher(9);
  printf("IFUNC_WEAK result=%d weak_is_null=%d\n",got,optional_function==0);
  return got==51 && optional_function==0?0:51;
}
""")
    src_write(src/"thrower.cpp", r"""
#include <stdexcept>
extern "C" int throw_stress(int n) {
  if(n%2==0) throw std::runtime_error("pressure");
  return n*7;
}
""")
    src_write(src/"cpp_catch.cpp", r"""
#include <cstdio>
#include <stdexcept>
extern "C" int throw_stress(int);
thread_local int tls_instance=11;
int main() {
  long long total=0, thrown=0;
  for(int i=0;i<3000;i++) {
    try {total += throw_stress(i) + tls_instance;}
    catch(const std::runtime_error &e) { ++thrown; total += e.what()[0]; }
  }
  printf("CPP_DSO_EXC caught=%lld checksum=%lld\n",thrown,total);
  return thrown==1500?0:61;
}
""")
    src_write(src/"vers.c", r"""
int old_impl(void) {return 17;}
int new_impl(void) {return 29;}
__asm__(".symver old_impl,version_api@VERS_1");
__asm__(".symver new_impl,version_api@@VERS_2");
""")
    src_write(src/"versions.map", "VERS_1 { global: version_api; };\nVERS_2 { global: version_api; } VERS_1;\n")
    src_write(src/"vers_main.c", r"""
#include <stdio.h>
extern int version_one(void);
extern int version_two(void);
__asm__(".symver version_one,version_api@VERS_1");
__asm__(".symver version_two,version_api@VERS_2");
int main(void) {
  int a=version_one(),b=version_two();
  printf("VERSIONS old=%d new=%d\n",a,b);
  return (a==17 && b==29)?0:71;
}
""")

def normalized(s):
    ignored=("[LINKER]","[SHELL]","linker: Warning:","WARNING: linker:")
    return "\n".join(line for line in s.splitlines() if not line.startswith(ignored)).strip()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--ndk",required=True)
    ap.add_argument("--qemu",required=True)
    ap.add_argument("--sysroot",required=True)
    ap.add_argument("--packer")
    ap.add_argument("--shell")
    ap.add_argument("--out",default="stress-results")
    ap.add_argument("--api",type=int,default=35)
    ap.add_argument("--scale",type=int,default=1)
    ap.add_argument("--repeats",type=int,default=2)
    ap.add_argument("--timeout",type=int,default=90)
    ap.add_argument("--page16k",action="store_true")
    args=ap.parse_args()
    if bool(args.packer) != bool(args.shell):
        ap.error("--packer and --shell must be supplied together")
    if args.scale<1 or args.scale>16: ap.error("--scale must be 1..16")
    out=Path(args.out).absolute();out.mkdir(parents=True,exist_ok=True)
    src=out/"sources";generate(src,args.scale)
    ndk=Path(args.ndk)
    tc=ndk/"toolchains/llvm/prebuilt/linux-x86_64/bin"
    cc=tc/("aarch64-linux-android%d-clang" % args.api)
    cxx=tc/("aarch64-linux-android%d-clang++" % args.api)
    qemu=Path(args.qemu).absolute()
    rootfs=Path(args.sysroot).absolute()
    libcxx=ndk/"toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib/aarch64-linux-android/libc++_shared.so"
    if libcxx.exists():shutil.copy2(libcxx,out/"libc++_shared.so")
    env=os.environ.copy()
    env.pop("LD_PRELOAD",None)
    env["ANDROID_ROOT"]="/system"
    env["ANDROID_DATA"]="/data"
    env["LD_LIBRARY_PATH"]=str(out)+":/system/lib64:/apex/com.android.runtime/lib64:/apex/com.android.runtime/lib64/bionic"
    logs=out/"logs";logs.mkdir(exist_ok=True)
    def build(name, compiler, source, flags, deps=()):
        res=run([compiler,"-fPIE","-O2","-g",*flags,"-o",out/name,
                 source,*deps],env=env)
        save_log(logs/(name+".build.log"),res)
        if res["rc"]!=0:raise RuntimeError("BUILD FAIL: "+name+"\n"+res["stderr"])
    def lib(name, source, deps=(), flags=(), cxx_mode=False):
        res=run([cxx if cxx_mode else cc,"-fPIC","-O2","-g","-shared",
                 *flags,"-o",out/name,source,*deps],env=env)
        save_log(logs/(name+".build.log"),res)
        if res["rc"]:raise RuntimeError("LIB BUILD FAIL: "+name+"\n"+res["stderr"])
    lib("libstress_plugin.so",src/"plugin.c")
    lib("libleaf.so",src/"leaf.c",flags=["-Wl,-soname,libleaf.so"])
    lib("libmid.so",src/"mid.c",deps=["-L"+str(out),"-lleaf","-Wl,-rpath,$ORIGIN"],flags=["-Wl,-soname,libmid.so"])
    lib("libtop.so",src/"top.c",deps=["-L"+str(out),"-lmid","-Wl,-rpath,$ORIGIN"],flags=["-Wl,-soname,libtop.so"])
    lib("libthrower.so",src/"thrower.cpp",cxx_mode=True,flags=["-Wl,-soname,libthrower.so"])
    lib("libvers.so",src/"vers.c",flags=["-Wl,-soname,libvers.so","-Wl,--version-script="+str(src/"versions.map")])
    default=["-pie","-Wl,--export-dynamic"]
    build("reloc_rela",cc,src/"relocs.c",default)
    build("reloc_aps2",cc,src/"relocs.c",default+["-Wl,--pack-dyn-relocs=android"])
    build("reloc_relr",cc,src/"relocs.c",default+["-Wl,--pack-dyn-relocs=relr"])
    build("reloc_aps2_4k",cc,src/"relocs.c",default+["-Wl,--pack-dyn-relocs=android","-Wl,-z,max-page-size=4096"])
    build("thread_tls",cc,src/"thread_tls.c",default+["-pthread"])
    build("big_bss",cc,src/"big_bss.c",default)
    build("dlopen_repeat",cc,src/"dlopen_repeat.c",default+["-ldl"])
    build("needed_chain",cc,src/"needed_chain.c",default,
          ["-L"+str(out),"-ltop","-Wl,-rpath,$ORIGIN"])
    build("constructors",cc,src/"constructors.c",default)
    build("ifunc_weak",cc,src/"ifunc_weak.c",default)
    build("cpp_catch",cxx,src/"cpp_catch.cpp",default,["-L"+str(out),"-lthrower","-Wl,-rpath,$ORIGIN"])
    build("vers_main",cc,src/"vers_main.c",default,["-L"+str(out),"-lvers","-Wl,-rpath,$ORIGIN"])
    # Verify that compiler output actually exercises packed relocations.
    # Otherwise a green run could silently be testing ordinary RELA only.
    readelf=tc/"llvm-readelf"
    elf_tags={}
    for tag_case,required in (
        ("reloc_aps2","ANDROID_RELA"),
        ("reloc_aps2_4k","ANDROID_RELA"),
        ("reloc_relr","RELR"),
    ):
        probe=run([readelf,"--dynamic",out/tag_case],env=env,timeout=30)
        save_log(logs/(tag_case+".dynamic.log"),probe)
        present=(probe["rc"]==0 and required in probe["stdout"])
        elf_tags[tag_case]={"required":required,"present":present}
        if not present:
            raise RuntimeError("EXPECTED DYNAMIC TAG MISSING: "+tag_case+" / "+required+
                               "\n"+probe["stdout"]+"\n"+probe["stderr"])
    samples=["reloc_rela","reloc_aps2","reloc_relr","reloc_aps2_4k",
             "thread_tls","big_bss","dlopen_repeat","needed_chain",
             "constructors","ifunc_weak","cpp_catch","vers_main"]
    summary=[]
    qbase=[str(qemu)]
    if args.page16k:qbase+=["-p","16384"]
    qbase+=["-L",str(rootfs)]
    for sample in samples:
        p=out/sample
        if args.packer:
            packed=out/(sample+".packed")
            pkg=run([args.packer,args.shell,p,packed],env=env,timeout=args.timeout)
            save_log(logs/(sample+".pack.log"),pkg)
            pack_rc=pkg["rc"]
        else:pack_rc=None
        for n in range(args.repeats):
            orig=run([*qbase,p],env=env,timeout=args.timeout)
            save_log(logs/(sample+".native.%d.log" % n),orig)
            if args.packer and pack_rc==0:
                shell=run([*qbase,packed],env=env,timeout=args.timeout)
                save_log(logs/(sample+".packed.%d.log" % n),shell)
            else:shell=None
            # AOSP Bionic may correctly reject a 4 KiB-aligned ELF on a
            # 16 KiB guest. Track that as an explicit expected rejection,
            # NOT as a successful execution or a packed parity pass.
            expected_native_reject=(args.page16k and sample=="reloc_aps2_4k")
            if expected_native_reject:
                passed=(orig["rc"]!=0 and (not args.packer or
                        (shell is not None and shell["rc"]==0)))
            else:
                passed=(orig["rc"]==0 and
                        ((shell is None and not args.packer) or
                         (shell is not None and shell["rc"]==0 and
                          normalized(orig["stdout"])==normalized(shell["stdout"]))))
            row={"case":sample,"iteration":n,"page16k":args.page16k,
                 "native_rc":orig["rc"],"native_rejection_expected":expected_native_reject,
                 "packer_rc":pack_rc,
                 "packed_rc":shell["rc"] if shell else None,
                 "same_stdout":normalized(orig["stdout"])==normalized(shell["stdout"]) if shell else None,
                 "pass":passed}
            summary.append(row)
            print(("PASS" if passed else "FAIL"),sample,n,
                  "native",orig["rc"],"pack",pack_rc,
                  "packed",shell["rc"] if shell else None,
                  "same",row["same_stdout"],
                  "native_expected_reject",expected_native_reject,flush=True)
    # Malformed input checks: only Packer rejection, never execute corrupt ELFs.
    negative=[]
    if args.packer:
        good=(out/"reloc_rela").read_bytes()
        mutants=[
          ("truncated",good[:64]),
          ("bad_magic",b"ABCD"+good[4:]),
          ("et_exec",good[:16]+struct.pack("<H",2)+good[18:]),
          ("wrong_arch",good[:18]+struct.pack("<H",62)+good[20:]),
          ("oversized_phnum",good[:56]+struct.pack("<H",0xffff)+good[58:])
        ]
        for name,raw in mutants:
            dest=out/("negative_"+name)
            dest.write_bytes(raw)
            packaged=out/(name+".packed")
            r=run([args.packer,args.shell,dest,packaged],timeout=20)
            save_log(logs/(name+".negative.log"),r)
            ok=r["rc"]!=0
            negative.append({"case":name,"rejected":ok,"rc":r["rc"]})
            print("NEGATIVE",name,"REJECT" if ok else "UNEXPECTED_ACCEPT",flush=True)
    result={"metadata":{"api":args.api,"page16k":args.page16k,
                        "scale":args.scale,"repeats":args.repeats,
                        "packed_mode":bool(args.packer)},
            "positive":summary,"negative":negative,"elf_tags":elf_tags,
            "passed":sum(x["pass"] for x in summary),
            "total":len(summary),
            "negative_rejected":sum(x["rejected"] for x in negative)}
    (out/"results.json").write_text(json.dumps(result,ensure_ascii=False,indent=2))
    print("SUMMARY",result["passed"],"/",result["total"],
          "negative",result["negative_rejected"],"/",len(negative),flush=True)
    return 0 if result["passed"]==len(summary) and all(x["rejected"] for x in negative) else 1

if __name__=="__main__":
    try:sys.exit(main())
    except Exception as exc:
        print("HARNESS ERROR:",exc,file=sys.stderr)
        raise
