#!/usr/bin/env python3
"""Configure the pinned Android-compatible dependency; no runtime-hook changes."""
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
v = root / 'verification'
v.mkdir(parents=True, exist_ok=True)
(v / 'dobby-provenance.json').write_text(json.dumps({
    'upstream_repository': 'jmpews/Dobby',
    'upstream_commit': commit,
    'configuration': 'Android arm64, static library, symbol resolver enabled, examples/tests disabled',
    'upstream_source_modified': False,
    'cmake_sha256': hashlib.sha256(cmake.read_bytes()).hexdigest(),
    'reason': 'The newer refactored source tree did not compile for Android; use a fixed complete pre-refactor tree'
}, indent=2) + '\n')
core = root / 'jni/renderer/VulkanCore.h'
text = core.read_text().replace(
    'acquire.dstAccessMask = VK_ACCESS_COLOR_ATTACHMENT_WRITE_BIT;',
    'acquire.dstAccessMask = VK_ACCESS_COLOR_ATTACHMENT_READ_BIT | VK_ACCESS_COLOR_ATTACHMENT_WRITE_BIT;')
core.write_text(text)
print('Configured pinned Dobby:', commit)
