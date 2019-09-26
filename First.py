class lista:
	def __init__(self):
		self.number=None
		self.next=None
	def ingresar_lista(self,number):#Put a element to the list
		while self.next!=None:
			self=self.next
		if self.number==None:
			self.number=number
		else:
			tmp=lista()
			tmp.number=number
			self.next=tmp
			tmp.next=None
	def print_lista(self):#Print the list
		if self==None:
			print("Your list is completly empty")
		while self!=None:
			print('->',self.number,end='')
			self=self.next

	def delet_lista_element(self,number):#Delet a element of the list
		head=self
		if self==None:
			print("Your list is completly empty")
		if self.number==number:
			print('llego')
			tmp=lista()
			tmp=self
			self=self.next
			del tmp
			return self
		else:
			tmp=self
			while self.number!=number:
				if self.next==None:
					return head
				tmp=self
				self=self.next
			if self.next==None:
				tmp.next=None
			else:	
				tmp.next=self.next
			del self
			return head

def init(lista1,number):#Change a number to a list
	head=lista1
	tmp=lista()
	while  number!=0:
		lista1.ingresar_lista(number%10)
		number=int(number/10)
	return head

lista1=lista()
lista1=init(lista1,123124)
lista1.print_lista()
lista1=lista1.delet_lista_element(3)
print('')
lista1.print_lista()
