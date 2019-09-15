class lista:
	def ingresar_lista(self,number):#Put a element to the list
		
		if(self.number==None):
			self.number=number
		else:
			tmp=lista()
			tmp.number=self.number
			self.number=number
			tmp.next=self.next
			self.next=tmp
	def print_lista(self):#Print the list
		if self==None:
			print("Your list is completly empty")
		while self!=None:
			if(self.number==None):
					break
			print('->',self.number,end='')
			self=self.next
	def ingresar_lista_normal(self,number):#Put a element to the list
		while self.next!=None:
			self=self.next
		if self.number==None:
			self.number=number
		else:
			tmp=lista()
			tmp.number=number
			self.next=tmp
			tmp.next=None

def Reading(c,a1,a2):#Read the line
	flag1=0
	flag2=0
	flagn=0
	for i in range(len(c)):
		#print(c[i])
		if c[i]=='(' and flag1==0 and flag2==0:
			flag1=1
			flagn=0
		elif c[i]=='(' and flag1==-1 and flag2==0:
			flag2=0
			flagn=0
		elif c[i]==')':
			if flag1==1:
				flag1=-1
				flagn=0
			elif flag2==1:
				flag2==-1
				flagn=0
				break
		elif(c[i]=='+'):
			flag2=0
			flag1=-1
			#print("lle")
		elif(ord(c[i])>=ord('0') and ord(c[i])<=ord('9')):
			if(i==0):
				flag1=1
			if flag1==1: 
				a1.ingresar_lista(int(c[i]))
				flagn=1
			else:
				a2.ingresar_lista(int(c[i]))
				flagn=1
		elif c[i]=='-':
			if flagn==0:
				print("Error de digitacion 1")
				break
			else:
				flagn=2
		elif c[i]=='>':
			if flagn!=2:
				print("Error de digitacion 2")
				break
		else:
			#print(c[i])
			print("Error de digitacion 3")
			break

def Sumar(a1,a2):#Is the function that add the two lists
	flagn=0
	a3=lista()
	a3.number=None
	a3.next=None
	head=a3
	flage1=0
	flage2=0
	while a1!=None or a2!=None:
		if a2==None and a1!=None:
				a3.ingresar_lista_normal((a1.number+flagn)%10)
				#print("wqw: "+a3.number)
				flagn=int((a1.number+flagn)/10)
				a1=a1.next
		elif a1==None and a2!=None:
				a3.ingresar_lista_normal((a2.number+flagn)%10)
				flagn=int((a2.number+flagn)/10)
				a2=a2.next
		else:
			a3.ingresar_lista_normal((a1.number+a2.number+flagn)%10)
			flagn=int((a1.number+a2.number+flagn)/10)
			a1=a1.next
			a2=a2.next
	if(flagn!=0):
		a3.ingresar_lista_normal(flagn)
	return head

a1=lista()
a2=lista()
a3=lista()
a3.number=None
a3.next=None
a1.number=None
a1.next=None
a2.number=None
a2.next=None
c=input()
Reading(c,a1,a2)
#sumar(a1,a2)

a1.print_lista()
print()
a2.print_lista()
a3=Sumar(a1,a2)
print()
a3.print_lista()
