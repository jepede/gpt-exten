import importlib.util, tempfile, zipfile, hashlib, json
from pathlib import Path
base=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('upgrade',base/'upgrade.py');u=importlib.util.module_from_spec(spec);spec.loader.exec_module(u)
checks=[]
def check(name,value):
    assert value,name
    checks.append(name)
with tempfile.TemporaryDirectory() as td:
    root=Path(td)/'fixture'
    def write(name,text):
        p=root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)
    write('jni/Android.mk','''LOCAL_PATH := $(call my-dir)
include $(CLEAR_VARS)
LOCAL_MODULE := imgui_chain_1_47
LOCAL_SRC_FILES := src/main.cpp
LOCAL_SRC_FILES += real_backdrop/NativeBackdrop.cpp
include $(BUILD_EXECUTABLE)
''')
    write('jni/Application.mk','APP_ABI := arm64-v8a\nAPP_PLATFORM := android-28\nAPP_STL := c++_static\n')
    write('jni/src/main.cpp','int main(int argc, char* argv[]) { return argc==0 || argv==nullptr; }\n')
    write('jni/real_backdrop/NativeBackdrop.cpp','// existing module\n')
    write('jni/src/Android_draw/SurfaceGlass.cpp','''int materialIndex=1;
float lens=18.0f;
float blur=8.0f;
float chroma=0.35f;
bool BeginWindow(){
    const bool real = screenbackdrop_ui::Prepare();
    auto material = ytbl::MakeMaterial();
    material.readability=0.25f;
    return real;
}
''')
    write('jni/src/Android_draw/draw_Gui.cpp','''bool permeate_record = false;
void draw(){if(SurfaceGlass::Checkbox("排除本窗口截图/录屏", &::permeate_record)){recreate();}}
''')
    write('jni/include/native_surface/ANativeWindowCreator.h','''struct SurfaceComposerClient {
SurfaceControl CreateSurface(const char* name,int width,int height,bool skipScrenshot) {
    if (skipScrenshot && (version==10 || version==11)) { metadata.setInt32(2,441731); }
    unsigned flags=0;
    if (skipScrenshot && version>=12) { flags |= 0x40; }
    if (version==9) { int windowType=-1; if(skipScrenshot) { windowType=441731; } }
    return {};
}
};
struct ANativeWindowCreator {
static void* Create(const char* name,int width,int height,bool skipScrenshot_){
    auto surfaceControl=surfaceComposerClient.CreateSurface(name, width, height, skipScrenshot_ || detail::Functionals::GetInstance().systemVersion >= 12);
    auto nativeWindow=surfaceControl.GetSurface();
    m_cachedSurfaceControl.emplace(nativeWindow, std::move(surfaceControl));
    return nativeWindow;
}
static void Destroy(void* nativeWindow) {
    m_cachedSurfaceControl[nativeWindow].DestroySurface(reinterpret_cast<detail::Surface *>(nativeWindow));
}
};
''')
    original=Path(td)/'input.zip'
    with zipfile.ZipFile(original,'w') as z:
        for p in root.rglob('*'):
            if p.is_file():z.write(p,Path('Surface_RealBackdrop')/p.relative_to(root))
    sha=hashlib.sha256(original.read_bytes()).hexdigest()
    out=Path(td)/'Surface_PerRequest'
    u.upgrade(original,out)
    check('input_not_changed',sha==hashlib.sha256(original.read_bytes()).hexdigest())
    creator=(out/'jni/include/native_surface/ANativeWindowCreator.h').read_text()
    check('no_skip_flag_write','flags |= 0x40' not in creator)
    check('no_legacy_screenshot_metadata','441731' not in creator)
    check('creation_registered','hosted::Register(nativeWindow, surfaceControl.data, width, height)' in creator)
    check('destruction_unregistered','hosted::Unregister(nativeWindow)' in creator)
    check('no_global_flag_forcing','CreateSurface(name, width, height, false)' in creator)
    make=(out/'jni/Android.mk').read_text()
    check('native_core_shared','LOCAL_MODULE := ytbl_host' in make and 'BUILD_SHARED_LIBRARY' in make)
    check('same_executable_name','LOCAL_MODULE := imgui_chain_1_47' in make and 'real_backdrop/HostLauncher.cpp' in make)
    core=(out/'jni/src/main.cpp').read_text()
    check('original_main_renamed','extern "C" int ytbl_original_main' in core)
    surface=(out/'jni/src/Android_draw/SurfaceGlass.cpp').read_text()
    check('clear_default','materialIndex = 0;' in surface)
    check('lighter_blur','blur = 3.5f;' in surface)
    check('lighter_scrim','material.readability = 0.06f;' in surface)
    check('lighter_tint','ImVec4(1,1,1,0.035f)' in surface)
    check('checkbox_removed','SurfaceGlass::Checkbox' not in (out/'jni/src/Android_draw/draw_Gui.cpp').read_text())
    check('dex_included',(out/'capture/prebuilt/capture.dex.jar').is_file())
    check('dist_not_ndk_libs','stage/capture_runtime' in (out/'build_real_backdrop.sh').read_text())
    check('manifest_not_claiming_host_build',json.loads((out/'EXCLUDE_REQUEST_INSTALL.json').read_text())['full_user_host_ndk_build']=='not_run')
    try:u.upgrade(original,out)
    except ValueError:checks.append('existing_output_rejected')
    else:raise AssertionError('overwrote output')
    evil=Path(td)/'evil.zip'
    with zipfile.ZipFile(evil,'w') as z:z.writestr('../outside','bad')
    try:u.safe_extract(evil,Path(td)/'bad')
    except ValueError:checks.append('traversal_rejected')
    else:raise AssertionError('unsafe path accepted')
    # Validate the no-argument native-main adapter too.
    plain=Path(td)/'plain'
    import shutil
    shutil.copytree(root,plain)
    (plain/'jni/src/main.cpp').write_text('int main() { return 0; }\n')
    u.modify(plain)
    check('no_arg_main_supported','return ytbl_original_main();' in (plain/'jni/real_backdrop/HostEntryAdapter.cpp').read_text())
print(json.dumps({'scope':'synthetic source fixtures; not the uploaded user ZIP','passed':checks},indent=2))
