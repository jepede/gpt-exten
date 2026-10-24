import base64
import http.client
import json
import os
import time
import urllib.error
import urllib.request
from pathlib import Path

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey, X25519PublicKey
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

SESSION = 'ctf-t123-20261024-04a7'
BRANCH = 'work/t123-format-tools-20261024'
REPO = 'jepede/gpt-exten'
TEMP = Path(os.environ['RUNNER_TEMP'])
KEY = TEMP / 't123-private-key.bin'
b64 = lambda data: base64.b64encode(data).decode()

if os.environ['BRIDGE_STAGE'] == 'generate':
    private = X25519PrivateKey.generate()
    KEY.write_bytes(private.private_bytes(serialization.Encoding.Raw, serialization.PrivateFormat.Raw, serialization.NoEncryption()))
    KEY.chmod(0o600)
    target = Path('bridge_public');target.mkdir()
    public = private.public_key().public_bytes(serialization.Encoding.Raw, serialization.PublicFormat.Raw)
    (target / 'pubkey.json').write_text(json.dumps({'session': SESSION, 'server_public': b64(public)}))
    print('EPHEMERAL_PUBLIC_KEY_READY')
    raise SystemExit(0)

private = X25519PrivateKey.from_private_bytes(KEY.read_bytes())
api = 'https://api.github.com/repos/' + REPO + '/contents/bridge-requests/' + SESSION + '.json?ref=' + BRANCH.replace('/', '%2F')
deadline = time.monotonic() + 300
envelope = None
while time.monotonic() < deadline:
    request = urllib.request.Request(api, headers={'Authorization': 'Bearer ' + os.environ['GH_TOKEN'], 'Accept': 'application/vnd.github+json'})
    try:
        with urllib.request.urlopen(request, timeout=15) as stream:
            result = json.load(stream)
        envelope = json.loads(base64.b64decode(result['content']))
        break
    except urllib.error.HTTPError as ex:
        if ex.code != 404:raise RuntimeError('Private request retrieval failed: ' + str(ex.code)) from None
    time.sleep(1)
if envelope is None:raise RuntimeError('Private request wait expired')
client_public = X25519PublicKey.from_public_bytes(base64.b64decode(envelope['client_public']))
shared = private.exchange(client_public)
key = HKDF(algorithm=hashes.SHA256(), length=32, salt=None, info=b't123-private-bridge-v1').derive(shared)
plain = AESGCM(key).decrypt(base64.b64decode(envelope['nonce']), base64.b64decode(envelope['ciphertext']), b'request')
payload = json.loads(plain)
raw = base64.b64decode(payload['request_base64'])
head, _, body = raw.partition(b'\r\n\r\n')
rows = head.decode('iso-8859-1').split('\r\n')
method, path, version = rows[0].split(' ', 2)
headers = [row.split(':', 1) for row in rows[1:] if ':' in row]
host = next(v.strip() for k,v in headers if k.lower() == 'host')
if method != 'GET' or host.lower() not in ['w.t3yanzheng.com', 'w.t3yanzheng.com:80']:
    raise RuntimeError('The captured destination is outside this sample scope')
connection = http.client.HTTPConnection('w.t3yanzheng.com', 80, timeout=30)
connection.putrequest(method, path, skip_host=True, skip_accept_encoding=True)
for name, value in headers:
    if name.lower() not in ['connection', 'proxy-connection']:
        connection.putheader(name, value.strip())
connection.putheader('Connection', 'close');connection.endheaders()
response = connection.getresponse()
body = response.read(64 * 1024 * 1024 + 1)
if len(body) > 64 * 1024 * 1024:raise RuntimeError('Response exceeds sample limit')
status = response.status
wire = ('HTTP/1.1 ' + str(status) + ' ' + response.reason + '\r\n').encode('iso-8859-1')
for name, value in response.getheaders():
    if name.lower() not in ['transfer-encoding', 'content-length', 'connection']:
        wire += (name + ': ' + value + '\r\n').encode('iso-8859-1')
wire += ('Content-Length: ' + str(len(body)) + '\r\nConnection: close\r\n\r\n').encode() + body
nonce = os.urandom(12)
cipher = AESGCM(key).encrypt(nonce, wire, b'response')
output = Path('bridge_response');output.mkdir()
(output / 'response.enc.json').write_text(json.dumps({'session': SESSION, 'nonce': b64(nonce), 'ciphertext': b64(cipher)}))
KEY.unlink()
print('PRIVATE_FETCH_DONE', 'status=' + str(status), 'bytes=' + str(len(wire)))
