#Python provides a built-in function filter(f, a) that returns items of the list a for which f(item) returns true. Provide an implementation for filter using list comprehensions
def even(x):
	return x%2==0
def filter(function,list):
	print [x for x in list if function(x) is True]
print filter(even,range(10))
