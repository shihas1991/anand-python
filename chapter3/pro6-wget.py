#Write a program wget.py to download a given URL. The program should accept a URL as argument, download it and save it with the basename of the URL. If the URL ends with a /, consider the basename as index.html.
import urllib
import sys
import re
def wget(url):
	x=re.search(r'(\w)+.(\w)+$',sys.argv[1])
	if sys.argv[1][-1]=='/':
		urllib.urlretrieve(sys.argv[1],'index.html')
	else:
		 urllib.urlretrieve(sys.argv[1],x.group())
wget(sys.argv[1])

