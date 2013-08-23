import os
import sys
def dirtree(dir):
	f=os.listdir(sys.argv[1])
	for path, dirs, files in os.walk("f"):
    		print path
    	for file in files:
        	print os.path.join(path, file)
dirtree(sys.argv[1])
