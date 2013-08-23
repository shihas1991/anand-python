#Write a program wrap.py that takes filename and width as aruguments and wraps the lines longer than width.
def wrap(filename):
 k = int(sys.argv[2])
 f=open(filename).readlines()
 for i in f:
  new=i
  while len(new)>k:
    print new[:k]
    new=new[k:]
  print new
import sys
wrap(sys.argv[1])

					
