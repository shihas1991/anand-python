import itertools
def permute(list1):
	l=itertools.permutations(list1)
	return list(l)
print permute([1,2,3])
