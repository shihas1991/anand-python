#Write a function enumerate that takes a list and returns a list of tuples containing (index,item) for each item in the list
def enumerate(list):
	print[(index,list[index]) for index in range(len(list))]
enumerate(['a','b','c','d'])
