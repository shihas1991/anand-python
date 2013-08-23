#program to print line reverse
def line_reverse(filename):
 f=open(filename).readlines()
 for i in f:
  print i[::-1]
import sys
line_reverse(sys.argv[1])
 
