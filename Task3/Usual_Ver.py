import os
import shutil
import threading
import time
import numpy as np
import librosa as lr
from glob import glob
from concurrent.futures import ProcessPoolExecutor
def Reader(audio_files,files):
	for i in range(len(audio_files)):
		x, fs = lr.load(audio_files[i])
		mfccs = lr.feature.mfcc(x, sr=fs)
		numpy.savetxt("{}/{}.csv".format(root, files), mfccs, delimiter=",")
		return str(mfccs.shape)
def Organizador(path):#It organize to read the audio files
	my_array=np.array([[" "],[" "]])
	for root, subdirs, files in os.walk(path):
		for i in range(len(files)):
			audio_files=glob(root+'\\'+files[i])
			b=np.array([[str(Reader(audio_files,files[i]))],[root+'\\'+str(files[i])]])
			my_array=np.concatenate((my_array,b))
	return my_array
path=r'C:\Users\1\Documents\Python\Programacion_Paralela\Audio2'
t_start = time.time()
my_array=Organizador(path)
#print(my_array)
p=open("Readme.txt",'a')
p.write("Secuence program:"+str(time.time() - t_start)+'\n')
