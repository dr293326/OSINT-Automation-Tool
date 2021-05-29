import http.server
import socketserver
import os
import webbrowser
from threading import Thread



class HTTPServer:
    PORT = 8080
    IP = '127.0.0.1'
    DIRECTORY = "web"

    def __init__(self):
        web_dir = os.path.join(os.path.dirname(__file__), self.DIRECTORY)
        os.chdir(web_dir)

        handler = http.server.SimpleHTTPRequestHandler
        httpd = socketserver.TCPServer(("", self.PORT), handler)
        print("Serving at port: ", self.PORT)
        Thread(target=httpd.serve_forever).start()

    def open_report(self):
        webbrowser.open_new('http://' + self.IP + ':' + self.PORT.__str__())
