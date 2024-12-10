import requests

# 发送请求
response = requests.get('https://www.baidu.com')

# 返回网页内容
print(response.text)