#Write a program split.py, that takes an integer n and a filename as command line arguments and splits the file into multiple small files with each having n lines.
import sys
def split(filename):
	n=int(sys.argv[2])
	new='file'
	f=open(sys.argv[1]).read().split('\n')
	x=1
	for lines in range(0,len(f),n):
		line=f[lines:lines+n]
		new_file=open(new+str(x)+'.txt','w')
		new_file.write('\n'.join(line))
		new_file.close()
		x+=1
split(sys.argv[1])

