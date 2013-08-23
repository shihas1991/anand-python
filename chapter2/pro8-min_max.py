#Python has built-in functions min and max to compute minimum and maximum of a given list. Provide an implementation for these functions. What happens when you call your min and max functions with a list of strings?
def min(list):
 list.sort()
 return list[0]

def max(list):
 list.sort()
 return list[-1]

print min([1,2,4,6])
print min(['hai','shihas','ashna'])
print max([1,2,4,6])
print max(['hai','shihas','ashna'])
