# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 11:23:51 2017

@author: laa037
"""


import re
filename = 'regex_sum_13958.txt'
data=open(filename,'r').readlines()
output = []
for line in data:
    num = re.findall('[0-9]+',line)
    if num: 
        #print num
        for x in num:
            output.append(int(x))
    #print line
#print output
print sum(output)