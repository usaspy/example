import types

class Bird(object):
    def fly(self):
        print("all bird can fly! ")

    def __str__(self):
        print("hahha哈哈")
    __repr__ = __str__



class Parrot(Bird):
    def eat(self):
        print("Parrot eat a lot of little rice")

    def fly(self):
        print('Parrot fly is  very highest!')

p = Parrot()
s = Bird()
p.fly()
p.eat()
s.fly()

print('p是鹦鹉额？',isinstance(p,Parrot))
print('p是额？',isinstance(p,Bird))

def aa():
    pass


if type(isinstance) == types.BuiltinFunctionType:
    print(True)
else:
    print(False)
print("-------------------------------")
print(isinstance([1,2],(tuple,list)))
print(dir({1:1}))

