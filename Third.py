def contador1(lin,rev):#Is counting the times that see rev in linea
	counter=0
	j=0
	for i in range(len(lin)):
		if len(rev)==1:
			if(rev[0]==lin[i]):
				counter+=1
		elif j+1==(len(rev)):
			counter+=1
			j=0
		elif lin[i]==rev[j]:
			j+=1
		else:
			j=0
	return counter
def juntador(lin,emp,num):
	final=''
	for i in range(num+1):
		final=final+lin[emp+i]
	return final
def principal(lin):
	longo=len(lin)
	contador=0
	maxi=0
	line=''
	for i in range(len(lin)):
		for j in range(int(len(lin)/(i+1))):
			for p in range(j+1):
				coco=''
				line=juntador(lin,p*(i+1),i)
				contador=contador1(lin,line)
				if(longo%(i+1)!=0):
					for k in range(i):
						coco=coco+lin[longo-i+k]
					if(coco==line):
						contador+=1
				if contador>maxi:
					maxi=contador
					contador=0
	return maxi
print("Ingreasa la linea inicial")
lin=input()
print(principal(lin))