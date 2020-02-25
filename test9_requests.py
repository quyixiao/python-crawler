import urllib3

import urllib3

import requests

ua = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36"
url = 'https://movie.douban.com/'
response = requests.request('GET', url, headers={'User-Agent': ua})
with response:
    print(type(response))
    print(response.url)
    print(response.status_code)
    print(response.request.headers)  # 请求头 print(response.headers) # 响应头 print(response.text[:200]) # HTML的内容
    with open('/Users/quyixiao/PycharmProjects/python-crawler/movie.html', 'w', encoding='utf-8') as f:
        f.write(response.text)  # 保存文件，以后备用