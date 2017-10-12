

#import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import urllib2
from urlparse import urlparse

url = 'http://py4e-data.dr-chuck.net/comments_13962.xml'

uh = urllib2.urlopen(url)
data = uh.read()
    

tree = ET.fromstring(data)

comments = tree.find('comments').findall('comment')

print(len(comments))
output=[]

for comment in comments:
    count=comment.find('count').text
    output.append(int(count))
    
print(sum(output))
