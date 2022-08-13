from config import web_server as server_config
from handler.api import search, post_data, get_status

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import json


class HandleRequests(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        parsed_url = urlparse(self.path)

        parsed = parse_qs(parsed_url.query)
        print(parsed_url)
        result = ""
        if self.path.__contains__('search'):
            result = search(parsed["key"])

        if self.path.__contains__('get_status'):
            result = get_status(parsed["key"])

        self.wfile.write(json.dumps(result))

    def do_POST(self):
        '''Reads post request body'''
        self._set_headers()
        content_len = int(self.headers.getheader('content-length', 0))
        post_body = self.rfile.read(content_len)
        self.wfile.write("received post request:<br>{}".format(post_body))

    def do_PUT(self):
        self.do_POST()


HTTPServer((server_config.HOST, server_config.PORT), HandleRequests).serve_forever()
