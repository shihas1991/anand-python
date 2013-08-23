#Write a function dups to find all duplicates in the list
def dup(l):
 s=[]
 for i in range(len(l)):
  if l[i] in l[i+1:] and l[i] not in s:
   s.append(l[i])
 return s 
print dup([1,2,3,4,1,1,2])
