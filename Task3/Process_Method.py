import os
import shutil
import threading
import time
import numpy
import librosa as lr
from glob import glob
from concurrent.futures import ProcessPoolExecutor
def Reader(files,root):
	#path1='C:\\Users\\1\\Documents\\Python\\Programacion_Paralela\\Info_files'
	audio_files=glob(str(root)+'\\'+str(files))
	x, fs = lr.load(audio_files[i])
	mfccs = lr.feature.mfcc(x, sr=fs)
	numpy.savetxt("{}/{}.csv".format(root, files), mfccs, delimiter=",")
def Organizador(path):#It organize to read the audio files
	print("Joder")
	results=('hola','pepe')
	for root, subdirs, files in os.walk(path):
		with ProcessPoolExecutor(max_workers=4) as pool:
			for i in range(len(files)):
				pool.submit(Reader,files[i],root)
path=r'C:\Users\1\Documents\Python\Programacion_Paralela\Audio2'
t_start = time.time()
if __name__ == '__main__':
	Organizador(path)
	p=open("Readme.txt",'a')
	p.write("Process_program:"+str(time.time() - t_start)+'\n')
