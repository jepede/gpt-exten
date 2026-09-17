import importlib.util
from pathlib import Path
import tempfile
import unittest
import zipfile

spec=importlib.util.spec_from_file_location('installer',Path(__file__).resolve().parents[1]/'install.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

# Synthetic fixtures, not an uploaded user's complete source files.
HEADER='''class ANativeWindowCreator {
public:
        static ANativeWindow *Create(const char *name, int width = -1, bool skipScrenshot_ = false) {
            m_cachedSurfaceControl.emplace(nativeWindow, std::move(surfaceControl));
        }
        static void Destroy(ANativeWindow *nativeWindow) {
            m_cachedSurfaceControl.erase(nativeWindow);
        }
private:
        inline static std::unordered_map<ANativeWindow *, detail::SurfaceControl> m_cachedSurfaceControl;
};
'''
BRIDGE='''void Shutdown() {
}
void BeginFrame() {
    ytbl::BeginFrame();
}
void DrawSettings() {
}
void BeginWindow() {
    auto material = ytbl::MakeMaterial(ytbl::Material::Clear);
    if (preview)
        DrawLocalBackdrop(windowPos, windowSize);
    ytbl::QueueBackdropCapture(ImGui::GetWindowDrawList());
    ytbl::DrawWindowGlass(material);
}
'''
class Tests(unittest.TestCase):
    def test_header(self):
        s=m.patch_header(HEADER)
        self.assertIn('skipScrenshot_ = true',s)
        self.assertIn('IsBackdropExclusionReady',s)
        self.assertIn('m_backdropExclusion.erase',s)
        self.assertIn('systemVersion >= 12',s)
        with self.assertRaises(ValueError):m.patch_header(s)
    def test_bridge(self):
        s=m.patch_bridge(BRIDGE)
        self.assertIn('SurfaceBackdrop::BeginFrame()',s)
        self.assertIn('preview && !SurfaceBackdrop::Requested()',s)
        self.assertIn('SurfaceBackdrop::Shutdown()',s)
        self.assertLess(s.index('SurfaceBackdrop::Bind()'),s.index('MakeMaterial('))
        with self.assertRaises(ValueError):m.patch_bridge(s)
    def test_no_snapshot(self):
        s=m.patch_bridge(BRIDGE.replace('    ytbl::QueueBackdropCapture(ImGui::GetWindowDrawList());\n',''))
        self.assertEqual(s.count('QueueBackdropCapture('),1)
    def test_missing_anchor(self):
        with self.assertRaises(ValueError):m.patch_bridge('unknown source')
        with self.assertRaises(ValueError):m.patch_header('unknown header')
    def test_archive_traversal(self):
        with tempfile.TemporaryDirectory() as t:
            root=Path(t);z=root/'bad.zip'
            with zipfile.ZipFile(z,'w') as f:f.writestr('../escape','no')
            with self.assertRaises(ValueError):m.extract(z,root/'out')
            self.assertFalse((root/'escape').exists())
    def test_full_apply_fixture(self):
        with tempfile.TemporaryDirectory() as t:
            root=Path(t)/'project';module=Path(t)/'module';jni=root/'jni'
            (jni/'include/window').mkdir(parents=True);(jni/'src/Android_draw').mkdir(parents=True)
            (jni/'liquid_glass').mkdir()
            (jni/'liquid_glass/ytbl.h').write_text('// fixture')
            (jni/'include/window/ANativeWindowCreator.h').write_text(HEADER)
            (jni/'src/Android_draw/SurfaceGlass.cpp').write_text(BRIDGE)
            (jni/'Android.mk').write_text('LOCAL_SRC_FILES := src/main.cpp\ninclude $(BUILD_EXECUTABLE)\n')
            (jni/'Application.mk').write_text('APP_PLATFORM := android-21\n')
            for sub,names in [('native',['LiveBackdrop.cpp','LiveBackdrop.h','wire.h']),('adapter',['SurfaceBackdrop.cpp','SurfaceBackdrop.h']),('runtime/live_backdrop',['capture-helper.jar','liblivebg_jni.so'])]:
                (module/sub).mkdir(parents=True)
                for name in names:(module/sub/name).write_text('fixture')
            (module/'README.md').write_text('fixture')
            self.assertEqual(len(m.apply(root,module)),4)
            self.assertIn('android-28',(jni/'Application.mk').read_text())
            self.assertIn('SURFACEGLASS_EXCLUDE_OWN_CAPTURE',(jni/'Android.mk').read_text())
            self.assertFalse((jni/'live_backdrop/native/producer_jni.cpp').exists())
            self.assertTrue((root/'runtime/live_backdrop/capture-helper.jar').exists())

if __name__=='__main__':unittest.main(verbosity=2)
