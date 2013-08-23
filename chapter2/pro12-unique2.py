#Write a function unique to find all the unique elements of a list.
def unique(l):
 s=[]
 for i in l:
  s.sort()
  if len(s)==0 or i!=s[-1]:
   s.append(i)
 return s
print unique([1,2,2,1,2,7,6])
