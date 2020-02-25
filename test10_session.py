# 直接使用Session import requests
import requests

ua = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36"
urls = ['https://www.baidu.com/s?wd=magedu', 'https://www.baidu.com/s?wd=magedu']
session = requests.Session()
with session:
    for url in urls:
        response = session.get(url, headers={'User-Agent': ua})
        with response:
            print(type(response))
            print(response.url)
            print(response.status_code)
            print(response.request.headers)  # 请求头 print(response.cookies) # 响应的cookie print(response.text[:20]) # HTML的内容
