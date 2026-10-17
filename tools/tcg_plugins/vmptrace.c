/*
 * QEMU 10.0.13 (Plugin API v4) - passive AArch64 instruction trace
 * Logs VMP-relevant PCs without assuming a fixed PIE load base.
 * Uses upper 32bits == 0x0000aaaa for target PIE region; 
 * this filter was observed in the experiment and is not a universal ELF rule.
 * This plugin never changes guest execution or registers.
 */
#include <qemu-plugin.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <inttypes.h>
#include <stdatomic.h>
#include <glib.h>

QEMU_PLUGIN_EXPORT int qemu_plugin_version = QEMU_PLUGIN_VERSION;
static _Atomic uint64_t hit_count;
static _Atomic uint64_t mem_count;
static uint64_t max_events = 15000;
static uint64_t translated;

typedef struct {
    uint64_t pc;
    uint32_t opcode;
    char dis[100];
    bool mem;
} Hit;

static bool interesting_offset(uint64_t va)
{
    uint64_t lo = va & 0xfff;
    switch (lo) {
    case 0x8c8: case 0x8cc: case 0x8d0: case 0x8e0:
    case 0x8f8: case 0x8fc: case 0x900: case 0x904:
    case 0x91c: case 0x920: case 0x930:
    case 0x948: case 0x94c: case 0x950:
    case 0x954: case 0x958:
    case 0x5e0: case 0x5e4: case 0x5e8: case 0x5ec:
        return true;
    default:
        return false;
    }
}

static bool selected(uint64_t pc, const char *dis)
{
    if ((pc >> 32) != 0xaaaa) {
        return false;
    }
    if (interesting_offset(pc)) {
        return true;
    }
    return g_str_has_prefix(dis, "dc ") ||
           g_str_has_prefix(dis, "ic ") ||
           g_str_has_prefix(dis, "blr ") ||
           g_str_has_prefix(dis, "br ") ||
           g_str_has_prefix(dis, "isb");
}

static void on_exec(unsigned int vcpu, void *userdata)
{
    const Hit *h = userdata;
    uint64_t n = atomic_fetch_add_explicit(&hit_count, 1, memory_order_relaxed);
    if (n >= max_events) {
        return;
    }
    char line[270];
    snprintf(line, sizeof(line),
             "[TCG-EXEC] vcpu=%u pc=0x%016"PRIx64" opcode=%08"PRIx32" %s\n",
             vcpu, h->pc, h->opcode, h->dis);
    qemu_plugin_outs(line);
}

static void on_mem(unsigned int vcpu, qemu_plugin_meminfo_t info,
                   uint64_t vaddr, void *userdata)
{
    const Hit *h = userdata;
    uint64_t n = atomic_fetch_add_explicit(&mem_count, 1, memory_order_relaxed);
    if (n >= max_events) {
        return;
    }
    char line[230];
    snprintf(line, sizeof(line),
             "[TCG-MEM] vcpu=%u pc=0x%016"PRIx64" %s vaddr=0x%016"PRIx64"\n",
             vcpu, h->pc, qemu_plugin_mem_is_store(info) ? "WRITE" : "READ",
             vaddr);
    qemu_plugin_outs(line);
}

static void translate(qemu_plugin_id_t id, struct qemu_plugin_tb *tb)
{
    size_t n = qemu_plugin_tb_n_insns(tb);
    for (size_t i = 0; i < n; ++i) {
        struct qemu_plugin_insn *insn = qemu_plugin_tb_get_insn(tb, i);
        uint64_t pc = qemu_plugin_insn_vaddr(insn);
        if ((pc >> 32) != 0xaaaa) {
            continue;
        }
        char *dis = qemu_plugin_insn_disas(insn);
        if (!dis) {
            continue;
        }
        bool use = selected(pc, dis);
        if (use) {
            Hit *h = g_new0(Hit, 1);
            h->pc = pc;
            h->mem = interesting_offset(pc);
            qemu_plugin_insn_data(insn, &h->opcode, sizeof(h->opcode));
            g_strlcpy(h->dis, dis, sizeof(h->dis));
            qemu_plugin_register_vcpu_insn_exec_cb(
                insn, on_exec, QEMU_PLUGIN_CB_NO_REGS, h);
            if (h->mem) {
                qemu_plugin_register_vcpu_mem_cb(insn, on_mem,
                        QEMU_PLUGIN_CB_NO_REGS, QEMU_PLUGIN_MEM_RW, h);
            }
            translated++;
        }
        g_free(dis);
    }
}

static void at_exit(qemu_plugin_id_t id, void *user)
{
    char line[220];
    snprintf(line, sizeof(line),
             "[TCG-SUMMARY] target_insns_translated=%"PRIu64
             " exec_events=%"PRIu64" mem_events=%"PRIu64
             " max_events=%"PRIu64"\n",
             translated, atomic_load(&hit_count), atomic_load(&mem_count),
             max_events);
    qemu_plugin_outs(line);
}

QEMU_PLUGIN_EXPORT int qemu_plugin_install(qemu_plugin_id_t id,
                                           const qemu_info_t *info,
                                           int argc, char **argv)
{
    if (!info->system_emulation) {
        fprintf(stderr, "vmptrace expects qemu-system AArch64\n");
        return -1;
    }
    for (int i = 0; i < argc; ++i) {
        if (strncmp(argv[i], "limit=", 6) == 0) {
            max_events = strtoull(argv[i] + 6, NULL, 0);
        } else {
            fprintf(stderr, "unknown plugin argument: %s\n", argv[i]);
            return -1;
        }
    }
    qemu_plugin_register_vcpu_tb_trans_cb(id, translate);
    qemu_plugin_register_atexit_cb(id, at_exit, NULL);
    return 0;
}
