#Write a function flatten_dict to flatten a nested dictionary by joining the keys with.character
def flatten_dict(a,x=''):
	result={}
	for k,v in a.items():
		key=x+k
		if isinstance(v,dict):
			result.update(flatten_dict(v,key+'.'))
		else:
			result[key]=v
	return result
print flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
