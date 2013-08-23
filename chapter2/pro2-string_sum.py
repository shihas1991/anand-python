# What happens when the above sum function is called with a list of strings? Can you make your sum function work for a list of strings as well
def sum(list):
	sum=''
	for i in list:
		sum=str(sum)+str(i)
	return sum
print sum(['aa','bb','cc','dd'])
