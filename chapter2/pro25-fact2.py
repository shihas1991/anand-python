#To find factorial of a number
def fact(x):
 f=1
 for i in range(1,x+1):
  f=f*i
 return f
print fact(4)
