# Python provides a built-in function map that applies a function to each element of a list. Provide an implementation for map using list comprehensions.
def square(num):
	return num*num
print square(2)
def map(function,list):
	print [function(x) for x in list]
print map(square,[1,2,3,4,5])
