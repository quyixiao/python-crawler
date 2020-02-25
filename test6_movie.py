import ssl
from urllib.request import Request, urlopen
from urllib.parse import urlencode

# 打开一个url返回一个Request请求对象
import simplejson

ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://movie.douban.com/j/search_subjects'
request = Request(url)
request.add_header(
    'User-agent',
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36"
)
data = urlencode({
    'type': 'movie',
    'tag': '热门',
    'page_limit': 10,
    'page_start': 10
})

# POST方法
res = urlopen(request, data=data.encode())

with res:
    print(res._method)
    text = res.read().decode();
    d = simplejson.loads(text)
    print(d)
# GET方法
# with urlopen('{}?{}'.format(url, data)) as res:
#     print(res._method)
#     print(res.read().decode())
