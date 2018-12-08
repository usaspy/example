import urllib.request
import urllib.response
import re
import os

class Spider(object):
    data = ''
    def __init__(self):
        self.baseurl = 'http://www.sohu.com'

    def getPageData(self):
        print(self.baseurl)
        request = urllib.request.Request(self.baseurl)
        with urllib.request.urlopen(request) as resp:
            self.data = resp.read().decode('utf-8')
            #print(self.data)

    def getPicNews(self):
        pattern = re.compile('"picUrl":"(.*?)","mediaId":',re.S)
        items = re.findall(pattern,self.data)
        for item in items:
            print(item)
        return items

    def savePic(self,dir,pics):
        for pic in pics:
            with urllib.request.urlopen(pic) as p:
                s = pic.split('/news/')
                f=open('%s%s%s'%(dir,'/',s[1]),'wb')
                f.write(p.read())

def mkdir(dir):
    try:
        isExist = os.path.exists(dir)
        if isExist:
            return True
        else:
            os.makedirs(dir)
            return True
    except:
        return False

def walk_dir(dir,fileinfo,topdown=True):
    for root, dirs, files in os.walk(dir, topdown):
        #if root != dir: break
        for name in files:
            print(name)
            fileinfo.write(os.path.join(root,name) + '\n')
        for name in dirs:
            print('>>>',name)
            fileinfo.write('  ' + os.path.join(root,name) + '\n')


if __name__ == '__main__':
    a = Spider()
    a.getPageData()
    pics = a.getPicNews()
    if mkdir('./pics'):
        a.savePic('./pics',pics)

    dir = input('please input the path:')
    fileinfo = open('list.txt', 'w')
    walk_dir(dir, fileinfo)