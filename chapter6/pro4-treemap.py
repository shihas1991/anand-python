#Write a function treemap to map a function over nested list.
def treemap(list1):
	for i in list1:
		if isinstance(i,list):
			treemap(i)
		else:
			p=list1.index(i)
			list1.remove(list1[p])
			list1.insert(p,i*i)
	return list1
print treemap([1, 2, [3, 4, [5]]])
#[1, 4, [9, 16, [25]]]
