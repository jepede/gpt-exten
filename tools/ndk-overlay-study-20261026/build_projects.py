#!/usr/bin/env python3
"""Fetch pinned graphics demos and build Android ARM64 executables."""

import difflib
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tarfile
import time
import urllib.request

ROOT = Path.cwd()
OUT = ROOT / "overlay-study-output"
OUT.mkdir(exist_ok=True)
for name in ("sources", "bin", "logs", "patches", "metadata"):
    (OUT / name).mkdir(exist_ok=True)
WORK = ROOT / "overlay-study-build"
WORK.mkdir(exist_ok=True)

PROJECTS = [
    ("enen", "enenH/AndroidImgui", "63c9d83620665f87dce26e0a6de9f209b6d69593"),
    ("afan", "AFan4724/AndroidSurfaceImgui-Enhanced", "3ba27a694d428b053a4c3c0d7e6859b6a42e670f"),
    ("wanmian", "wanmian0323/Android_imgui_Vulkan", "ab6aa630b3244ac8fba12c544f48f9b62fab581e"),
]
SUBMODULES = [
    ("imgui", "ocornut/imgui", "0666da6a72b20f6586b6d7f059b29f2c09ca8371"),
    ("freetype", "freetype/freetype", "b04db3872cfac5ee4fd4f895933cebce3576fbf0"),
]
records = []
builds = []


def download_source(repo, commit, destination):
    archive = WORK / (repo.replace("/", "-") + "-" + commit + ".tar.gz")
    url = f"https://codeload.github.com/{repo}/tar.gz/{commit}"
    for attempt in range(3):
        try:
            with urllib.request.urlopen(url, timeout=90) as response, archive.open("wb") as output:
                shutil.copyfileobj(response, output)
            break
        except Exception:
            if attempt == 2:
                raise
            time.sleep(3)
    extraction = WORK / (archive.stem + "-extract")
    extraction.mkdir(exist_ok=True)
    with tarfile.open(archive, "r:gz") as bundle:
        bundle.extractall(extraction, filter="data")
    roots = list(extraction.iterdir())
    assert len(roots) == 1
    shutil.copytree(roots[0], destination, dirs_exist_ok=True, symlinks=True)
    records.append({"repository": repo, "commit": commit, "source_url": url,
                    "archive_bytes": archive.stat().st_size,
                    "archive_sha256": hashlib.sha256(archive.read_bytes()).hexdigest(),
                    "local_path": str(destination.relative_to(OUT))})


def run(name, args, cwd, timeout=720):
    log = OUT / "logs" / (name + ".log")
    start = time.monotonic()
    result = {"name": name, "command": [str(x) for x in args], "cwd": str(cwd)}
    try:
        with log.open("wb") as stream:
            process = subprocess.run([str(x) for x in args], cwd=cwd, stdout=stream,
                                     stderr=subprocess.STDOUT, timeout=timeout)
        result["rc"] = process.returncode
    except subprocess.TimeoutExpired:
        result["rc"] = 124
    result["seconds"] = round(time.monotonic() - start, 2)
    builds.append(result)
    print(json.dumps(result), flush=True)
    if result["rc"]:
        print(log.read_text(errors="replace")[-7000:], flush=True)
    return result["rc"] == 0


def patch_record(name, before, after):
    (OUT / "patches" / (name + ".patch")).write_text("".join(difflib.unified_diff(
        before.splitlines(keepends=True), after.splitlines(keepends=True),
        fromfile=name + ".upstream", tofile=name + ".build")))


def retain_binary(name, path):
    assert path.is_file(), path
    target = OUT / "bin" / name
    shutil.copy2(path, target)
    target.chmod(0o755)
    return target


for name, repo, commit in PROJECTS:
    download_source(repo, commit, OUT / "sources" / name)
for path, repo, commit in SUBMODULES:
    download_source(repo, commit, OUT / "sources" / "enen" / path)

sdk = Path(os.environ.get("ANDROID_HOME", "/usr/local/lib/android/sdk"))
candidates = [sdk / "ndk" / "28.2.13676358", sdk / "ndk" / "27.2.12479018"]
if os.environ.get("ANDROID_NDK_LATEST_HOME"):
    candidates.append(Path(os.environ["ANDROID_NDK_LATEST_HOME"]))
candidates.extend(sorted((sdk / "ndk").glob("*"), reverse=True))
ndk = next((path for path in candidates if (path / "ndk-build").is_file()), None)
assert ndk is not None, "No preinstalled Android NDK; no automatic external toolchain download."
(OUT / "metadata" / "ndk-source.properties").write_text((ndk / "source.properties").read_text())
(OUT / "metadata" / "sources.json").write_text(json.dumps(records, indent=2) + "\n")

for backend in ("vulkan", "opengl"):
    source = WORK / ("afan-" + backend)
    shutil.copytree(OUT / "sources" / "afan", source, symlinks=True)
    main = source / "jni/src/main.cpp"
    before = main.read_text()
    after = before.replace("GraphicsManager::VULKAN", "GraphicsManager::OPENGL") if backend == "opengl" else before
    main.write_text(after)
    if before != after:
        patch_record("afan-main-opengl", before, after)
    libs = WORK / ("afan-" + backend + "-libs")
    success = run("afan-" + backend, [ndk / "ndk-build", "-j2", "APP_ABI=arm64-v8a",
                  "APP_PLATFORM=android-26", "APP_STL=c++_static",
                  "NDK_OUT=" + str(WORK / ("afan-" + backend + "-objects")),
                  "NDK_LIBS_OUT=" + str(libs)], source)
    if success:
        retain_binary("afan-" + backend, libs / "arm64-v8a/AndroidSurfaceImguiEnhanced")

