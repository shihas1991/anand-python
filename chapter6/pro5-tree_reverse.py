#Write a function tree_reverse to reverse elements of a nested-list recursively
def tree_reverse(list1):
	list1.reverse()
	for i in list1:
		if isinstance(i,list):
			tree_reverse(i)
	return list1
print tree_reverse([[1, 2], [3, [4, 5]], 6])
