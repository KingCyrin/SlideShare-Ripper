#!/usr/bin/env python2

import os
import sys
import urllib2
from bs4 import BeautifulSoup

if len(sys.argv) != 2:
	print("Usage: slideShareRipper.py <url>")
	exit()

url = sys.argv[1]
page = urllib2.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

title_dir = str( soup.find("span", class_="j-title-breadcrumb").string ).rstrip()[-38:] + "/"
os.mkdir(title_dir)

slide_share_array = soup.find_all("img", class_="slide_image")
count = 0

for link in slide_share_array:
	count += 1
	_cmd_ = 'curl ' + link.get('data-full') + ' -o "./' + title_dir + 'slide-' + str(count) + '.jpg"'
	os.system( _cmd_ )
	print( _cmd_ )

