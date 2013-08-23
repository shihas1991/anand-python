#Write a python program zip.py to create a zip file. The program should take name of zip file as first argument and files to add as rest of the arguments.
import zipfile
import sys
z=zipfile.ZipFile(sys.argv[1],'w')
for i in range(2,len(sys.argv)):
	z.write(sys.argv[i])
