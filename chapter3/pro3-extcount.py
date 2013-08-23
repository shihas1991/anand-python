#Write a program extcount.py to count number of files for each extension in the given directory. The program should take a directory name as argument and print count and extension for each available file extension.
import sys
import os
import re
def extcount(dir):
	f=os.listdir(sys.argv[1])
	list=[]
	d={}
	for i in f:
		x=i.find('.')
		list.append(i[x+1:])
#		match=re.search(r'\.\S+',i)
#		list.append(match.group())
	for j in list:
		d[j]=d.get(j,0)+1
	for key,value in d.items():
		print value,key
extcount(sys.argv[1])
