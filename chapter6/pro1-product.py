# Implement a function product to multiply 2 numbers recursively using + and - operators only
def product(n1,n2):
	if n2==0:
		return 0
	else:
		return n1+product(n1,n2-1)
print product(2,10)
