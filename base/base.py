print('Hello Python')

# 数据类型
a = "aa"
bb = True
b = 1
c = 1.1
d = 9223372036854775807
e = 92233720368547758071111
f = None

print("---------------------------------------------------------------------------------------------------------")
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


# list数据类型
print(
    "---------------------------------------------------------------------------------------------------------")

list = ['两点水', 'twowter', 'liangdianshui', 123]
print(type(list))
print(list)
# 通过索引来访问列表
print(list[2])
# 通过方括号的形式来截取列表中的数据
print(list[0:2])
# 使用 del 语句来删除列表的的元素
del list[3]
print(list)

# dict（字典）
print("---------------------------------------------------------------------------------------------------------")
map = {'一点水': '131456780001', '两点水': '131456780002', '三点水': '131456780003', '四点水': '131456780004',
       '五点水': '131456780005'}
print(map['两点水'])
map['两点水'] = 11
print(map['两点水'])
map.clear()
print(map)
del map
print(map)

# set（集合）
print("---------------------------------------------------------------------------------------------------------")
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

# 条件
print("---------------------------------------------------------------------------------------------------------")

results = 59
if results >= 60:
    print('及格')
else:
    print('不及格')

# 非零数值、非空字符串、非空 list 等，判断为 True，否则为 False。因此也可以这样写：
if results:
    print('Hello Python')

# 循环
print("---------------------------------------------------------------------------------------------------------")

for ele in list:
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
