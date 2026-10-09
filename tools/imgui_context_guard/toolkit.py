#!/usr/bin/env python3
"""Offline ImGui input-context guard. Not a complete project repair or concurrency fix."""
from __future__ import annotations
import argparse
import copy
import difflib
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import sys
import zipfile

VERSION = "1.0.0"
NOTE_DIR = ".imgui_context_guard/"
MAX_TOTAL = 512 * 1024 * 1024
MAX_MEMBER = 128 * 1024 * 1024
MARKER = "IMGUI_CONTEXT_GUARD_20261010"

class GuardError(Exception):
    pass

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def file_hash(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def mask_cpp(text: str) -> str:
    """Blank comments/literals without moving source offsets; reject malformed input."""
    result = list(text)
    i, n = 0, len(text)
    def blank(a: int, b: int) -> None:
        for k in range(a, b):
            if result[k] not in "\r\n":
                result[k] = " "
    while i < n:
        end = None
        if text.startswith("//", i):
            end = text.find("\n", i + 2)
            end = n if end < 0 else end
            # Continued // comments can hide code across a physical newline.
            while end < n and text[i:end].rstrip("\r").endswith("\\"):
                end = text.find("\n", end + 1)
                if end < 0:
                    end = n
        elif text.startswith("/*", i):
            stop = text.find("*/", i + 2)
            if stop < 0:
                raise GuardError("Unterminated C++ block comment")
            end = stop + 2
        else:
            raw = re.match(r'(?:u8|u|U|L)?R"([^\s()\\]{0,16})\(', text[i:]) if text[i] in "uULR" else None
            if raw:
                terminal = ")" + raw.group(1) + '"'
                stop = text.find(terminal, i + raw.end())
                if stop < 0:
                    raise GuardError("Unterminated C++ raw string")
                end = stop + len(terminal)
            elif text[i] in "\"'":
                # Digit separators in numeric literals are not character literals.
                if text[i] == "'" and i > 0 and i + 1 < n and text[i-1].isalnum() and text[i+1].isalnum():
                    i += 1
                    continue
                quote = text[i]
                end = i + 1
                while end < n:
                    if text[end] == "\\":
                        end += 2
                    elif text[end] == quote:
                        end += 1
                        break
                    else:
                        end += 1
                else:
                    raise GuardError("Unterminated C++ string/character literal")
        if end is not None:
            blank(i, min(end, n))
            i = end
        else:
            i += 1
    return "".join(result)

def patch_source(data: bytes) -> tuple[bytes, dict]:
    try:
        text = data.decode("utf-8")
    except UnicodeError as exc:
        raise GuardError("Backend source is not UTF-8; refusing a lossy rewrite") from exc
    masked = mask_cpp(text)
    signature = re.compile(r'\bint32_t\s+ImGui_ImplAndroid_HandleInputEvent\s*\(\s*(?:const\s+)?AInputEvent\s*\*\s*(?:const\s+)?([A-Za-z_]\w*)\s*\)\s*\{')
    matches = list(signature.finditer(masked))
    if len(matches) != 1:
        raise GuardError(f"Expected exactly one standard backend definition, found {len(matches)}")
    match = matches[0]
    brace = match.end() - 1
    depth = 1
    close = brace + 1
    while close < len(masked) and depth:
        if masked[close] == "{":
            depth += 1
        elif masked[close] == "}":
            depth -= 1
        close += 1
    if depth:
        raise GuardError("Unbalanced function braces")
    name = match.group(1)
    nl = "\r\n" if "\r\n" in text else "\n"
    insertion = nl + "    // " + MARKER + ": caller must still serialize context lifetime." + nl
    insertion += f"    if ({name} == nullptr || ImGui::GetCurrentContext() == nullptr)" + nl
    insertion += "        return 0;" + nl
    if text[brace + 1:close].startswith(insertion):
        return data, {"changed": False, "status": "already_contains_this_guard"}
    if MARKER in text:
        raise GuardError("Guard marker exists but its contents differ; manual review required")
    body = masked[brace + 1:close - 1]
    first = re.match(r'\s*ImGuiIO\s*&\s*[A-Za-z_]\w*\s*=\s*ImGui\s*::\s*GetIO\s*\(\s*\)\s*;', body)
    if first is None:
        raise GuardError("Nonstandard backend body: expected GetIO as its first statement; no automatic edit")
    updated = text[:brace + 1] + insertion + text[brace + 1:]
    return updated.encode("utf-8"), {
        "changed": True,
        "status": "CONTEXT_GUARD_ONLY_ORIGINAL_PROJECT_NOT_BUILT_OR_RUN",
        "function": "ImGui_ImplAndroid_HandleInputEvent",
        "definition_line_before": text[:match.start()].count("\n") + 1,
        "argument": name,
        "before_sha256": sha256(data),
        "after_sha256": sha256(updated.encode("utf-8")),
    }

def checked_members(archive: zipfile.ZipFile) -> list[zipfile.ZipInfo]:
    infos = archive.infolist()
    if len(infos) > 50000 or sum(i.file_size for i in infos) > MAX_TOTAL:
        raise GuardError("Archive exceeds safety limits")
    seen = set()
    for info in infos:
        name = info.filename
        parts = name.rstrip("/").split("/")
        if not name or name.startswith("/") or "\\" in name or any(p in ("", ".", "..") for p in parts) or ":" in parts[0]:
            raise GuardError(f"Unsafe archive path: {name!r}")
        if name in seen:
            raise GuardError(f"Duplicate archive entry: {name}")
        seen.add(name)
        if info.flag_bits & 1 or info.file_size > MAX_MEMBER:
            raise GuardError(f"Encrypted or oversized archive entry: {name}")
        if stat.S_ISLNK(info.external_attr >> 16):
            raise GuardError(f"Symlink archive entry is not accepted: {name}")
    return infos

def audit_archive(source: Path) -> dict:
    symbols = re.compile(r'\b(?:GetIO|GetCurrentContext|CreateContext|DestroyContext|SetCurrentContext|NewFrame|Render|ImGui_ImplAndroid_HandleInputEvent|pthread_create)\s*\(')
    result = {"source_sha256": file_hash(source), "source_sites": [], "skipped_sources": []}
    with zipfile.ZipFile(source) as archive:
        infos = checked_members(archive)
        result["entry_count"] = len(infos)
        result["backend_candidates"] = [i.filename for i in infos if PurePosixPath(i.filename).name == "imgui_impl_android.cpp"]
        for info in infos:
            if PurePosixPath(info.filename).suffix not in (".cpp", ".cc", ".c", ".h", ".hpp"):
                continue
            if info.file_size > 5 * 1024 * 1024:
                result["skipped_sources"].append({"file": info.filename, "reason": "over_5_MiB"})
                continue
            try:
                masked = mask_cpp(archive.read(info).decode("utf-8"))
            except (UnicodeError, GuardError) as exc:
                result["skipped_sources"].append({"file": info.filename, "reason": str(exc)})
                continue
            for number, line in enumerate(masked.splitlines(), 1):
                for match in symbols.finditer(line):
                    result["source_sites"].append({"file": info.filename, "line": number, "symbol": match.group(0).split("(")[0].strip()})
    return result

def patch_archive(source: Path, destination: Path, member: str | None = None) -> dict:
    if source.resolve() == destination.resolve() or destination.exists():
        raise GuardError("Output must be a new path; original files are never overwritten")
    source_digest = file_hash(source)
    created = False
    try:
        with zipfile.ZipFile(source) as original:
            infos = checked_members(original)
            if any(i.filename.startswith(NOTE_DIR) for i in infos):
                raise GuardError("Archive already contains guard metadata; use the untouched original")
            candidates = [i.filename for i in infos if PurePosixPath(i.filename).name == "imgui_impl_android.cpp"]
            if member is not None:
                if member not in candidates:
                    raise GuardError("Selected --member is not an exact backend candidate")
                target = member
            elif len(candidates) == 1:
                target = candidates[0]
            else:
                raise GuardError(f"Found {len(candidates)} backend files. Run audit; select one with --member")
            before = original.read(target)
            after, report = patch_source(before)
            if not report["changed"]:
                raise GuardError("This exact guard already exists; no second patched archive was written")
            report.update({"tool_version": VERSION, "input_zip_sha256": source_digest, "modified_member": target,
                "original_entry_count": len(infos), "original_project_compiled": False,
                "original_project_run": False, "thread_safety_fixed": False,
                "scope": "Only a null-input/current-context guard in the standard ImGui Android backend"})
            diff = "".join(difflib.unified_diff(before.decode("utf-8").splitlines(True), after.decode("utf-8").splitlines(True), fromfile="a/" + target, tofile="b/" + target))
            notes = {
                NOTE_DIR + "REPORT.json": json.dumps(report, ensure_ascii=False, indent=2).encode("utf-8"),
                NOTE_DIR + "PATCH.diff": diff.encode("utf-8"),
                NOTE_DIR + "README.txt": ("This is a source-level context guard, NOT a verified full repair.\n"
                    "The original project was NOT compiled or run. This guard is NOT synchronization.\n"
                    "Serialize context creation, input, rendering and destruction, or queue copied input data\n"
                    "to a single ImGui owner thread. An upstream callback can still crash if it calls GetIO\n"
                    "before this backend. Do not use a newly rebuilt binary to symbolize an older crash.\n").encode("utf-8"),
            }
            manifest = []
            with destination.open("xb") as stream:
                created = True
                with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_DEFLATED) as output:
                    output.comment = original.comment
                    for info in infos:
                        payload = after if info.filename == target else original.read(info)
                        output.writestr(copy.copy(info), payload)
                        if not info.is_dir():
                            manifest.append(f"{sha256(payload)}  {info.filename}")
                    for name, payload in notes.items():
                        output.writestr(name, payload)
                        manifest.append(f"{sha256(payload)}  {name}")
                    output.writestr(NOTE_DIR + "SHA256SUMS", "\n".join(manifest) + "\n")
                stream.flush()
                os.fsync(stream.fileno())
        with zipfile.ZipFile(destination) as verify:
            bad = verify.testzip()
            if bad:
                raise GuardError(f"Output CRC verification failed: {bad}")
        report["output_zip_sha256"] = file_hash(destination)
        return report
    except Exception:
        if created:
            destination.unlink(missing_ok=True)
        raise

