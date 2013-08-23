# Cumulative sum of a list [a, b, c, ...] is defined as [a, a+b, a+b+c, ...]. Write a function cumulative_sum to compute cumulative sum of a list. Does your implementation work for a list of strings?
def cumulative_sum(l):
	s=[]
	sum=0
	for i in l:
		sum=sum+i
		s.append(sum)
	return s
  
print cumulative_sum([1,2,3,4])
print cumulative_sum([4,3,2,1])
#print cumulative_sum(['hai','shihas'])
