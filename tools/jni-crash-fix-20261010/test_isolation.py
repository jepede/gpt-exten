import json
from pathlib import Path
import tempfile
import unittest
import zipfile

from isolate_input import MARKER, isolate, patch_source


class IsolationTests(unittest.TestCase):
    def fixture(self, path, code=None, extra=None):
        # Synthetic fixture: these are not the user's original source/libraries.
        data = {
            'jni/NativeWindow.h': code or b'void f() {\n DobbyHook(a, hook_input, orig_input);\n}\n',
            'jni/Library/placeholder.a': bytes(range(256)),
            'jni/unchanged.txt': 'unchanged content\n'.encode(),
        }
        data.update(extra or {})
        with zipfile.ZipFile(path, 'w') as out:
            for name, value in data.items():
                out.writestr(name, value)
        return data

    def test_copies_every_other_file_unchanged(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / 'source.zip'
            output = Path(directory) / 'isolated.zip'
            original = self.fixture(source)
            source_bytes = source.read_bytes()
            result = isolate(source, output)
            self.assertEqual(source_bytes, source.read_bytes())
            self.assertFalse(result['device_runtime_verified'])
            self.assertFalse(result['android_build_verified'])
            with zipfile.ZipFile(output) as archive:
                self.assertIsNone(archive.testzip())
                self.assertIn(MARKER.encode(), archive.read('jni/NativeWindow.h'))
                for name, value in original.items():
                    if name != 'jni/NativeWindow.h':
                        self.assertEqual(archive.read(name), value)
                report = json.loads(archive.read('_CRASH_ISOLATION_REPORT.json'))
                self.assertEqual(report['touch_interaction'], 'disabled')

    def test_crlf_preserved(self):
        output = patch_source(b'void f(){\r\n DobbyHook(a, hook_input, orig_input);\r\n}\r\n')
        self.assertEqual(output.count(b'\n'), output.count(b'\r\n'))

    def test_refuses_already_isolated(self):
        with self.assertRaises(ValueError):
            patch_source((MARKER + '\n').encode())

    def test_refuses_unfamiliar_source(self):
        with self.assertRaises(ValueError):
            patch_source(b'void f() {}\n')
        with self.assertRaises(ValueError):
            patch_source(b'DobbyHook(a, hook_input, orig_input);\n' * 2)

    def test_refuses_overwrite(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / 'source.zip'
            output = Path(directory) / 'result.zip'
            self.fixture(source)
            output.write_bytes(b'KEEP')
            with self.assertRaises(FileExistsError):
                isolate(source, output)
            self.assertEqual(output.read_bytes(), b'KEEP')
            with self.assertRaises(ValueError):
                isolate(source, source)

    def test_refuses_path_traversal(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / 'bad.zip'
            output = Path(directory) / 'result.zip'
            self.fixture(source, extra={'../escape.txt': b'bad'})
            with self.assertRaises(ValueError):
                isolate(source, output)
            self.assertFalse(output.exists())


if __name__ == '__main__':
    unittest.main(verbosity=2)
