#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
: "${ANDROID_NDK_HOME:?Set ANDROID_NDK_HOME to an installed NDK}"
SDK="${ANDROID_HOME:-${ANDROID_SDK_ROOT:-}}"
[[ -n "$SDK" ]] || { echo 'Set ANDROID_HOME to an installed SDK'; exit 2; }
CXX="$ANDROID_NDK_HOME/toolchains/llvm/prebuilt/linux-x86_64/bin/aarch64-linux-android28-clang++"
AR="$ANDROID_NDK_HOME/toolchains/llvm/prebuilt/linux-x86_64/bin/llvm-ar"
READELF="$ANDROID_NDK_HOME/toolchains/llvm/prebuilt/linux-x86_64/bin/llvm-readelf"
JAR="$(find "$SDK/platforms" -maxdepth 2 -name android.jar | sort -V | tail -1)"
D8="$(find "$SDK/build-tools" -maxdepth 2 -name d8 | sort -V | tail -1)"
[[ -x "$CXX" && -f "$JAR" && -x "$D8" ]] || { echo 'Installed compiler/android.jar/d8 missing'; exit 2; }
mkdir -p runtime/live_backdrop validation build/classes build/dex
exec > >(tee validation/build.log) 2>&1
printf 'NDK: ';cat "$ANDROID_NDK_HOME/source.properties"
echo "SDK jar: $JAR";echo "D8: $D8"
"$CXX" --version
python3 -m py_compile install.py
python3 tests/test_installer.py
c++ -std=c++17 -Wall -Wextra -Werror -Inative tests/wire_test.cpp -pthread -o build/wire_test
./build/wire_test
"$CXX" -std=c++17 -O2 -fPIC -Wall -Wextra -Werror -Inative -shared \
  native/producer_jni.cpp -landroid -static-libstdc++ -Wl,-z,max-page-size=16384 \
  -o runtime/live_backdrop/liblivebg_jni.so
"$CXX" -std=c++17 -O2 -fPIC -Wall -Wextra -Werror -Inative -c native/LiveBackdrop.cpp -o build/LiveBackdrop.o
"$AR" rcs build/liblivebg_client.a build/LiveBackdrop.o
printf '#include "LiveBackdrop.h"\nint main(){livebg::Session s;return s.GetStatus().received?1:0;}\n' > build/smoke.cpp
"$CXX" -std=c++17 -O2 -Inative build/smoke.cpp build/liblivebg_client.a -landroid -lEGL -lGLESv3 \
  -static-libstdc++ -Wl,-z,max-page-size=16384 -o build/android_link_smoke
javac -source 8 -target 8 -classpath "$JAR" -d build/classes helper/io/github/surfaceglass/CaptureMain.java
"$D8" --min-api 34 --lib "$JAR" --output build/dex build/classes/io/github/surfaceglass/CaptureMain.class
python3 - <<'PY'
from pathlib import Path
import zipfile
with zipfile.ZipFile('runtime/live_backdrop/capture-helper.jar','w',zipfile.ZIP_DEFLATED) as z:
    z.write('build/dex/classes.dex','classes.dex')
PY
javap -private -s -classpath build/classes io.github.surfaceglass.CaptureMain > validation/java_descriptors.txt
"$READELF" -h -l -d runtime/live_backdrop/liblivebg_jni.so > validation/jni_elf.txt
"$READELF" -h -l -d build/android_link_smoke > validation/client_elf.txt
python3 - <<'PY'
from pathlib import Path
import hashlib,json
s=Path('validation/java_descriptors.txt').read_text()
for desc in ['(I)Z','(I)[I','(I[ILandroid/hardware/HardwareBuffer;IILjava/lang/String;)Z']:
    assert desc in s,desc
for f in ['validation/jni_elf.txt','validation/client_elf.txt']:
    assert 'AArch64' in Path(f).read_text()
assert Path('build/dex/classes.dex').read_bytes().startswith(b'dex\n')
report={
 'version':'0.1','android_abi':'arm64-v8a','ndk_min_api':28,
 'java_helper_ndk_compile_link':'passed','client_ndk_compile_link':'passed',
 'java_compile_and_dex':'passed','jni_descriptor_check':'passed',
 'native_protocol_tests':'passed','installer_fixture_tests':{'passed':6},
 'adapter_full_host_compile':'not_run','user_project_compile':'not_run',
 'android_runtime':'not_run','adreno_import':'not_run','compositor_exclusion':'not_run',
 'performance_benchmark':'not_run','capture_default':'off',
 'secure_content_capture':False,'network_image_transfer':False,
 'runtime_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(Path('runtime/live_backdrop').iterdir())}}
Path('validation/RESULTS.json').write_text(json.dumps(report,indent=2)+'\n')
PY
