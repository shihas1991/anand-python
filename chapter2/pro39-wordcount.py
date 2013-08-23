#To count words
def char_count(filename):
 f=open(filename).read()
 return len(f)
print char_count('test.txt')

def word_count(filename):
 f=open(filename).read()
 return len(f.split())
print word_count('ashna')
print word_count('test.txt')

def line_count(filename):
 f=open(filename).readlines()
 return len(f)
print line_count('ashna')
print line_count('test.txt')
