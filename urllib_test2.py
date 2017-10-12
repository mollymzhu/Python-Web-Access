# -*- coding: utf-8 -*-
"""
Created on Thu Sep 07 09:45:46 2017

@author: laa037
"""

# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib2
from urlparse import urlparse
# urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
#count=4
#position=3
url = raw_input('Enter Url:')
count = input('Enter count:')
position = input('Enter position:')

print("retrieving ",url)

i=1
html = urllib2.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
while i<=count:
    tags = soup('a')
    url = tags[position-1].get('href', None)
    print("retrieving ",url)
    html = urllib2.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    i = i + 1
    