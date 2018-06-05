from bs4 import BeautifulSoup
import urllib.request
import re

url = 'http://116.62.164.196:8080/portal/index'
request = urllib.request.Request(url)
response = urllib.request.urlopen(request,timeout=20)
content = response.read()

soup = BeautifulSoup(content,'html.parser')

print(soup.title.string)
print(soup.title.name)

attrs = soup.div.attrs
print(attrs)
print(soup.div['class'])

print('0000000000000')
for li in soup.body.find_all(class_=['sel','zzz']):
    print('------',li)

print('0000000000000')
for li in soup.body.find_all(string=re.compile('部门'),recursive=False):
    print('------',li)
tag = soup.body.div
print(tag.contents)
print(tag.children)
print(tag.parent.name)
