from sys import stdin
def contador(texto,palabra1):
	numero=0;
	palabra=''
	for i in range(len(texto)):
		if texto[i]==' ' or texto[i]=='\n':
			if palabra!='':
				if palabra==palabra1:
					numero+=1
			palabra=''
		elif (ord(texto[i])>=ord('A') and ord(texto[i])<=ord('Z')) or (ord(texto[i])>=ord('a') and ord(texto[i])<=ord('z')):
			palabra=palabra+texto[i]
	return numero
def definidor(texto):
	maxi=0
	numero=0
	palabra=''
	palabrap=''
	j=0
	for i in range(len(texto)):
		if texto[i]==' ' or texto[i]=='\n':
			if palabra!='':
				numero=contador(texto,palabra)
				if numero>maxi:
					maxi=numero
					palabrap=palabra
			palabra=''
		elif (ord(texto[i])>=ord('A') and ord(texto[i])<=ord('Z')) or (ord(texto[i])>=ord('a') and ord(texto[i])<=ord('z')):
			palabra=palabra+texto[i]
	return palabrap
print("Ingresa el texo:")
texto=''
for line in stdin:
  	texto=texto+line
print(texto)
print(definidor(texto))