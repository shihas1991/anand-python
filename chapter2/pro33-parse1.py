#eneralize the above implementation of csv parser to support any delimiter and comments
def parse(filename,i,j):
	print [x[:-1].split('!') for x in open(filename).readlines() if x[0]!='#']
parse('she.txt','!','#')
