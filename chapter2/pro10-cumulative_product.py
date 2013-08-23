#Write a function cumulative_product to compute cumulative product of a list of numbers
def cumulative_product(list):
	sum=1
	list1=[]
	for num in list:
		sum=sum*num
		list1.append(sum)
	return list1
print cumulative_product([4,3,2,1])
