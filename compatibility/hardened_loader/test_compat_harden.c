/* SPDX-License-Identifier: MIT */
#include "compat_harden.h"
#include <assert.h>
#include <errno.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct { size_t released; size_t expected; } close_state;
static void check_close(void *h, void *opaque) {
    close_state *s = (close_state *)opaque;
    assert((uintptr_t)h == s->expected);
    s->expected--;
    s->released++;
}
static void handles_test(void) {
    clh_handle_vector vec = {0};
    assert(clh_handles_init(&vec, 32768) == 0);
    for (size_t i = 1; i <= 8192; ++i)
        assert(clh_handles_push(&vec, (void *)(uintptr_t)i) == 0);
    assert(vec.count == 8192 && vec.capacity >= vec.count);
    close_state st = {0,8192};
    clh_handles_destroy(&vec, check_close, &st);
    assert(st.released == 8192);
    assert(vec.count == 0 && vec.items == NULL);
    assert(clh_handles_init(&vec, 72) == 0);
    for (size_t i = 1; i <= 72; ++i)
        assert(clh_handles_push(&vec, (void *)(uintptr_t)i) == 0);
    errno = 0;
    assert(clh_handles_push(&vec, (void *)(uintptr_t)73) == -1);
    assert(errno == E2BIG && vec.count == 72);
    close_state limited = {0,72};
    clh_handles_destroy(&vec, check_close, &limited);
    assert(limited.released == 72);
    errno = 0;
    assert(clh_handles_init(&vec, SIZE_MAX) == -1 && errno == EINVAL);
    puts("HANDLE_VECTOR_8192_REVERSE_RELEASE_AND_LIMIT_PASS");
}

typedef struct { size_t count; const char *target; int stopped; } path_state;
static int visit_path(const char *candidate, void *arg) {
    path_state *s = (path_state *)arg;
    s->count++;
    assert(strncmp(candidate, "/tmp/edge", 9) == 0);
    assert(strstr(candidate, "libedge_far.so") != NULL);
    if (strcmp(candidate, s->target) == 0) {
        s->stopped = 1;
        return 1;
    }
    return 0;
}
static void path_test(void) {
    char path[10000];
    size_t off = 0;
    for (int i = 0; i < 100; ++i) {
        int n = snprintf(path + off, sizeof(path) - off,
                         "$ORIGIN/missing%03d:",i);
        assert(n > 0 && (size_t)n < sizeof(path) - off);
        off += (size_t)n;
    }
    int n = snprintf(path + off, sizeof(path) - off,"$" "{ORIGIN}/edgefar");
    assert(n > 0 && (size_t)n < sizeof(path) - off);
    off += (size_t)n;
    assert(off > 1024);
    path_state st = {0, "/tmp/edge/edgefar/libedge_far.so",0};
    assert(clh_foreach_runpath(path, off, "/tmp/edge", "libedge_far.so",
                               visit_path, &st) == 1);
    assert(st.count == 101 && st.stopped == 1);
    errno = 0;
    assert(clh_foreach_runpath(path, off, "relative", "libedge_far.so",
                               visit_path, &st) == -1 && errno == EINVAL);
    errno = 0;
    assert(clh_foreach_runpath(path, off + 1, "/tmp/edge", "libedge_far.so",
                               visit_path, &st) == -1 && errno == EINVAL);
    puts("RUNPATH_GT_1024_ORIGIN_LAST_ENTRY_PASS");
}
static void tls_test(void) {
    const uintptr_t base = (uintptr_t)0x10000000u;
    const size_t cap = 4u * 1024u * 1024u;
    assert(clh_tls_image_fits(16, 128, 16, 0, base,cap));
    assert(clh_tls_image_fits(0, 0, 0, 0, base,cap));
    assert(!clh_tls_image_fits(5u*1024u*1024u, 5u*1024u*1024u,
                               16,0,base,cap));
    assert(!clh_tls_image_fits(256, 128, 16,0,base,cap));
    assert(!clh_tls_image_fits(16, 128, 16,cap-100,base,cap));
    assert(!clh_tls_image_fits(16, 128, 16,1,base,cap));
    assert(!clh_tls_image_fits(16, 128, 3,0,base,cap));
    assert(!clh_tls_image_fits(16, 128, 16,UINT64_MAX,base,cap));
    assert(!clh_tls_image_fits(16,128,16,0,UINTPTR_MAX-1,cap));
    uint64_t state = UINT64_C(0x9e3779b97f4a7c15);
    for (unsigned i = 0; i != 200000; ++i) {
        state ^= state << 13;
        state ^= state >> 7;
        state ^= state << 17;
        uint64_t size = state % (cap + 65536u);
        uint64_t offset = (state >> 24) % (cap + 65536u);
        int valid = clh_tls_image_fits(size,size,1,offset,base,cap);
        if (valid) assert(size <= cap && offset <= cap - size);
    }
    puts("TLS_BOUNDARY_200000_CASES_PASS");
}
int main(void) {
    handles_test();
    path_test();
    tls_test();
    puts("COMPAT_HARDEN_ALL_PASS");
    return 0;
}
