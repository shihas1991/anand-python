#strs=['aa','BB','CC','zz']
#print sorted(strs)
#print sorted(strs,reverse=True)
def sr(s):
 return s[-1]
strs=['aa','BB','CC','zz']
print sorted(strs,key=sr)
