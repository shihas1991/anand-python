#Write a function valuesort to sort values of a dictionary based on the key.
def valuesort(dictionary):
	return [dictionary[i] for i in sorted(dictionary.keys())]
print valuesort({'x':1,'y':2,'a':3})
