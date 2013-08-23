def flatten_list(a,result=None):
	if result is None:
		result=[]
	for x in a:
		if isinstance(x,list):
			flatten_list(x,result)
		else:
			result.append(x)
	return result
print flatten_list([1,2,[4,6,7],8,9,[3,4,5]])
