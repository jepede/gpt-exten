#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
ROOT="$PWD"
: "${NDK_ROOT:?NDK_ROOT is required}"
mkdir -p validation payload/capture/prebuilt
python3 finalize_sources.py
python3 -m py_compile install.py tests/installer_test.py
CXX="$NDK_ROOT/toolchains/llvm/prebuilt/linux-x86_64/bin/aarch64-linux-android28-clang++"
READELF="$NDK_ROOT/toolchains/llvm/prebuilt/linux-x86_64/bin/llvm-readelf"
{
  "$CXX" --version
  javac -version
  echo "NDK=$(cat "$NDK_ROOT/source.properties" | tr '\n' ' ')"
  echo "Native target: Android API 28, ARM64; capture runtime: SDK 34-36"
} > validation/environment.txt 2>&1
COMMON=(-std=c++17 -O2 -g0 -fPIC -Wall -Wextra -Werror=return-type -I payload/jni/real_backdrop)
"$CXX" "${COMMON[@]}" -shared payload/capture/native_bridge.cpp \
  -o payload/capture/prebuilt/libglass_capture.so \
  -static-libstdc++ -Wl,--no-undefined -Wl,-z,max-page-size=16384 -landroid -llog \
  > validation/helper-ndk.log 2>&1
"$CXX" "${COMMON[@]}" -shared payload/jni/real_backdrop/NativeBackdrop.cpp \
  -o validation/libbackdrop_compilecheck.so \
  -static-libstdc++ -Wl,--no-undefined -Wl,-z,max-page-size=16384 -landroid -lEGL -lGLESv3 -llog -pthread \
  > validation/receiver-ndk.log 2>&1
"$READELF" -h -d payload/capture/prebuilt/libglass_capture.so validation/libbackdrop_compilecheck.so > validation/elf.txt
"$NDK_ROOT/toolchains/llvm/prebuilt/linux-x86_64/bin/llvm-nm" -D payload/capture/prebuilt/libglass_capture.so | grep Java_com_ytbl_capture_Main > validation/jni-exports.txt
[[ $(wc -l < validation/jni-exports.txt) -eq 4 ]]
SDK="${ANDROID_HOME:-${ANDROID_SDK_ROOT:-/usr/local/lib/android/sdk}}"
D8_JAR="$(find "$SDK/build-tools" -name d8.jar | sort -V | tail -1)"
ANDROID_JAR="$(find "$SDK/platforms" -maxdepth 2 -name android.jar | sort -V | tail -1)"
[[ -f "$D8_JAR" && -f "$ANDROID_JAR" ]]
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
mkdir -p "$TMP/classes" "$TMP/dex"
javac --release 8 -Xlint:all -d "$TMP/classes" payload/capture/Main.java > validation/javac.log 2>&1
mapfile -t CLASSES < <(find "$TMP/classes" -name '*.class' | sort)
java -cp "$D8_JAR" com.android.tools.r8.D8 --min-api 34 --lib "$ANDROID_JAR" --output "$TMP/dex" "${CLASSES[@]}" > validation/d8.log 2>&1
jar cf payload/capture/prebuilt/capture.dex.jar -C "$TMP/dex" classes.dex
chmod 0444 payload/capture/prebuilt/capture.dex.jar
printf '\nD8=%s\nandroid.jar=%s\n' "$D8_JAR" "$ANDROID_JAR" >> validation/environment.txt
c++ -std=c++17 -Wall -Wextra -Werror -pthread -fsanitize=address,undefined -fno-omit-frame-pointer \
  -I payload/jni/real_backdrop tests/protocol_test.cpp -o "$TMP/protocol_test"
ASAN_OPTIONS=detect_leaks=1 "$TMP/protocol_test" > validation/protocol.txt 2>&1
python3 tests/installer_test.py > validation/installer.txt 2>&1
python3 tests/shader_test.py > validation/shader.txt 2>&1
python3 - <<'PY'
from pathlib import Path
import hashlib,json,zipfile
root=Path('.')
with zipfile.ZipFile('payload/capture/prebuilt/capture.dex.jar') as z:
    assert z.namelist()==['META-INF/','META-INF/MANIFEST.MF','classes.dex'] or 'classes.dex' in z.namelist()
    assert z.read('classes.dex')[:4]==b'dex\n'
report={'native_helper_arm64_ndk':'passed','native_receiver_arm64_ndk':'passed',
        'java_compile':'passed','dex_build':'passed','jni_exports':4,
        'protocol_asan_ubsan':'passed','installer_fixture_tests':'passed',
        'shader_test':Path('validation/shader.txt').read_text().strip(),
        'original_user_archive_applied':False,'full_user_host_ndk_build':'not_run',
        'android_device_capture':'not_run','adreno_performance':'not_run'}
Path('VALIDATION.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
files=[p for p in sorted(root.rglob('*')) if p.is_file() and '__pycache__' not in p.parts and p.name!='SHA256SUMS.txt']
Path('SHA256SUMS.txt').write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+str(p)+'\n' for p in files))
print(json.dumps(report,ensure_ascii=False,indent=2))
PY
