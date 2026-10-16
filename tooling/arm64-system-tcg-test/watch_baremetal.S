/* ARM64 bare-metal breakpoint/watchpoint target. No output is faked:
 * GDB must stop at phase_exec or on the real LDR/STR watched_value accesses.
 */
.section .text.boot, "ax"
.balign 4
.global _start
.type _start,%function
_start:
    ldr x0, =stack_top
    mov sp, x0
    bl phase_exec
    ldr x0, =watched_value
    mov x1, #42
    bl phase_write
    bl phase_read
    bl phase_end
1:  b 1b

.balign 4
.global phase_exec
.type phase_exec,%function
phase_exec:
    mov x8, #88
    ret

.balign 4
.global phase_write
.type phase_write,%function
phase_write:
    str x1, [x0]
    ret

.balign 4
.global phase_read
.type phase_read,%function
phase_read:
    ldr x2, [x0]
    ret

.balign 4
.global phase_end
.type phase_end,%function
phase_end:
2:  b 2b

.section .data, "aw", %progbits
.balign 8
.global watched_value
.type watched_value,%object
.size watched_value,8
watched_value:
    .quad 0
