#Implement unix commands head and tail. The head and tail commands take a file as argument and prints its first and last 10 lines of the file respectively.
def head(filename):
 f=open(filename).readlines()
 for i in range(0,10):
  print f[i]   
import sys
head(sys.argv[1])

def tail(filename):
 f=open(filename).readlines()
 for i in range(len(f)-10,len(f)):
  print f[i]
import sys
tail(sys.argv[1])
  
