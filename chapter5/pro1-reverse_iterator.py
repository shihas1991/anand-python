#Write an iterator class reverse_iter, that takes a list and iterates it from the reverse direction
class reverse_iterator:
        def __init__(self,l):
                self.i=len(l)-1
                self.l=l
        def iter(self):
               return self
        def next(self):
                if self.i>0:
                        i=self.i
                        self.i-=1
                        return l[i]
		else:
			raise StopIteration()
l=[1,2,3,4,5,7,4]
a=reverse_iterator(l)
a.iter()
print a.next()
print a.next()
print a.next()
print a.next()
print a.next()
print a.next()                           
