#Write a program center_align.py to center align all lines in the given file.
import sys
def center_alignment(filename):
	f=open(filename).readlines()
	x=len(max(f))
	for line in f:
		p=(x-len(line))/2
		print ' '*p+line 
center_alignment(sys.argv[1])		 
