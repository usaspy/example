import queue
import threading
import time

class ThreadPool(object):  #创建线程池类

    def __init__(self, max_num=20):  #创建一个最大长度为20的队列
        self.queue = queue.Queue(max_num)  #创建一个队列
        for i in range(max_num):  #循环把线程对象加入到队列中
            self.queue.put(threading.Thread)  #把线程的类名放进去，执行完这个Queue

    def get_thread(self):  #定义方法从队列里获取线程
        return self.queue.get()  #在队列中获取值

    def add_thread(self):  #线程执行完任务后，在队列里添加线程
        self.queue.put(threading.Thread)




def func(pool,a1):
    time.sleep(1)
    print(a1)
    pool.add_thread()  #线程执行完任务后，队列里再加一个线程

p = ThreadPool(10)  #执行init方法；  一次最多执行10个线程

for i in range(100):
    thread = p.get_thread()  #线程池10个线程，每一次循环拿走一个拿到类名，没有就等待
    t = thread(target=func, args=(p, i,))  #创建线程；  线程执行func函数的这个任务；args是给函数传入参数
    t.start()  #激活线程