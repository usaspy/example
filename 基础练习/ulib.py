import urllib.request
from urllib import request
import sys
from sys import stdin

def getWebData():
    f = request.urlopen('http://www.baidu.com')

    data = f.read()
    print(f.reason)
    with open('d:/a.txt','wb') as file:
        file.write(data)

    print(data.decode('utf-8'))

getWebData()