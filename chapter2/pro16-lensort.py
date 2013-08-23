#Write a function lensort to sort a list of strings based on length.
def lensort(l):
 return sorted(l,key=lambda x:len(x))
print lensort(['python','perl','java','c','haskell','ruby'])
