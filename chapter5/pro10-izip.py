#Implement a function izip that works like itertools.izip.
def izip(*list):
	it= map(iter,list)
	while it:
		yield tuple(map(next,it))
x=izip(['a','b','c'],[1,2,3])
print x.next()
print x.next()
