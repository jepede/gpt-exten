#!/usr/bin/env python3
"""Offline upgrade of a Surface_RealBackdrop ZIP/directory into a NEW project.
Requires Python 3.9+. Never overwrites the input or uploads its source.
"""
from __future__ import annotations
import argparse,difflib,hashlib,json,re,shutil,stat,tempfile,zipfile
from pathlib import Path,PurePosixPath
HERE=Path(__file__).resolve().parent

def one(text,old,new,label):
    n=text.count(old)
    if n!=1:raise ValueError(f'{label}: expected one anchor, found {n}')
    return text.replace(old,new,1)

def balanced(text,start,opening='{',closing='}'):
    if text[start]!=opening:raise ValueError('Invalid block start')
    depth=0;quote=None;line=block=False;i=start
    while i<len(text):
        c=text[i];pair=text[i:i+2]
        if line:
            if c=='\n':line=False
        elif block:
            if pair=='*/':block=False;i+=1
        elif quote:
            if c=='\\':i+=1
            elif c==quote:quote=None
        elif pair=='//':line=True;i+=1
        elif pair=='/*':block=True;i+=1
        elif c in '\"\'':quote=c
        elif c==opening:depth+=1
        elif c==closing:
            depth-=1
            if depth==0:return i+1
        i+=1
    raise ValueError('Unclosed source block')

def span(text,signature):
    at=text.find(signature)
    if at<0 or text.find(signature,at+1)>=0:raise ValueError('Missing/ambiguous function: '+signature)
    brace=text.index('{',at)
    return at,brace,balanced(text,brace)

def safe_extract(source,destination):
    seen=set();total=0
    with zipfile.ZipFile(source) as z:
        for info in z.infolist():
            path=PurePosixPath(info.filename);total+=info.file_size
            if path.is_absolute() or '..' in path.parts or '\\' in info.filename or stat.S_ISLNK(info.external_attr>>16):
                raise ValueError('Unsafe ZIP entry: '+info.filename)
            if info.filename in seen:raise ValueError('Duplicate ZIP entry: '+info.filename)
            seen.add(info.filename)
            if total>512*1024*1024:raise ValueError('Input exceeds 512 MiB source limit')
        z.extractall(destination)

def locate(root):
    candidates=[p.parent.parent for p in root.rglob('jni/Android.mk')]
    if (root/'jni/Android.mk').is_file() and root not in candidates:candidates.append(root)
    if len(candidates)!=1:raise ValueError(f'Expected one NDK project; found {len(candidates)}')
    return candidates[0]

BUILD='''#!/system/bin/sh
set -eu
cd "$(dirname "$0")"
NDK_BUILD="${NDK_BUILD:-ndk-build}"
# Only remove the obsolete generated subdirectory which ndk-build treats as a file.
if [ -d ./libs/arm64-v8a/capture_runtime ]; then
    rm -rf ./libs/arm64-v8a/capture_runtime
fi
"$NDK_BUILD" NDK_PROJECT_PATH=. NDK_APPLICATION_MK=jni/Application.mk "$@"
test -s ./libs/arm64-v8a/imgui_chain_1_47
test -s ./libs/arm64-v8a/libytbl_host.so
test -s ./capture/prebuilt/capture.dex.jar
stage=$(mktemp -d ./.dist-exclude-XXXXXX)
trap 'rm -rf "$stage"' EXIT HUP INT TERM
mkdir -p "$stage/capture_runtime"
cp ./libs/arm64-v8a/imgui_chain_1_47 "$stage/"
cp ./libs/arm64-v8a/libytbl_host.so "$stage/capture_runtime/"
cp ./capture/prebuilt/capture.dex.jar "$stage/capture_runtime/"
chmod 700 "$stage" "$stage/capture_runtime" "$stage/imgui_chain_1_47"
chmod 444 "$stage/capture_runtime/capture.dex.jar"
chmod 644 "$stage/capture_runtime/libytbl_host.so"
if [ -e dist ]; then
    backup="dist.previous.$(date +%s)"
    if [ -e "$backup" ]; then echo "Backup already exists: $backup" >&2; exit 1; fi
    mv dist "$backup"
fi
mv "$stage" dist
trap - EXIT HUP INT TERM
echo 'Build complete. Deploy the entire dist/ directory, NOT only the launcher ELF.'
echo 'dist/imgui_chain_1_47 + dist/capture_runtime/{capture.dex.jar,libytbl_host.so}'
'''

