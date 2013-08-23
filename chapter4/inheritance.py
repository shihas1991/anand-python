class Bankaccount:
	def __init__(self):
		self.balance=0
	def deposit(self,amount):
		self.balance+=amount
		return self.balance
	def withdraw(self,amount):
		self.balance-=amount
		return self.balance
#	def sh(self,amount):
#		return amount

class minimumbalanceaccount(Bankaccount):
	def __init__(self,minimumbalance):
		Bankaccount.__init__(self)
		self.minimumbalance=minimumbalance
	def withdraw(self,amount):
		if self.balance - amount < self.minimumbalance:
			print 'minimum balance must be maintain'
		else:
			return Bankaccount.withdraw(self, amount)
a=minimumbalanceaccount(100)
b=minimumbalanceaccount(100)
c=Bankaccount()
print a.deposit(1000)
print b.deposit(500)
print b.withdraw(100)
print a.withdraw(500)
#print c.sh(100)

