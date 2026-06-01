import time
import logging


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


print(
    "---------------------------------------------------------------------------------------------------------------------- \n"
)


def decorator(func):
    def punch(*args, **kwargs):
        print(time.strftime("%Y-%m-%d", time.localtime(time.time())))
        func(*args, **kwargs)

    return punch


@decorator
def punch(name, department):
    print(f"昵称：{name}  部门：{department} 上班打卡成功")


punch("两点水", "做鸭事业部")

# logging 默认的级别是 WARNING，比它低的 INFO 和 DEBUG 直接被丢掉了。
# filename：写到文件，比如 'app.log'
# filemode：写文件的模式，'a' 追加（默认），'w' 覆盖
# encoding：文件编码，强烈建议加 encoding='utf-8'，不然 Windows 上中文很容易挂
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logging.info("两点水开始打卡了")