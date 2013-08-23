class Rationalnumber:
	def __init__(self,numerator,denominator=1):
		self.n=numerator
		self.d=denominator
	def add(self,other):
		if not isinstance(other,Rationalnumber):
			other=Rationalnumber(other)
		n,d=self.n,self.d
		n1,d1=other.n,other.d
		return Rationalnumber(n*d1+n1*d,d*d1)
	def __sub__(self,other):
		if not isinstance(other,Rationalnumber):
			other=Rationalnumber(other)
		n,d=self.n,self.d
		n1,d1=other.n,other.d
		return Rationalnumber(n*d1-n1*d,d*d1)
	def __mul__(self,other):
		if not isinstance(other,Rationalnumber):
			other=Rationalnumber(other)
		n,d=self.n,self.d
		n1,d1=other.n,other.d
		return Rationalnumber(n*n1,d*d1)
	def __div__(self,other):
		if not isinstance(other,Rationalnumber):
			other=Rationalnumber(other)
		n,d=self.n,self.d
		n1,d1=other.n,other.d
		return Rationalnumber(n*d1,d*n1)
	def __str__(self):
		return '%s/%s'%(self.n,self.d)
a=Rationalnumber(1,2)
b=Rationalnumber(1,3)
print a.add(b)
print a-b
print a*b
print a/b

