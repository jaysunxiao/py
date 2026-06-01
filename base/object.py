from dataclasses import dataclass
#####################################################################################################################

print("类定义-----------------------------------------------------------------------------------------------------\n")


class ClassA:
    var1 = 100
    var2 = 0.01
    var3 = '两点水'

    def __init__(self):
        print("init method")
        pass

    # static类方法
    @classmethod
    def fun1(self):
        print('我是 fun1')


ClassA.fun1()
classAObject = ClassA()



@dataclass
class User:
    name: str
    age: int
    sex: str = '男'


u = User('两点水', 18, '女')
print(u)