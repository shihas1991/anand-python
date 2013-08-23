#Write a function to compute the total number of lines of code, ignoring empty and comment lines, in all python files in the specified directory recursively.
import os
def find_number_lines(dir):
	f=os.listdir('foo')
	list3=[]
	list2=[]
	list=[]
	for i in f:
		if '.py' in i:
			list.append(i)
	for j in list:
		file=open(os.path.join('foo',j)).readlines()
		count=0
		for x in file:
			if '#' not in x:
				count+=1
		print j,count
find_number_lines('foo')
