import hashlib
from pathlib import Path
import shutil
import stat
import subprocess
import tempfile
import unittest
import zipfile

import toolkit as t

BACKEND = b'''int32_t ImGui_ImplAndroid_HandleInputEvent(const AInputEvent* input_event)
{
    ImGuiIO& io = ImGui::GetIO();
    io.count++;
    return AInputEvent_getType(input_event);
}
'''
MEMBER = "jni/imgui/backends/imgui_impl_android.cpp"

class ToolkitTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
    def tearDown(self):
        self.temp.cleanup()
    def archive(self, name="source.zip", extra=(), backend=BACKEND):
        path = self.root / name
        with zipfile.ZipFile(path, "w") as z:
            z.comment = b"original archive comment"
            z.writestr(MEMBER, backend)
            z.writestr("jni/data.bin", bytes(range(256)))
            z.writestr("jni/Android.mk", b"LOCAL_MODULE := fixture\n")
            for filename, data in extra:
                z.writestr(filename, data)
        return path
    def test_guard_precedes_getio(self):
        after, report = t.patch_source(BACKEND)
        self.assertTrue(report["changed"])
        self.assertLess(after.index(b"GetCurrentContext"), after.index(b"GetIO"))
        self.assertIn(b"input_event == nullptr", after)
    def test_idempotent_source_guard(self):
        first, _ = t.patch_source(BACKEND)
        second, report = t.patch_source(first)
        self.assertEqual(first, second)
        self.assertFalse(report["changed"])
    def test_crlf_and_utf8_bom_preserved(self):
        original = b"\xef\xbb\xbf" + BACKEND.replace(b"\n", b"\r\n")
        result, _ = t.patch_source(original)
        self.assertTrue(result.startswith(b"\xef\xbb\xbf"))
        self.assertNotIn(b"\n", result.replace(b"\r\n", b""))
    def test_parameter_name_detected(self):
        original = BACKEND.replace(b"input_event", b"event")
        result, _ = t.patch_source(original)
        self.assertIn(b"if (event == nullptr", result)
    def test_comment_and_raw_string_not_function(self):
        fake = b'/* ' + BACKEND + b' */\nconst char* x = R"tag(' + BACKEND + b')tag";\n'
        result, report = t.patch_source(fake + BACKEND)
        self.assertTrue(result.startswith(fake))
        self.assertTrue(report["changed"])
    def test_two_definitions_rejected(self):
        with self.assertRaises(t.GuardError):
            t.patch_source(BACKEND + BACKEND)
    def test_custom_body_not_blindly_changed(self):
        data = BACKEND.replace(b"    ImGuiIO&", b"    custom_side_effect();\n    ImGuiIO&")
        with self.assertRaises(t.GuardError):
            t.patch_source(data)
    def test_non_utf8_rejected(self):
        with self.assertRaises(t.GuardError):
            t.patch_source(b"\xff" + BACKEND)
    def test_archive_preserves_original_bytes(self):
        source = self.archive()
        before = t.file_hash(source)
        output = self.root / "guard_only.zip"
        report = t.patch_archive(source, output)
        self.assertEqual(t.file_hash(source), before)
        self.assertFalse(report["original_project_compiled"])
        self.assertFalse(report["thread_safety_fixed"])
        with zipfile.ZipFile(source) as a, zipfile.ZipFile(output) as b:
            self.assertEqual(a.comment, b.comment)
            for entry in a.infolist():
                if entry.filename != MEMBER:
                    self.assertEqual(a.read(entry), b.read(entry.filename))
                self.assertEqual(entry.external_attr, b.getinfo(entry.filename).external_attr)
            self.assertIsNone(b.testzip())
            for line in b.read(t.NOTE_DIR + "SHA256SUMS").decode().splitlines():
                digest, name = line.split("  ", 1)
                self.assertEqual(hashlib.sha256(b.read(name)).hexdigest(), digest)
    def test_existing_output_never_overwritten(self):
        source = self.archive()
        output = self.root / "existing.zip"
        output.write_bytes(b"KEEP")
        with self.assertRaises(t.GuardError):
            t.patch_archive(source, output)
        self.assertEqual(output.read_bytes(), b"KEEP")
    def test_original_path_never_overwritten(self):
        source = self.archive()
        digest = t.file_hash(source)
        with self.assertRaises(t.GuardError):
            t.patch_archive(source, source)
        self.assertEqual(t.file_hash(source), digest)
    def test_ambiguous_backends_require_selection(self):
        extra = "other/imgui_impl_android.cpp"
        source = self.archive(extra=[(extra, BACKEND)])
        with self.assertRaises(t.GuardError):
            t.patch_archive(source, self.root / "no.zip")
        output = self.root / "selected.zip"
        t.patch_archive(source, output, MEMBER)
        with zipfile.ZipFile(output) as z:
            self.assertEqual(z.read(extra), BACKEND)
    def test_archive_path_traversal_rejected(self):
        source = self.archive(extra=[("../escape.txt", b"data")])
        with self.assertRaises(t.GuardError):
            t.patch_archive(source, self.root / "no.zip")
        self.assertFalse((self.root / "no.zip").exists())
    def test_control_character_path_rejected(self):
        source = self.archive(extra=[("evil\nname.txt", b"data")])
        with self.assertRaises(t.GuardError):
            t.patch_archive(source, self.root / "no.zip")
    def test_symlink_entry_rejected(self):
        source = self.archive()
        with zipfile.ZipFile(source, "a") as z:
            info = zipfile.ZipInfo("jni/link")
            info.create_system = 3
            info.external_attr = (stat.S_IFLNK | 0o777) << 16
            z.writestr(info, "../../outside")
        with self.assertRaises(t.GuardError):
            t.patch_archive(source, self.root / "no.zip")
    def test_audit_read_only(self):
        source = self.archive()
        before = source.read_bytes()
        report = t.audit_archive(source)
        self.assertEqual(report["backend_candidates"], [MEMBER])
        self.assertTrue(any(x["symbol"] == "GetIO" for x in report["source_sites"]))
        self.assertEqual(source.read_bytes(), before)
    def test_fault_instruction_decoding(self):
        result = t.decode_load(0xf9406808, 0x28)
        self.assertEqual(result["base_register"], "x0")
        self.assertEqual(result["target_register"], "x8")
        self.assertEqual(result["offset"], "0xd0")
        self.assertEqual(result["effective_address"], "0xf8")
        self.assertEqual(result["access_bytes"], 8)
    def test_wrong_instruction_rejected(self):
        with self.assertRaises(t.GuardError):
            t.decode_load(0xd65f03c0, 0x28)
    def test_decoder_register_ranges(self):
        result = t.decode_load(0xf94003ff, 0x1000)
        self.assertEqual(result["base_register"], "sp")
        self.assertEqual(result["target_register"], "xzr")
        with self.assertRaises(t.GuardError):
            t.decode_load(0xf9406808, -1)
    def test_cpp_lifecycle_fixture_with_sanitizers(self):
        compiler = shutil.which("g++")
        self.assertIsNotNone(compiler, "g++ is required: do not count an unrun C++ fixture as passed")
        patched, _ = t.patch_source(BACKEND)
        prefix = r'''
#include <cassert>
#include <cstdint>
struct AInputEvent { int type; };
int32_t AInputEvent_getType(const AInputEvent* e) { assert(e); return e->type; }
struct ImGuiIO { int count = 0; };
struct ImGuiContext {};
namespace ImGui {
    ImGuiContext* current = nullptr;
    ImGuiIO io;
    int get_io_calls = 0;
    ImGuiContext* GetCurrentContext() { return current; }
    ImGuiIO& GetIO() { ++get_io_calls; assert(current); return io; }
}
'''
        suffix = r'''
int main() {
    AInputEvent event{7};
    ImGuiContext context;
    assert(ImGui_ImplAndroid_HandleInputEvent(nullptr) == 0);
    assert(ImGui_ImplAndroid_HandleInputEvent(&event) == 0);
    assert(ImGui::get_io_calls == 0);
    ImGui::current = &context;
    assert(ImGui_ImplAndroid_HandleInputEvent(nullptr) == 0);
    assert(ImGui::get_io_calls == 0);
    assert(ImGui_ImplAndroid_HandleInputEvent(&event) == 7);
    assert(ImGui::get_io_calls == 1 && ImGui::io.count == 1);
    ImGui::current = nullptr;
    assert(ImGui_ImplAndroid_HandleInputEvent(&event) == 0);
    assert(ImGui::get_io_calls == 1);
    return 0;
}
'''
        source = self.root / "fixture.cpp"
        binary = self.root / "fixture"
        source.write_text(prefix + patched.decode() + suffix)
        built = subprocess.run([compiler, "-std=c++11", "-O1", "-Wall", "-Wextra", "-Werror", "-fsanitize=address,undefined", "-fno-omit-frame-pointer", str(source), "-o", str(binary)], capture_output=True, text=True, timeout=45)
        self.assertEqual(built.returncode, 0, built.stdout + built.stderr)
        run = subprocess.run([str(binary)], capture_output=True, text=True, timeout=15)
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)

if __name__ == "__main__":
    unittest.main(verbosity=2)
