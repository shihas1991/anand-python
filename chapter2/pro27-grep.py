#Implement unix command grep. The grep command takes a string and a file as arguments and prints all lines in the file which contain the specified string
def grep(filename):
 f=open(filename).readlines()
 for i in f:
  if sys.argv[2] in i:
   print i

import sys
grep(sys.argv[1]) 
