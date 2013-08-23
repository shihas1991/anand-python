#Write a program to print directory tree. The program should take path of a directory as argument and print all the files in it recursively as a tree.
import os
import sys
a='|--'
b=' |    '
c='\--'
x=0
print sys.argv[1]
def dirtree(dir,x):
	f=os.listdir(os.path.abspath(dir))
	p=f[-1]
	for i in f:
		if not os.path.isdir(os.path.abspath(dir+'/'+i)):
			if i==p:
				print b*x,c,i
			else:
				print b*x,a,i
		else:
			print b*x+' '+a,i
			dir=dir+'/'+i
			dirtree(dir,x+1)
dirtree(sys.argv[1],x)
