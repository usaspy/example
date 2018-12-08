from multiprocessing import Pool
import time

def x(args):
    time.sleep(4)
    print("args=%d"% args)
    return args

if __name__ == "__main__":
    p = Pool(3)
    res = []
    for i in range(10):
        r= p.apply_async(func=x,args=(i,))
        res.append(r)
    print("hello-------------------------------------")
    p.close()
    p.join()
    print("over-")
    print(res)
    for r in res:
        print(r.get())
