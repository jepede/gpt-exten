#!/usr/bin/env python3
"""Pinned-source build portability corrections, recorded in the delivered project."""
from pathlib import Path
import sys, hashlib, json

root = Path(sys.argv[1])
path = root / 'jni/Library/dobby/source/source/TrampolineBridge/ClosureTrampolineBridge/arm64/closure_bridge_arm64.asm'
before = path.read_text()
old = ('adrp TMP_REG_0, cdecl(common_closure_bridge_handler)@PAGE\n'
       'add TMP_REG_0, TMP_REG_0, cdecl(common_closure_bridge_handler)@PAGEOFF')
new = ('#if defined(__APPLE__)\n' + old + '\n'
       '#else\n'
       '// ELF position-independent GOT relocation syntax (Android/Linux).\n'
       'adrp TMP_REG_0, :got:cdecl(common_closure_bridge_handler)\n'
       'ldr TMP_REG_0, [TMP_REG_0, :got_lo12:cdecl(common_closure_bridge_handler)]\n'
       '#endif')
if new not in before:
    if before.count(old) != 1:
        raise SystemExit('Pinned Dobby assembly anchor changed; refusing a partial patch')
    after = before.replace(old, new, 1)
    path.write_text(after)
else:
    after = before
v = root / 'verification'
v.mkdir(parents=True, exist_ok=True)
(v / 'dobby-portability.json').write_text(json.dumps({
    'upstream_commit': '5dfc8546954ce3b3198132ab13fddb89ee92cdd7',
    'file': str(path.relative_to(root)),
    'change': 'Use ELF GOT relocation syntax on non-Apple ARM64; same callback address and calling convention',
    'before_sha256': hashlib.sha256(before.encode()).hexdigest(),
    'after_sha256': hashlib.sha256(after.encode()).hexdigest()
}, indent=2) + '\n')
core = root / 'jni/renderer/VulkanCore.h'
text = core.read_text()
text = text.replace('acquire.dstAccessMask = VK_ACCESS_COLOR_ATTACHMENT_WRITE_BIT;',
                    'acquire.dstAccessMask = VK_ACCESS_COLOR_ATTACHMENT_READ_BIT | VK_ACCESS_COLOR_ATTACHMENT_WRITE_BIT;')
core.write_text(text)
print('Applied Android ELF build portability fix and color-attachment blend access mask')
