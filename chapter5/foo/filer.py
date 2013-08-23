def rev(filename):
	f=open(filename).readlines()
	for i in f:
		s=i[::-1]
		print  s
rev('sa.txt')
