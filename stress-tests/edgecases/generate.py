#!/usr/bin/env python3
"""Public, standalone ARM64/Bionic compatibility edge fixtures.
No custom linker source or binaries are included.
"""
import argparse
import json
import pathlib
import subprocess

P = argparse.ArgumentParser()
P.add_argument("--ndk", required=True, type=pathlib.Path)
P.add_argument("--out", required=True, type=pathlib.Path)
P.add_argument("--api", type=int, default=35)
a = P.parse_args()
out = a.out.resolve()
out.mkdir(parents=True, exist_ok=True)
clang = a.ndk / "toolchains/llvm/prebuilt/linux-x86_64/bin" / f"aarch64-linux-android{a.api}-clang"
strip = a.ndk / "toolchains/llvm/prebuilt/linux-x86_64/bin/llvm-strip"
assert clang.is_file(), clang
assert strip.is_file(), strip

def write(name, src):
    p = out / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(src)
    return p

def run(argv):
    print("+", " ".join(map(str, argv)), flush=True)
    subprocess.run([str(x) for x in argv], check=True)

def shared(src, dst, *extra):
    run([clang, "-O2", "-shared", "-fPIC", str(src), "-o", str(dst), *extra])

def executable(src, dst, *extra):
    run([clang, "-O2", "-fPIE", "-pie", str(src), "-o", str(dst), *extra])
    dst.chmod(0o755)

# AOSP uses a dynamic dependency graph; Phase2 currently has a fixed-size 64 handle table.
count = 72
deps = []
for i in range(count):
    name = f"libedge_dep{i:02d}.so"
    f = write(f"src/dep{i:02d}.c", f"int edge_dep{i:02d}(void){{return {i+1};}}\n")
    shared(f, out / name, "-Wl,-soname," + name)
    deps.append("-ledge_dep%02d" % i)
decl = "\n".join(f"extern int edge_dep{i:02d}(void);" for i in range(count))
calls = "\n".join(f"    value+=edge_dep{i:02d}();" for i in range(count))
needed_src = write("src/needed72.c",f"""#include <stdio.h>
{decl}
int main(void) {{
    int value=0;
{calls}
    printf("EDGE_NEEDED72=%d\\n",value);
    return value=={count*(count+1)//2}?0:1;
}}
""")
executable(needed_src, out/"needed72", "-L"+str(out), "-Wl,--no-as-needed",
           "-Wl,-rpath,$ORIGIN", *deps)

# A dlopened plugin legitimately references symbols exported by the main executable.
rev_so = write("src/host_reverse_lib.c", """extern int edge_host_api(int);
int edge_plugin_run(void) { return edge_host_api(23); }
""")
shared(rev_so, out/"libedge_host_reverse.so", "-Wl,-soname,libedge_host_reverse.so")
rev_main = write("src/host_reverse.c", """#include <stdio.h>
#include <dlfcn.h>
__attribute__((visibility("default"))) int edge_host_api(int x) { return x+19; }
int main(void) {
    void* h=dlopen("libedge_host_reverse.so",RTLD_NOW|RTLD_LOCAL);
    if (!h) { fprintf(stderr,"EDGE_HOST_DLERROR=%s\\n",dlerror()); return 7; }
    int (*fn)(void)=(int (*)(void))dlsym(h,"edge_plugin_run");
    if (!fn) { fprintf(stderr,"EDGE_HOST_DLSYM=%s\\n",dlerror());return 8; }
    int value=fn();
    printf("EDGE_HOST_EXPORT=%d\\n",value);
    dlclose(h);
    return value==42?0:9;
}
""")
executable(rev_main,out/"host_reverse","-Wl,--export-dynamic")

# A plugin's TLS reference must resolve against a main executable's genuine TLS module.
tls_so = write("src/host_tls_lib.c", """extern __thread int edge_host_tls;
int edge_tls_plugin_run(void){edge_host_tls+=5;return edge_host_tls;}
""")
shared(tls_so,out/"libedge_host_tls.so","-Wl,-soname,libedge_host_tls.so")
tls_main = write("src/host_tls.c", """#include <stdio.h>
#include <dlfcn.h>
__attribute__((visibility("default"))) __thread int edge_host_tls=7;
int main(void) {
    void* h=dlopen("libedge_host_tls.so",RTLD_NOW);
    if (!h) { fprintf(stderr,"EDGE_TLS_DLERROR=%s\\n",dlerror()); return 7; }
    int (*fn)(void)=(int (*)(void))dlsym(h,"edge_tls_plugin_run");
    if (!fn) { fprintf(stderr,"EDGE_TLS_DLSYM=%s\\n",dlerror());return 8; }
    int value=fn();
    printf("EDGE_HOST_TLS=%d\\n",value);
    dlclose(h);
    return value==12?0:9;
}
""")
executable(tls_main,out/"host_tls","-Wl,--export-dynamic")

# More than 1024 bytes of RUNPATH, with the required DSO only in its last path.
far = out / "edgefar"
far.mkdir(exist_ok=True)
far_src = write("src/far.c","int edge_far(void){return 2718;}\n")
shared(far_src,far/"libedge_far.so","-Wl,-soname,libedge_far.so")
rpath = ":".join(["$ORIGIN/missing%03d" % i for i in range(100)] + ["$ORIGIN/edgefar"])
long_src = write("src/long_runpath.c", """#include <stdio.h>
extern int edge_far(void);
int main(void){int v=edge_far();printf("EDGE_LONG_RUNPATH=%d\\n",v);return v==2718?0:1;}
""")
executable(long_src,out/"long_runpath","-L"+str(far),"-ledge_far","-Wl,-rpath,"+rpath)

# Standard stripped PIE: valid e_entry, but no static symbol named "main".
strip_src = write("src/stripped_main.c","""#include <stdio.h>
static int answer(void){return 12345;}
int main(void){int a=answer(); printf("EDGE_STRIPPED_MAIN=%d\\n",a);return a==12345?0:2;}
""")
executable(strip_src,out/"stripped_main")
run([strip,"--strip-all",out/"stripped_main"])

# The main executable may require more than a 4 MiB TLS segment.
huge_src = write("src/huge_tls.c", """#include <stdio.h>
__thread unsigned char edge_big_tls[5*1024*1024];
int main(void) {
    unsigned sum=0;
    for (unsigned i=0;i<sizeof(edge_big_tls);i+=4096) {
        edge_big_tls[i]=(unsigned char)(i>>12);
        sum+=edge_big_tls[i];
    }
    printf("EDGE_HUGE_TLS=%u\\n",sum);
    return sum==163200?0:1;
}
""")
executable(huge_src,out/"huge_tls")
meta={"cases":["needed72","host_reverse","host_tls","long_runpath","stripped_main","huge_tls"],
      "dependency_count":72,"runpath_length":len(rpath),"tls_bytes":5*1024*1024}
(out/"manifest.json").write_text(json.dumps(meta,indent=2))
print("GENERATED",meta,flush=True)
