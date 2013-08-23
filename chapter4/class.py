class Bankaccount:
	def __init__(self):
		self.balance=0
	def deposit(self,amount):
		self.balance+=amount
		return self.balance
	def withdraw(self,amount):
		self.balance-=amount
		return self.balance
a=Bankaccount()
b=Bankaccount()
print a.deposit(1000)
print b.deposit(500)
print b.withdraw(100)
print a.withdraw(500)

