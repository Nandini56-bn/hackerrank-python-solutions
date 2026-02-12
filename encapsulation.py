'''class demo():
    __a=4 #private using double underscores
    _b=5 #protected using single underscore
    print(__a)
    print(_b)'''

'''class demo():
    def __init__(self,a,b):
        self.__a=a
        self._b=b
class demo2(demo):
    def output(self):
        print(self._demo__a + self._b)
t=demo2(4,8)
t.output()'''

'''class demo(): # this is public
    def __init__(self):
        self.a=5
obj=demo()
print(obj.a)'''

'''class demo(): # this is protected 
    def __init__(self):
        self._a=8
class demo3(demo):
    def output(self):
        print(self._a)
obj=demo3()
obj.output()
print(obj._a)'''

class demo(): # this is private
    def __init__(self,a):
        self.__a=a
class demo2(demo):
    def output(self):
        print(self._demo__a)
obj=demo2(3)
obj.output()

