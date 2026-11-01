#!/usr/bin/env python3
"""Bounded read-only C2 corroboration; no target executable, credentials, POSTs, or command execution."""
import datetime, hashlib, json, os, pathlib, socket, ssl, time
HOST = "103.36.63.136"
ROOT = pathlib.Path("evidence")
CA = pathlib.Path("forensics/program_elf/embedded_tls_ca.pem")
EXPECTED_CA_SHA256 = "030e390b63d5d9ccc489c8274f56bff6c300237102a2852883d280d4d9e3097e"
SAMPLE_SHA256 = "e2f6dab884afb7a61da706d2140108d734993018430bd69084682ab0275675d6"
MAX_RESPONSE = 65536
events = []
def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()
def hash_bytes(b):
    return hashlib.sha256(b).hexdigest()
def log(kind, **kw):
    rec = {"time_utc":now(), "kind":kind, **kw}
    events.append(rec)
    print(json.dumps(rec, ensure_ascii=False), flush=True)
def save(name, data):
    (ROOT/name).write_bytes(data)
    return {"sha256":hash_bytes(data),"bytes":len(data)}
def make_request(path, port):
    return (f"GET {path} HTTP/1.1\r\nHost: {HOST}:{port}\r\nUser-Agent: forensic-readonly-v2\r\nConnection: close\r\n\r\n").encode()
def get(path, port, prefix):
    req=make_request(path,port)
    save(prefix+"_request.raw",req)
    started=time.monotonic()
    try:
        with socket.create_connection((HOST,port),timeout=5) as s:
            s.settimeout(5)
            s.sendall(req)
            chunks=[]; total=0; truncated=False
            while total < MAX_RESPONSE:
                try: b=s.recv(min(8192,MAX_RESPONSE-total))
                except socket.timeout: truncated=True; break
                if not b: break
                chunks.append(b); total+=len(b)
            if total>=MAX_RESPONSE: truncated=True
        raw=b"".join(chunks)
        rec=save(prefix+"_response.raw",raw)
        header,sep,body=raw.partition(b"\r\n\r\n")
        status=header.split(b"\r\n",1)[0].decode("ascii","replace")[:180]
        response_meta={"status_line":status, "contains_header_separator":bool(sep),
                       "content_length_matches":None, "body_count":None, "body_users_count":None}
        if sep:
            for line in header.split(b"\r\n")[1:]:
                if line.lower().startswith(b"content-length:"):
                    try: response_meta["content_length_matches"]=int(line.split(b":",1)[1].strip())==len(body)
                    except ValueError: pass
            if path=="/online":
                try:
                    payload=json.loads(body.decode("utf-8"))
                    response_meta["body_count"]=payload.get("count")
                    users=payload.get("users")
                    response_meta["body_users_count"]=len(users) if isinstance(users,list) else None
                except (ValueError,UnicodeError): pass
        log("GET", target=f"{HOST}:{port}{path}",ok=True,elapsed_ms=round(1000*(time.monotonic()-started),1),
            evidence=rec,truncated=truncated,**response_meta)
    except OSError as e:
        log("GET", target=f"{HOST}:{port}{path}",ok=False,error=type(e).__name__,detail=str(e),
            elapsed_ms=round(1000*(time.monotonic()-started),1))
def main():
    ROOT.mkdir(exist_ok=True)
    ca=CA.read_bytes()
    if hash_bytes(ca)!=EXPECTED_CA_SHA256:
        raise ValueError("CA source bytes do not match the original ELF offset")
    save("embedded_tls_ca.pem",ca)
    log("provenance",repo=os.getenv("GITHUB_REPOSITORY"),run_id=os.getenv("GITHUB_RUN_ID"),
        sha=os.getenv("GITHUB_SHA"),sample_sha256=SAMPLE_SHA256,embedded_ca_sha256=hash_bytes(ca),
        policy="read-only; no uploaded sample; no POST; no credentials; no commands")
    for port in (8974,3000):
        started=time.monotonic()
        try:
            with socket.create_connection((HOST,port),timeout=5) as s:
                log("tcp_connect",target=f"{HOST}:{port}",ok=True,peer=list(s.getpeername()),
                    elapsed_ms=round(1000*(time.monotonic()-started),1))
        except OSError as e:
            log("tcp_connect",target=f"{HOST}:{port}",ok=False,error=type(e).__name__,detail=str(e),
                elapsed_ms=round(1000*(time.monotonic()-started),1))
    ctx=ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ctx.verify_mode=ssl.CERT_REQUIRED
    ctx.check_hostname=True
    ctx.minimum_version=ssl.TLSVersion.TLSv1_2
    ctx.load_verify_locations(cafile=str(CA))
    started=time.monotonic()
    try:
        with socket.create_connection((HOST,8974),timeout=5) as s:
            s.settimeout(5)
            with ctx.wrap_socket(s,server_hostname=HOST) as tls:
                leaf=tls.getpeercert(binary_form=True)
                der=save("verified_tls_leaf.der",leaf)
                log("tls_verified",ok=True,target=f"{HOST}:8974",verified_against_original_elf_ca=True,
                    ip_hostname_check=True,cert=der,tls_version=tls.version(),cipher=tls.cipher(),
                    elapsed_ms=round(1000*(time.monotonic()-started),1))
    except (OSError,ssl.SSLError) as e:
        log("tls_verified",ok=False,target=f"{HOST}:8974",error=type(e).__name__,detail=str(e),
            elapsed_ms=round(1000*(time.monotonic()-started),1))
    get("/online",3000,"online")
    get("/v3/hello",8974,"hello_get_no_credentials")
    save("events.json", (json.dumps(events,ensure_ascii=False,indent=2)+"\n").encode())
    files={p.name:{"sha256":hash_bytes(p.read_bytes()),"bytes":p.stat().st_size}
           for p in sorted(ROOT.iterdir()) if p.is_file()}
    (ROOT/"manifest.json").write_text(json.dumps({"created_utc":now(),"files":files},indent=2)+"\n")
    print("EVIDENCE_FILE_SHA256",json.dumps(files),flush=True)
if __name__=="__main__":
    main()
