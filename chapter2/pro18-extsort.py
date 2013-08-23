#Write a function extsort to sort a list of files based on extension.
def extsort(l):
 for i in range(len(l)):
  return sorted(l,key=lambda x:x[l[i].find('.'):])
print extsort(['a.c','a.py','b.py','bar.txt','foo.txt','x.c'])
