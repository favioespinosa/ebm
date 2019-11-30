from http.server import HTTPServer, BaseHTTPRequestHandler
import pickle
import pandas as pd
from pycorenlp import StanfordCoreNLP
import os
from multiprocessing import Process
import Tweets
class RequestHeandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write(self._html("hi!"))

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        print(content_length)
        data = self.rfile.read(content_length)
        data = pickle.loads(data)
        self._set_headers()
        if self.path == '/stat':
            Tweets.main(data,'Result.csv')
        elif self.path=='/enti':
            result=[]
            nlp = StanfordCoreNLP('http://localhost:9000')
            for i in range(len(data['Tweet content'])):
                 result.append(Tweets.Stands(nlp, data['Tweet content'][i]))
                 print(result)
            with open("Results.csv",'w') as f:
                for i in range(len(result)):
                    f.write(str(result[i]))
        with open("Results.csv") as f:
            data = f.read()
        self.wfile.write(data.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=RequestHeandler, addr="localhost", port=8000):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on {addr}:{port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
