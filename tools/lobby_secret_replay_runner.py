#!/usr/bin/env python3
import argparse
import base64
import binascii
import json
import os
import socket
import struct
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Tuple

SENSITIVE_SUBSTRINGS = (
    "auth", "token", "secret", "password", "passwd", "openkey", "openid",
    "deviceid", "login", "session", "ticket", "cookie", "sign", "key"
)


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def redact_value(key: str, value: Any) -> Any:
    k = key.lower()
    if any(s in k for s in SENSITIVE_SUBSTRINGS):
        if value is None:
            return None
        if isinstance(value, (int, float, bool)):
            return "<redacted>"
        s = str(value)
        if len(s) <= 8:
            return "<redacted>"
        return f"<redacted:{len(s)} chars>"
    return redact_json(value)


def redact_json(obj: Any) -> Any:
    if isinstance(obj, dict):
        return {k: redact_value(k, v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [redact_json(x) for x in obj]
    return obj


def safe_json_loads(text: str) -> Any:
    try:
        return json.loads(text)
    except Exception:
        return None


def parse_lobby_frame(buf: bytes) -> Dict[str, Any]:
    if len(buf) < 10:
        return {"error": "short_frame", "raw_len": len(buf)}
    packet, total_len, checksum = struct.unpack_from("<HII", buf, 0)
    payload = buf[10:total_len]
    item: Dict[str, Any] = {
        "packet": packet,
        "totalLen": total_len,
        "checksum": checksum,
        "payloadLen": len(payload),
    }
    if packet == 3002 and len(payload) >= 6:
        seq, result_code, http_status = struct.unpack_from("<HHH", payload, 0)
        body = payload[6:]
        if b"\x00" in body:
            body = body.split(b"\x00", 1)[0]
        text = body.decode("utf-8", "replace")
        item.update({
            "seq": seq,
            "resultCode": result_code,
            "httpStatus": http_status,
            "jsonTextLen": len(text),
        })
        js = safe_json_loads(text)
        if js is not None:
            item["json"] = js
        else:
            item["textPreview"] = text[:512]
    elif packet in (3003, 3004):
        item["kind"] = "heartbeat" if packet == 3003 else "heartbeat_ack"
    else:
        # Store only a short preview by default.
        preview = payload[:256].decode("utf-8", "replace")
        item["payloadPreview"] = preview
    return item


def extract_frames_from_buffer(buffer: bytearray) -> List[bytes]:
    frames = []
    while True:
        if len(buffer) < 10:
            break
        packet, total_len, checksum = struct.unpack_from("<HII", buffer, 0)
        if total_len < 10 or total_len > 8 * 1024 * 1024:
            # Desync: drop one byte and try again, but record nothing.
            del buffer[0]
            continue
        if len(buffer) < total_len:
            break
        frames.append(bytes(buffer[:total_len]))
        del buffer[:total_len]
    return frames


def recv_frames(sock: socket.socket, wait_seconds: float) -> Tuple[List[bytes], bytes]:
    end = time.time() + wait_seconds
    buf = bytearray()
    frames: List[bytes] = []
    while time.time() < end:
        remaining = max(0.05, end - time.time())
        sock.settimeout(min(0.5, remaining))
        try:
            data = sock.recv(65536)
            if not data:
                break
            buf.extend(data)
            frames.extend(extract_frames_from_buffer(buf))
        except socket.timeout:
            continue
    return frames, bytes(buf)


def load_templates_from_secret() -> Dict[str, Any]:
    b64 = os.environ.get("LOBBY_REPLAY_TEMPLATES_B64", "").strip()
    if not b64:
        raise SystemExit("Missing GitHub secret/env: LOBBY_REPLAY_TEMPLATES_B64")
    try:
        raw = base64.b64decode(b64, validate=True)
    except binascii.Error as e:
        raise SystemExit(f"Invalid base64 in LOBBY_REPLAY_TEMPLATES_B64: {e}")
    try:
        return json.loads(raw.decode("utf-8"))
    except Exception as e:
        raise SystemExit(f"Decoded secret is not valid UTF-8 JSON: {e}")


def normalize_pairs(templates: Dict[str, Any]) -> List[Dict[str, Any]]:
    pairs = templates.get("pairs")
    if not isinstance(pairs, list):
        raise SystemExit("Template JSON must contain a list field: pairs")
    out = []
    for item in pairs:
        req = item.get("request", {}) if isinstance(item, dict) else {}
        raw_hex = req.get("rawFrameHex")
        if not raw_hex:
            continue
        try:
            raw = bytes.fromhex(raw_hex)
        except ValueError:
            continue
        if len(raw) < 10:
            continue
        packet, total_len, checksum = struct.unpack_from("<HII", raw, 0)
        if total_len != len(raw):
            raise SystemExit(f"Bad rawFrameHex length for seq={item.get('seq')}: totalLen={total_len} actual={len(raw)}")
        out.append({
            "seq": int(item.get("seq", req.get("seq", -1))),
            "cmd": int(item.get("cmd", req.get("cmd", -1))),
            "name": item.get("name", ""),
            "packet": packet,
            "totalLen": total_len,
            "checksum": checksum,
            "raw": raw,
        })
    if not out:
        raise SystemExit("No usable request frames in template JSON")
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="One-shot lobby TCP replay runner for GitHub Actions. Reads frames from LOBBY_REPLAY_TEMPLATES_B64 secret.")
    ap.add_argument("--host", default=os.environ.get("LOBBY_HOST", "82.156.181.229"))
    ap.add_argument("--port", type=int, default=int(os.environ.get("LOBBY_PORT", "9005")))
    ap.add_argument("--seqs", default=os.environ.get("LOBBY_SEQS", "1,3,4,5,8,10"))
    ap.add_argument("--timeout", type=float, default=float(os.environ.get("LOBBY_TIMEOUT", "5.0")))
    ap.add_argument("--read-window", type=float, default=float(os.environ.get("LOBBY_READ_WINDOW", "2.0")))
    ap.add_argument("--sleep", type=float, default=float(os.environ.get("LOBBY_SLEEP", "0.25")))
    ap.add_argument("--out", default=os.environ.get("LOBBY_OUT_DIR", "lobby_replay_out"))
    ap.add_argument("--save-full", action="store_true", default=os.environ.get("LOBBY_SAVE_FULL", "false").lower() in ("1", "true", "yes"))
    args = ap.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    templates = load_templates_from_secret()
    pairs = normalize_pairs(templates)
    wanted = {int(x) for x in args.seqs.replace(";", ",").split(",") if x.strip()}
    send_list = [p for p in pairs if p["seq"] in wanted]
    if not send_list:
        raise SystemExit(f"No request frames match seqs={sorted(wanted)}")

    summary = {
        "startedAt": now_iso(),
        "target": {"host": args.host, "port": args.port},
        "seqs": [p["seq"] for p in send_list],
        "templateSummary": [
            {"seq": p["seq"], "cmd": p["cmd"], "name": p["name"], "packet": p["packet"], "totalLen": p["totalLen"], "checksum": p["checksum"]}
            for p in send_list
        ],
        "events": [],
        "responsesRedacted": [],
    }
    full_responses: List[Dict[str, Any]] = []
    raw_response_frames: List[bytes] = []

    try:
        t0 = time.time()
        with socket.create_connection((args.host, args.port), timeout=args.timeout) as sock:
            summary["connect"] = {"ok": True, "elapsedMs": round((time.time() - t0) * 1000, 3), "localSockname": list(sock.getsockname())}
            for p in send_list:
                ev = {"type": "send", "seq": p["seq"], "cmd": p["cmd"], "name": p["name"], "bytes": len(p["raw"]), "checksum": p["checksum"], "ts": now_iso()}
                sock.sendall(p["raw"])
                summary["events"].append(ev)
                frames, leftover = recv_frames(sock, args.read_window)
                response_items = []
                for fr in frames:
                    raw_response_frames.append(fr)
                    parsed = parse_lobby_frame(fr)
                    full_responses.append(parsed)
                    response_items.append(redact_json(parsed))
                summary["responsesRedacted"].append({
                    "afterSeq": p["seq"],
                    "afterCmd": p["cmd"],
                    "frameCount": len(frames),
                    "leftoverLen": len(leftover),
                    "frames": response_items,
                })
                time.sleep(args.sleep)
            # Drain a little at the end.
            frames, leftover = recv_frames(sock, min(args.read_window, 2.0))
            if frames or leftover:
                response_items = []
                for fr in frames:
                    raw_response_frames.append(fr)
                    parsed = parse_lobby_frame(fr)
                    full_responses.append(parsed)
                    response_items.append(redact_json(parsed))
                summary["responsesRedacted"].append({"afterSeq": "final-drain", "frameCount": len(frames), "leftoverLen": len(leftover), "frames": response_items})
    except Exception as e:
        summary["connect"] = summary.get("connect", {"ok": False})
        summary["error"] = repr(e)

    summary["finishedAt"] = now_iso()
    summary["success"] = bool(summary.get("connect", {}).get("ok")) and "error" not in summary

    (out_dir / "replay_result_redacted.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        f"target={args.host}:{args.port}",
        f"success={summary['success']}",
        f"seqs={summary['seqs']}",
        f"connect={summary.get('connect')}",
        f"response_groups={len(summary['responsesRedacted'])}",
    ]
    for group in summary["responsesRedacted"]:
        frames = group.get("frames", [])
        lines.append(f"after={group.get('afterSeq')} frames={len(frames)} leftover={group.get('leftoverLen')}")
        for fr in frames:
            lines.append(f"  packet={fr.get('packet')} totalLen={fr.get('totalLen')} seq={fr.get('seq')} result={fr.get('resultCode')} http={fr.get('httpStatus')}")
    (out_dir / "summary.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")

    if args.save_full:
        (out_dir / "replay_result_full.json").write_text(json.dumps({"responses": full_responses}, ensure_ascii=False, indent=2), encoding="utf-8")
        with open(out_dir / "raw_response_frames.bin", "wb") as f:
            for fr in raw_response_frames:
                f.write(struct.pack("<I", len(fr)))
                f.write(fr)

    print("\n".join(lines))
    return 0 if summary["success"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
