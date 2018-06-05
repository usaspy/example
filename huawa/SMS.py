# -*- coding: utf-8 -*-
import huawa.alidayu

# 其中appkey和secret是必须的参数
# url可选，默认为沙箱的URL，正式应用请传入 https://eco.taobao.com/router/rest
# partner_id为可选，其值为下载的TOP SDK中的top/api/base.py里的SYSTEM_GENERATE_VERSION
appkey = 'LTAIOzRCcKlF0y6B'
secret= '3uvJ1ECrUJy8lpNrcg9uCnnrQzNHLe'
url = "http://gw.api.taobao.com/router/rest"
partner_id = None
req=huawa.alidayu.AlibabaAliqinFcSmsNumSendRequest(appkey, secret,url)

req.extend="123456"
req.sms_type="normal"
req.sms_free_sign_name="必云科技"
req.sms_param="{\"name\":\"2\"}"
req.rec_num="18180620221"
req.sms_template_code="SMS_115260237"
try:
    resp= req.getResponse()
    print(resp)
except (Exception) as e:
    print(e)