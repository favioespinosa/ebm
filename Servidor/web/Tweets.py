import pandas as pd
import datetime
import os
import numpy as np
import warnings
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pycorenlp import StanfordCoreNLP
warnings.filterwarnings("ignore")
class arr_twets():
	def __init__(self,word,data):
		self.elements=[]
		i=0
		p=0
		while p<10:
			if(not pd.isna(data[word][i])):
				self.elements.append(data[word][i])
				self.elements.append(i)
				p+=1
			i+=1
		self.max_10(data,i,word)
	def sort_twets(self):
		for i in range(9):
			for j in range(i,10):
				if(i%2==0 and j%2==0):	
					if(i!=j):
						if self.elements[j]>self.elements[i]:
							p=self.elements[j]
							self.elements[j]=self.elements[i]
							self.elements[i]=p
							p=self.elements[i+1]
							self.elements[i+1]=self.elements[j+1]
							self.elements[j+1]=p
	def colocar(self,data,i):
		if data>self.elements[8]:
			self.elements[8]=data
			self.elements[9]=i
	def max_10(self,data,i,name):
		self.sort_twets()
		for j in range(i,len(data[name])):
			if(not pd.isna(data[name][j])):
				self.colocar(data[name][j],j)
				self.sort_twets()
	def popular_twets(self,data,name):
		popular=pd.DataFrame(columns=['Author','RTs'])
		for i in range(20):
			if i%2==0:
				popular=popular.append({'Author':data['User Name'][self.elements[i+1]],'RTs':self.elements[i]},ignore_index=True)
		print(popular)
		popular.to_csv(name,mode='a',sep='\t')
	def popular_Authors(self,data,name):
		popular=pd.DataFrame(columns=['Author','Followers'])
		for i in range(20):
			if i%2==0:
				popular=popular.append({'Author':data['User Name'][self.elements[i+1]],'Followers':self.elements[i]},ignore_index=True)
		print(popular)
		popular.to_csv(name,mode='a',sep='\t')
def sort_words(lista):
	longitud=len(lista['Quantity'])
	for i in range(longitud-1):
		for j in range(i,longitud):
			if lista['Quantity'][i]>lista['Quantity'][j]:
				p=lista['Quantity'][i]
				lista["Quantity"][i]=lista['Quantity'][j]
				lista["Quantity"][j]=p
				p=lista['Word'][i]
				lista['Word'][i]=lista['Word'][j]
				lista['Word'][j]=p
	return lista
def finder(lista,palabra):
	p=len(lista['Word'])
	if p!=0:
		for i in range(len(lista['Word'])):
			if palabra==lista['Word'][i]:
				return True,i
	return False,-1
def words(data,name):
	lista=pd.DataFrame(columns=['Word','Quantity'])
	try:
		for i in range(10):
			for j in range(len(data['Tweet content'][i].split(' '))):
				existe,indice=finder(lista,data['Tweet content'][i].split(' ')[j])
				if existe==True:
					lista['Quantity'][int(indice)]=lista['Quantity'][int(indice)]+1
				else:
					lista=lista.append({'Word':data['Tweet content'][i].split(' ')[j],'Quantity':1},ignore_index=True)
	except Exception as e:
		print(e)
	lista=sort_words(lista)
	print(lista)
	lista.iloc[0:11].to_csv(name,mode='a',sep='\t')
def main(data,name_file_csv):
	t_start = time.time()
	with ThreadPoolExecutor(max_workers=1) as pool:
		pool.submit(words,data,name_file_csv)
	print(time.time()-t_start)
	pepe=arr_twets('RTs',data)
	maria=arr_twets('Followers',data)
	pepe.popular_twets(data,name_file_csv)
	maria.popular_Authors(data,name_file_csv)
def Stands(nlp, data):
	print(data)
	result = nlp.annotate(data, properties={ 'annotators': 'ner', 'outputFormat': 'csv', 'timeout': 1000, })
	pos = []
	if type(result) == str:
		return result
	for word in result["sentences"][1]['tokens']:
		pos.append('{} ({})'.format(word['word'], word['ner']))
		print(pos)
	return (" ".join(pos))