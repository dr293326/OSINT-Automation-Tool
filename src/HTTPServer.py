import http.server
import socketserver
import os
import webbrowser
from threading import Thread
import flask
from flask import render_template, render_template_string
import jinja2
from jinja2 import Template, Environment, FileSystemLoader


def prepare_html(nmap_result, theharvester_result, virustotal_result):
    env = Environment(loader=FileSystemLoader('template'))
    template = env.get_template('index.html')
    output_from_parsed_template = template.render(nmap=nmap_result, theharvester=theharvester_result, virustotal=virustotal_result)
    web_dir = os.path.join(os.path.dirname(__file__), 'web/index.html')
    with open(web_dir, "w") as fh:
        fh.write(output_from_parsed_template)


class HTTPServer:
    PORT = 8080
    IP = '127.0.0.1'
    DIRECTORY = "web"
    TEMPLATES = "template"

    def __init__(self):
        web_dir = os.path.join(os.path.dirname(__file__), self.DIRECTORY)
        os.chdir(web_dir)

        # handler = http.server.SimpleHTTPRequestHandler
        # httpd = socketserver.TCPServer(("", self.PORT), handler)
        # # print("Serving at port: ", self.PORT)
        # # Thread(target=httpd.serve_forever).start()

    def open_report(self):
        webbrowser.open_new(os.path.join(os.path.dirname(__file__), 'web/index.html'))

