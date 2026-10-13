/*
 * Android AArch64/arm64-v8a UPX-KeyGuard outer loader.
 * SPDX-License-Identifier: GPL-2.0-or-later
 *
 * Format: [Android PIE launcher][AES256-GCM(zlib(ELF))][44-byte footer]
 * Footer: magic[8] | encrypted-size-LE64 | nonce[12] | GCM-tag[16]
 *
 * CRITICAL: Do not print the inner password prompt until the key is valid,
 * the authenticated ciphertext is decrypted, and the compressed ELF is valid.
 * Missing/corrupt keys cause a SILENT process exit by default. Debug logs
 * are opt-in via UPX_GUARD_DEBUG=1.
 *
 * By default tries memory-only execution. Android SELinux may deny exec on a
 * memfd, in which case the loader uses a 0700 temporary file as a fallback.
 * Set UPX_GUARD_NO_DISK=1 to forbid the fallback (some devices will then fail).
 * The temporary file is executable plaintext, a deliberate compatibility
 * trade-off, not an anti-dump defense.
 */
#define _GNU_SOURCE 1
#include <errno.h>
#include <fcntl.h>
#include <limits.h>
#include <mbedtls/gcm.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/syscall.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <zlib.h>

#ifndef PATH_MAX
#define PATH_MAX 4096
#endif
#ifndef MFD_CLOEXEC
#define MFD_CLOEXEC 1U
#endif
#ifndef KG_ELF_MACHINE
#define KG_ELF_MACHINE 183U /* EM_AARCH64 on Android */
#endif
#define KG_CHUNK 65536U
#define KG_FOOTER 44U
#define KG_MAX_ELF (1024ULL * 1024ULL * 1024ULL)
#define KG_MAX_PAYLOAD (1024ULL * 1024ULL * 1024ULL)
static const unsigned char KG_MAGIC[8] = { 'U','G','A','E','A','D','1', 0 };
static const unsigned char KG_AAD[] = "UPX-GUARD/AES256GCM/V1";
extern char **environ;

