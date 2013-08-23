#Provide an implementation for zip function using list comprehensions.
def zip(list1,list2):
	print [(list1[x],list2[x])for x in range(len(list1)) if len(list1)==len(list2) ]
print zip([1,2,3,4,5],['a','b','c','d','shihas'])
