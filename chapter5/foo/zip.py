def zip(l,s):
 print [(l[x],s[x]) for x in range(len(l)) if len(l)==len(s)]
print zip([1,2,3,4],['a','b','c','d'])
