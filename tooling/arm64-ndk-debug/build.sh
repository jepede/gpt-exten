#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
NDK_ROOT="${NDK_ROOT:-/opt/android-ndk-r28c}"
BUILD_DIR="${BUILD_DIR:-$SCRIPT_DIR/build}"
CC="$NDK_ROOT/toolchains/llvm/prebuilt/linux-x86_64/bin/aarch64-linux-android28-clang"
READELF="$NDK_ROOT/toolchains/llvm/prebuilt/linux-x86_64/bin/llvm-readelf"
test -x "$CC" || { echo "Missing $CC" >&2; exit 1; }
mkdir -p "$BUILD_DIR"
COMMON=(-g3 -O0 -fno-omit-frame-pointer -fno-inline -fno-optimize-sibling-calls -Wall -Wextra)
"$CC" "${COMMON[@]}" -fPIE -pie "$SCRIPT_DIR/probe.c" -o "$BUILD_DIR/probe" -pthread -ldl
"$CC" "${COMMON[@]}" -fPIC -shared "$SCRIPT_DIR/probe_plugin.c" -o "$BUILD_DIR/libprobe_plugin.so"
"$CC" --version | head -3
"$READELF" -h "$BUILD_DIR/probe" | head -24
"$READELF" -l "$BUILD_DIR/probe" | grep -A1 INTERP || true
"$READELF" -s "$BUILD_DIR/probe" | grep -E 'breakpoint_target|watched_value|watch_stage_start' || true
sha256sum "$BUILD_DIR/probe" "$BUILD_DIR/libprobe_plugin.so" | tee "$BUILD_DIR/SHA256SUMS.txt"
printf 'BUILT_ANDROID_ARM64_ELF=%s\n' "$BUILD_DIR/probe"
