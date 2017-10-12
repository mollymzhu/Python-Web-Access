# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 16:35:00 2017

@author: LAA037
"""

import json
from urllib2 import urlopen
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = 'http://py4e-data.dr-chuck.net/comments_13963.json'
data =urlopen(url, context=ctx).read()

info = json.loads(data)
print('User count:', len(info))

comments = info['comments']
output=[]
#print(comments)

for item in comments:
    print('Name', item['name'])
    print('Count', item['count'])
    output.append(int(item['count']))
    
print sum(output)
