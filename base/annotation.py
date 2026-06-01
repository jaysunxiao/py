import time


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()


print("---------------------------------------------------------------------------------------------------------------------- \n")

def decorator(func):
    def punch(*args, **kwargs):
        print(time.strftime('%Y-%m-%d', time.localtime(time.time())))
        func(*args, **kwargs)

    return punch


@decorator
def punch(name, department):
    print(f'昵称：{name}  部门：{department} 上班打卡成功')



punch('两点水', '做鸭事业部')
