#Implement a function product, to compute product of a list of numbers.
def product(list):
	sum=1
	for i in list:
		sum=sum*i
	return sum
print product([1,2,3,4])
