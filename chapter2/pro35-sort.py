#For sorting list of tuples sorted by last element of each tuple
s=[(1,4),(1,9),(4,3),(8,7),(4,1)]
q=sorted(s,key=lambda x:x[-1])
print q
q.reverse()
print q

