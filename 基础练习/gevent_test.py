#生产者/消费者队列
import gevent
import random
from gevent.queue import Queue

products = Queue()

def  consumer(name):
    while not products.empty():
        print("%s got product %s"%(name,products.get()))
        gevent.sleep(random.random())
    print("%s Quit"%name)

def producer():
    for i in range(1,10):
        products.put(i)
        print(i)

gevent.joinall([
    gevent.spawn(producer),
    gevent.spawn(consumer,'zhang'),
    gevent.spawn(consumer,'luo'),
    gevent.spawn(consumer,'lulu'),
])
