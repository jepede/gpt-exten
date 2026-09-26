#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import socket
import struct
import time
from pathlib import Path


def split_frames(buf: bytes):
    frames = []
    off = 0
    while off + 10 <= len(buf):
        packet, total_len, checksum = struct.unpack_from('<HII', buf, off)
        if packet not in (3001, 3002, 3003, 3004, 4001) or total_len < 10 or total_len > 2000000:
            break
        if off + total_len > len(buf):
            break
        frames.append(buf[off:off + total_len])
        off += total_len
    return frames


def parse_frame(frame: bytes):
    packet, total_len, checksum = struct.unpack_from('<HII', frame, 0)
    body = frame[10:total_len]
    out = {
        'packet': packet,
        'total_len': total_len,
        'checksum': checksum,
        'body_len': len(body),
    }
    if packet == 3002 and len(body) >= 6:
        seq, result_code, http_status = struct.unpack_from('<HHH', body, 0)
        raw = body[6:].rstrip(b'\x00')
        out.update({'seq': seq, 'result_code': result_code, 'http_status': http_status})
        try:
            txt = raw.decode('utf-8', 'replace')
            out['text_preview'] = txt[:500]
        except Exception as e:
            out['decode_error'] = repr(e)
            out['raw_preview_hex'] = raw[:160].hex()
    else:
        out['raw_preview_hex'] = body[:160].hex()
    return out


def recv_window(sock: socket.socket, seconds: float, max_bytes: int = 262144) -> bytes:
    deadline = time.time() + seconds
    chunks = []
    total = 0
    sock.setblocking(False)
    while time.time() < deadline and total < max_bytes:
        try:
            chunk = sock.recv(min(65536, max_bytes - total))
            if not chunk:
                break
            chunks.append(chunk)
            total += len(chunk)
            deadline = max(deadline, time.time() + 0.25)
        except BlockingIOError:
            time.sleep(0.02)
    sock.setblocking(True)
    return b''.join(chunks)


def main() -> int:
    ap = argparse.ArgumentParser(description='Lobby TCP active heartbeat probe')
    ap.add_argument('--host', default='82.156.181.229')
    ap.add_argument('--port', type=int, default=9005)
    ap.add_argument('--timeout', type=float, default=5.0)
    ap.add_argument('--read-window', type=float, default=2.0)
    ap.add_argument('--out-dir', default='out')
    args = ap.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    result = {'target': {'host': args.host, 'port': args.port}, 'events': []}

    try:
        infos = socket.getaddrinfo(args.host, args.port, type=socket.SOCK_STREAM)
        result['dns'] = sorted({x[4][0] for x in infos})
    except Exception as e:
        result['dns_error'] = repr(e)

    try:
        t0 = time.perf_counter()
        sock = socket.create_connection((args.host, args.port), timeout=args.timeout)
        connect_ms = (time.perf_counter() - t0) * 1000.0
        sock.settimeout(args.timeout)
        result['connect'] = {'ok': True, 'elapsed_ms': round(connect_ms, 3), 'local_sockname': list(sock.getsockname())}
    except Exception as e:
        result['connect'] = {'ok': False, 'error': repr(e)}
        (out_dir / 'lobby_tcp_heartbeat_probe_result.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
        return 2

    rx = b''
    try:
        heartbeat = struct.pack('<HII', 3003, 10, 0)
        t0 = time.perf_counter()
        sock.sendall(heartbeat)
        result['events'].append({'type': 'send_3003_heartbeat', 'bytes': len(heartbeat), 'hex': heartbeat.hex()})
        rx = recv_window(sock, args.read_window)
        result['events'].append({
            'type': 'recv_after_heartbeat',
            'elapsed_ms': round((time.perf_counter() - t0) * 1000.0, 3),
            'bytes': len(rx),
            'raw_preview_hex': rx[:256].hex(),
            'frames': [parse_frame(f) for f in split_frames(rx)],
        })
    except Exception as e:
        result['runtime_error'] = repr(e)
    finally:
        try:
            sock.close()
        except Exception:
            pass

    (out_dir / 'lobby_tcp_heartbeat_probe_result.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    (out_dir / 'lobby_tcp_heartbeat_probe_rx.hex').write_text(rx.hex() + '\n', encoding='ascii')
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
