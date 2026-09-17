#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
: "${NDK_ROOT:?NDK_ROOT required}"
mkdir -p validation payload/capture/prebuilt
python3 generate_payload.py > validation/generation.txt
python3 -m py_compile upgrade.py generate_payload.py tests/upgrade_test.py
TMP=$(mktemp -d);trap 'rm -rf "$TMP"' EXIT
CXX="$NDK_ROOT/toolchains/llvm/prebuilt/linux-x86_64/bin/aarch64-linux-android28-clang++"
TOOLS="$NDK_ROOT/toolchains/llvm/prebuilt/linux-x86_64/bin"
COMMON=(-std=c++17 -O2 -g0 -fPIC -fvisibility=hidden -fexceptions -Wall -Wextra -Werror=return-type -I payload/jni/real_backdrop)
printf 'extern "C" int ytbl_run_original(int, char**){return 0;}\n' > "$TMP/host_stub.cpp"
"$CXX" --version > validation/environment.txt
cat "$NDK_ROOT/source.properties" >> validation/environment.txt
javac -version >> validation/environment.txt 2>&1
"$CXX" "${COMMON[@]}" -shared payload/jni/real_backdrop/NativeBackdrop.cpp \
  payload/jni/real_backdrop/HostedCapture.cpp payload/jni/real_backdrop/native_bridge.cpp "$TMP/host_stub.cpp" \
  -static-libstdc++ -Wl,--no-undefined -Wl,--version-script=payload/jni/real_backdrop/host.exports \
  -Wl,-z,max-page-size=16384 -landroid -lEGL -lGLESv3 -llog -pthread -o "$TMP/libytbl_host_compilecheck.so" \
  > validation/host-modules-ndk.log 2>&1
"$CXX" -std=c++17 -O2 -Wall -Wextra -static-libstdc++ payload/jni/real_backdrop/HostLauncher.cpp \
  -Wl,-z,max-page-size=16384 -o "$TMP/launcher_compilecheck" > validation/launcher-ndk.log 2>&1
"$TOOLS/llvm-readelf" -h -d "$TMP/libytbl_host_compilecheck.so" "$TMP/launcher_compilecheck" > validation/elf.txt
"$TOOLS/llvm-nm" -D "$TMP/libytbl_host_compilecheck.so" | grep Java_com_ytbl_capture_ > validation/jni-exports.txt
[[ $(wc -l < validation/jni-exports.txt) -eq 6 ]]
mkdir -p "$TMP/classes" "$TMP/tests" "$TMP/dex"
javac --release 8 -Xlint:all -d "$TMP/classes" payload/capture/*.java > validation/javac.txt 2>&1
javac --release 8 -cp "$TMP/classes" -d "$TMP/tests" tests/LayerRegistryTest.java >> validation/javac.txt 2>&1
java -ea -cp "$TMP/classes:$TMP/tests" com.ytbl.capture.LayerRegistryTest > validation/registry.txt 2>&1
SDK="${ANDROID_HOME:-${ANDROID_SDK_ROOT:-/usr/local/lib/android/sdk}}"
D8_JAR=$(find "$SDK/build-tools" -name d8.jar | sort -V | tail -1)
ANDROID_JAR=$(find "$SDK/platforms" -maxdepth 2 -name android.jar | sort -V | tail -1)
[[ -f "$D8_JAR" && -f "$ANDROID_JAR" ]]
mapfile -t CLASSES < <(find "$TMP/classes" -name '*.class' | sort)
java -cp "$D8_JAR" com.android.tools.r8.D8 --min-api 34 --lib "$ANDROID_JAR" --output "$TMP/dex" "${CLASSES[@]}" > validation/d8.txt 2>&1
jar cf payload/capture/prebuilt/capture.dex.jar -C "$TMP/dex" classes.dex
chmod 0444 payload/capture/prebuilt/capture.dex.jar
python3 tests/upgrade_test.py > validation/upgrade.txt 2>&1
python3 - "$TMP" <<'PY'
from pathlib import Path
import sys
base=Path('../real_screen_backdrop/tests/protocol_test.cpp').read_text()
base=base.replace('Response r;r.sequence=17;', 'Response r;r.sequence=17;r.exclusionGeneration=1;r.excludedCount=1;')
base=base.replace('r.timestampNs=NowNs();assert(Valid(r,17));',
'''r.timestampNs=NowNs();assert(Valid(r,17));
r.excludedCount=0;assert(!Valid(r,17));r.excludedCount=1;
r.exclusionGeneration=0;assert(!Valid(r,17));r.exclusionGeneration=1;''')
Path(sys.argv[1]+'/protocol_test.cpp').write_text(base)
PY
c++ -std=c++17 -Wall -Wextra -Werror -pthread -fsanitize=address,undefined -fno-omit-frame-pointer \
  -I payload/jni/real_backdrop "$TMP/protocol_test.cpp" -o "$TMP/protocol_test"
ASAN_OPTIONS=detect_leaks=1 "$TMP/protocol_test" > validation/protocol.txt 2>&1
cp ../real_screen_backdrop/tests/shader_test.py tests/shader_test.py
python3 tests/shader_test.py > validation/shader.txt 2>&1
python3 - <<'PY'
from pathlib import Path
import json,zipfile,hashlib
with zipfile.ZipFile('payload/capture/prebuilt/capture.dex.jar') as z:assert z.read('classes.dex')[:4]==b'dex\n'
source=Path('payload/capture/Main.java').read_text()
assert '"setExcludeLayers"' in source
assert 'exclusion.current()' in source
assert 'nativeFrame(fd,request[0]' in source
assert '.setSkipScreenshot' not in source
assert 'setCaptureSecureLayers",new Class<?>[]{boolean.class},false' in source
assert 'setAllowProtected",new Class<?>[]{boolean.class},false' in source
report={'version':'per-request-exclusion-2','arm64_hosted_modules_link':'passed (stub original main; not full user host)',
        'arm64_launcher_build':'passed','jni_exports':6,'java_compile':'passed','dex_build':'passed',
        'layer_registry_tests':Path('validation/registry.txt').read_text().strip(),
        'protocol_asan_ubsan':'passed','upgrade_fixture_tests':'passed',
        'shader_test':Path('validation/shader.txt').read_text().strip(),
        'original_user_zip_applied':False,'full_user_host_ndk_build':'not_run','android_device_capture':'not_run'}
Path('VALIDATION.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
files=[p for p in sorted(Path('.').rglob('*')) if p.is_file() and '__pycache__' not in p.parts and p.name!='SHA256SUMS.txt']
Path('SHA256SUMS.txt').write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+str(p)+'\n' for p in files))
print(json.dumps(report,ensure_ascii=False,indent=2))
PY
