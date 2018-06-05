import urllib.request
import urllib.response
from urllib.parse import urlencode

values = {"username":"1016903103@qq.com","password":"XXXX"}
data = urlencode(values)
print(data)
url = "http://quote.eastmoney.com/stocklist.html"
request = urllib.request.Request('%s?%s'%(url,data))
#request = urllib.request.Request(url,data.encode('utf-8'))
response = urllib.request.urlopen(request)
print(response.read().decode('gbk'))