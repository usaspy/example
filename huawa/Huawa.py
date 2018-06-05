import threading
import time
from  datetime import datetime
import urllib.request
import urllib.parse
import urllib.error
from huawa.HuawaException import GetOrdersError
from huawa.CatchOrder import catchOrder
from bs4 import BeautifulSoup
from huawa.db import writeDB
from huawa.db import queryOrder
import re
import os

DATE_TIME_FORMATE_1='%y-%M-%d %H:%M:%S'

class Huawa(object):
    #http://www.huawa.com/order/search?provinceid=24&cityid=382&keyword=&isdefault=0&paystate=1&o=2&price=0&time=0
    #http://www.huawa.com/orders-24-382-1-0-0-2.html?price=0&time=0
    #http://www.huawa.com/orders-24-382-1-0-0-3.html?price=0&time=0
    #orders-24-382-1-0-0-3  24四川-382成都-1-0-0keyword-2页码

     url="http://www.huawa.com/order/search"
     city=''    #382=成都
     province='24' #24=四川
     time=0   # 0=不限 今天 1-3天 4-7天 1周以上
     price=0   # 0=不限 100以下 100-200元 200-300元 300-400元 400以上
     paystate=1  # 1=已付款 0=未付款
     keyword='' #查询关键字

     def __init__(self):
         pass
        #todo 这里加入模拟登陆

     def start(self):
         print('>> 抢单程序启动...',datetime.strftime(datetime.now(),DATE_TIME_FORMATE_1))
         while True:
             #抓取指定页面上的数据
            try:
                orders = self.__getOrdersList()
                writeDB(len(orders))
            #    for id,order in orders.items(): #有订单，开始抢单
            #        #print(id,order)
            #        t = threading.Thread(target=catchOrder,args=(id,order),daemon=True)
            #        t.start()
            except GetOrdersError as e:
                print(e)
            time.sleep(20)

     def __getOrdersList(self):
         values = {'provinceid': self.province ,'cityid': self.city ,'keyword': self.keyword ,'isdefault': 0 , 'paystate': self.paystate , 'price': self.price , 'time': self.time}
         params = urllib.parse.urlencode(values)
         url = "%s?%s"% (self.url,params)
         #print(url)
         headers = {'Accept':'*/*',
                    'Referer':'http://www.huawa.com/orders',
                    'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
                    'X-Requested-With':'XMLHttpRequest'
                    }
         req = urllib.request.Request(url,headers=headers)
         try:
            with urllib.request.urlopen(req) as resp:
                content = resp.read()
                #print(content.decode('utf-8'))
                orders = self.__soup2orders(content)
                print('抓单完成,找到%s个可以抢的订单'% len(orders))
                return orders
         except urllib.error.URLError as e:
             if hasattr(e, 'reason'):
                 print('错误原因:', e.reason)
             raise GetOrdersError('获取订单失败')

     def __soup2orders(self,content):
         orders = {}
         try:
            soup = BeautifulSoup(content, 'html.parser')
            for html in soup.ul.find_all('li',class_='listuili', recursive=False):
                status = html.find('a', class_='baojia')
                if status.string == '我要接单':
                    #print('------------',html)
                    order = {}
                    order['address'] = html.find('a',attrs={'href':re.compile('http://www.huawa.com/order/'),'style':'color:#000; font-size:22px; font-weight:600;'}).get_text().strip()
                    order['price'] = html.find('font',attrs={'color':'#666','style':'font-size:22px; color:red'}).get_text().lstrip('￥').rstrip('元')
                    order['send_time'] = html.find('p', attrs={'class': 'delivery_date'}).get_text().strip()
                    order['description'] = html.find('p', attrs={'class': 'goods_material'}).get_text().strip()
                    order['url'] = html.find('a',attrs={'href':re.compile('http://www.huawa.com/order/'),'style':'color:#000; font-size:22px; font-weight:600;'}).get('href')

                    id = os.path.basename(order['url'])
                    orders[id] = order
         except Exception as e:
             print("bs4转换失败")
         finally:
             return orders

if __name__ == '__main__':
    Huawa().start()