static void secure_erase(void *buf, size_t n) {
    volatile unsigned char *p = (volatile unsigned char *)buf;
    while (n--) *p++ = 0;
}
static int fail_silent(int code, const char *reason) {
    const char *p = getenv("UPX_GUARD_DEBUG");
    if (p && !strcmp(p, "1")) fprintf(stderr, "[KeyGuard] %s (code=%d)\n", reason, code);
    return code;
}
static int read_n(int fd, void *ptr, size_t n) {
    unsigned char *p = (unsigned char *)ptr;
    while (n) {
        ssize_t r = read(fd, p, n);
        if (r < 0 && errno == EINTR) continue;
        if (r <= 0) return -1;
        p += (size_t)r;
        n -= (size_t)r;
    }
    return 0;
}
static int write_n(int fd, const void *ptr, size_t n) {
    const unsigned char *p = (const unsigned char *)ptr;
    while (n) {
        ssize_t r = write(fd, p, n);
        if (r < 0 && errno == EINTR) continue;
        if (r <= 0) return -1;
        p += (size_t)r;
        n -= (size_t)r;
    }
    return 0;
}
static uint64_t le64(const unsigned char *p) {
    uint64_t u = 0;
    for (int i = 7; i >= 0; --i) u = (u << 8) | p[i];
    return u;
}
static int secure_eq16(const unsigned char *a, const unsigned char *b) {
    unsigned d = 0;
    for (unsigned i = 0; i < 16; ++i) d |= a[i] ^ b[i];
    return d == 0;
}
static int read_key(unsigned char key[32]) {
    const char *path = getenv("UPX_GUARD_KEY_FILE");
    if (!path || !path[0]) return -1;
    int fd = open(path, O_RDONLY | O_CLOEXEC | O_NOFOLLOW);
    if (fd < 0) return -1;
    struct stat st;
    int good = fstat(fd, &st) == 0 && S_ISREG(st.st_mode) &&
               st.st_size == 32 && read_n(fd, key, 32) == 0;
    close(fd);
    return good ? 0 : -1;
}
/* Memfd: contains only authenticated compressed bytes. */
static int decrypt_authenticated(int from, int to, uint64_t length,
                                 const unsigned char key[32],
                                 const unsigned char nonce[12],
                                 const unsigned char expected[16]) {
    mbedtls_gcm_context g;
    unsigned char in[KG_CHUNK], out[KG_CHUNK + 32], tag[16];
    int good = 1;
    mbedtls_gcm_init(&g);
    if (mbedtls_gcm_setkey(&g, MBEDTLS_CIPHER_ID_AES, key, 256) ||
        mbedtls_gcm_starts(&g, MBEDTLS_GCM_DECRYPT, nonce, 12) ||
        mbedtls_gcm_update_ad(&g, KG_AAD, sizeof(KG_AAD) - 1))
        good = 0;
    while (good && length) {
        size_t chunk = (size_t)(length > KG_CHUNK ? KG_CHUNK : length);
        size_t outlen = 0;
        if (read_n(from, in, chunk) != 0 ||
            mbedtls_gcm_update(&g, in, chunk, out, sizeof(out), &outlen) != 0 ||
            write_n(to, out, outlen) != 0) good = 0;
        length -= chunk;
    }
    if (good) {
        size_t last = 0;
        if (mbedtls_gcm_finish(&g, out, sizeof(out), &last, tag, 16) ||
            (last && write_n(to, out, last)) ||
            !secure_eq16(tag, expected)) good = 0;
    }
    mbedtls_gcm_free(&g);
    secure_erase(in, sizeof(in));
    secure_erase(out, sizeof(out));
    secure_erase(tag, sizeof(tag));
    return good ? 0 : -1;
}
/* Inflate only AFTER GCM authentication. Input is an authenticated zlib stream. */
static int decompress_zlib(int src, int dst) {
    z_stream z = {0};
    unsigned char in[KG_CHUNK], out[KG_CHUNK];
    uint64_t total = 0;
    int good = inflateInit(&z) == Z_OK;
    int stream_finished = 0;
    if (good && lseek(src, 0, SEEK_SET) < 0) good = 0;
    while (good && !stream_finished) {
        ssize_t got = read(src, in, sizeof(in));
        if (got < 0 && errno == EINTR) continue;
        if (got <= 0) { good = 0; break; }
        z.next_in = in;
        z.avail_in = (uInt)got;
        while (good && z.avail_in > 0 && !stream_finished) {
            z.next_out = out;
            z.avail_out = sizeof(out);
            int rc = inflate(&z, Z_NO_FLUSH);
            size_t wrote = sizeof(out) - z.avail_out;
            if ((rc != Z_OK && rc != Z_STREAM_END) ||
                wrote > KG_MAX_ELF - total ||
                (wrote && write_n(dst, out, wrote) != 0)) {
                good = 0;
                break;
            }
            total += wrote;
            if (rc == Z_STREAM_END) {
                stream_finished = 1;
                if (z.avail_in != 0) good = 0;
            } else if (wrote == 0 && z.avail_in == 0) {
                break;
            }
        }
    }
    if (good && stream_finished) {
        unsigned char test = 0;
        if (read(src, &test, 1) != 0) good = 0;
    }
    inflateEnd(&z);
    secure_erase(in, sizeof(in));
    secure_erase(out, sizeof(out));
    if (!good || !stream_finished || total < 64) return -1;
    unsigned char header[20];
    if (lseek(dst, 0, SEEK_SET) != 0 ||
        read_n(dst, header, sizeof(header)) != 0) return -1;
    /* ELF64 little endian, EM_AARCH64, ET_DYN/ET_EXEC */
    if (memcmp(header, "\177ELF", 4) || header[4] != 2 ||
        header[5] != 1 || header[18] != KG_ELF_MACHINE || header[19] != 0 ||
        (header[16] != 2 && header[16] != 3)) return -1;
    return lseek(dst, 0, SEEK_SET) == 0 ? 0 : -1;
}
static int copy_fd(int from, int to) {
    unsigned char buf[KG_CHUNK];
    uint64_t total = 0;
    for (;;) {
        ssize_t got = read(from, buf, sizeof(buf));
        if (got == 0) break;
        if (got < 0 && errno == EINTR) continue;
        if (got < 0 || (uint64_t)got > KG_MAX_ELF - total ||
            write_n(to, buf, (size_t)got) != 0) {
            secure_erase(buf, sizeof(buf));
            return -1;
        }
        total += (uint64_t)got;
    }
    secure_erase(buf, sizeof(buf));
    return 0;
}
/* Memory-only exec may be blocked by SELinux; a temporary executable is the fallback. */
static int fallback_exec(int memory_fd, char **argv) {
    const char *dir = getenv("UPX_GUARD_TMPDIR");
    if (!dir || !dir[0]) dir = "/data/local/tmp";
    char path[PATH_MAX];
    if (snprintf(path, sizeof(path), "%s/.upx-keyguard-%ld-XXXXXX",
                 dir, (long)getpid()) >= (int)sizeof(path))
        return fail_silent(76, "temporary pathname too long");
    int fd = mkstemp(path);
    if (fd < 0) return fail_silent(76, "unable to create temporary executable");
    int good = fchmod(fd, 0700) == 0 && lseek(memory_fd, 0, SEEK_SET) == 0 &&
               copy_fd(memory_fd, fd) == 0 && fsync(fd) == 0;
    close(fd);
    if (!good) {
        unlink(path);
        return fail_silent(76, "unable to write temporary executable");
    }
    pid_t pid = fork();
    if (pid < 0) {
        unlink(path);
        return fail_silent(76, "fork failed");
    }
    if (pid == 0) {
#if defined(KG_QEMU_TEST_HARNESS)
        /*
         * TEST HARNESS ONLY, excluded from the production Android binary:
         * QEMU linux-user does not automatically re-execute an ARM64 target
         * when an ARM64 process calls execve(). Explicitly run the host QEMU
         * executable so the authentication->inflate->inner ELF path can be
         * tested end to end under the extracted Android/Bionic rootfs.
         */
        const char *qemu = getenv("UPX_GUARD_QEMU_TEST_PATH");
        if (qemu && qemu[0] == '/') {
            size_t ac = 0;
            while (argv[ac] != NULL && ac < 1024) ++ac;
            if (ac == 1024) _exit(77);
            char **qargv = calloc(ac + 2, sizeof(*qargv));
            if (!qargv) _exit(77);
            qargv[0] = (char *)qemu;
            qargv[1] = path;
            for (size_t i = 1; i < ac; ++i) qargv[i + 1] = argv[i];
            qargv[ac + 1] = NULL;
            execve(qemu, qargv, environ);
            _exit(77);
        }
#endif
        execve(path, argv, environ);
        _exit(75);
    }
    int status = 0;
    while (waitpid(pid, &status, 0) < 0) {
        if (errno == EINTR) continue;
        unlink(path);
        return fail_silent(76, "waitpid failed");
    }
    unlink(path);
    if (WIFEXITED(status)) return WEXITSTATUS(status);
    if (WIFSIGNALED(status)) return 128 + WTERMSIG(status);
    return fail_silent(76, "child process failed");
}
int main(int argc, char **argv) {
    (void)argc;
    unsigned char key[32] = {0};
    if (read_key(key) != 0) return fail_silent(71, "missing or invalid external key");
    int self = open("/proc/self/exe", O_RDONLY | O_CLOEXEC);
    if (self < 0) {
        secure_erase(key, sizeof(key));
        return fail_silent(72, "cannot open outer ELF");
    }
    struct stat st;
    unsigned char footer[KG_FOOTER];
    int good = fstat(self, &st) == 0 && st.st_size > KG_FOOTER &&
               pread(self, footer, KG_FOOTER, st.st_size - KG_FOOTER) == KG_FOOTER &&
               memcmp(footer, KG_MAGIC, sizeof(KG_MAGIC)) == 0;
    uint64_t encrypted = good ? le64(footer + 8) : 0;
    if (!good || encrypted < 32 || encrypted > KG_MAX_PAYLOAD ||
        encrypted >= (uint64_t)(st.st_size - KG_FOOTER) ||
        (uint64_t)(st.st_size - KG_FOOTER) - encrypted < 4096) {
        secure_erase(key, sizeof(key));
        close(self);
        return fail_silent(72, "invalid encrypted payload footer");
    }
    off_t position = st.st_size - KG_FOOTER - (off_t)encrypted;
    if (lseek(self, position, SEEK_SET) != position) {
        secure_erase(key, sizeof(key));
        close(self);
        return fail_silent(72, "cannot locate encrypted data");
    }
#if defined(__NR_memfd_create)
    int compfd = (int)syscall(__NR_memfd_create, "kg-auth", MFD_CLOEXEC);
    int elffd = (int)syscall(__NR_memfd_create, "kg-elf", MFD_CLOEXEC);
#else
    int compfd = -1, elffd = -1;
#endif
    if (compfd < 0 || elffd < 0) {
        secure_erase(key, sizeof(key));
        close(self);
        if (compfd >= 0) close(compfd);
        if (elffd >= 0) close(elffd);
        return fail_silent(74, "memfd unavailable");
    }
    good = decrypt_authenticated(self, compfd, encrypted, key,
                                 footer + 16, footer + 28) == 0;
    secure_erase(key, sizeof(key));
    close(self);
    if (!good) {
        close(compfd); close(elffd);
        return fail_silent(73, "AES-256-GCM authentication failed");
    }
    good = decompress_zlib(compfd, elffd) == 0;
    close(compfd);
    if (!good) {
        close(elffd);
        return fail_silent(74, "authenticated compressed ELF invalid");
    }
    char fdpath[64];
    snprintf(fdpath, sizeof(fdpath), "/proc/self/fd/%d", elffd);
    execve(fdpath, argv, environ);
    const char *strict = getenv("UPX_GUARD_NO_DISK");
    if (strict && !strcmp(strict, "1")) {
        close(elffd);
        return fail_silent(75, "memfd exec denied; disk fallback disabled");
    }
    int status = fallback_exec(elffd, argv);
    close(elffd);
    return status;
}
