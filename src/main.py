# from src.application import uploader, data_gather, text_fetcher
#
#
# def main():
#     while True:
#         data_gather.run()
#         uploader.run()
#         text_fetcher.run()


import SimpleHTTPServer
import SocketServer

PORT = 8001

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print("serving at port ", PORT)
httpd.serve_forever()
