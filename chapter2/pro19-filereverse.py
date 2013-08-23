#Write a program reverse.py to print lines of a file in reverse order.
def reverse(filename):
 f=open(filename).readlines()
 f.reverse()
 for line in f:
  print line
import sys
reverse(sys.argv[1])
