import importlib.util
from pathlib import Path
import tempfile,zipfile,json,hashlib
base=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('install',base/'install.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
checks=[]
def check(name,condition):
    assert condition,name
    checks.append(name)
with tempfile.TemporaryDirectory() as temp:
    root=Path(temp)/'fixture'
    def write(path,text):
        p=root/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)
    write('jni/Android.mk','LOCAL_PATH := $(call my-dir)\nLOCAL_MODULE := test\ninclude $(BUILD_EXECUTABLE)\n')
    write('jni/Application.mk','APP_ABI := arm64-v8a\nAPP_PLATFORM := android-21\n')
    write('jni/src/Android_draw/SurfaceGlass.cpp','''bool BeginWindow(const char* title, bool* open) {
    int flags=ImGuiWindowFlags_NoBackground;
    if (!visible) return false;
    auto material = ytbl::MakeMaterial();
    if (preview) DrawLocalBackdrop(pos,size);
    ytbl::QueueBackdropCapture(ImGui::GetWindowDrawList());
    ytbl::DrawWindowGlass(material);
    return true;
}
void DrawSettings() { ImGui::Text("}"); }
void Shutdown() { ytbl::Shutdown(); }
''')
    write('jni/include/ANativeWindowCreator.h','''void Create() {
    flags |= 0x40;
    auto surfaceControl = surfaceComposerClient.CreateSurface(name, width, height, skipScrenshot_);
}''')
    write('jni/liquid_glass/ytbl_widgets.cpp','void FocusRing(const ImRect& rect) { /* } */ old(); }\n')
    original=Path(temp)/'original.zip'
    with zipfile.ZipFile(original,'w') as z:
        for p in root.rglob('*'):
            if p.is_file():z.write(p,Path('fixture')/p.relative_to(root))
    before=hashlib.sha256(original.read_bytes()).hexdigest()
    output=Path(temp)/'Integrated'
    m.install(original,output)
    check('original_archive_unchanged',hashlib.sha256(original.read_bytes()).hexdigest()==before)
    ui=(output/'jni/src/Android_draw/SurfaceGlass.cpp').read_text()
    check('only_one_fallback_snapshot',ui.count('QueueBackdropCapture(')==1)
    check('external_snapshot_is_guarded','if (!realScreenBackdrop) ytbl::QueueBackdropCapture' in ui)
    check('demo_disabled_when_capture_requested','preview && !screenbackdrop_ui::Requested()' in ui)
    check('capture_cleanup_installed','screenbackdrop_ui::Shutdown();' in ui)
    check('visible_opt_in_controls_installed','screenbackdrop_ui::DrawSettings();' in ui)
    check('self_exclusion_applies_on_every_create','systemVersion >= 12' in (output/'jni/include/ANativeWindowCreator.h').read_text())
    check('minimum_ndk_api_28','android-28' in (output/'jni/Application.mk').read_text())
    check('imgui_signature_compatibility','IMGUI_VERSION_NUM >= 19208' in (output/'jni/liquid_glass/ytbl_widgets.cpp').read_text())
    check('helper_dex_included',(output/'capture/prebuilt/capture.dex.jar').is_file())
    check('helper_native_included',(output/'capture/prebuilt/libglass_capture.so').is_file())
    try:m.patch_host(output)
    except ValueError:checks.append('already_patched_input_rejected')
    else:raise AssertionError('double patch accepted')
    evil=Path(temp)/'evil.zip'
    with zipfile.ZipFile(evil,'w') as z:z.writestr('../outside','no')
    try:m.extract(evil,Path(temp)/'bad')
    except ValueError:checks.append('zip_traversal_rejected')
    else:raise AssertionError('unsafe ZIP accepted')
    check('no_escape_file',not (Path(temp)/'outside').exists())
    manifest=json.loads((output/'REAL_BACKDROP_INSTALL.json').read_text())
    check('does_not_claim_full_host_build',manifest['full_host_ndk_build']=='not_run')
print(json.dumps({'scope':'synthetic integration fixtures, NOT the user archive','passed':checks},indent=2))
