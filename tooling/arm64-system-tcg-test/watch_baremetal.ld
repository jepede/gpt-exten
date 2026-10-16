ENTRY(_start)
SECTIONS {
  . = 0x40080000;
  .text : { *(.text.boot) *(.text*) }
  .rodata : ALIGN(16) { *(.rodata*) }
  .data : ALIGN(16) { *(.data*) }
  .bss (NOLOAD) : ALIGN(16) { *(.bss*) *(COMMON) }
  . = ALIGN(16);
  stack_bottom = .;
  . += 0x8000;
  stack_top = .;
}