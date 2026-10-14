#include <stdint.h>
#include <stdio.h>
#include <unistd.h>

__attribute__((constructor))
static void plugin_init(void)
{
    static const char msg[] = "MARK:PLUGIN_CONSTRUCTOR\n";
    (void)write(STDOUT_FILENO, msg, sizeof(msg) - 1);
}

__attribute__((destructor))
static void plugin_fini(void)
{
    static const char msg[] = "MARK:PLUGIN_DESTRUCTOR\n";
    (void)write(STDOUT_FILENO, msg, sizeof(msg) - 1);
}

__attribute__((visibility("default"), noinline, used))
int plugin_add(int a, int b)
{
    volatile int result = a + b;
    return result;
}
