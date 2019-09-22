class lista:
	def ingresar_lista(self,number):#Put a element to the list
		
		while self.next!=None:
			self=self.next
		if self.number==None:
			self.number=number
			letras(self)
		else:
			tmp=lista()
			tmp.number=number
			letras(tmp)
			self.next=tmp
			tmp.next=None
def letras(a1):
	if a1.number==0:
		a1.letras=' '
		a1.longitud=1
	elif a1.number==1:
		a1.longitud=1
		a1.letra='#'
	elif a1.number==2:
		a1.letra="abc"
		a1.longitud=3
	elif a1.number==3:
		a1.letra="def"
		a1.longitud=3
	elif a1.number==4:
		a1.letra="ghi"
		a1.longitud=3
	elif a1.number==5:
		a1.letra="jkl"
		a1.longitud=3
	elif a1.number==6:
		a1.letra="mno"
		a1.longitud=3
	elif a1.number==7:
		a1.letra="pqrs"
		a1.longitud=4
	elif a1.number==8:
		a1.letra="tuv"
		a1.longitud=3
	elif a1.number==9:
		a1.letra="wxyz"
		a1.longitud=4
	else:
		print("The numbers needs to be from 0 to 9 and you can't use: ",endl='')
		print(a1.number)
		return -1
def Iniciador(a1,number):
	head=a1
	tmp=lista()
	while  number!=0:
		a1.ingresar_lista(number%10)
		number=int(number/10)
	return head
def Maslist(a1,mas,tam):
	p=["" for x in range(a1.longitud)]
	for i in range(a1.longitud):
		p[i]=a1.letra[i]
	mas=p
	tam=a1.longitud
	return mas,tam
def Multi(a1,mas,tamano):
	k=["" for x in range(a1.longitud*tamano)]
	l=0
	for i in range(tamano):
		for p in range(a1.longitud):
			k[l]=mas[i]+a1.letra[p]
			l+=1
	tamano=tamano*a1.longitud
	mas=["" for x in range(a1.longitud*tamano)]
	mas=k
	return mas,tamano
def Mezclar(a1,mas,tam):
	tam=a1.longitud
	mas,tam=Maslist(a1,mas,tam)
	a1=a1.next
	while a1!=None:
		if a1.next==None:
			mas,tam=Multi(a1,mas,tam)
			return mas,tam
		mas,tam=Multi(a1,mas,tam)
		a1=a1.next
	return mas,tam
def alrevez(number):
	pepe=int(number)
	nuevo=0
	while pepe!=0:
		nuevo=nuevo*10+pepe%10
		pepe=int(pepe/10)
	return int(nuevo)
def Render(mes,tam):
	k=["" for x in range(tam)]
	flag=0
	l=0
	for i in range(tam):
		for j in range(tam):
			if mes[i]==mes[j] and i!=j:
				flag=1
		if flag==0:
			k[l]=mes[i]
			l+=1
		flag=0
	return k,l
tam=0
a1=lista()
a1.next=None
a1.number=None
a1.longitud=0
a1.letra=''
numero=input()
numero=alrevez(numero)
Iniciador(a1,int(numero))
mas=["" for x in range(3)]
p=["" for x in range(3)]
mas,tam=Mezclar(a1,mas,tam)
p,tam=Render(mas,tam)
print("[ ",end=' ')
for i in range(tam):
	print(p[i],end=', ')
print("]")