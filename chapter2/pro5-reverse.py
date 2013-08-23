#Write a function reverse to reverse a list. Can you do this without using list slicing?
def reverse(list):
	list.reverse()
	return list
print reverse(reverse([1,2,3,4]))
#this program done by list slicing
def rev(list):
	return list[::-1]
print rev(rev([1,2,3,4,5,6]))
