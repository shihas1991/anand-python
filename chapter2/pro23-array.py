#Write a function array to create an 2-dimensional array. The function should take both dimensions as arguments. Value of each element can be initialized to None:
def array(d1,d2):
	return [[None]*d2 for d1 in range(1,d2)]
a=array(3,4)
a[0][2]=8
print a
