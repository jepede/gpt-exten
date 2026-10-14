/* SPDX-License-Identifier: MIT */
#include "compat_harden.h"
#include <errno.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

#define CLH_MAX_RUNPATH (16u * 1024u * 1024u)

static int clh_add(size_t a, size_t b, size_t *out) {
    if (b > SIZE_MAX - a) { errno = EOVERFLOW; return -1; }
    *out = a + b;
    return 0;
}

int clh_handles_init(clh_handle_vector *v, size_t hard_limit) {
    if (v == NULL || hard_limit == 0 ||
        hard_limit > SIZE_MAX / sizeof(void *)) {
        errno = EINVAL;
        return -1;
    }
    memset(v, 0, sizeof(*v));
    v->hard_limit = hard_limit;
    return 0;
}

int clh_handles_push(clh_handle_vector *v, void *handle) {
    if (v == NULL || handle == NULL || v->hard_limit == 0) {
        errno = EINVAL;
        return -1;
    }
    if (v->count >= v->hard_limit) {
        errno = E2BIG;
        return -1;
    }
    if (v->count == v->capacity) {
        size_t cap = v->capacity == 0 ? 8 : v->capacity;
        if (v->capacity != 0) {
            size_t grow = v->capacity / 2 + 1;
            cap = grow > SIZE_MAX - v->capacity ?
                  v->hard_limit : v->capacity + grow;
        }
        if (cap > v->hard_limit) cap = v->hard_limit;
        if (cap <= v->capacity || cap > SIZE_MAX / sizeof(void *)) {
            errno = EOVERFLOW;
            return -1;
        }
        void **new_items = (void **)realloc(v->items, cap * sizeof(void *));
        if (new_items == NULL) { errno = ENOMEM; return -1; }
        v->items = new_items;
        v->capacity = cap;
    }
    v->items[v->count++] = handle;
    return 0;
}

void clh_handles_destroy(clh_handle_vector *v, clh_close_fn close_fn, void *user) {
    if (v == NULL) return;
    while (v->count > 0) {
        void *handle = v->items[--v->count];
        if (close_fn != NULL) close_fn(handle, user);
    }
    free(v->items);
    memset(v, 0, sizeof(*v));
}

static size_t clh_origin_token_size(const char *p, size_t n) {
    if (n >= 9 && p[0] == '$' && p[1] == '{' &&
        memcmp(p + 2, "ORIGIN}", 7) == 0) return 9;
    if (n >= 7 && p[0] == '$' &&
        memcmp(p + 1, "ORIGIN", 6) == 0) return 7;
    return 0;
}

int clh_foreach_runpath(const char *runpath, size_t runpath_len,
                       const char *origin, const char *soname,
                       clh_path_visit_fn visit, void *user) {
    if (runpath == NULL || origin == NULL || soname == NULL || visit == NULL ||
        soname[0] == '\0' || strchr(soname, '/') != NULL || origin[0] != '/') {
        errno = EINVAL;
        return -1;
    }
    if (runpath_len > CLH_MAX_RUNPATH) { errno = E2BIG; return -1; }
    if (memchr(runpath, '\0', runpath_len) != NULL) {
        errno = EINVAL;
        return -1;
    }
    const size_t origin_len = strlen(origin);
    const size_t soname_len = strlen(soname);
    size_t start = 0;
    while (start < runpath_len) {
        size_t end = start;
        while (end < runpath_len && runpath[end] != ':') end++;
        if (end > start) {
            size_t expanded_len = 0;
            for (size_t i = start; i < end;) {
                const size_t token = clh_origin_token_size(runpath + i, end - i);
                const size_t part = token ? origin_len : 1;
                if (clh_add(expanded_len, part, &expanded_len) != 0)
                    return -1;
                i += token ? token : 1;
            }
            size_t candidate_len = 0;
            if (clh_add(expanded_len, 1, &candidate_len) != 0 ||
                clh_add(candidate_len, soname_len, &candidate_len) != 0 ||
                clh_add(candidate_len, 1, &candidate_len) != 0)
                return -1;
            if (candidate_len > CLH_MAX_RUNPATH) {
                errno = E2BIG;
                return -1;
            }
            char *candidate = (char *)malloc(candidate_len);
            if (candidate == NULL) { errno = ENOMEM; return -1; }
            size_t n = 0;
            for (size_t i = start; i < end;) {
                size_t token = clh_origin_token_size(runpath + i, end - i);
                if (token) {
                    memcpy(candidate + n, origin, origin_len);
                    n += origin_len;
                    i += token;
                } else {
                    candidate[n++] = runpath[i++];
                }
            }
            if (n == 0 || candidate[n - 1] != '/') candidate[n++] = '/';
            memcpy(candidate + n, soname, soname_len);
            n += soname_len;
            candidate[n] = '\0';
            int rc = visit(candidate, user);
            free(candidate);
            if (rc > 0) return 1;
            if (rc < 0) { if (errno == 0) errno = EIO; return -1; }
        }
        start = end == runpath_len ? end : end + 1;
    }
    return 0;
}

int clh_tls_image_fits(uint64_t p_filesz, uint64_t p_memsz, uint64_t p_align,
                       uint64_t destination_offset, uintptr_t area_base,
                       size_t area_capacity) {
    if (p_filesz > p_memsz || p_memsz > SIZE_MAX ||
        destination_offset > SIZE_MAX || p_memsz > area_capacity ||
        destination_offset > area_capacity - p_memsz)
        return 0;
    if (p_align == 0) p_align = 1;
    if ((p_align & (p_align - 1)) != 0 || p_align > UINTPTR_MAX)
        return 0;
    if (destination_offset > UINTPTR_MAX - area_base)
        return 0;
    uintptr_t dest = area_base + (uintptr_t)destination_offset;
    if (dest % (uintptr_t)p_align != 0) return 0;
    return 1;
}
