#!/usr/bin/python
import sys
import urllib

url = sys.argv[1]
path = sys.argv[2]
print url
file = urllib.urlopen(url)
print 'Meta Information of The Link'
info = file.info()
print info
urllib.urlretrieve('http://www.google.com',path)
if info.gettype() == 'text/html':
	text = file.read()
	