def modify(project):
    changes={}
    def edit(path,transform):
        p=project/path;old=p.read_text(encoding='utf-8-sig');new=transform(old)
        if new!=old:p.write_text(new,encoding='utf-8');changes[path]=(old,new)
    if (project/'EXCLUDE_REQUEST_INSTALL.json').exists():raise ValueError('Already upgraded; use the preceding project as input')
    if not (project/'jni/real_backdrop/NativeBackdrop.cpp').is_file():
        raise ValueError('This upgrade requires the installed RealBackdrop project')

    creators=list((project/'jni').rglob('ANativeWindowCreator.h'))
    if len(creators)!=1:raise ValueError('Expected one ANativeWindowCreator.h')
    def creator(text):
        a,brace,b=span(text,'SurfaceControl CreateSurface(');body=text[a:b]
        # Remove each old global-screenshot flag / metadata branch, not secure/DRM policy.
        found=0
        while True:
            match=re.search(r'\bif\s*\(\s*skipScrenshot\b',body)
            if not match:break
            op=body.index('(',match.start());end=balanced(body,op,'(',')')
            start=body.index('{',end)
            if body[end:start].strip():raise ValueError('Unexpected screenshot branch layout')
            end=balanced(body,start)
            if re.match(r'\s*else\b',body[end:]):raise ValueError('Unsupported screenshot branch with else')
            body=body[:match.start()]+body[end:];found+=1
        if found<1:raise ValueError('Could not locate the legacy screenshot-exclusion branches')
        first=body.index('{')+1
        body=body[:first]+'\n                (void)skipScrenshot; // Global exclusion removed; requests use excludeLayers.\n'+body[first:]
        text=text[:a]+body+text[b:]
        call=r'surfaceComposerClient\.CreateSurface\(\s*name\s*,\s*width\s*,\s*height\s*,\s*[^;]+\)'
        text,n=re.subn(call,'surfaceComposerClient.CreateSurface(name, width, height, false)',text)
        if n!=1:raise ValueError('Expected one public native-window creation call')
        anchor='m_cachedSurfaceControl.emplace(nativeWindow, std::move(surfaceControl));'
        text=one(text,anchor,
            'if (nativeWindow && surfaceControl.data) {\n'
            '                screenbackdrop::hosted::Register(nativeWindow, surfaceControl.data, width, height);\n'
            '            }\n            '+anchor,'surface registration')
        anchor='m_cachedSurfaceControl[nativeWindow].DestroySurface(reinterpret_cast<detail::Surface *>(nativeWindow));'
        text=one(text,anchor,'screenbackdrop::hosted::Unregister(nativeWindow);\n            '+anchor,'surface unregister')
        if re.search(r'flags\s*\|=\s*0x0*40\b',text):raise ValueError('A global skip-screenshot write remains')
        return '#include "HostedCapture.h"\n'+text
    edit(str(creators[0].relative_to(project)),creator)

    main=project/'jni/src/main.cpp'
    text=main.read_text(encoding='utf-8-sig')
    matches=list(re.finditer(r'\bint\s+main\s*\(([^)]*)\)\s*\{',text))
    if len(matches)!=1:raise ValueError('Cannot uniquely identify the original int main entry')
    entry=matches[0];parameters=entry.group(1).strip()
    if parameters in ('','void'):call='ytbl_original_main()';prototype='void'
    elif re.match(r'int\s+\w+\s*,\s*char\s*(\*\s*\*\s*\w+|\*\s*\w+\s*\[\s*\])\s*$',parameters):
        call='ytbl_original_main(argc,argv)';prototype='int, char**'
    else:raise ValueError('Unsupported original main signature: '+parameters)
    edit('jni/src/main.cpp',lambda t:t[:entry.start()]+t[entry.start():].replace('int main','extern "C" int ytbl_original_main',1))
    adapter='extern "C" int ytbl_original_main('+prototype+');\nextern "C" int ytbl_run_original(int argc,char** argv){(void)argc;(void)argv;return '+call+';}\n'
    (project/'jni/real_backdrop/HostEntryAdapter.cpp').write_text(adapter)

    def surface(text):
        if 'screenbackdrop_ui::Prepare()' not in text:raise ValueError('Missing existing real-background integration')
        for name,value in [('materialIndex','0'),('lens','18.0f'),('blur','3.5f'),('chroma','0.18f')]:
            pattern=rf'\b(int|float)\s+{name}\s*=\s*[^;]+;'
            text,n=re.subn(pattern,lambda m:m.group(1)+' '+name+' = '+value+';',text,count=1)
            if n!=1:raise ValueError('Missing material default: '+name)
        text,n=re.subn(r'material\.readability\s*=\s*[^;]+;',
            'material.readability = 0.06f;\n    material.grain = 0.0015f;\n'
            '    material.surfaceColor = ytbl::IsLightTheme() ? ImVec4(1,1,1,0.035f) : ImVec4(0.06f,0.08f,0.12f,0.05f);',text,count=1)
        if n!=1:raise ValueError('Missing main-window readability setting')
        # If a later old assignment exists, use the same reduced grain there too.
        text=re.sub(r'material\.grain\s*=\s*[^;]+;','material.grain = 0.0015f;',text)
        return text
    edit('jni/src/Android_draw/SurfaceGlass.cpp',surface)
    def draw(text):
        pattern=r'SurfaceGlass::Checkbox\("[^"\n]*",\s*&::permeate_record\)'
        text,n=re.subn(pattern,'false /* global screenshot-exclusion switch removed */',text)
        if n>1:raise ValueError('Unexpected multiple global exclusion controls')
        text=re.sub(r'bool\s+permeate_record\s*=\s*(true|false)\s*;','bool permeate_record = false;',text)
        return text
    edit('jni/src/Android_draw/draw_Gui.cpp',draw)

    def make(text):
        if text.count('include $(BUILD_EXECUTABLE)')!=1:raise ValueError('Expected one native executable target')
        if 'real_backdrop/NativeBackdrop.cpp' not in text:raise ValueError('Missing NativeBackdrop in the existing makefile')
        text,n=re.subn(r'(?m)^(\s*LOCAL_MODULE\s*:?=\s*)imgui_chain_1_47\s*$',r'\1ytbl_host',text)
        if n!=1:raise ValueError('Expected the imgui_chain_1_47 module name')
        if re.search(r'(^|\s)-(static|pie)(\s|$)',text):raise ValueError('Host linker flags require review before converting the UI to a shared library')
        addition='''# Keep the native UI and its capture API in ONE process; export JNI only.
LOCAL_SRC_FILES += real_backdrop/HostedCapture.cpp
LOCAL_SRC_FILES += real_backdrop/native_bridge.cpp
LOCAL_SRC_FILES += real_backdrop/HostEntryAdapter.cpp
LOCAL_CPPFLAGS += -std=c++17 -fexceptions -fvisibility=hidden
LOCAL_LDFLAGS += -Wl,--version-script=$(LOCAL_PATH)/real_backdrop/host.exports
LOCAL_LDFLAGS += -Wl,-z,max-page-size=16384
include $(BUILD_SHARED_LIBRARY)

include $(CLEAR_VARS)
LOCAL_MODULE := imgui_chain_1_47
LOCAL_SRC_FILES := real_backdrop/HostLauncher.cpp
LOCAL_CPPFLAGS := -std=c++17 -fvisibility=hidden
LOCAL_LDFLAGS := -Wl,-z,max-page-size=16384
include $(BUILD_EXECUTABLE)
'''
        return text.replace('include $(BUILD_EXECUTABLE)',addition,1)
    edit('jni/Android.mk',make)
    def application(text):
        if re.search(r'(?m)^\s*APP_STL\s*:?=',text):text=re.sub(r'(?m)^\s*APP_STL\s*:?=.*$','APP_STL := c++_static',text)
        else:text+='\nAPP_STL := c++_static\n'
        match=re.search(r'(?m)^\s*APP_PLATFORM\s*:?=\s*android-(\d+)\s*$',text)
        if not match:text+='\nAPP_PLATFORM := android-28\n'
        elif int(match.group(1))<28:text=text[:match.start()]+'APP_PLATFORM := android-28'+text[match.end():]
        if not re.search(r'(?m)^\s*APP_ABI\s*:?=\s*arm64-v8a\s*$',text):raise ValueError('Select APP_ABI := arm64-v8a for this target')
        return text
    edit('jni/Application.mk',application)
    return changes

