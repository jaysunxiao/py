from dataclasses import dataclass
#####################################################################################################################

print("类定义-----------------------------------------------------------------------------------------------------\n")


class ClassA(object):
    VERSION = "static filed"

    name: str
    age: int

    def __init__(self, name: str = "张三", age: int = 100):
        print("init method")
        self.name = name
        self.age = age
        pass

    # static类方法
    @classmethod
    def fun1(cls):
        print('static filed VERSION:[{}]'.format(cls.VERSION))

    def info(self):
        print("info:{} - {}".format(self.name, self.age))


ClassA.fun1()
classAObject = ClassA("李四", 200)
classAObject.info()



@dataclass
class User(object):
    name: str
    age: int
    sex: str = '男'
    pass


u = User('两点水', 18, '女')
print(u)

@dataclass
class User1(User):
    weight: float = 11.1
    pass

u1 = User1('两点水', 18, '女', 22.2)
print(u1)
print(isinstance(u1, User))

# 一个类创建的时候，就会包含一些方法，主要有以下方法：
#
# 类的专有方法：
#
# 方法	说明
# __init__	构造函数，在生成对象时调用
# __del__	析构函数，释放对象时使用
# __repr__	打印，转换
# __setitem__	按照索引赋值
# __getitem__	按照索引获取值
# __len__	获得长度
# __cmp__	比较运算
# __call__	函数调用
# __add__	加运算
# __sub__	减运算
# __mul__	乘运算
# __div__	除运算
# __mod__	求余运算
# __pow__	乘方