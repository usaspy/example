from multiprocessing import Process
import os
import time

def exet(name):
    for i in range(10000000):
       i = i+1
    print("run child process %s %i "% (os.getpid(),i))

if __name__=='__main__':
    print("父进程号是%s"% os.getpid())
    processes = []
    for i in range(4):
        p = Process(target=exet, args=('x',))
        p.start()
        print("进程%d就绪,随时可能执行"% i)
        processes.append(p)
        print(processes)

    for p in processes:
        p.join()

    print('结束')