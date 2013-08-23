#write a program add.py that takes 2 numbers as command line arguments and prints its sum
def add(a,b):
 return int(a)+int(b)

import sys
x=add(sys.argv[1],sys.argv[2])
print x
