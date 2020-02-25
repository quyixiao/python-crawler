from urllib.request import Request, urlopen
import ssl  # 导入ssl模块

# request = Request('http://www.12306.cn/mormhweb/') # 可以访问
# request = Request('https://www.baidu.com/') # 可以访问
request = Request('https://www.12306.cn/mormhweb/')  # 报SSL认证异常
request.add_header(
    'User-agent',
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36"
)
# 忽略不信任的证书
context = ssl._create_unverified_context()
res = urlopen(request, context=context)
# ssl.CertificateError: hostname 'www.12306.cn' doesn't match either of ...... with res:
print(res._method)
print(res.geturl())
print(res.read().decode())
