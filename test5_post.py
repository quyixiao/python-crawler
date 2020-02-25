from urllib.request import Request, urlopen
from urllib.parse import urlencode
import simplejson

request = Request('http://httpbin.org/post')
request.add_header(
    'User-agent',
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36"
)
data = urlencode({'name': '张三,@=/&*', 'age': '6'})

print(data)
# res = urlopen(request, data='name=张三,@=/&*,&age=6'.encode()) # 不做url编码有风险
res = urlopen(request, data=data.encode())  # POST方法，Form提交数据
with res:
    text = res.read()
    d = simplejson.loads(text)
    print(d)
    print(type(d))
