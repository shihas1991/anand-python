#Write a program to list all files in the given directory.
import os
import sys
def find(dir):
	print os.listdir(sys.argv[1])
find(sys.argv[1])