source = WORK / "wanmian"
shutil.copytree(OUT / "sources" / "wanmian", source, symlinks=True)
libs = WORK / "wanmian-libs"
if run("wanmian-vulkan", [ndk / "ndk-build", "-j2", "APP_ABI=arm64-v8a",
       "APP_PLATFORM=android-26", "APP_STL=c++_static",
       "NDK_OUT=" + str(WORK / "wanmian-objects"), "NDK_LIBS_OUT=" + str(libs)], source):
    retain_binary("wanmian-vulkan", libs / "arm64-v8a/Android_imgui_Vulkan.rc")

source = WORK / "enen"
shutil.copytree(OUT / "sources" / "enen", source, symlinks=True)
cmake = source / "CMakeLists.txt"
before = cmake.read_text()
after = before + "\n# Standalone upstream example with explicit renderer selection.\n"
main = (source / "test/main.cpp").read_text()
for backend in ("vulkan", "opengl", "software"):
    variant = main.replace("GraphicsManager::SOFTWARE", "GraphicsManager::" + backend.upper())
    (source / ("test/main_" + backend + ".cpp")).write_text(variant)
    if variant != main:
        patch_record("enen-main-" + backend, main, variant)
    after += (f"add_executable(enen_{backend} test/main_{backend}.cpp test/TouchHelperA.cpp)\n"
              f"target_link_libraries(enen_{backend} PRIVATE AndroidImgui)\n")
cmake.write_text(after)
patch_record("enen-cmake", before, after)
build_dir = WORK / "enen-objects"
configured = run("enen-configure", ["cmake", "-S", source, "-B", build_dir, "-G", "Ninja",
                 "-DCMAKE_TOOLCHAIN_FILE=" + str(ndk / "build/cmake/android.toolchain.cmake"),
                 "-DCMAKE_ANDROID_NDK=" + str(ndk), "-DANDROID_ABI=arm64-v8a",
                 "-DANDROID_PLATFORM=android-26", "-DANDROID_STL=c++_static",
                 "-DCMAKE_BUILD_TYPE=RelWithDebInfo", "-DFT_DISABLE_ZLIB=ON",
                 "-DFT_DISABLE_BZIP2=ON", "-DFT_DISABLE_PNG=ON", "-DFT_DISABLE_HARFBUZZ=ON",
                 "-DFT_DISABLE_BROTLI=ON"], source)
if configured and run("enen-build", ["cmake", "--build", build_dir, "-j2"], source):
    for backend in ("vulkan", "opengl", "software"):
        retain_binary("enen-" + backend, build_dir / ("enen_" + backend))

probe = ROOT / "tools/ndk-overlay-study-20261026/environment_probe.c"
if probe.exists():
    compiler = ndk / "toolchains/llvm/prebuilt/linux-x86_64/bin/aarch64-linux-android26-clang"
    run("environment-probe-build", [compiler, "-O1", "-g", probe, "-ldl", "-llog", "-lEGL", "-lGLESv3", "-o", OUT / "bin/environment-probe"], ROOT)
    shutil.copy2(probe, OUT / "metadata/environment_probe.c")

readelf = ndk / "toolchains/llvm/prebuilt/linux-x86_64/bin/llvm-readelf"
for binary in sorted((OUT / "bin").iterdir()):
    run("elf-" + binary.name, [readelf, "-h", "-d", "-l", binary], ROOT)
(OUT / "metadata" / "build-results.json").write_text(json.dumps(builds, indent=2) + "\n")
hashes = []
for file in sorted(OUT.rglob("*")):
    if file.is_file() and not file.is_symlink():
        hashes.append(hashlib.sha256(file.read_bytes()).hexdigest() + "  " + str(file.relative_to(OUT)))
(OUT / "SHA256SUMS.txt").write_text("\n".join(hashes) + "\n")
archive = ROOT / "native-overlay-study-20261026.tar.gz"
with tarfile.open(archive, "w:gz") as bundle:
    bundle.add(OUT, arcname=OUT.name)
part_dir = ROOT / "overlay-study-parts"
part_dir.mkdir(exist_ok=True)
parts = []
with archive.open("rb") as stream:
    index = 0
    while data := stream.read(95_000_000):
        part = part_dir / f"part-{index:02d}.bin"
        part.write_bytes(data)
        parts.append({"file": part.name, "size": len(data), "sha256": hashlib.sha256(data).hexdigest()})
        index += 1
manifest = {"archive": archive.name, "size": archive.stat().st_size,
            "sha256": hashlib.sha256(archive.read_bytes()).hexdigest(), "parts": parts,
            "sources": records, "builds": builds}
(part_dir / "TRANSFER_MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n")
assert all(part["size"] < 100_000_000 for part in parts)
print(json.dumps({"archive_bytes": archive.stat().st_size, "parts": parts,
                  "binaries": [p.name for p in (OUT / "bin").iterdir()]}, indent=2))
