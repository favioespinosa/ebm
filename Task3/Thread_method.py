import os
import shutil
import threading
import time
import numpy as np
import librosa as lr
from glob import glob
from concurrent.futures import ThreadPoolExecutor, as_completed
import warnings
warnings.filterwarnings('ignore')
def Reader(files,root):
	audio_files=glob(str(root)+'\\'+str(files))
	x, fs = lr.load(audio_files[0])
	mfccs = lr.feature.mfcc(x, sr=fs)
	numpy.savetxt("{}/{}.csv".format(root, files), mfccs, delimiter=",")
	return str(mfccs.shape)+"+"+root+"\\"+files
def Organizador(path):#It organize to read the audio files
	print("Joder")
	for root, subdirs, files in os.walk(path):
		with ThreadPoolExecutor(max_workers=24) as pool:
			results=[pool.submit(Reader,files[i],root) for i in range(len(files))]
path=r'C:\Users\1\Documents\Python\Programacion_Paralela\Audio2'
t_start = time.time()
Organizador(path)
p=open("Readme.txt",'a')
p.write("Thread_program:"+str(time.time() - t_start)+'\n')
