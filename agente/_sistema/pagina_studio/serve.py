"""Quaderno di ripasso come sito locale: http://127.0.0.1:8765

Ricostruisce la pagina (dati freschi dai Word, dai quiz e dalle schede), la serve e salva i progressi in
_sistema/progressi.json (oltre che nel browser), così restano anche cambiando browser e Claude può leggerli.
Ascolta solo su 127.0.0.1: non è raggiungibile da altri computer.

Uso:  python serve.py [--port 8765] [--no-open] [--no-build]
Se il sito è già in esecuzione apre solo il browser.
"""
import argparse
import json
import re
import socket
import subprocess
import sys
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

PAG = Path(__file__).resolve().parent
BASE = PAG.parent
STATO = BASE / "progressi.json"
FILES = {"/": ("index.html", "text/html; charset=utf-8"), "/index.html": ("index.html", "text/html; charset=utf-8"),
         "/data.json": ("data.json", "application/json; charset=utf-8")}
MAX_POST = 2 * 1024 * 1024


def make_handler(port):
    hosts = {f"127.0.0.1:{port}", f"localhost:{port}"}

    class H(BaseHTTPRequestHandler):
        def log_message(self, *a):  # silenzioso
            pass

        def _send(self, code, body=b"", ctype="text/plain; charset=utf-8"):
            self.send_response(code)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            if self.command != "HEAD":
                self.wfile.write(body)

        def _host_ok(self):
            if self.headers.get("Host", "") not in hosts:
                return False
            org = self.headers.get("Origin")
            return org is None or org in {f"http://{h}" for h in hosts}

        def do_GET(self):
            if not self._host_ok():
                return self._send(403, b"host non ammesso")
            path = self.path.split("?")[0]
            if path == "/api/stato":
                return self._send(200, STATO.read_bytes() if STATO.exists() else b"{}", "application/json; charset=utf-8")
            mi = re.match(r"^/img/([a-z0-9_\-]+\.(png|jpe?g|gif|webp))$", path)
            if mi:  # disegni delle domande (scaricati dal sito esami)
                f = PAG / "img" / mi.group(1)
                tipo = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg", "gif": "image/gif", "webp": "image/webp"}[mi.group(2)]
                return self._send(200, f.read_bytes(), tipo) if f.exists() else self._send(404, b"manca")
            if path in FILES:
                name, ctype = FILES[path]
                f = PAG / name
                return self._send(200, f.read_bytes(), ctype) if f.exists() else self._send(404, b"manca " + name.encode())
            self._send(404, b"non trovato")

        do_HEAD = do_GET

        def do_POST(self):
            if not self._host_ok() or self.path.split("?")[0] != "/api/stato":
                return self._send(403, b"non ammesso")
            n = int(self.headers.get("Content-Length") or 0)
            if n <= 0 or n > MAX_POST:
                return self._send(413, b"dimensione non valida")
            try:
                x = json.loads(self.rfile.read(n))
                if isinstance(x, dict) and isinstance(x.get("stato"), dict):   # formato nuovo {stato, base, dirty}: in locale c'è un solo dispositivo
                    x = x["stato"]
                if not isinstance(x, dict) or x.get("v") != 2:
                    raise ValueError
            except Exception:
                return self._send(400, b"json non valido")
            tmp = STATO.with_suffix(".tmp")
            tmp.write_text(json.dumps(x, ensure_ascii=False), encoding="utf-8")
            tmp.replace(STATO)
            self._send(200, b'{"ok":true}')

    return H


def in_uso(port):
    with socket.socket() as s:
        s.settimeout(0.3)
        return s.connect_ex(("127.0.0.1", port)) == 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8765)
    ap.add_argument("--no-open", action="store_true")
    ap.add_argument("--no-build", action="store_true")
    a = ap.parse_args()
    url = f"http://127.0.0.1:{a.port}/"
    if in_uso(a.port):
        print(f"Già in esecuzione: {url}")
        if not a.no_open:
            webbrowser.open(url)
        return
    if not a.no_build:
        r = subprocess.run([sys.executable, str(BASE / "scripts" / "costruisci_pagina_studio.py")], capture_output=True, text=True, encoding="utf-8", stdin=subprocess.DEVNULL, creationflags=0x08000000)  # senza finestra, anche sotto pythonw
        print((r.stdout or r.stderr).strip().splitlines()[0] if (r.stdout or r.stderr) else "build eseguita")
    srv = ThreadingHTTPServer(("127.0.0.1", a.port), make_handler(a.port))
    print(f"Quaderno di ripasso su {url} (Ctrl+C per fermare)")
    if not a.no_open:
        webbrowser.open(url)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
