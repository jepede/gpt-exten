#!/usr/bin/env python3
"""Patch the cached, already-tested UPX 5.2.1 KeyGuard fork in place."""
from pathlib import Path
import sys
root = Path(sys.argv[1])
main = root / "src/main.cpp"
s = main.read_text()
marker = '#include "upx_guard_extension.hpp"'
assert s.count(marker) == 1, "UPX 5.2.1 existing KeyGuard include not found"
s = s.replace(marker, marker + '\n#include "upx_guard_android_extension.hpp"', 1)
marker = '''    if (argc > 1 && strcmp(argv[1], "--seal") == 0)
        return upx_keyguard::seal(argc, argv);'''
assert s.count(marker) == 1, "UPX 5.2.1 KeyGuard entrypoint changed"
s = s.replace(marker, marker +
''' 
    if (argc > 1 && strcmp(argv[1], "--seal-android-arm64") == 0)
        return upx_keyguard::seal_android(argc, argv);''', 1)
main.write_text(s)
header = Path(__file__).with_name("upx_guard_android_extension.hpp")
(root / "src/upx_guard_android_extension.hpp").write_bytes(header.read_bytes())
print("Modified UPX 5.2.1 packer: --seal-android-arm64")