def decode_load(instruction: int, base_value: int) -> dict:
    if not 0 <= instruction <= 0xffffffff or not 0 <= base_value <= 0xffffffffffffffff:
        raise GuardError("Instruction must be uint32 and base register uint64")
    if instruction & 0xffc00000 != 0xf9400000:
        raise GuardError("Only AArch64 LDR X unsigned-immediate instructions are supported")
    base = (instruction >> 5) & 31
    target = instruction & 31
    displacement = ((instruction >> 10) & 0xfff) * 8
    return {"instruction": f"0x{instruction:08x}", "operation": "LDR", "access_bytes": 8,
        "base_register": "sp" if base == 31 else f"x{base}",
        "target_register": "xzr" if target == 31 else f"x{target}",
        "offset": hex(displacement), "base_value": hex(base_value),
        "effective_address": hex((base_value + displacement) & 0xffffffffffffffff)}

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subs = parser.add_subparsers(dest="command", required=True)
    audit = subs.add_parser("audit", help="Read-only source inventory; no extraction, execution or network")
    audit.add_argument("source", type=Path)
    patch = subs.add_parser("patch", help="Insert ONLY a context guard into a recognized backend; not a full repair")
    patch.add_argument("source", type=Path)
    patch.add_argument("-o", "--output", required=True, type=Path)
    patch.add_argument("--member", help="Exact backend member path, necessary for ambiguous archives")
    decode = subs.add_parser("decode", help="Decode one known AArch64 LDR instruction")
    decode.add_argument("--instruction", type=lambda s: int(s, 0), default=0xf9406808)
    decode.add_argument("--base-value", type=lambda s: int(s, 0), default=0x28)
    args = parser.parse_args()
    try:
        if args.command == "audit":
            result = audit_archive(args.source)
        elif args.command == "patch":
            result = patch_archive(args.source, args.output, args.member)
        else:
            result = decode_load(args.instruction, args.base_value)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (GuardError, OSError, zipfile.BadZipFile, RuntimeError, NotImplementedError) as exc:
        print(f"ERROR: {exc}\nNo complete project repair is being claimed.", file=sys.stderr)
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
