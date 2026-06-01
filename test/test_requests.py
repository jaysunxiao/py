import requests


def test_requests():
    # 发送请求
    response = requests.get("https://www.baidu.com")
    print(response.status_code)  # 获取响应状态码
    print(response.headers)  # 获取响应头
    print(response.content)  # 获取响应内容



