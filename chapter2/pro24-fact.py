#To find factorial of a number by recursion
def fact(n):
 if n==0:
  return 1
 else:
  return n*fact(n-1)
print fact(4)
