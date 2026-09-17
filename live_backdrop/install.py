#!/usr/bin/env python3
"""Apply this module to a local Surface Liquid-Flow ZIP/folder. Never uploads input."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import shutil
import stat
import tempfile
import zipfile


def once(text: str, old: str, new: str) -> str:
    if text.count(old)!=1:
        raise ValueError(f'Expected one source anchor, got {text.count(old)}: {old[:90]!r}')
    return text.replace(old,new,1)


def patch_header(text: str) -> str:
    if 'IsBackdropExclusionReady' in text:
        raise ValueError('Header already contains live-backdrop patch')
    pattern=r'(static\s+ANativeWindow\s*\*\s*Create\([^\n]*\)\s*\{)'
    insertion='''
#if defined(SURFACEGLASS_EXCLUDE_OWN_CAPTURE) && SURFACEGLASS_EXCLUDE_OWN_CAPTURE
            // Exclude ONLY this creator's own surfaces to avoid recursive capture.
            // This does not grant permission or capture protected content.
            if (detail::Functionals::GetInstance().systemVersion >= 12)
                skipScrenshot_ = true;
#endif
'''
    text,count=re.subn(pattern,lambda m:m[1]+insertion,text)
    if count!=1:raise ValueError('Cannot locate ANativeWindowCreator::Create')
    text=once(text,'m_cachedSurfaceControl.emplace(nativeWindow, std::move(surfaceControl));',
        'm_cachedSurfaceControl.emplace(nativeWindow, std::move(surfaceControl));\n'
        '            m_backdropExclusion[nativeWindow] = nativeWindow && skipScrenshot_ &&\n'
        '                detail::Functionals::GetInstance().systemVersion >= 12;')
    text=once(text,'m_cachedSurfaceControl.erase(nativeWindow);',
        'm_cachedSurfaceControl.erase(nativeWindow);\n            m_backdropExclusion.erase(nativeWindow);')
    marker='        static void Destroy(ANativeWindow *nativeWindow) {'
    methods='''        // Render-thread-only bookkeeping of the requested creation flags.
        // OEM compositor behavior still requires the on-device recursion check.
        static bool IsBackdropExclusionReady() {
            if (m_cachedSurfaceControl.empty()) return false;
            for (const auto& entry : m_cachedSurfaceControl) {
                const auto flag = m_backdropExclusion.find(entry.first);
                if (!entry.first || flag == m_backdropExclusion.end() || !flag->second)
                    return false;
            }
            return true;
        }

'''
    text=once(text,marker,methods+marker)
    text=once(text,'inline static std::unordered_map<ANativeWindow *, detail::SurfaceControl> m_cachedSurfaceControl;',
        'inline static std::unordered_map<ANativeWindow *, detail::SurfaceControl> m_cachedSurfaceControl;\n'
        '        inline static std::unordered_map<ANativeWindow *, bool> m_backdropExclusion;')
    return text


def patch_bridge(text: str) -> str:
    if 'SurfaceBackdrop::' in text:raise ValueError('SurfaceGlass already patched')
    text='#include "SurfaceBackdrop.h"\n'+text
    text=once(text,'void Shutdown() {','void Shutdown() {\n    SurfaceBackdrop::Shutdown();')
    text=once(text,'    ytbl::BeginFrame();','    ytbl::BeginFrame();\n    SurfaceBackdrop::BeginFrame();')
    text=once(text,'void DrawSettings() {','void DrawSettings() {\n    SurfaceBackdrop::Settings();')
    anchor='    auto material = ytbl::MakeMaterial('
    text=once(text,anchor,'    SurfaceBackdrop::Bind();\n\n'+anchor)
    text,count=re.subn(r'if\s*\(preview\)(\s*DrawLocalBackdrop\()',
                      r'if (preview && !SurfaceBackdrop::Requested())\1',text)
    if count!=1:raise ValueError('Cannot locate single preview backdrop call')
    text,count=re.subn(r'(^[ \t]*)(ytbl::QueueBackdropCapture\([^;]+;)',
        r'\1if (!SurfaceBackdrop::Requested())\n\1    \2',text,flags=re.M)
    if count==0:
        text=once(text,'    ytbl::DrawWindowGlass(material);',
            '    if (!SurfaceBackdrop::Requested())\n'
            '        ytbl::QueueBackdropCapture(ImGui::GetWindowDrawList());\n'
            '    ytbl::DrawWindowGlass(material);')
    elif count!=1:raise ValueError('Multiple backdrop capture calls; manual review needed')
    return text


def extract(archive: Path, destination: Path) -> None:
    with zipfile.ZipFile(archive) as z:
        total=0
        for info in z.infolist():
            p=PurePosixPath(info.filename)
            if p.is_absolute() or '..' in p.parts or '\\' in info.filename or stat.S_ISLNK(info.external_attr>>16):
                raise ValueError('Unsafe archive path: '+info.filename)
            total+=info.file_size
            if total>512*1024*1024:raise ValueError('Unexpectedly large source archive')
        z.extractall(destination)


def project_root(root: Path) -> Path:
    matches=[p.parent.parent for p in root.rglob('jni/Android.mk')
             if (p.parent/'liquid_glass/ytbl.h').is_file()]
    if (root/'jni/Android.mk').is_file() and (root/'jni/liquid_glass/ytbl.h').is_file():
        matches=[root]
    if len(matches)!=1:raise ValueError('Expected one already-integrated Ytbl Surface project')
    return matches[0]


def apply(root: Path, module: Path) -> list[str]:
    jni=root/'jni'
    headers=list(jni.rglob('ANativeWindowCreator.h'))
    if len(headers)!=1:raise ValueError('Expected one ANativeWindowCreator.h')
    header=headers[0]
    bridge=jni/'src/Android_draw/SurfaceGlass.cpp'
    if not bridge.is_file():raise ValueError('Missing SurfaceGlass.cpp; use the Liquid-Flow project')
    if (jni/'live_backdrop').exists():raise ValueError('Target already has live_backdrop/')
    # Prepare ALL text edits before writing any of them.
    edits={header:patch_header(header.read_text(encoding='utf-8-sig')),
           bridge:patch_bridge(bridge.read_text(encoding='utf-8-sig'))}
    make=jni/'Android.mk'
    addition='''
# Local, explicitly enabled cross-app backdrop. Do not include the producer JNI
# library in the host executable: it is loaded only by the separate Java helper.
LOCAL_CPPFLAGS += -DSURFACEGLASS_EXCLUDE_OWN_CAPTURE=1
LOCAL_CPP_FEATURES += exceptions
LOCAL_C_INCLUDES += $(LOCAL_PATH)/live_backdrop/native $(LOCAL_PATH)/live_backdrop/adapter
LOCAL_C_INCLUDES += $(LOCAL_PATH)/HEADER_DIR
LOCAL_SRC_FILES += live_backdrop/native/LiveBackdrop.cpp live_backdrop/adapter/SurfaceBackdrop.cpp
LOCAL_LDLIBS += -landroid -lEGL -lGLESv3 -llog -ldl

'''.replace('HEADER_DIR',header.parent.relative_to(jni).as_posix())
    edits[make]=once(make.read_text(encoding='utf-8-sig'),'include $(BUILD_EXECUTABLE)',addition+'include $(BUILD_EXECUTABLE)')
    app=jni/'Application.mk'
    data=app.read_text(encoding='utf-8-sig')
    pattern=r'(APP_PLATFORM\s*:?=\s*android-)(\d+)'
    match=re.search(pattern,data)
    if match:
        if int(match[2])<28:data=data[:match.start(2)]+'28'+data[match.end(2):]
    else:data+='\nAPP_PLATFORM := android-28\n'
    edits[app]=data
    runtime=module/'runtime/live_backdrop'
    for required in ['capture-helper.jar','liblivebg_jni.so']:
        if not (runtime/required).is_file():raise ValueError('Missing built runtime: '+required)
    for path,data in edits.items():path.write_text(data,encoding='utf-8')
    destination=jni/'live_backdrop'
    (destination/'native').mkdir(parents=True)
    (destination/'adapter').mkdir()
    # producer_jni.cpp is deliberately NOT copied into the host source tree.
    for name in ['LiveBackdrop.cpp','LiveBackdrop.h','wire.h']:
        shutil.copy2(module/'native'/name,destination/'native'/name)
    for name in ['SurfaceBackdrop.cpp','SurfaceBackdrop.h']:
        shutil.copy2(module/'adapter'/name,destination/'adapter'/name)
    shutil.copytree(runtime,root/'runtime/live_backdrop',dirs_exist_ok=True)
    shutil.copy2(module/'README.md',root/'README_LIVE_BACKDROP.md')
    return [str(p.relative_to(root)) for p in edits]


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source',type=Path,help='Liquid-Flow ZIP or unpacked project')
    parser.add_argument('--output',type=Path,default=Path('Surface_LiveBackdrop'))
    parser.add_argument('--header-only',action='store_true',help='Patch the supplied standalone ANativeWindowCreator.h only')
    args=parser.parse_args();source=args.source.resolve(strict=True);output=args.output.resolve()
    if output.exists() or output.with_suffix('.zip').exists():raise ValueError('Output already exists; choose another --output')
    module=Path(__file__).resolve().parent
    if args.header_only:
        text=patch_header(source.read_text(encoding='utf-8-sig'))
        output.parent.mkdir(parents=True,exist_ok=True);output.write_text(text,encoding='utf-8')
        print('Patched header:',output);return
    if source.is_dir() and (source==output or source in output.parents):raise ValueError('Output cannot be inside source')
    if any(c in str(output) for c in ' []()~'):raise ValueError('Use a simple output path for ndk-build')
    output.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='livebg-',dir=output.parent) as tmp:
        stage=Path(tmp)
        if source.is_file():extract(source,stage/'input');original=project_root(stage/'input')
        else:original=project_root(source)
        staged=stage/'project'
        shutil.copytree(original,staged,ignore=shutil.ignore_patterns('obj','libs','.git','__pycache__'))
        changed=apply(staged,module)
        manifest={'source':source.name,'changed':changed,'full_host_ndk_build':'not_run',
                  'device_test':'not_run','capture_default':'off','secure_capture':False}
        if source.is_file():manifest['input_sha256']=hashlib.sha256(source.read_bytes()).hexdigest()
        manifest['sha256']={p:hashlib.sha256((staged/p).read_bytes()).hexdigest() for p in changed}
        (staged/'LIVE_BACKDROP_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        staged.rename(output)
    archive=output.with_suffix('.zip')
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p in sorted(output.rglob('*')):
            if p.is_file():z.write(p,Path(output.name)/p.relative_to(output))
    with zipfile.ZipFile(archive) as z:
        if z.testzip():raise ValueError('Archive integrity failure')
    print('Project:',output,'\nArchive:',archive)
    print('Next: ndk-build -C "'+str(output)+'" -j4')
    print('Then: cp -a "'+str(output)+'/runtime/live_backdrop" "'+str(output)+'/libs/arm64-v8a/"')
    print('Copy the executable AND the live_backdrop/ folder to the same on-device directory.')
    print('Original input unchanged. No Android runtime validation was performed by this script.')


if __name__=='__main__':
    try:main()
    except (ValueError,OSError,zipfile.BadZipFile) as error:raise SystemExit('ERROR: '+str(error))
