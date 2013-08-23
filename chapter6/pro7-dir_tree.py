#Implement a program dirtree.py that takes a directory as argument and prints all the files in that directory recursively as a tree
import sys
import os
a='|--'
b=' |   '
c='`--'
x=0
print sys.argv[1]
def dir_tree(dir,x):
	f=os.listdir(os.path.abspath(dir))
	for i in f:
		if not os.path.isdir(os.path.abspath(dir+'/'+i)):
			if i!=f[-1]:
				print b*x,a,i
			else:
				print b*x,c,i
		else:
			print b*x,a,i
			dir=dir+'/'+i
			dir_tree(dir,x+1)
dir_tree(sys.argv[1],x)
