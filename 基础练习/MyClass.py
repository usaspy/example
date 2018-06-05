class ClassMe(object):
    i=123

    def __init__(self,name):
        self.__aaa = name
        print("这是初始化。。。",name)

    def f(self):
        return "hellow world "

    def get_score(self):
        return self.__aaa

    def set_score(self,name):
        if 0<=name<=100:
            self.__aaa = name
        else:
            print('name必须在0-100之间')

    def __poo(self):
        print('这是私有的法国你发',ClassMe.i)

    def poo(self):
        self.__poo()


c = ClassMe('zhanghong')
print(c.i)
print(c.f())
c.set_score(-90)
c.i=44
print(c.f())
print(c.i)
print(c.get_score())
c.poo()


