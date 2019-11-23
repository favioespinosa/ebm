import sys
import json
import cgi
from http.server import HTTPServer, BaseHTTPRequestHandler
from socket import *
import threading
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
import Tweets
import pickle
from pycorenlp import StanfordCoreNLP
import multiprocessing
def CreateServer():
    serversocket=socket(AF_INET,SOCK_STREAM)
    try:
        serversocket.bind(('localhost',8000))
        serversocket.listen(5)
        (client,addr)=serversocket.accept()
        while (1):
            comando=client.recv(4096)
            longitud=client.recv(4096)
            comando=comando.decode('utf-8')
            longitud=longitud.decode('utf-8')
            print(int(longitud))
            print(comando)
            msg = client.recv(int(longitud))
            print(msg)
            data=pickle.loads(msg)
            if comando=='stat':
                Tweets.main(data,'Results.csv')
            elif comando=='enti':
                result=''
                nlp = StanfordCoreNLP('http://127.0.0.1:9000')
                for i in range(len(data['Tweet content'])):
                    result += Tweets.Stands(nlp, data['Tweet content'][i])
                with open("Results.csv") as f:
                    f.write(result)
            else:
                print("ERROR")
                client.close()
                return -1
            with open("Results.csv") as f:
                data = f.read()
            client.sendall(data.encode("utf-8"))
            client.close()

    except KeyboardInterrupt:
        print("Shutt")
if __name__=='__main__':
    CreateServer()