#!/usr/bin/env python3
"""Install the real local screen background into a NEW Surface/Ytbl project copy.
Never uploads the input, edits the original, fetches network data, or guesses a
missing source anchor. Requires Python 3.9+. The included prebuilt helper is ARM64.
"""
from __future__ import annotations
import argparse
import difflib
import hashlib
import json
import re
import shutil
import stat
import tempfile
import zipfile
from pathlib import Path, PurePosixPath

HERE=Path(__file__).resolve().parent

def one(text,old,new,label):
    if text.count(old)!=1: raise ValueError(f'{label}: expected one source anchor, found {text.count(old)}')
    return text.replace(old,new,1)

def function_span(text, signature):
    starts=[m.start() for m in re.finditer(re.escape(signature),text)]
    if len(starts)!=1: raise ValueError(f'Missing/ambiguous function: {signature}')
    start=starts[0]; brace=text.index('{',start); level=0; quote=None; line=False; block=False; i=brace
    while i<len(text):
        c=text[i]; nxt=text[i:i+2]
        if line:
            if c=='\n': line=False
        elif block:
            if nxt=='*/': block=False;i+=1
        elif quote:
            if c=='\\': i+=1
            elif c==quote: quote=None
        elif nxt=='//': line=True;i+=1
        elif nxt=='/*': block=True;i+=1
        elif c in '\"\'': quote=c
        elif c=='{': level+=1
        elif c=='}':
            level-=1
            if level==0:return start,i+1
        i+=1
    raise ValueError('Unterminated function: '+signature)

