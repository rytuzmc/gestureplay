#!/usr/bin/env python3
"""Local GesturePlay web server and photo saver for macOS and Windows."""
from __future__ import annotations

import json
import re
import secrets
import sys
import threading
import webbrowser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit

APP_DIR = Path(__file__).resolve().parent
DOWNLOADS = Path.home() / "Downloads" / "gestureplay"
TOKEN = secrets.token_urlsafe(32)
MAX_UPLOAD = 40 * 1024 * 1024


class FlashPopHandler(SimpleHTTPRequestHandler):
    extensions_map = {
        **SimpleHTTPRequestHandler.extensions_map,
        ".mjs": "text/javascript",
        ".wasm": "application/wasm",
        ".task": "application/octet-stream",
        ".woff2": "font/woff2",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(APP_DIR), **kwargs)

    def do_GET(self):
        if urlsplit(self.path).path in ("/", "/index.html"):
            page = (APP_DIR / "index.html").read_bytes()
            page = page.replace(b"__FLASHPOP_PRINT_TOKEN__", TOKEN.encode("ascii"))
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(page)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(page)
            return
        super().do_GET()

    def do_POST(self):
        if not self._authorized():
            self._json(403, {"error": "This local GesturePlay session is not authorized."})
            return
        path = urlsplit(self.path).path
        if path.startswith("/save/"):
            self._save_file(unquote(path[len("/save/"):]))
        else:
            self._json(404, {"error": "Unknown GesturePlay action."})

    def _authorized(self) -> bool:
        port = self.server.server_port
        origin = self.headers.get("Origin", "")
        allowed = {f"http://localhost:{port}", f"http://127.0.0.1:{port}"}
        return origin in allowed and secrets.compare_digest(self.headers.get("X-FlashPop-Token", ""), TOKEN)

    def _read_body(self) -> bytes | None:
        try:
            size = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            return None
        if size <= 0 or size > MAX_UPLOAD:
            return None
        return self.rfile.read(size)

    def _save_file(self, filename: str):
        if not re.fullmatch(r"[A-Za-z0-9._-]{1,140}", filename):
            self._json(400, {"error": "Invalid file name."})
            return
        body = self._read_body()
        if not body or not body.startswith(b"\x89PNG\r\n\x1a\n"):
            self._json(400, {"error": "The photo file was invalid."})
            return
        try:
            DOWNLOADS.mkdir(parents=True, exist_ok=True)
            (DOWNLOADS / filename).write_bytes(body)
        except OSError as exc:
            self._json(500, {"error": f"Could not save to Downloads/gestureplay: {exc}"})
            return
        self._json(200, {"saved": filename})

    def _json(self, status: int, payload: dict):
        data = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, fmt, *args):
        print(fmt % args)


def main():
    auto_open = "--open" in sys.argv[1:]
    requested_port = next((int(arg) for arg in sys.argv[1:] if arg.isdigit()), None)
    try:
        DOWNLOADS.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        print(f"Could not create {DOWNLOADS}: {exc}")
    server = None
    candidate_ports = [requested_port] if requested_port is not None else range(8000, 8011)
    for candidate in candidate_ports:
        try:
            server = ThreadingHTTPServer(("127.0.0.1", candidate), FlashPopHandler)
            break
        except OSError:
            continue
    if server is None:
        raise SystemExit("GesturePlay could not find a free local port. Close an old GesturePlay window and try again.")
    port = server.server_port
    print(f"GesturePlay is ready at http://localhost:{port}")
    print(f"Photos will save to {DOWNLOADS}")
    if auto_open:
        threading.Timer(0.8, webbrowser.open, args=(f"http://localhost:{port}",)).start()
    print("Use the browser print dialog to choose a printer. Press Control-C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
