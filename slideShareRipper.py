#!/usr/bin/env python2

import os
import sys
import urllib2
from bs4 import BeautifulSoup

if sys.argc != 2:
	print("Usage : slideShareRipper.py <url>")
	exit()

slide_share = sys.argv[1]
page = urllib2.urlopen(slide_share)
soup = BeautifulSoup(page, 'html.parser')
slide_share_array = soup.find_all("img", class_="slide_image")
count = 0

for link in slide_share_array:
	count += 1
	_cmd_ = "curl " + link.get("data-full") + " -o \"slide-number-" + str(count) + "\""
	os.system( _cmd_ )

	print( link.get("data-full") )
	print( _cmd_ )
