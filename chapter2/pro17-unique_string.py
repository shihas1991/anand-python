#Improve the unique function written in previous problems to take an optional key function as argument and use the return value of the key function to check for uniqueness.
def unique_string(l):
 s=[]
 for i in range(len(l)):
  if l[i].lower() not in s:
   s.append(l[i])
 return s
print unique_string(['python','java','Python','Java','perl','Perl'])
