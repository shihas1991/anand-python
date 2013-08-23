#word count program
def read_words(filename):
	return open(filename).read().split()
def word_count(list):
	d={}
	for w in list:
		d[w]=d.get(w,0)+1
	return d
#word_count(['hai','da','iam','shihas','hai','da'])
import sys
def main(filename):
	d=word_count(read_words(sys.argv[1]))
	for word,count in d.items():
		print word,count
if __name__ == "__main__":
	main(sys.argv[1])
