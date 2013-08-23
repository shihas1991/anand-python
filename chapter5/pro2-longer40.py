#write a program that takes one or more filenames as arguments and prints all the lines which are longer than 40 characters
import sys
def longer(filenames):
	for f in sys.argv:
		for line in open(f):
			if len(line)>56:
				print line
longer(sys.argv)
