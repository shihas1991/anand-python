#practice of functions
def square(x):
 return x*x
print square(3)
print square(2)+square(3)
print square(square(2))

def sum_of_squares(x,y):
 return square(x)+square(y)
print sum_of_squares(5,4)

f=square
print f(2)

x=0
y=0
def incr(x):
 y=x+1
 return y
print incr(5)
print (x,y)

pi=3.14
def area(r):
 return pi*r*r
print area(4)

num=0
def square(x):
 global num
 num=num+1
 return x*x
print num
print square(2)
print num
print square(4)
print num

def square(x):
 return x*x*x
print map(square,[2,4,5,6,3,8,9])

print map(lambda x:x*x*x,[5,6,4,3])
