def e(x):
	return x%2==0
def filter(f,list):
	return [x for x in list if f(x) is True]
print filter(e,range(10))
