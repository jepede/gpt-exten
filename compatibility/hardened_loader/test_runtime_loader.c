/* SPDX-License-Identifier: MIT */
/*
 * Runs on real Android/Bionic; acquires 72 distinct DSOs through dlopen,
 * records them in clh_handle_vector, invokes a symbol and closes in reverse.
 * Also searches a 100+ component RUNPATH where the valid DSO is last.
 */
#include "compat_harden.h"
#include <assert.h>
#include <dlfcn.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    void *loaded;
    unsigned candidates;
} search_ctx;
static int try_candidate(const char *candidate, void *opaque) {
    search_ctx *c = (search_ctx *)opaque;
    ++c->candidates;
    void *h = dlopen(candidate, RTLD_NOW | RTLD_LOCAL);
    if (!h) return 0;
    c->loaded = h;
    return 1;
}
static void close_handle(void *h, void *unused) {
    (void)unused;
    assert(dlclose(h) == 0);
}
int main(int argc, char **argv) {
    if (argc != 2 || argv[1][0] != '/') {
        fprintf(stderr, "usage: test_runtime_loader /absolute/fixture/directory\n");
        return 2;
    }
    const char *dir = argv[1];
    char name[8192];
    clh_handle_vector vec = {0};
    assert(clh_handles_init(&vec, 4096) == 0);
    unsigned sum = 0;
    for (unsigned i = 0; i < 72; ++i) {
        int n = snprintf(name, sizeof(name), "%s/libedge_dep%02u.so", dir, i);
        assert(n > 0 && (size_t)n < sizeof(name));
        void *h = dlopen(name, RTLD_NOW | RTLD_LOCAL);
        if (!h) {
            fprintf(stderr, "dlopen %s: %s\n",name,dlerror());
            return 3;
        }
        if (clh_handles_push(&vec, h) != 0) {
            dlclose(h);
            fprintf(stderr, "clh_handles_push: %d\n", errno);
            return 4;
        }
        char symbol[64];
        n = snprintf(symbol,sizeof(symbol), "edge_dep%02u",i);
        assert(n > 0 && (size_t)n < sizeof(symbol));
        int (*fn)(void) = (int (*)(void))dlsym(h,symbol);
        if (!fn || fn() != (int)i+1) {
            fprintf(stderr,"symbol check failed %s\n",symbol);
            return 5;
        }
        sum += (unsigned)fn();
    }
    assert(vec.count == 72 && sum == 2628);
    printf("NATIVE_BIONIC_DLOPEN_72_PASS count=%zu sum=%u\n",vec.count,sum);
    clh_handles_destroy(&vec,close_handle,NULL);
    char runpath[10000];
    size_t off=0;
    for (unsigned i=0;i<100;++i) {
        int n=snprintf(runpath+off,sizeof(runpath)-off,"$ORIGIN/missing%03u:",i);
        assert(n>0 && (size_t)n<sizeof(runpath)-off);
        off += (size_t)n;
    }
    int n=snprintf(runpath+off,sizeof(runpath)-off,
                   "$" "{ORIGIN}/edgefar");
    assert(n>0 && (size_t)n<sizeof(runpath)-off);
    off += (size_t)n;
    search_ctx search = {0,0};
    int rc=clh_foreach_runpath(runpath,off,dir,"libedge_far.so",
                                try_candidate,&search);
    if (rc!=1 || search.loaded==NULL || search.candidates!=101) {
        fprintf(stderr,"RUNPATH runtime failed: rc=%d candidates=%u\n",
                rc,search.candidates);
        return 6;
    }
    int (*farfn)(void)=(int(*)(void))dlsym(search.loaded,"edge_far");
    if (farfn==NULL || farfn()!=2718) return 7;
    assert(dlclose(search.loaded)==0);
    printf("NATIVE_BIONIC_RUNPATH_101_LAST_PASS size=%zu\n",off);
    return 0;
}
