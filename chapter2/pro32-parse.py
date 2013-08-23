#Write a python function parse_csv to parse csv (comma separated values) files.
def parse_csv(filename):
	print [x[:-1].split(',') for x in open(filename).readlines()]
parse_csv('she.txt')
