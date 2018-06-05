import uuid as uuid

from huawa.SendSMS import send_sms
import uuid

SEESIONID='ti1u15jklfhlq13sp2hnu67jm5'

def  catchOrder(id,order):
    print(order)
    uid = uuid.uuid1()
    print(uuid)
    pass
    params = "{\"name\":\"2\"}"
    print(send_sms(uuid, 18180620221, '必云科技', 'SMS_115260237', params))
    sms = send_sms()
    pass