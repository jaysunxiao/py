#####################################################################################################################
from typing import Callable

print(
    "函数---------------------------------------------------------------------------------------------------------\n"
)


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
def print_user_info(name: str, age: str, sex="男", *hobby) -> str | None:
    # 打印用户信息
    print("昵称：{}".format(name), end=" ")
    print("年龄：{}".format(age), end=" ")
    print("性别：{}".format(sex), end=" ")
    print("爱好：{}".format(hobby))
    return


print_user_info("两点水", 18, "女", "打篮球", "打羽毛球", "跑步")


# 只接受关键字参数
# 将强制关键字参数放到某个*参数或者单个*后面就能达到这种效
def print_user_info(name, *, age, sex="男"):
    # 打印用户信息
    print("昵称：{}".format(name), end=" ")
    print("年龄：{}".format(age), end=" ")
    print("性别：{}".format(sex))
    return


print_user_info("两点水", age=18, sex="女")


# type function
def get_users() -> list[str]:
    return ["一点水", "两点水", "三点水"]


def get_phones() -> dict[str, str]:
    return {"两点水": "131456780002"}


print(get_users())
print(get_phones())


# 匿名函数
nums: list[int] = [3, 2, 1]
nums.sort(key=lambda it: it)
print(nums)
result = map(lambda x: x * 2, nums)
result1 = filter(lambda x: x > 0, nums)
result2 = filter(lambda x: x > 0, nums)
