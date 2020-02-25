from urllib.request import Request, urlopen
import random
import ssl

# 打开一个url返回一个Request请求对象
ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://movie.douban.com/'  # 注意尾部的斜杠一定要有 url = 'http://www.bing.com/'
ua_list = [
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome / 57.0.2987.133 Safari / 537.36",    # chrome
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN) AppleWebKit/537.36 (KHTML, like Gecko)Version / 5.0.1 Safari / 537.36",    # safafi
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0",  # Firefox
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"  # IE
]
ua = random.choice(ua_list)  # pick one
# ua需要加到请求头中
request = Request(url)
request.add_header('User-Agent', random.choice(ua_list))
print(type(request))
response = urlopen(request, timeout=20)  # request对象或者url都可以
print(type(response))
with response:
    print(1, response.status, response.getcode(), response.reason)  # 状态，getcode本质上就是返回status
    print(2, response.geturl())  # 返回数据的url。如果重定向，这个url和原始url不一样 # 例如原始url是http://www.bing.com/，返回http://cn.bing.com/
    print(3, response.info())  # 返回响应头headers
    print(4, response.read())  # 读取返回的内容



print(5, request.get_header('User-agent'))
print(6, 'user-agent'.capitalize())
