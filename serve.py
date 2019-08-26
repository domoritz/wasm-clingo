#!/usr/bin/env python3

import http.server
import socketserver

PORT = 8000

class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        http.server.SimpleHTTPRequestHandler.end_headers(self)

CORSRequestHandler.extensions_map.update({
    '.wasm': 'application/wasm'
})

httpd = socketserver.TCPServer(("", PORT), CORSRequestHandler)

print(f"Serving HTTP with WebAssembly support on 0.0.0.0 port {PORT} (http://0.0.0.0:{PORT}/index.html and http://0.0.0.0:{PORT}/index_amd.html) ...")
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    httpd.shutdown()
