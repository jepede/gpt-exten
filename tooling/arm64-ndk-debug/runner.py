#!/usr/bin/env python3
"""Repeatable real QEMU/GDB probes for NDK-built ARM64 Android ELF.

This script reports unsupported features as UNSUPPORTED, never as PASS.
No fake GDB output is generated. Logs are raw subprocess stdout/stderr.
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import re
import socket
import subprocess
import sys
import time
from typing import Any

def free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])

def run_command(argv: list[str], timeout: int = 20) -> dict[str, Any]:
    try:
        proc = subprocess.run(argv, capture_output=True, text=True,
                              errors="replace", timeout=timeout)
        return {"returncode": proc.returncode, "stdout": proc.stdout,
                "stderr": proc.stderr}
    except subprocess.TimeoutExpired as exc:
        return {"returncode": 124, "stdout": (exc.stdout or b"").decode("utf-8", "replace")
                if isinstance(exc.stdout, bytes) else exc.stdout or "",
                "stderr": (exc.stderr or b"").decode("utf-8", "replace")
                if isinstance(exc.stderr, bytes) else exc.stderr or "",
                "timed_out": True}

def save(log_dir: pathlib.Path, name: str, content: str) -> None:
    (log_dir / name).write_text(content, encoding="utf-8")

def verdict(success: bool, raw: str, expect: str | None = None) -> str:
    if success:
        return "PASS"
    if expect == "watchpoint" and re.search(
        r"Could not insert hardware watchpoint|Could not insert hardware breakpoints|"
        r"Target does not support|does not support hardware|Cannot insert hardware|"
        r"not supported|No hardware breakpoint support", raw, re.I
    ):
        return "UNSUPPORTED"
    return "FAIL"

def qemu_args(ns: argparse.Namespace) -> list[str]:
    return [ns.qemu, "-L", ns.sysroot,
            "-E", "LD_LIBRARY_PATH=/data/local/tmp:/apex/com.android.runtime/lib64/bionic:/system/lib64",
            "-E", "LD_PRELOAD="]

def gdb_case(ns: argparse.Namespace, log_dir: pathlib.Path, name: str,
             mode: str, extra: list[str], marker: str, expect: str | None = None) -> dict[str, Any]:
    port = free_port()
    guest_log = log_dir / (name + ".guest.log")
    raw_log = log_dir / (name + ".gdb.log")
    commands = [
        "set pagination off", "set confirm off", "set print pretty off",
        "set breakpoint pending on", "set architecture aarch64",
        "file " + ns.elf, "target remote 127.0.0.1:" + str(port)
    ] + extra
    gdb_script = log_dir / (name + ".gdb")
    gdb_script.write_text("\n".join(commands) + "\n", encoding="utf-8")
    qemu_argv = qemu_args(ns) + ["-g", str(port), ns.elf, mode]
    start = time.monotonic()
    with guest_log.open("w", encoding="utf-8", errors="replace") as output:
        proc = subprocess.Popen(qemu_argv, stdout=output, stderr=subprocess.STDOUT,
                                start_new_session=True)
        try:
            # QEMU -g listens immediately on some versions, slower on others.
            gdb = run_command([ns.gdb, "-nx", "-q", "-batch",
                               "-x", str(gdb_script)], timeout=30)
            raw = gdb["stdout"] + "\n" + gdb["stderr"]
        finally:
            if proc.poll() is None:
                proc.terminate()
                try:
                    proc.wait(timeout=3)
                except subprocess.TimeoutExpired:
                    proc.kill()
                    proc.wait(timeout=3)
    save(log_dir, name + ".gdb.log", raw)
    matched = marker in raw
    status = verdict(matched, raw, expect=expect)
    duration = round(time.monotonic() - start, 2)
    return {"name": name, "status": status, "duration_seconds": duration,
            "returncode": gdb["returncode"],
            "marker": marker, "marker_found": matched,
            "log": raw_log.name, "guest_log": guest_log.name,
            "mode": "qemu-user-gdb"}

def direct_case(ns: argparse.Namespace, log_dir: pathlib.Path,
                name: str, mode: str, marker: str, strace: bool = False) -> dict[str, Any]:
    argv = qemu_args(ns)
    if strace:
        argv += ["-strace"]
    argv += [ns.elf, mode]
    r = run_command(argv, timeout=20)
    raw = r["stdout"] + "\n--- STDERR ---\n" + r["stderr"]
    save(log_dir, name + ".log", raw)
    matched = r["returncode"] == 0 and marker in raw
    if strace:
        matched = matched and "write(" in r["stderr"]
    return {"name": name, "status": "PASS" if matched else "FAIL",
            "returncode": r["returncode"], "marker": marker,
            "marker_found": matched, "log": name + ".log",
            "mode": "qemu-user-direct"}

def run_suite(ns: argparse.Namespace) -> dict[str, Any]:
    log_dir = pathlib.Path(ns.logs).absolute()
    log_dir.mkdir(parents=True, exist_ok=True)
    checks: list[dict[str, Any]] = []
    specs = [
        ("basic_run", "basic", "MARK:BASIC_DONE", False),
        ("write_run", "write", "MARK:WRITE_DONE value=1", False),
        ("read_run", "read", "MARK:READ_DONE value=1", False),
        ("threads_run", "threads", "MARK:THREADS_DONE count=5", False),
        ("dlopen_run", "dlopen", "MARK:DLOPEN_RESULT:42", False),
        ("mprotect_run", "mprotect", "MARK:MPROTECT_RESULT:0xabcdef1234567891", False),
        ("syscalls_strace", "syscall", "MARK:SYSCALL_DONE", True)
    ]
    for name, mode, marker, strace in specs:
        checks.append(direct_case(ns, log_dir, name, mode, marker, strace))
        print(name, checks[-1]["status"], flush=True)

    gdb_specs = [
        ("breakpoint_main", "basic", [
            "break main", "continue",
            'printf "MARK:GDB_MAIN_HIT pc=%p sp=%p\\n", $pc, $sp',
            "info registers pc sp x0 x1 x29 x30", "bt", "info threads",
            "x/8i $pc",
            "continue"
        ], "MARK:GDB_MAIN_HIT", None),
        ("hardware_exec", "basic", [
            "hbreak breakpoint_target", "continue",
            'printf "MARK:GDB_HBREAK_HIT pc=%p\\n", $pc',
            "info breakpoints", "continue"
        ], "MARK:GDB_HBREAK_HIT", None),
        ("conditional_break", "basic", [
            "break conditional_target if iteration == 3", "continue",
            'printf "MARK:GDB_COND_HIT iteration=%d\\n", iteration',
            "continue"
        ], "MARK:GDB_COND_HIT iteration=3", None),
        ("step_registers", "basic", [
            "break single_step_target", "continue",
            'printf "MARK:GDB_BEFORE_PC=%p\\n", $pc',
            "x/8i $pc", "si", 'printf "MARK:GDB_STEPPED_PC=%p\\n", $pc',
            "set $saved_x0 = $x0", "set $x0 = 0x1234",
            'printf "MARK:GDB_X0_EDIT=0x%lx\\n", $x0',
            "set $x0 = $saved_x0", "ni",
            'printf "MARK:GDB_NEXTI_PC=%p\\n", $pc',
            "continue"
        ], "MARK:GDB_NEXTI_PC", None),
        ("memory_edit", "basic", [
            "break main", "continue",
            "set $saved_stack = *(unsigned long long*)$sp",
            "set {unsigned long long}$sp = 0x1122334455667788",
            'printf "MARK:GDB_MEMORY_EDIT=0x%lx\\n", *(unsigned long long*)$sp',
            "set {unsigned long long}$sp = $saved_stack", "continue"
        ], "MARK:GDB_MEMORY_EDIT=0x1122334455667788", None),
        ("finish_backtrace", "basic", [
            "break breakpoint_target", "continue",
            "bt", "finish",
            'printf "MARK:GDB_FINISH_PC=%p\\n", $pc',
            "continue"
        ], "MARK:GDB_FINISH_PC", None),
        ("thread_break", "threads", [
            "break thread_worker", "continue",
            'printf "MARK:GDB_THREAD_BREAK\\n"',
            "info threads", "thread apply all bt", "continue"
        ], "MARK:GDB_THREAD_BREAK", None),
        ("software_watch", "write", [
            "break watch_stage_start", "continue", "finish",
            "set can-use-hw-watchpoints 0",
            "watch -l watched_value",
            "continue",
            'printf "MARK:GDB_SOFTWARE_WATCH_HIT value=%lu\\n", watched_value',
            "continue"
        ], "MARK:GDB_SOFTWARE_WATCH_HIT", None),
        ("hardware_watch_user", "write", [
            "break watch_stage_start", "continue", "finish",
            "watch -l watched_value", "continue",
            'printf "MARK:GDB_HARDWARE_WATCH_HIT\\n"'
        ], "MARK:GDB_HARDWARE_WATCH_HIT", "watchpoint"),
        ("hardware_rwatch_user", "read", [
            "break watch_stage_start", "continue", "finish",
            "rwatch -l watched_value", "continue",
            'printf "MARK:GDB_READ_WATCH_HIT\\n"'
        ], "MARK:GDB_READ_WATCH_HIT", "watchpoint"),
        ("hardware_awatch_user", "write", [
            "break watch_stage_start", "continue", "finish",
            "awatch -l watched_value", "continue",
            'printf "MARK:GDB_ACCESS_WATCH_HIT\\n"'
        ], "MARK:GDB_ACCESS_WATCH_HIT", "watchpoint"),
        ("trap_signal", "sigtrap", [
            "handle SIGTRAP stop print nopass", "continue",
            'printf "MARK:GDB_SIGTRAP_CAPTURED\\n"',
        ], "MARK:GDB_SIGTRAP_CAPTURED", None),
        ("segv_signal", "sigsegv", [
            "handle SIGSEGV stop print nopass", "continue",
            'printf "MARK:GDB_SIGSEGV_CAPTURED\\n"'
        ], "MARK:GDB_SIGSEGV_CAPTURED", None),
        ("aarch64_brk_signal", "brk", [
            "handle SIGTRAP stop print nopass", "continue",
            'printf "MARK:GDB_BRK_CAPTURED\\n"'
        ], "MARK:GDB_BRK_CAPTURED", None)
    ]
    for name, mode, commands, marker, expect in gdb_specs:
        checks.append(gdb_case(ns, log_dir, name, mode, commands, marker, expect))
        print(name, checks[-1]["status"], flush=True)

    summary = {status: sum(c["status"] == status for c in checks)
               for status in ("PASS", "UNSUPPORTED", "FAIL")}
    result = {
        "target": "Android AArch64 built with Android NDK",
        "test_environment": ns.environment,
        "qemu": ns.qemu, "gdb": ns.gdb,
        "elf": ns.elf, "sysroot": ns.sysroot,
        "summary": summary, "checks": checks
    }
    (log_dir / "results.json").write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print("FINAL", json.dumps(summary), flush=True)
    return result

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--qemu", required=True)
    parser.add_argument("--gdb", required=True)
    parser.add_argument("--sysroot", required=True)
    parser.add_argument("--elf", required=True)
    parser.add_argument("--logs", required=True)
    parser.add_argument("--environment", default="local")
    ns = parser.parse_args()
    for attribute in ("qemu", "gdb", "elf", "sysroot"):
        if not os.path.exists(getattr(ns, attribute)):
            parser.error("missing " + attribute + ": " + getattr(ns, attribute))
    run_suite(ns)

if __name__ == "__main__":
    main()
