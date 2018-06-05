import threading
import time
import datetime

loops = [4,2]
dtf = '%Y-%m-%d %H:%M:%S'

class Tfunc(object):
    def __init__(self,func,args,name=""):
        self.name= name
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)

def date_time_str(dt):
    return datetime.datetime.strftime(dt,dtf)

def loop(i,sec):
    print('线程号：[',i,'] 〉〉',date_time_str(datetime.datetime.now()),',先休眠',sec,'秒')
    time.sleep(sec)
    print('线程号：[', i, '] 休眠结束，开始执行〉〉', date_time_str(datetime.datetime.now()))

def x():
    print('---所有线程开始执行:',date_time_str(datetime.datetime.now()))
    threads = []
    n_loops = range(len(loops))

    for i in n_loops:
        t = threading.Thread(target=Tfunc(loop,(i,loops[i]),__name__))
        print(x.__name__)
        threads.append(t)
        t.setDaemon(False)

    for i in n_loops:
        threads[i].start()

    print('主线程结束----------------')

if __name__ == '__main__':
    x()
