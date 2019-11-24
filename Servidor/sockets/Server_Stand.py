import socket
import threading
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
import Tweets
import pickle
from pycorenlp import StanfordCoreNLP
import multiprocessing
def process_request(conn, addr):
    print("connected client:", addr)
    with conn:
        comando=conn.recv(4096)
        longitud=conn.recv(4096)
        comando=comando.decode('utf-8')
        longitud=longitud.decode('utf-8')
        print(int(longitud))
        print(comando)
        msg = conn.recv(int(longitud))
        #print(msg)
        data=pickle.loads(msg)
        print(data)
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
            conn.close()
            return -1
        with open("Results.csv") as f:
            data = f.read()
        conn.sendall(data.encode("utf-8"))
        conn.close()
def worker(sock):
    while True:
        conn, addr = sock.accept()
        th = threading.Thread(target=process_request, args=(conn, addr))
        th.start()
with socket.socket() as sock:
    sock.bind((socket.gethostname(), 1234))
    sock.listen(5)
    worker(sock)
