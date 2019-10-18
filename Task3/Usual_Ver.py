import os
import shutil
import threading
import time
import numpy
import librosa as lr
from glob import glob
import conv
def Reader(audio_files,files,f):
	for i in range(len(audio_files)):
		x, fs = lr.load(audio_files[i])
		mfccs = lr.feature.mfcc(x, sr=fs)
		f.write(files+': ',)
		f.write(str(mfccs.shape)+'\n')
def Organizador(path):#It organize to read the audio files
	print("Joder")
	f=open("mfccs_coeficients.txt",'w')
	for root, subdirs, files in os.walk(path):
		for i in range(len(files)):
			audio_files=glob(root+'\\'+files[i])
			Reader(audio_files,files[i],f)
path=r'C:\Users\1\Documents\Python\Programacion_Paralela\Audio'
t_start = time.time()
Organizador(path)
p=open("Readme.txt",'a')
p.write(str(time.time() - t_start)+'\n')