def patch_host(root):
    changes={}
    def edit(path, transform):
        path=Path(path); old=path.read_text(encoding='utf-8-sig'); new=transform(old)
        if old!=new:
            path.write_text(new,encoding='utf-8');changes[str(path.relative_to(root))]=(old,new)
    surface=root/'jni/src/Android_draw/SurfaceGlass.cpp'
    if not surface.is_file():raise ValueError('Missing existing SurfaceGlass.cpp; install into the liquid-flow project, not the original unmodified Surface project')
    def patch_surface(text):
        if 'screenbackdrop_ui::' in text:raise ValueError('Project already has this adapter; use an unpatched input')
        text='#include "SurfaceBackdropUi.h"\n'+text
        a,b=function_span(text,'bool BeginWindow('); body=text[a:b]
        if 'ImGuiWindowFlags_NoBackground' not in body:raise ValueError('Expected a NoBackground glass window')
        match=list(re.finditer(r'\bauto\s+material\s*=',body))
        if len(match)!=1:raise ValueError('Expected one main glass material')
        at=match[0].start();body=body[:at]+'const bool realScreenBackdrop = screenbackdrop_ui::Prepare();\n    '+body[at:]
        body,count=re.subn(r'if\s*\(\s*preview\s*\)',
                           'if (preview && !screenbackdrop_ui::Requested())',body)
        if count!=1:raise ValueError('Expected one preview background condition')
        # Remove the old unguarded snapshot. Capture only the local fallback;
        # the external texture must never be overwritten by the overlay itself.
        captures=list(re.finditer(r'ytbl::QueueBackdropCapture\s*\([^;]*\);',body))
        if len(captures)>1:raise ValueError('Multiple captures need a manual layering review')
        body=re.sub(r'ytbl::QueueBackdropCapture\s*\([^;]*\);','',body)
        body=one(body,'ytbl::DrawWindowGlass(material);',
                 'if (!realScreenBackdrop) ytbl::QueueBackdropCapture(ImGui::GetWindowDrawList());\n'
                 '    ytbl::DrawWindowGlass(material);','DrawWindowGlass')
        text=text[:a]+body+text[b:]
        for signature,insertion in [('void DrawSettings()', 'screenbackdrop_ui::DrawSettings();'),
                                    ('void Shutdown()', 'screenbackdrop_ui::Shutdown();')]:
            a,b=function_span(text,signature);brace=text.index('{',a)
            text=text[:brace+1]+'\n    '+insertion+text[brace+1:]
        return text
    edit(surface,patch_surface)
    creators=list((root/'jni').rglob('ANativeWindowCreator.h'))
    if len(creators)!=1:raise ValueError('Expected exactly one ANativeWindowCreator.h')
    def patch_creator(text):
        if 'flags |= 0x40' not in text and 'flags |= 0x00000040' not in text:
            raise ValueError('The supplied creator has no verified eSkipScreenshot implementation')
        pattern=r'surfaceComposerClient\.CreateSurface\(\s*name\s*,\s*width\s*,\s*height\s*,\s*skipScrenshot_\s*\)'
        result,count=re.subn(pattern,
            'surfaceComposerClient.CreateSurface(name, width, height,\n'
            '                skipScrenshot_ || detail::Functionals::GetInstance().systemVersion >= 12)',text)
        if count!=1:raise ValueError('Creator differs from the reviewed header; refusing to guess its ownership/flags path')
        return '// Real backdrop integration: own surfaces are excluded from screenshots on Android 12+.\n'+result
    edit(creators[0],patch_creator)
    mk=root/'jni/Android.mk'
    def patch_mk(text):
        return one(text,'include $(BUILD_EXECUTABLE)',
            '# Real screen backdrop (native UI owns the process and texture lifecycle).\n'
            'LOCAL_C_INCLUDES += $(LOCAL_PATH)/real_backdrop\n'
            'LOCAL_CPPFLAGS += -std=c++17 -fexceptions\n'
            'LOCAL_SRC_FILES += real_backdrop/NativeBackdrop.cpp\n'
            'LOCAL_LDLIBS += -lGLESv3 -lEGL -landroid -llog\n\n'
            'include $(BUILD_EXECUTABLE)','native executable make target')
    edit(mk,patch_mk)
    application=root/'jni/Application.mk'
    def patch_application(text):
        match=re.search(r'(?m)^\s*APP_PLATFORM\s*:?=\s*android-(\d+)\s*$',text)
        if match:
            if int(match.group(1))<28:text=text[:match.start()]+'APP_PLATFORM := android-28'+text[match.end():]
        else:text+='\nAPP_PLATFORM := android-28\n'
        match=re.search(r'(?m)^\s*APP_ABI\s*:?=([^\n]+)',text)
        if match and match.group(1).strip()!='arm64-v8a':
            raise ValueError('The prebuilt capture helper is arm64-v8a only; select that ABI explicitly')
        if not match:text+='\nAPP_ABI := arm64-v8a\n'
        return text
    edit(application,patch_application)
    widgets=root/'jni/liquid_glass/ytbl_widgets.cpp'
    if widgets.is_file() and 'void FocusRing(' in widgets.read_text(encoding='utf-8-sig'):
        def focus(text):
            a,b=function_span(text,'void FocusRing(')
            fixed='''void FocusRing(const ImRect& rect) {
    if (!ImGui::IsItemFocused() || !GImGui->NavCursorVisible) return;
    const float rounding=ImGui::GetStyle().FrameRounding+2.0f;
    const ImVec2 lo(rect.Min.x-2.0f,rect.Min.y-2.0f), hi(rect.Max.x+2.0f,rect.Max.y+2.0f);
#if IMGUI_VERSION_NUM >= 19208
    ImGui::GetWindowDrawList()->AddRect(lo,hi,ImGui::GetColorU32(ImGuiCol_NavCursor),rounding,2.0f,ImDrawFlags_RoundCornersAll);
#else
    ImGui::GetWindowDrawList()->AddRect(lo,hi,ImGui::GetColorU32(ImGuiCol_NavCursor),rounding,ImDrawFlags_RoundCornersAll,2.0f);
#endif
}'''
            return text[:a]+fixed+text[b:]
        edit(widgets,focus)
    return changes

BUILD_SH='''#!/system/bin/sh
set -eu
cd "$(dirname "$0")"
NDK_BUILD="${NDK_BUILD:-ndk-build}"
"$NDK_BUILD" NDK_PROJECT_PATH=. NDK_APPLICATION_MK=jni/Application.mk "${@:- -j4}"
mkdir -p libs/arm64-v8a/capture_runtime
cp capture/prebuilt/capture.dex.jar libs/arm64-v8a/capture_runtime/
cp capture/prebuilt/libglass_capture.so libs/arm64-v8a/capture_runtime/
chmod 0444 libs/arm64-v8a/capture_runtime/capture.dex.jar
chmod 0644 libs/arm64-v8a/capture_runtime/libglass_capture.so
printf '\\nCopy the ELF AND capture_runtime directory together to a private executable directory.\\n'
'''.replace('"${@:- -j4}"','"$@"')

