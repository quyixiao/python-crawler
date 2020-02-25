from urllib.request import Request, urlopen
from urllib.parse import urlencode

keyword = input('>> 请输入搜索关键字 ')

data = urlencode({
    'q': keyword
})

base_url = 'http://cn.bing.com/search'
url = '{}?{}'.format(base_url, data)

print(url)
# 伪装
ua = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36"
request = Request(url, headers={'User-agent': ua})
response = urlopen(request)
with response:
    with open('/Users/quyixiao/PycharmProjects/python-crawler/bing.html', 'wb') as f:
        f.write(response.read())
print('成功')