def upgrade(source:Path,output:Path):
    source=source.expanduser().resolve(strict=True);output=output.expanduser().resolve();archive=output.with_name(output.name+'.zip')
    if output.exists() or archive.exists():raise ValueError('Output exists; select a fresh -o directory')
    if source.is_dir() and (source==output or source in output.parents):raise ValueError('Output must not be inside input')
    needed=['capture/prebuilt/capture.dex.jar','jni/real_backdrop/HostedCapture.cpp','jni/real_backdrop/NativeBackdrop.cpp']
    for name in needed:
        if not (HERE/'payload'/name).is_file():raise ValueError('Incomplete upgrade bundle: '+name)
    output.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='exclude-upgrade-',dir=output.parent) as temp:
        temp=Path(temp)
        if source.is_file():safe_extract(source,temp/'input');original=locate(temp/'input')
        else:original=locate(source)
        stage=temp/'stage'
        shutil.copytree(original,stage,ignore=shutil.ignore_patterns('obj','libs','dist','dist.previous.*','.git','__pycache__'))
        changes=modify(stage)
        shutil.copytree(HERE/'payload',stage,dirs_exist_ok=True)
        (stage/'capture/native_bridge.cpp').write_text('// The active JNI bridge is now jni/real_backdrop/native_bridge.cpp, built into libytbl_host.so.\n')
        obsolete=stage/'capture/prebuilt/libglass_capture.so'
        if obsolete.exists():obsolete.unlink()
        (stage/'build_real_backdrop.sh').write_text(BUILD,encoding='utf-8');(stage/'build_real_backdrop.sh').chmod(0o755)
        (stage/'REAL_BACKDROP_README.md').write_text((HERE/'README.md').read_text(encoding='utf-8'),encoding='utf-8')
        (stage/'SCREENSHOT_VISIBLE_CHANGES.md').write_text('See REAL_BACKDROP_README.md. Global screenshot exclusion has been removed; only individual capture requests exclude the owned surfaces.\n')
        diff=''.join(''.join(difflib.unified_diff(a.splitlines(True),b.splitlines(True),fromfile='a/'+name,tofile='b/'+name)) for name,(a,b) in changes.items())
        (stage/'EXCLUDE_REQUEST_CHANGES.patch').write_text(diff,encoding='utf-8')
        manifest={'version':'per-request-exclusion-2','source':source.name,'original_unchanged':True,
                  'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest() if source.is_file() else None,
                  'changed_host_files':list(changes),'full_user_host_ndk_build':'not_run','android_runtime':'not_run',
                  'global_skip_screenshot':False,'per_request_exclude_layers':True,'launch_mode':'same-process app_process host'}
        (stage/'EXCLUDE_REQUEST_INSTALL.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        (stage/'SHA256SUMS_CURRENT.txt').write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+str(p.relative_to(stage))+'\n' for p in sorted(stage.rglob('*')) if p.is_file()),encoding='utf-8')
        stage.rename(output)
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p in sorted(output.rglob('*')):
            if p.is_file():z.write(p,Path(output.name)/p.relative_to(output))
    with zipfile.ZipFile(archive) as z:
        bad=z.testzip()
        if bad:raise ValueError('ZIP integrity failed: '+bad)
    print('Upgraded project:',output)
    print('Upgraded archive:',archive)
    print('Next: cd "'+str(output)+'" && sh build_real_backdrop.sh -j4')
    print('Deploy the ENTIRE dist directory. System screenshots remain visible; internal capture is request-scoped.')
    print('Input unchanged. Full user host build/device tests are NOT performed by this updater.')

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('source',type=Path);p.add_argument('-o','--output',type=Path,default=Path('Surface_PerRequest'))
    a=p.parse_args()
    try:upgrade(a.source,a.output)
    except (ValueError,OSError,zipfile.BadZipFile) as error:p.exit(2,'ERROR: '+str(error)+'\n')
