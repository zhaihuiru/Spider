import urllib.request
import urllib.parse  # 解析器，将中英文键值对解析
from wsgiref import headers

# 获取一个get请求
# response = urllib.request.urlopen("http://www.baidu.com")  #打开网页，并将数据返回
# print(response.read().decode("utf-8"))  #对获取的网页，用utf-8解码

# 获取一个post请求
# data = bytes(urllib.parse.urlencode({'hello': 'world'}), 'utf-8')   #模拟浏览器发出请求
# response = urllib.request.urlopen("https://httpbin.org/post", data = data)
# print(response.read().decode('utf-8'))

#超时处理
# try:
#     response = urllib.request.urlopen("https://httpbin.org/get", timeout=5)
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("time out")

# response = urllib.request.urlopen("https://httpbin.org/get", timeout=5)
# print(response.status)  #反馈响应状态，状态码（200、404）

# response = urllib.request.urlopen("https://douban.com", timeout=5)
# print(response.status)  #状态码（418）被发现是爬虫

# response = urllib.request.urlopen("https://www.baidu.com", timeout=5)
# print(response.getheaders()) #获得所以标头

# url = "https://httpbin.org/post"
# headers = {
#     "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36 Edg/137.0.0.0"
# }
# data = bytes(urllib.parse.urlencode({"name":"Zzzhr"}), "utf-8")
# req = urllib.request.Request(url=url,data=data,headers=headers,method='POST')
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))

url = "https://www.douban.com"
headers = {
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36 Edg/137.0.0.0"
}
req = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))