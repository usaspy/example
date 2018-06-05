from ctypes import cdll
from greenlet import greenlet

libc = cdll.msvcrt
print(libc.time(None))


def  consumer():
    print('6')
    pro.switch(7)


def producer(n=None):
    print(n)
    z = con.switch()
    print(z)



pro = greenlet(producer)
con = greenlet(consumer)
pro.switch(5)
print('---------------------------------')
def  x(n):
    while True:
        print(n)
        n += 1
        if n > 6:
            break
        Y.switch(n)


def y(n):
    i = 0
    while i < n:
        i += 1
        print("生产者〉%d"%i)
        X.switch(i)




Y = greenlet(y)
X = greenlet(x,Y)
Y.switch(16)
print("=============================")