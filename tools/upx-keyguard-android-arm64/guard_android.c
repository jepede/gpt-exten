/*
 * UPX-KeyGuard Android ARM64 executable loader.
 * SPDX-License-Identifier: GPL-2.0-or-later
 *
 * The distributed ELF contains ciphertext appended behind this Android/Bionic
 * PIE executable. AES-256-GCM requires a 32-byte external key file.
 *
 * Prefer memfd execution; Android release SELinux may deny it. In that case
 * we fall back to an executable 0700 temp file in /data/local/tmp. A strict
 * no-plaintext-on-disk mode is available with UPX_GUARD_NO_DISK=1.
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
#ifndef PATH_MAX
#define PATH_MAX 4096
#endif
#ifndef MFD_CLOEXEC
#define MFD_CLOEXEC 1U
#endif
#define KG_FOOTER_SIZE 44
#define KG_CHUNK 65536
static const unsigned char kg_magic[8] = { 'U','G','A','E','A','D','1',0 };
static const unsigned char kg_aad[] = "UPX-GUARD/AES256GCM/V1";
extern char **environ;

static void zero_sensitive(void *ptr, size_t n) {
    volatile unsigned char *p = (volatile unsigned char *)ptr;
    while (n--) *p++ = 0;
}
static int read_exact(int fd, void *dst, size_t len) {
    unsigned char *p = (unsigned char *)dst;
    while (len > 0) {
        ssize_t n = read(fd, p, len);
        if (n < 0 && errno == EINTR) continue;
        if (n <= 0) return -1;
        p += n;
        len -= (size_t)n;
    }
    return 0;
}
static int write_exact(int fd, const void *src, size_t len) {
    const unsigned char *p = (const unsigned char *)src;
    while (len > 0) {
        ssize_t n = write(fd, p, len);
        if (n < 0 && errno == EINTR) continue;
        if (n <= 0) return -1;
        p += n;
        len -= (size_t)n;
    }
    return 0;
}
static int read_key(const char *path, unsigned char key[32]) {
    if (!path || !*path) return -1;
    int fd = open(path, O_RDONLY | O_CLOEXEC | O_NOFOLLOW);
    if (fd < 0) return -1;
    struct stat st;
    int ok = fstat(fd, &st) == 0 && S_ISREG(st.st_mode)
          && st.st_size == 32 && read_exact(fd, key, 32) == 0;
    close(fd);
    return ok ? 0 : -1;
}
static uint64_t get_u64le(const unsigned char *ptr) {
    uint64_t x = 0;
    for (int i = 7; i >= 0; --i) x = (x << 8) | ptr[i];
    return x;
}
static int constant_time_eq16(const unsigned char a[16],
                              const unsigned char b[16]) {
    unsigned int diff = 0;
    for (unsigned i = 0; i < 16; i++) diff |= a[i] ^ b[i];
    return diff == 0;
}
/*
 * Verify the GCM tag BEFORE attempting execution. Bytes are written only to
 * an anonymous descriptor until authentication finishes.
 */
