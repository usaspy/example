import time
import sys
import datetime
import calendar

print(time.localtime())

t = (2016,8,11,2,34,28,6,48,0)
print(time.mktime(t))
print(time.asctime(time.localtime()))

print("start:%s"% time.ctime())
time.sleep(2)
print("start:%s"% time.ctime())


dt = datetime.datetime.now()
print('time is:',dt.strftime('%Y-%m-%d %H:%M:%S'))
print(calendar.calendar(w=2,l=1,c=6))