import urllib.request
import urllib.parse
import urllib.error
import re
# 百度贴吧
# 支持代理
class BDTB(object):
    def __init__(self,url,seeLZ):
        self.url = url
        self.seeLZ = seeLZ

    def getPage(self,pageNum):
        try:
            #http: // tieba.baidu.com / p / 3138733512?see_lz=1&pn=1
            values = {"see_lz": self.seeLZ, "pn": pageNum}
            data = urllib.parse.urlencode(values)
            url = '%s?%s'% (self.url,data)
            print(url)
            headers = {'User-Agent':'Mozilla/5.0'}
            req = urllib.request.Request(url,headers=headers)
            proxy_support = urllib.request.ProxyHandler({'http':'http://127.0.0.1:12345/pac?t=201711140939034656'})
            opener = urllib.request.build_opener(proxy_support,urllib.request.HTTPHandler)
            urllib.request.install_opener(opener)
            with urllib.request.urlopen(req) as resp:
                self.__scanHTML(resp.read().decode('utf-8'))
        except urllib.error.URLError as e:
            if hasattr(e,'reason'):
                print('错误原因:',e.reason)
            if hasattr(e,'errno'):
                print('错误代码:',e.errno)
        finally:
            print("抓取完成")

    def  __scanHTML(self,page):
        #print(page)
        pattern = re.compile(u'<cc>.*?<div.*?>(.*?)</div>.*?</cc>',re.S)
        hfs = re.findall(pattern,page)
        for hf in hfs:
            dr = re.compile(u'<[^>]+>', re.S)
            content = dr.sub('', hf)
            #print(dd)
            dr = re.compile(u'<img.*?src="(.*?)"', re.S)
            pics = re.findall(dr, hf)
           # print(dd)
            dr = re.compile(u'<a.*?href="(.*?)"', re.S)
            urls = re.findall(dr, hf)
            #print(dd)
            self.__write_to_file(content,url=urls)

    def __write_to_file(self,title,pic=[],url=True):

        print(title)
        print(pic)
        print(url)

obj = BDTB('http://tieba.baidu.com/p/3138733512',1)
#obj = BDTB('http://www.minghui.org/',1)  ##哈哈，抓取明慧网

obj.getPage(1)