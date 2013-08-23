#Write a function to compute the number of python files (.py extension) in a specified directory recursively
import os
def find_py(dir):
	f=os.listdir('foo')
	list=[]
	for i in f:
		if i[-3:]=='.py':
			list.append(i)
	print len(list)
find_py('foo')
