from http.server import BaseHTTPRequestHandler, HTTPServer

class HTTPServerRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        self.wfile.write(b"<!DOCTYPE html")
        
