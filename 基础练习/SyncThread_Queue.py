import threading
import time
import datetime

class RWThread(threading.Thread):
    def __init__(self,threadID,rw_type,nums):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.rw_type = rw_type
        self.nums = nums

    def run(self):
        threadLock.acquire()
        while self.nums > 0:
            print('线程[',self.threadID,']开始打印...',self.nums)
            time.sleep(1)
            self.nums -= 1
        threadLock.release()

def main():
    thread_R = RWThread(1,"R",20)
    thread_W = RWThread(2,"W",10)
    thread_X = RWThread(3,"X",5)
    thread_R.setDaemon(False)
    thread_W.setDaemon(False)
    thread_X.setDaemon(False)
    thread_R.start()
    thread_W.start()
    thread_X.start()


if __name__ == '__main__':
    threadLock = threading.Lock()
    threads = []
    main()
