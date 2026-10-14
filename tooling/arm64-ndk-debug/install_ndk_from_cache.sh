#!/usr/bin/env bash
# Restore NDK r28c using the two verified existing GitHub Actions artifact parts.
# No network access required after the two artifact ZIPs have been obtained.
set -euo pipefail
PART00="\${1:-/mnt/data/ndk-r28c-part-00-artifact.zip}"
PART01="\${2:-/mnt/data/ndk-r28c-part-01-artifact.zip}"
DEST="\${NDK_DEST:-/opt}"
STAGE="\${NDK_STAGE:-/mnt/data/ndk-r28c-staging}"
mkdir -p "$STAGE" "$DEST"
test -f "$PART00"
test -f "$PART01"
printf '%s  %s\n' \
  07ce7d79e2c15bfa567e2c97e961b812eb879e96fcdfe13761889fff492adf97 "$PART00" \
  40693e9180b35cdbcb23ac27e1d274d783d93af3667ca126e4fd4b98febda894 "$PART01" | sha256sum -c -
unzip -oq "$PART00" -d "$STAGE/part00"
unzip -oq "$PART01" -d "$STAGE/part01"
P0="$(find "$STAGE/part00" -type f -name 'ndk-r28c.part.00' -print -quit)"
P1="$(find "$STAGE/part01" -type f -name 'ndk-r28c.part.01' -print -quit)"
test -n "$P0"; test -n "$P1"
printf '%s  %s\n' \
  6e87d3bb98c2bfcdb9a703affd174b85ef00fff69b9aa0056372f79046308fa1 "$P0" \
  bf9baef30047e4a7e1040034619728cce0b291d76e4d67b44a0d5d0554c0197c "$P1" | sha256sum -c -
cat "$P0" "$P1" > "$STAGE/android-ndk-r28c-linux.zip"
printf '%s  %s\n' \
  dfb20d396df28ca02a8c708314b814a4d961dc9074f9a161932746f815aa552f \
  "$STAGE/android-ndk-r28c-linux.zip" | sha256sum -c -
unzip -q "$STAGE/android-ndk-r28c-linux.zip" -d "$DEST"
CLANG="$DEST/android-ndk-r28c/toolchains/llvm/prebuilt/linux-x86_64/bin/aarch64-linux-android28-clang"
test -x "$CLANG"
"$CLANG" --version | head -2
printf 'NDK_INSTALLED=%s\n' "$DEST/android-ndk-r28c"
