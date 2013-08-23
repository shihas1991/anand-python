#Write a program links.py that takes URL of a webpage as argument and prints all the URLs linked from that webpage.
import sys
import urllib
import re
file=urllib.urlopen(sys.argv[1]).read()
x=re.findall(r'http://[\w.]+.+"',file)
for i in x:
	print i[:-1]
sys.argv[1]
