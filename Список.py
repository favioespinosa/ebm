class lista:
	def ingresar_lista(self,number):#Put a element to the list
		while self.next!=None:
			self=self.next
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

def init(a1,number):#Change a number to a list
	head=a1
	tmp=lista()
	while  number!=0:
		a1.ingresar_lista(number%10)
		number=int(number/10)
	return head

a1=lista()
a1.number=0
a1.next=None
a1=init(a1,123124)
a1.print_lista()
a1=a1.delet_lista_element(3)
print('')
a1.print_lista()
