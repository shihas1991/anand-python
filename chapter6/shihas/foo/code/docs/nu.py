def count(x):
 x=x+1
 return x 
s=[1,5,3,6,7,3,4,9,4]
for i in s:
 if s[i]==i:
 return s[i]
 else:
  count(s[i]!=i)
 print s[i]
