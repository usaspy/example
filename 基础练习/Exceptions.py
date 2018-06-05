class Cals(object):
    def chufa(self,x,y):
        try:
            a = x/y
            print(a)
            raise MyError()
            return
        except (NameError,TypeError,MyError) as e:
            print(e)
        except Exception:
            raise Exception
        finally:
            print("hellll-------------")

class MyError(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return "this is custom Error"



u = Cals()
u.chufa(2,4)