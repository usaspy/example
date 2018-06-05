import threading
import time
from  datetime import datetime
import urllib.request
import urllib.parse
import urllib.error
from huawa.HuawaException import GetOrdersError
from bs4 import BeautifulSoup
import re
import os


def test():

    url = "http://www.huawa.com/index.php?c=member_placeorder&a=index"
    # print(url)

    headers = {#'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               #'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
              # 'Accept-Language':'zh-CN,zh;q=0.8',
              # 'Connection':'keep-alive',
               #'Host':'www.huawa.com',
               #'Upgrade-Insecure-Requests':'1',
               #'Cookie':'tencentSig=706910208; PHPSESSID=nhuoho21vfdk35udgtd6en9iq6; 53kf_1827303_keyword=http://www.huawa.com/login?ref_url=http%3A%2F%2Fwww.huawa.com%2F; 4047_alert_app_down_new_36671=1; _qddamta_4006780020=3-0; _qddaz=QD.jm02qa.8isi45.ja7mn7b6; _qdda=3-1.1; _qddab=3-c5o8gt.jac5qnl1; Hm_lvt_4175f2a72ac6f0c111ec482d34734339=1511159163,1511246067,1511336921,1511422176; Hm_lpvt_4175f2a72ac6f0c111ec482d34734339=1511426140; 4047_seccode52f9dc26=KmRGLgch_hjV2fD8BTWXcARXyhSRF6ZG3YCPWaINTLoiUP2J4XN; 4047_login_member_info=gYYYFocZ5TrI6Cn6YpioIFqw26JUroAi7QtvbN54uGwfKMB2ID9inMHpsh-SaMB2ID5gYs23fe0euZ4xLUpvbY2qAVBUbsoT9luONuFVCbBOrx5o4f6inNB1f-pffNlzrQpub02qAVBSbgAi4f4gYMJost8ULVG2sf2s7BBks26UrI5o3k1tb521gSmheBo0rMtcoxHqsN4UqM3mIv8h4oJocd5SaMB2ID5gIs23fe0euZ4xMstvHMP48x3UqMooMnCiIs24PO6i_h127rqi8QOo8RBOuc3m436sYcJp8t9fLNqzYr-toQMoMZ7Trhqzokrs4F5ks26UrI2o3kps7RD5fC7d-pqi4IxioEP48x4Srsoyrorv8ZC5OG1ee5ri4I7ioEOkrRCi7s3mIDqsbR33Ae1jNB20bY2tXMP48x3UqMooMnCgYEOkvOqe-B718snwcI2qAVBSLsoi4I7ioQOkwewfKMB2ID8inMMoch7OrxD'
                'Cookie': 'PHPSESSID=ti1u15jklfhlq13sp2hnu67jm5;'
               }
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            content = resp.read().decode('utf-8')
            print(content)
    except urllib.error.URLError as e:
        if hasattr(e, 'reason'):
            print('错误原因:', e.reason)

test()