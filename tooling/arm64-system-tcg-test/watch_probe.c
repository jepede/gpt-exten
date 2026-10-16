/*
 * watch_probe.c - Android ARM64 NDK debug laboratory (API 36).
 * Build: $NDK/toolchains/llvm/prebuilt/linux-x86_64/bin/aarch64-linux-android36-clang
 *          -O0 -g3 -fno-omit-frame-pointer -fno-inline -o watch_probe watch_probe.c
 * In a full QEMU System guest compile additionally with -static -fno-pie -no-pie,
 * or run dynamically using the Android Bionic sysroot.
 */
#include <stdint.h>
#include <inttypes.h>
#include <stdio.h>
#include <string.h>
#include <signal.h>
#include <unistd.h>
#include <sys/mman.h>

#define NOINLINE __attribute__((noinline,used))
__attribute__((aligned(8))) volatile uint64_t watched_value = 0;
__attribute__((aligned(8))) volatile uint64_t read_sink = 0;

NOINLINE uint64_t exec_target(uint64_t input) {
    __asm__ __volatile__("" ::: "memory");
    return (input ^ UINT64_C(0x1234)) + 7;
}
NOINLINE void store_target(uint64_t val) {
    __asm__ __volatile__("" ::: "memory");
    watched_value = val;
    __asm__ __volatile__("" ::: "memory");
}
NOINLINE uint64_t load_target(void) {
    __asm__ __volatile__("" ::: "memory");
    uint64_t val = watched_value;
    read_sink = val;
    return val;
}
NOINLINE void break_target(void) {
#if defined(__aarch64__)
    __asm__ __volatile__("brk #0x42" ::: "memory");
#endif
}
NOINLINE void stage_target(void) {
    __asm__ __volatile__("" ::: "memory");
}
int main(int argc, char **argv) {
    const char *mode = argc > 1 ? argv[1] : "all";
    setbuf(stdout, NULL);
    printf("MARK:READY arch=aarch64 pid=%ld watched=%p mode=%s\n",
           (long)getpid(), (void*)&watched_value, mode);
    if (strcmp(mode,"all")==0 || strcmp(mode,"exec")==0) {
        uint64_t x = exec_target(42);
        printf("MARK:EXEC_RESULT value=%" PRIu64 "\n",x);
    }
    if (strcmp(mode,"all")==0 || strcmp(mode,"write")==0 ||
        strcmp(mode,"read")==0 || strcmp(mode,"access")==0) {
        watched_value = 0;
        stage_target();
        store_target(0x12345678);
        printf("MARK:WRITE_DONE value=0x%" PRIx64 "\n", watched_value);
        uint64_t val=load_target();
        printf("MARK:READ_DONE value=0x%" PRIx64 "\n", val);
        if(val != 0x12345678) return 2;
    }
    if (strcmp(mode,"brk")==0) {
        puts("MARK:BEFORE_BRK");
        break_target();
        puts("MARK:AFTER_BRK");
    }
    puts("MARK:COMPLETE");
    return 0;
}
