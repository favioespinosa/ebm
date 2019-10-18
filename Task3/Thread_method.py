import os
import shutil
import threading
import time
import numpy
import librosa as lr
from glob import glob
from concurrent.futures import ThreadPoolExecutor, as_completed
def Reader(files,root):
	path1='C:\\Users\\1\\Documents\\Python\\Programacion_Paralela\\Info_files'#IS the path of the folder where will be the files
	audio_files=glob(str(root)+'\\'+str(files))
	f=open(path1+"\\"+str(files)+".txt",'w')#os.createdirs..
	p=open(path1+"\\"+str(files)+"_Catalogs.txt",'w')
	for i in range(len(audio_files)):
		#print("dasjdasjk")
		x, fs = lr.load(audio_files[i])
		mfccs = lr.feature.mfcc(x, sr=fs)
		f.write(files+': ',)
		f.write(str(mfccs.shape)+'\n')
		p.write(str(audio_files[i])+'\n')
def Organizador(path):#It organize to read the audio files
	print("Joder")
	results=('hola','pepe')
	for root, subdirs, files in os.walk(path):
		with ThreadPoolExecutor(max_workers=24) as pool:
			for i in range(len(files)):
				pool.submit(Reader,files[i],root)
path=r'C:\Users\1\Documents\Python\Programacion_Paralela\Audio2'
t_start = time.time()
Organizador(path)
p=open("Readme.txt",'a')
p.write("Thread_program:"+str(time.time() - t_start)+'\n')
