#Write a function unique to find all the unique elements of a list.
def unique(l):
 s=[]
 for i in range(len(l)):
  if l[i] not in s:
   s.append(l[i])
 return s
print unique([1,2,1,3,2,5])
