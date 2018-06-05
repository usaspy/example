# -*- coding: utf-8 -*-
from aliyunsdkdysmsapi.request.v20170525 import SendSmsRequest
from aliyunsdkdysmsapi.request.v20170525 import QuerySendDetailsRequest
from aliyunsdkcore.client import AcsClient
import uuid

REGION = "cn-hangzhou"
ACCESS_KEY_ID = "LTAIxxmj6Zm4EE1s"
ACCESS_KEY_SECRET = "omCebY8aFRAgCUB9CvXOuUKN3roPMS"

acs_client = AcsClient(ACCESS_KEY_ID, ACCESS_KEY_SECRET, REGION)

def send_sms(businessId,phoneNumber,signName,templateCode,templateParam=None):
    smsRequest = SendSmsRequest.SendSmsRequest()
    smsRequest.set_TemplateCode(templateCode)

    if templateParam != None:
        smsRequest.set_TemplateParam(templateParam)

    smsRequest.set_OutId(businessId)

    smsRequest.set_SignName(signName)

    smsRequest.set_PhoneNumbers(phoneNumber)

    #发送短消息
    smsResponse = acs_client.do_action_with_exception(smsRequest)
    return smsResponse


if __name__ == '__main__':
    uuid = uuid.uuid1()
    print(uuid)
    params = "{\"name\":\"2\"}"
    print(send_sms(uuid,18180620221,'必云科技','SMS_115260237',params))