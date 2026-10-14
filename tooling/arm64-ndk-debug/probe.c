#define _GNU_SOURCE
#include <errno.h>
#include <dlfcn.h>
#include <inttypes.h>
#include <pthread.h>
#include <signal.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <sys/types.h>
#include <time.h>
#include <unistd.h>

/* ARM64 Android NDK debug probe. Compile with -O0 -g3. */
__attribute__((aligned(8))) volatile uint64_t watched_value = 0;
__attribute__((aligned(8))) volatile uint64_t read_sink = 0;
volatile unsigned int thread_counter = 0;

#if defined(__aarch64__)
#define ARCH "aarch64"
#else
#define ARCH "other"
#endif

#define NOINLINE __attribute__((noinline, used))
static void report(const char *s) { puts(s); fflush(stdout); }

NOINLINE uint64_t breakpoint_target(uint64_t x)
{
    __asm__ __volatile__("" ::: "memory");
    return (x ^ UINT64_C(0x12345)) + 7;
}

NOINLINE uint64_t conditional_target(int iteration)
{
    __asm__ __volatile__("" ::: "memory");
    return breakpoint_target((uint64_t)iteration);
}

NOINLINE void watch_stage_start(void)
{
    __asm__ __volatile__("" ::: "memory");
}

NOINLINE void write_watch(uint64_t x)
{
    watched_value = x;
    __asm__ __volatile__("" ::: "memory");
}

NOINLINE uint64_t read_watch(void)
{
    uint64_t value = watched_value;
    read_sink = value;
    return value;
}

NOINLINE void single_step_target(void)
{
#if defined(__aarch64__)
    __asm__ __volatile__("mov x9, #8\n\tadd x9, x9, #3\n\teor x9, x9, x9" ::: "x9", "cc", "memory");
#else
    __asm__ __volatile__("" ::: "memory");
#endif
}

static void *thread_worker(void *arg)
{
    (void)arg;
    report("MARK:THREAD_START");
    for (unsigned int i = 0; i < 5; ++i) {
        thread_counter++;
        (void)breakpoint_target(i + 99);
        struct timespec ts = {.tv_sec = 0, .tv_nsec = 20000000L};
        nanosleep(&ts, NULL);
    }
    report("MARK:THREAD_END");
    return NULL;
}

NOINLINE int run_plugin(void)
{
    report("MARK:DLOPEN_BEGIN");
    void *handle = dlopen("libprobe_plugin.so", RTLD_NOW | RTLD_LOCAL);
    if (!handle) {
        fprintf(stderr, "DLOPEN_ERROR:%s\n", dlerror());
        return 51;
    }
    dlerror();
    int (*fn)(int, int) = (int (*)(int, int))dlsym(handle, "plugin_add");
    const char *error = dlerror();
    if (error || !fn) {
        fprintf(stderr, "DLSYM_ERROR:%s\n", error ? error : "null");
        dlclose(handle);
        return 52;
    }
    int result = fn(23, 19);
    printf("MARK:DLOPEN_RESULT:%d\n", result);
    fflush(stdout);
    dlclose(handle);
    return result == 42 ? 0 : 53;
}

static int run_mprotect(void)
{
    const long page = sysconf(_SC_PAGESIZE);
    if (page <= 0) return 61;
    void *mem = mmap(NULL, (size_t)page, PROT_READ | PROT_WRITE,
                     MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    if (mem == MAP_FAILED) {
        perror("mmap");
        return 62;
    }
    *(volatile uint64_t *)mem = UINT64_C(0xABCDEF1234567890);
    if (mprotect(mem, (size_t)page, PROT_READ) != 0) {
        perror("mprotect/read");
        munmap(mem, (size_t)page);
        return 63;
    }
    uint64_t readback = *(volatile uint64_t *)mem;
    if (mprotect(mem, (size_t)page, PROT_READ | PROT_WRITE) != 0) {
        perror("mprotect/write");
        munmap(mem, (size_t)page);
        return 64;
    }
    *(volatile uint64_t *)mem = readback + 1;
    uint64_t result = *(volatile uint64_t *)mem;
    munmap(mem, (size_t)page);
    printf("MARK:MPROTECT_RESULT:0x%016" PRIx64 "\n", result);
    fflush(stdout);
    return result == UINT64_C(0xABCDEF1234567891) ? 0 : 65;
}

int main(int argc, char **argv)
{
    const char *mode = argc > 1 ? argv[1] : "basic";
    printf("MARK:READY arch=%s pid=%ld mode=%s watched=%p\n",
           ARCH, (long)getpid(), mode, (void *)&watched_value);
    fflush(stdout);

    if (strcmp(mode, "basic") == 0) {
        single_step_target();
        uint64_t acc = 0;
        for (int i = 0; i < 5; ++i) {
            acc += conditional_target(i);
        }
        printf("MARK:BASIC_DONE acc=%" PRIu64 "\n", acc);
        return 0;
    }
    if (strcmp(mode, "write") == 0) {
        watched_value = 0;
        watch_stage_start();
        write_watch(1);
        printf("MARK:WRITE_DONE value=%" PRIu64 "\n", watched_value);
        return 0;
    }
    if (strcmp(mode, "read") == 0) {
        watched_value = 1;
        watch_stage_start();
        uint64_t value = read_watch();
        printf("MARK:READ_DONE value=%" PRIu64 "\n", value);
        return value == 1 ? 0 : 2;
    }
    if (strcmp(mode, "threads") == 0) {
        pthread_t tid;
        if (pthread_create(&tid, NULL, thread_worker, NULL) != 0) return 3;
        (void)breakpoint_target(7);
        if (pthread_join(tid, NULL) != 0) return 4;
        printf("MARK:THREADS_DONE count=%u\n", thread_counter);
        return thread_counter == 5 ? 0 : 5;
    }
    if (strcmp(mode, "dlopen") == 0) return run_plugin();
    if (strcmp(mode, "mprotect") == 0) return run_mprotect();
    if (strcmp(mode, "syscall") == 0) {
        static const char line[] = "MARK:SYSCALL_WRITE\n";
        ssize_t n = write(STDOUT_FILENO, line, sizeof(line)-1);
        printf("MARK:SYSCALL_DONE n=%ld pid=%ld\n", (long)n, (long)getpid());
        return n == (ssize_t)(sizeof(line)-1) ? 0 : 6;
    }
    if (strcmp(mode, "sigtrap") == 0) {
        report("MARK:SIGTRAP_BEFORE");
        raise(SIGTRAP);
        report("MARK:SIGTRAP_AFTER");
        return 0;
    }
    if (strcmp(mode, "sigsegv") == 0) {
        report("MARK:SIGSEGV_BEFORE");
        raise(SIGSEGV);
        report("MARK:SIGSEGV_AFTER");
        return 0;
    }
    if (strcmp(mode, "brk") == 0) {
        report("MARK:BRK_BEFORE");
#if defined(__aarch64__)
        __asm__ __volatile__("brk #0x42");
#else
        raise(SIGTRAP);
#endif
        report("MARK:BRK_AFTER");
        return 0;
    }
    fprintf(stderr, "unknown mode: %s\n", mode);
    return 64;
}
