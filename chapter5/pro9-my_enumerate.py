#Write a function my_enumerate that works like enumerate.
def my_enumerate(list):
	for i in range(len(list)):
		yield i,list[i]
x=my_enumerate(['a','b','c','d'])
print x.next()
print x.next()
