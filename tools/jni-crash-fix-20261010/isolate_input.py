#!/usr/bin/env python3
"""Create a complete COPY of a JNI archive with private input interception disabled.

This is an isolation tool, not a feature-complete crash fix. It removes a call;
it does not install hooks, inject processes, modify authentication, or contact
any network endpoint. Original libraries and other source files are preserved.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import sys
import tempfile
import zipfile

MARKER = '// CRASH_ISOLATION: private input interception disabled; touch UI unavailable.'
PATTERN = re.compile(
    r'^[ \t]*DobbyHook\([^;\n]*\b(?:hook_input|orig_input)\b[^;\n]*\);[ \t]*$',
    re.MULTILINE,
)
MAX_TOTAL_BYTES = 512 * 1024 * 1024
MAX_FILES = 10000


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def patch_source(data: bytes) -> bytes:
    text = data.decode('utf-8-sig')
    newline = '\r\n' if '\r\n' in text else '\n'
    text = text.replace('\r\n', '\n')
    if MARKER in text:
        raise ValueError('This source is already an isolation build.')
    patched, count = PATTERN.subn(MARKER, text)
    if count != 1:
        raise ValueError(
            f'Expected exactly one private-input registration, found {count}; '
            'refusing to guess or modify an unfamiliar source version.'
        )
    patched = patched.replace('\n', newline)
    return patched.encode('utf-8')


def isolate(source: Path, output: Path) -> dict:
    source = source.resolve(strict=True)
    output = output.resolve()
    if source == output:
        raise ValueError('The output must not overwrite the original archive.')
    if output.exists():
        raise FileExistsError(f'Output already exists: {output}')
    original_archive_sha256 = sha256(source.read_bytes())
    entries = []
    names = set()
    total = 0
    changed = []
    with zipfile.ZipFile(source, 'r') as archive:
        infos = archive.infolist()
        if len(infos) > MAX_FILES:
            raise ValueError('Archive entry count exceeds the safety limit.')
        for info in infos:
            name = info.filename
            path = PurePosixPath(name)
            if ('\\' in name or path.is_absolute() or '..' in path.parts
                    or '\x00' in name or ':' in name):
                raise ValueError(f'Unsafe archive path: {name!r}')
            if name in names:
                raise ValueError(f'Duplicate archive entry: {name!r}')
            if stat.S_ISLNK(info.external_attr >> 16):
                raise ValueError(f'Symlinks are not supported: {name!r}')
            names.add(name)
            total += info.file_size
            if total > MAX_TOTAL_BYTES:
                raise ValueError('Uncompressed archive exceeds 512 MiB.')
            data = archive.read(info)
            entries.append((info, data))
        candidates = [i for i, _ in entries
                      if i.filename.endswith('jni/NativeWindow.h') or
                      i.filename == 'NativeWindow.h']
        if len(candidates) != 1:
            raise ValueError('Could not uniquely identify jni/NativeWindow.h.')
        target = candidates[0].filename
        replacements = {}
        for info, data in entries:
            if info.filename == target:
                replacement = patch_source(data)
                replacements[target] = replacement
                changed.append({'path': target, 'before_sha256': sha256(data),
                                'after_sha256': sha256(replacement)})

    report = {
        'status': 'diagnostic_isolation_only',
        'original_archive_sha256': original_archive_sha256,
        'source_file_count': len(entries),
        'changed_files': changed,
        'touch_interaction': 'disabled',
        'android_build_verified': False,
        'device_runtime_verified': False,
        'other_project_files': 'preserved byte-for-byte',
        'warning': 'Not a feature-complete repair. Other rendering/lifetime bugs may remain.'
    }
    report_path = '_CRASH_ISOLATION_REPORT.json'
    if report_path in names:
        raise ValueError('The input already contains an isolation report.')
    output.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary_name = tempfile.mkstemp(prefix='.jni-isolation-', suffix='.zip', dir=output.parent)
    os.close(fd)
    temporary = Path(temporary_name)
    try:
        with zipfile.ZipFile(temporary, 'w', compression=zipfile.ZIP_DEFLATED,
                             compresslevel=6) as archive:
            for info, data in entries:
                archive.writestr(info, replacements.get(info.filename, data))
            archive.writestr(report_path, json.dumps(report, ensure_ascii=False, indent=2))
        with zipfile.ZipFile(temporary) as check:
            if check.testzip() is not None:
                raise ValueError('Generated ZIP failed the CRC check.')
            for info, data in entries:
                actual = check.read(info.filename)
                expected = replacements.get(info.filename, data)
                if actual != expected:
                    raise ValueError(f'Content verification failed: {info.filename}')
        # Refuse an existing destination even when it appeared during processing.
        # Hard-link publication is atomic and cannot silently overwrite another file.
        os.link(temporary, output)
        report['output_archive_sha256'] = sha256(temporary.read_bytes())
    finally:
        temporary.unlink(missing_ok=True)
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path, help='Original jni.zip')
    parser.add_argument('--output', type=Path, default=Path('jni_input_isolated.zip'))
    args = parser.parse_args()
    try:
        result = isolate(args.source, args.output)
    except (OSError, ValueError, UnicodeError, zipfile.BadZipFile) as error:
        print(f'ERROR: {error}', file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    print(f'Generated: {args.output.resolve()}')
    print('This is an isolation build. Touch interaction is disabled; device validation is still required.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
