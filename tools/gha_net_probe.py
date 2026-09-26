#!/usr/bin/env python3
import argparse
import json
import os
import socket
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

DEFAULT_URLS = [
    "https://api.github.com/repos/jepede/gpt-exten/releases/tags/v1.0.2",
    "https://github.com/jepede/gpt-exten/releases/download/v1.0.2/global-metadata-8.39.0.dat",
    "https://httpbin.org/ip",
]


def resolve_host(host: str):
    rows = []
    try:
        for item in socket.getaddrinfo(host, None, proto=socket.IPPROTO_TCP):
            fam, _socktype, _proto, _canon, sockaddr = item
            addr = sockaddr[0]
            if addr not in rows:
                rows.append(addr)
    except Exception as e:
        return {"ok": False, "error": repr(e), "addresses": []}
    return {"ok": True, "addresses": rows}


def fetch_url(url: str, method: str, timeout: float, max_body: int):
    parsed = urllib.parse.urlparse(url)
    started = time.time()
    dns = resolve_host(parsed.hostname or "") if parsed.hostname else {"ok": False, "error": "missing host", "addresses": []}
    req = urllib.request.Request(url, method=method, headers={
        "User-Agent": "gpt-exten-gha-net-probe/1.0",
        "Accept": "*/*",
    })
    out = {
        "url": url,
        "method": method,
        "host": parsed.hostname,
        "dns": dns,
        "ok": False,
        "status": None,
        "headers": {},
        "elapsed_ms": None,
        "body_sample_utf8": "",
        "body_sample_hex": "",
        "error": None,
    }
    try:
        ctx = ssl.create_default_context()
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            body = resp.read(max_body) if method != "HEAD" and max_body > 0 else b""
            out.update({
                "ok": True,
                "status": resp.status,
                "headers": dict(resp.headers.items()),
                "elapsed_ms": round((time.time() - started) * 1000, 3),
                "body_sample_utf8": body.decode("utf-8", "replace"),
                "body_sample_hex": body[:256].hex(),
            })
    except urllib.error.HTTPError as e:
        body = b""
        try:
            body = e.read(max_body)
        except Exception:
            pass
        out.update({
            "ok": False,
            "status": e.code,
            "headers": dict(e.headers.items()) if e.headers else {},
            "elapsed_ms": round((time.time() - started) * 1000, 3),
            "body_sample_utf8": body.decode("utf-8", "replace"),
            "body_sample_hex": body[:256].hex(),
            "error": repr(e),
        })
    except Exception as e:
        out.update({
            "ok": False,
            "elapsed_ms": round((time.time() - started) * 1000, 3),
            "error": repr(e),
        })
    return out


def parse_urls(raw: str):
    if not raw.strip():
        return DEFAULT_URLS
    urls = []
    for part in raw.replace("\r", "\n").replace(",", "\n").split("\n"):
        u = part.strip()
        if u:
            urls.append(u)
    return urls or DEFAULT_URLS


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--urls", default=os.environ.get("PROBE_URLS", ""), help="newline/comma separated URLs")
    ap.add_argument("--method", default=os.environ.get("PROBE_METHOD", "GET"), choices=["GET", "HEAD"])
    ap.add_argument("--timeout", type=float, default=float(os.environ.get("PROBE_TIMEOUT", "20")))
    ap.add_argument("--max-body", type=int, default=int(os.environ.get("PROBE_MAX_BODY", "4096")))
    ap.add_argument("--out", default="net_probe_results.json")
    args = ap.parse_args()

    urls = parse_urls(args.urls)
    results = {
        "runner": {
            "platform": sys.platform,
            "python": sys.version,
            "github_run_id": os.environ.get("GITHUB_RUN_ID"),
            "github_sha": os.environ.get("GITHUB_SHA"),
            "github_ref": os.environ.get("GITHUB_REF"),
        },
        "urls": urls,
        "results": [fetch_url(u, args.method, args.timeout, args.max_body) for u in urls],
    }
    Path(args.out).write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