static int decrypt_stream(int src, int dst, uint64_t remain,
                          const unsigned char key[32],
                          const unsigned char nonce[12],
                          const unsigned char expected_tag[16]) {
    mbedtls_gcm_context gcm;
    unsigned char in[KG_CHUNK];
    unsigned char out[KG_CHUNK + 32];
    unsigned char computed[16] = {0};
    int ok = 1;
    mbedtls_gcm_init(&gcm);
    if (mbedtls_gcm_setkey(&gcm, MBEDTLS_CIPHER_ID_AES, key, 256) != 0 ||
        mbedtls_gcm_starts(&gcm, MBEDTLS_GCM_DECRYPT, nonce, 12) != 0 ||
        mbedtls_gcm_update_ad(&gcm, kg_aad, sizeof(kg_aad) - 1) != 0)
        ok = 0;
    while (ok && remain > 0) {
        size_t n = remain > KG_CHUNK ? KG_CHUNK : (size_t)remain;
        size_t produced = 0;
        if (read_exact(src, in, n) != 0 ||
            mbedtls_gcm_update(&gcm, in, n, out, sizeof(out), &produced) != 0 ||
            write_exact(dst, out, produced) != 0) {
            ok = 0;
            break;
        }
        remain -= n;
    }
    if (ok) {
        size_t last = 0;
        if (mbedtls_gcm_finish(&gcm, out, sizeof(out), &last,
                               computed, sizeof(computed)) != 0 ||
            (last > 0 && write_exact(dst, out, last) != 0) ||
            !constant_time_eq16(computed, expected_tag)) ok = 0;
    }
    mbedtls_gcm_free(&gcm);
    zero_sensitive(in, sizeof(in));
    zero_sensitive(out, sizeof(out));
    zero_sensitive(computed, sizeof(computed));
    return ok ? 0 : -1;
}
static int copy_data(int src, int dst) {
    unsigned char buf[KG_CHUNK];
    for (;;) {
        ssize_t n = read(src, buf, sizeof(buf));
        if (n == 0) break;
        if (n < 0 && errno == EINTR) continue;
        if (n < 0 || write_exact(dst, buf, (size_t)n) != 0) {
            zero_sensitive(buf, sizeof(buf));
            return -1;
        }
    }
    zero_sensitive(buf, sizeof(buf));
    return 0;
}
static int disk_exec_fallback(int memory_fd, char **argv) {
    const char *dir = getenv("UPX_GUARD_TMPDIR");
    if (!dir || !*dir) dir = "/data/local/tmp";
    char path[PATH_MAX];
    if (snprintf(path, sizeof(path), "%s/.upx-keyguard-%ld-XXXXXX",
                 dir, (long)getpid()) >= (int)sizeof(path)) return 76;
    int fd = mkstemp(path);
    if (fd < 0) {
        fprintf(stderr, "[KeyGuard] 无法在 %s 创建临时文件: %s\n",
                dir, strerror(errno));
        return 76;
    }
    int ok = fchmod(fd, 0700) == 0
          && lseek(memory_fd, 0, SEEK_SET) == 0
          && copy_data(memory_fd, fd) == 0
          && fsync(fd) == 0;
    close(fd);
    if (!ok) {
        unlink(path);
        fputs("[KeyGuard] 写入可执行临时文件失败。\n", stderr);
        return 76;
    }
    pid_t child = fork();
    if (child < 0) {
        unlink(path);
        return 76;
    }
    if (child == 0) {
        execve(path, argv, environ);
        fprintf(stderr, "[KeyGuard] Android 执行内层 ELF 失败: %s\n",
                strerror(errno));
        _exit(75);
    }
    int status = 0;
    while (waitpid(child, &status, 0) < 0) {
        if (errno == EINTR) continue;
        unlink(path);
        return 76;
    }
    unlink(path);
    if (WIFEXITED(status)) return WEXITSTATUS(status);
    if (WIFSIGNALED(status)) return 128 + WTERMSIG(status);
    return 76;
}
int main(int argc, char **argv) {
    (void)argc;
    unsigned char key[32] = {0}, footer[KG_FOOTER_SIZE] = {0};
    if (read_key(getenv("UPX_GUARD_KEY_FILE"), key) != 0) {
        fputs("[KeyGuard] 缺少有效的32字节密钥文件。\n", stderr);
        return 71;
    }
    int self = open("/proc/self/exe", O_RDONLY | O_CLOEXEC);
    if (self < 0) {
        fputs("[KeyGuard] 无法打开当前 ELF。\n", stderr);
        zero_sensitive(key, sizeof(key));
        return 72;
    }
    struct stat st;
    int valid = fstat(self, &st) == 0
             && st.st_size > KG_FOOTER_SIZE
             && pread(self, footer, KG_FOOTER_SIZE,
                      st.st_size - KG_FOOTER_SIZE) == KG_FOOTER_SIZE
             && memcmp(footer, kg_magic, sizeof(kg_magic)) == 0;
    uint64_t cipher_len = valid ? get_u64le(footer + 8) : 0;
    if (!valid || cipher_len < 64
        || cipher_len > (uint64_t)(st.st_size - KG_FOOTER_SIZE)
        || (uint64_t)(st.st_size - KG_FOOTER_SIZE) - cipher_len < 4096) {
        fputs("[KeyGuard] ELF 密文尾部格式不正确。\n", stderr);
        zero_sensitive(key, sizeof(key));
        close(self);
        return 72;
    }
    off_t cipher_start = st.st_size - KG_FOOTER_SIZE - (off_t)cipher_len;
    if (lseek(self, cipher_start, SEEK_SET) < 0) {
        zero_sensitive(key, sizeof(key)); close(self); return 72;
    }
#if defined(__NR_memfd_create)
    int mem = (int)syscall(__NR_memfd_create, "upx-keyguard-inner", MFD_CLOEXEC);
#else
    int mem = -1;
#endif
    if (mem < 0) {
        fputs("[KeyGuard] 此设备不支持 memfd 创建。\n", stderr);
        zero_sensitive(key, sizeof(key)); close(self); return 74;
    }
    int decrypted = decrypt_stream(self, mem, cipher_len,
                                   key, footer + 16, footer + 28);
    zero_sensitive(key, sizeof(key));
    close(self);
    if (decrypted != 0) {
        close(mem);
        fputs("[KeyGuard] AES-256-GCM 认证失败（密钥错误或密文受损）。\n", stderr);
        return 73;
    }
    /* Some Android release builds deny exec on memfd. Try it first anyway. */
    char fdpath[64];
    snprintf(fdpath, sizeof(fdpath), "/proc/self/fd/%d", mem);
    execve(fdpath, argv, environ);
    int error = errno;
    if (getenv("UPX_GUARD_NO_DISK") &&
        strcmp(getenv("UPX_GUARD_NO_DISK"), "1") == 0) {
        fprintf(stderr, "[KeyGuard] memfd exec失败 (%d), 严格模式禁止落盘。\n",
                error);
        close(mem);
        return 75;
    }
    int rc = disk_exec_fallback(mem, argv);
    close(mem);
    return rc;
}
