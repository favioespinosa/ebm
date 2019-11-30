import sys
import json
import requests
import csv
import requests
from pandas import read_csv
import pandas as pd
import pickle

comand = input('Ingresa el comando\n')
if  comand != 'stat' and comand != 'enti':
	print('Error: Incorrect operating mode')
	exit(1)
data = pd.read_csv('dataSet.csv', sep=';', encoding='ISO8859-1')
msg = pickle.dumps(data)
r = requests.post('http://localhost:8000/'+comand, data=msg)
data='h'
with open("Results2.csv",'w') as f:
	data=r.content

	f.write(data.decode('utf-8'))
