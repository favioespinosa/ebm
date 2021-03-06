import socket
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
import pandas as pd
import pickle
with ThreadPoolExecutor(max_workers=5) as pool:
	with socket.create_connection((socket.gethostname(), 1234)) as s:
		data = pd.read_csv('dataSet.csv', sep=';',encoding ='latin1')
		print(data.memory_usage(deep=True).sum())
	#	print(len(data))
		message=input("Ingresa un comnado\n")
		s.send(message.encode('utf-8'))
		s.send((str(data.memory_usage(deep=True).sum()).encode('utf-8')))
		msg=pickle.dumps(data)
		s.send(msg)
		with open("Results2.csv",'wb') as f:
			while True:
				data=s.recv(4096)
				if not data:
					break
				print(data)
				f.write(data)
		s.close()

