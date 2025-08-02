print('Hello Python')

#####################################################################################################################
print("数据类型-----------------------------------------------------------------------------------------------------\n")

a = "aa"
bb = True
b = 1
c = 1.1
d = 9223372036854775807
e = 1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
f = None

print(type(a))
print(type(b))
print(type(bb))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

# 基本数据类型转换
# int(x [,base ])	将x转换为一个整数
# float(x )	将x转换到一个浮点数
# complex(real [,imag ])	创建一个复数
# str(x )	将对象 x 转换为字符串
# repr(x )	将对象 x 转换为表达式字符串
# eval(str )	用来计算在字符串中的有效 Python 表达式,并返回一个对象
# tuple(s )	将序列 s 转换为一个元组
# list(s )	将序列 s 转换为一个列表
# chr(x )	将一个整数转换为一个字符
# unichr(x )	将一个整数转换为 Unicode 字符
# ord(x )	将一个字符转换为它的整数值
# hex(x )	将一个整数转换为一个十六进制字符串
# oct(x )	将一个整数转换为一个八进制字符串


#####################################################################################################################
print("List--------------------------------------------------------------------------------------------------------\n")
l = ['两点水', 'twowter', 'liangdianshui', 123]
print(type(l))
print(l)
# 通过索引来访问列表
print(l[2])
# 通过方括号的形式来截取列表中的数据
print(l[0:2])
# 使用 del 语句来删除列表的的元素
del l[3]
print(l)
print("--------------------------------------------------------------------------------------------------------\n")
# tuple 和 List 非常类似，但是 tuple 一旦初始化就不能修改。 也就是说元组（tuple）是不可变的

list1 = list(range(1, 31))
print(list1)

list1 = [x * x for x in range(1, 11)]
print(list1)

list1 = [x * x for x in range(1, 11) if x % 2 == 0]
print(list1)

list2 = [(x + 1, y + 1) for x in range(3) for y in range(5)]
print(list2)

names = ['laingdianshui', 'twowater', '两点水']
ages = [18, 19, 20]
# 使用zip函数来同时遍历多个可迭代对象
for name, age in zip(names, ages):
    print(name, age)
#####################################################################################################################
print("dict（字典）------------------------------------------------------------------------------------------------\n")
map = {'一点水': '131456780001', '两点水': '131456780002', '三点水': '131456780003', '四点水': '131456780004',
       '五点水': '131456780005'}
print(map['两点水'])
map['两点水'] = 11
print(map['两点水'])
map.clear()
print(map)
del map
print(map)

#####################################################################################################################
print("set（集合）----------------------------------------------------------------------------------------------------\n")
set1 = {1, 2, 3}
print(set1)
set2 = {2, 3, 4}
print(set2)
# 交集 (求两个 set 集合中相同的元素)
set3 = set1 & set2
print('\n交集 set3:')
print(set3)
# 并集 （合并两个 set 集合的元素并去除重复的值）
set4 = set1 | set2
print('\n并集 set4:')
print(set4)
# 差集
set5 = set1 - set2
set6 = set2 - set1
print('\n差集 set5:')
print(set5)

#####################################################################################################################
print("条件---------------------------------------------------------------------------------------------------------\n")
results = 59
if results >= 60:
    print('及格')
else:
    print('不及格')

# 非零数值、非空字符串、非空 list 等，判断为 True，否则为 False。因此也可以这样写：
if results:
    print('Hello Python')

#####################################################################################################################
print("循环---------------------------------------------------------------------------------------------------------\n")
for ele in l:
    print(ele)

for i in range(3):
    print(i)

# for 循环也可以迭代 dict （字典）
dict1 = {'name': '两点水', 'age': '23', 'sex': '男'}
for key in dict1:  # 迭代 dict 中的 key
    print(key, end=' ')

print('\n')

for value in dict1.values():  # 迭代 dict 中的 value
    print(value, end=' ')

for key, value in dict1.items():  # 迭代 dict 中的 value
    print(key + "->" + value)

for i, item in enumerate(dict1.keys()): # i代表索引
    print(i, item)
#####################################################################################################################
print("函数---------------------------------------------------------------------------------------------------------\n")


# 返回一个值
def sum(num1, num2):
    return num1 + num2


print(sum(5, 6))


# 返回两个值
def division(num1, num2):
    a = num1 % num2
    b = (num1 - a) / num2
    return b, a


num1, num2 = division(9, 4)
tuple1 = division(9, 4)

print(num1, num2)


# 不定长参数
def print_user_info(name, age, sex='男', *hobby):
    # 打印用户信息
    print('昵称：{}'.format(name), end=' ')
    print('年龄：{}'.format(age), end=' ')
    print('性别：{}'.format(sex), end=' ')
    print('爱好：{}'.format(hobby))
    return


print_user_info('两点水', 18, '女', '打篮球', '打羽毛球', '跑步')


# 只接受关键字参数
def print_user_info(name, age, sex='男'):
    # 打印用户信息
    print('昵称：{}'.format(name), end=' ')
    print('年龄：{}'.format(age), end=' ')
    print('性别：{}'.format(sex))
    return


print_user_info(name='两点水', age=18, sex='女')

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
