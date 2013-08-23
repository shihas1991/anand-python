#Write a program antihtml.py that takes a URL as argument, downloads the html from web and print it after stripping html tags.
import urllib
import sys
import re
def antihtml(url):
	urllib.urlretrieve(sys.argv[1],'web')
	f=open('web').read()
	x=re.findall(r'>[^<]+<',f)
	for i in x:
		print i[1:-1]
antihtml(sys.argv[1])	
