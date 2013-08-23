#Write a function triplets that takes a number n as argument and returns a list of triplets such that sum of first two elements of the triplet equals the third element using numbers below n. Please note that (a, b, c) and (b, a, c) represent same triplet.
def triplets(num):
	print [(x,y,z) for x in range(1,num) for y in range(x,num) for z in range(y,num) if x+y==z]
print triplets(5)
		