def extract(archive,dest):
    total=0;seen=set()
    with zipfile.ZipFile(archive) as z:
        for item in z.infolist():
            path=PurePosixPath(item.filename);total+=item.file_size
            if path.is_absolute() or '..' in path.parts or '\\' in item.filename or stat.S_ISLNK(item.external_attr>>16):
                raise ValueError('Unsafe archive path: '+item.filename)
            if item.filename in seen:raise ValueError('Duplicate archive path: '+item.filename)
            seen.add(item.filename)
            if total>512*1024*1024:raise ValueError('Source archive is unexpectedly large')
        z.extractall(dest)

def locate(root):
    candidates=[p.parent.parent for p in root.rglob('jni/Android.mk')]
    if (root/'jni/Android.mk').is_file() and root not in candidates:candidates.append(root)
    if len(candidates)!=1:raise ValueError(f'Expected one project, found {len(candidates)}')
    return candidates[0]

def install(source,output):
    source=source.resolve(strict=True);output=output.resolve()
    zipout=output.with_name(output.name+'.zip')
    if output.exists() or zipout.exists():raise ValueError('Refusing to overwrite existing output')
    if source.is_dir() and (output==source or source in output.parents):raise ValueError('Output must not be inside the input')
    for needed in ('capture/prebuilt/capture.dex.jar','capture/prebuilt/libglass_capture.so','jni/real_backdrop/NativeBackdrop.cpp'):
        if not (HERE/'payload'/needed).is_file():raise ValueError('Incomplete bundle: '+needed)
    output.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='glass-integrate-',dir=output.parent) as temp:
        temp=Path(temp)
        if source.is_file():extract(source,temp/'input');project=locate(temp/'input')
        else:project=locate(source)
        stage=temp/'project'
        shutil.copytree(project,stage,ignore=shutil.ignore_patterns('obj','libs','.git','__pycache__'))
        changes=patch_host(stage)
        shutil.copytree(HERE/'payload',stage,dirs_exist_ok=True)
        (stage/'build_real_backdrop.sh').write_text(BUILD_SH,encoding='utf-8')
        (stage/'build_real_backdrop.sh').chmod(0o755)
        (stage/'REAL_BACKDROP_README.md').write_text((HERE/'README.md').read_text(encoding='utf-8'),encoding='utf-8')
        patch=''.join(''.join(difflib.unified_diff(a.splitlines(True),b.splitlines(True),fromfile='a/'+name,tofile='b/'+name))
                      for name,(a,b) in changes.items())
        (stage/'REAL_BACKDROP_CHANGES.patch').write_text(patch,encoding='utf-8')
        manifest={'version':'real-screen-ahb-1','source':source.name,
                  'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest() if source.is_file() else None,
                  'changed_host_files':list(changes),'original_unchanged':True,
                  'full_host_ndk_build':'not_run','android_runtime':'not_run'}
        (stage/'REAL_BACKDROP_INSTALL.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        stage.rename(output)
    with zipfile.ZipFile(zipout,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for path in sorted(output.rglob('*')):
            if path.is_file():z.write(path,Path(output.name)/path.relative_to(output))
    with zipfile.ZipFile(zipout) as z:
        if z.testzip():raise ValueError('Output ZIP integrity failed')
    print('Integrated source directory:',output)
    print('Integrated source archive:',zipout)
    print('Next: cd "'+str(output)+'" && sh build_real_backdrop.sh -j4')
    print('Original source unchanged. Full host build and Android runtime NOT tested by this installer.')

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source',type=Path,help='Your modified Surface ZIP or extracted project')
    parser.add_argument('-o','--output',type=Path,default=Path('Surface_RealBackdrop'))
    args=parser.parse_args()
    try:install(args.source,args.output)
    except (ValueError,OSError,zipfile.BadZipFile) as error:parser.exit(2,'ERROR: '+str(error)+'\n')
