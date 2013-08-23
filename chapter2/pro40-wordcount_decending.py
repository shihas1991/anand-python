#prove the above program to print the words in the descending order of the number of occurrences.
def read_file(filename):
	return open(filename).read().split()
def word_count(words):
	d={}
	for w in words:
		d[w]=d.get(w,0)+1
	return d
#import sys
#print word_count(sys.argv[1])
def main(filename):
	d=word_count(read_file(sys.argv[1]))
	for i in sorted(d.keys(),key=lambda x:d[x],reverse=True):
			print i+' '+str(d[i])
import sys
if __name__ == '__main__':
	main(sys.argv[1])
