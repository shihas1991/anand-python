#Write a function to compute the total number of lines of code in all python files in the specified directory recursively
import os
def find(dir):
	f=os.listdir('foo')
	list2=[]
	list=[]
	for i in f:
		if '.py' in i:
			list.append(i)
	for j in list:
		file=open(os.path.join('foo',j)).readlines()
		print j,len(file)
find('foo')

