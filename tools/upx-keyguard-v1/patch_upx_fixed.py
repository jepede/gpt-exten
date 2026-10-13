#!/usr/bin/env python3
"""Patch a clean official UPX v5.2.1 tree with an AES-256-GCM external-key seal command."""
from pathlib import Path
import sys
root=Path(sys.argv[1])
main=root/'src/main.cpp'
cmake=root/'CMakeLists.txt'
s=main.read_text()
# OpenSSL must be included BEFORE UPX's conf.h: conf.h #defines noreturn
# which collides with OpenSSL 3's ossl_noreturn macro expansion.
anchor='#define WANT_WINDOWS_LEAN_H 1'
assert s.count(anchor)==1
s=s.replace(anchor,'''#if defined(__linux__) && defined(__x86_64__)
#include "upx_guard_extension.hpp"
#endif
'''+anchor,1)
anchor='int __acc_cdecl_main main(int argc, char *argv[]) /*noexcept*/ {'
assert s.count(anchor)==1
s=s.replace(anchor,anchor+'''
#if defined(__linux__) && defined(__x86_64__)
    if (argc > 1 && strcmp(argv[1], "--seal") == 0)
        return upx_keyguard::seal(argc, argv);
#endif''',1)
main.write_text(s)
s=cmake.read_text()
anchor='target_link_libraries(upx upx_vendor_ucl upx_vendor_zlib)'
assert s.count(anchor)==1
s=s.replace(anchor,anchor+'''
if(CMAKE_SYSTEM_NAME STREQUAL "Linux" AND CMAKE_SYSTEM_PROCESSOR MATCHES "^(x86_64|amd64)$")
  find_package(OpenSSL REQUIRED COMPONENTS Crypto)
  target_link_libraries(upx OpenSSL::Crypto)
endif()''',1)
cmake.write_text(s)
(root/'src/upx_guard_extension.hpp').write_bytes((Path(__file__).parent/'upx_guard_extension.hpp').read_bytes())
print('Patched upstream UPX 5.2.1 src/main.cpp, CMakeLists.txt, and header')
