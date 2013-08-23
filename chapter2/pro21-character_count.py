def read_file(filename):
	return open(filename).read()
#import sys
#print read_file(sys.argv[1])
def char_count(file):
	d={}
	for ch in file:
		d[ch]=d.get(ch,0)+1
	return d
#import sys
#print char_count(sys.argv[1])
def main(filename):
	d=char_count(read_file(sys.argv[1]))
	for char,count in d.items():
		if '\n' not in char:
			print char,count
import sys
if __name__ == '__main__':
	main(sys.argv[1])

