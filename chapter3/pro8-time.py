#Write a program to list all the files in the given directory along with their length and last modification time. The output should contain one line for each file containing filename, length and modification date separated by tabs.
import sys
import os
def stat(dir):
	f=os.listdir(sys.argv[1])
	for i in f:
		print i,len(open(os.path.abspath(sys.argv[1]+'/'+i)).readlines()),os.stat(os.path.abspath(sys.argv[1]+'/'+i))[8]
stat(sys.argv[1])
