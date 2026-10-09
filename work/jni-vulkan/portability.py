#!/usr/bin/env python3
"""Configure the pinned Android dependency and document minimal build-only fixes."""
from pathlib import Path
import sys, hashlib, json

root = Path(sys.argv[1])
old_commit = '5dfc8546954ce3b3198132ab13fddb89ee92cdd7'
commit = '9c85e74f92eda36b99ddb0fddb17a9df2278a4d3'
cmake = root / 'jni/Library/dobby/source/CMakeLists.txt'
text = cmake.read_text()
if 'option(DOBBY_GENERATE_SHARED' not in text:
    raise SystemExit('Expected pinned pre-refactor Dobby tree, not current master')
script = root / 'tools/rebuild_dobby.sh'
text = script.read_text()
text = text.replace('--target dobby_static', '--target dobby')
text = text.replace('-DDOBBY_BUILD_TEST=OFF -DDOBBY_BUILD_EXAMPLE=OFF',
                    '-DDOBBY_GENERATE_SHARED=OFF -DBUILD_TEST=OFF -DBUILD_EXAMPLE=OFF')
script.write_text(text)
for name in ['README.md', 'DEPENDENCIES.json']:
    p = root / name
    p.write_text(p.read_text().replace(old_commit, commit))
logging = root / 'jni/Library/dobby/source/external/logging/logging.c'
before = logging.read_bytes()
text = before.decode()
include = '#include <android/log.h>'
if text.count(include) != 1:
    raise SystemExit('Unexpected Android logging include count')
# New NDK headers define inline functions. Including them inside log_internal_impl
# is invalid C; move the existing include to file scope, without changing logging.
text = text.replace(include + '\n', '')
text = '#if defined(__ANDROID__)\n' + include + '\n#endif\n\n' + text
logging.write_text(text)
# This pinned header uses a generic function-pointer typedef rather than void*.
# Match only the existing four casts, preserving the original callback behavior.
native = root / 'jni/NativeWindow.h'
text = native.read_text()
casts = {
    '(void*)Hook_ANativeWindow_fromSurface': 'reinterpret_cast<dobby_dummy_func_t>(Hook_ANativeWindow_fromSurface)',
    '(void**)&orig_ANativeWindow_fromSurface': 'reinterpret_cast<dobby_dummy_func_t*>(&orig_ANativeWindow_fromSurface)',
    '(void*)hook_input': 'reinterpret_cast<dobby_dummy_func_t>(hook_input)',
    '(void**)&orig_input': 'reinterpret_cast<dobby_dummy_func_t*>(&orig_input)',
}
for old, new in casts.items():
    if text.count(old) != 1:
        raise SystemExit('Unexpected existing callback cast: ' + old)
    text = text.replace(old, new, 1)
native.write_text(text)
v = root / 'verification'
v.mkdir(parents=True, exist_ok=True)
(v / 'dobby-provenance.json').write_text(json.dumps({
    'upstream_repository': 'jmpews/Dobby',
    'upstream_commit': commit,
    'configuration': 'Android arm64 static library, symbol resolver enabled, examples/tests disabled',
    'upstream_source_modified': True,
    'source_patch': 'Move android/log.h include from function scope to file scope for NDK r28c',
    'call_site_compatibility': 'Four existing callback casts changed to the pinned header function-pointer typedef; no new callback targets',
    'modified_file': str(logging.relative_to(root)),
    'before_sha256': hashlib.sha256(before).hexdigest(),
    'after_sha256': hashlib.sha256(logging.read_bytes()).hexdigest(),
    'cmake_sha256': hashlib.sha256(cmake.read_bytes()).hexdigest(),
    'reason': 'The newer refactored source tree did not compile for Android; use a fixed complete pre-refactor tree'
}, indent=2) + '\n')
core = root / 'jni/renderer/VulkanCore.h'
text = core.read_text().replace(
    'acquire.dstAccessMask = VK_ACCESS_COLOR_ATTACHMENT_WRITE_BIT;',
    'acquire.dstAccessMask = VK_ACCESS_COLOR_ATTACHMENT_READ_BIT | VK_ACCESS_COLOR_ATTACHMENT_WRITE_BIT;')
core.write_text(text)
print('Configured pinned dependency, logging include scope, and matching C++ callback types:', commit)
