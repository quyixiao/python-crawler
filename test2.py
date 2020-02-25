from urllib import parse

u = parse.urlencode({
    'url': 'http://www.magedu.com/python',
    'p_url': 'http://www.magedu.com/python?id=1&name=张三',
})
print(u)
# 运行结果如下 p_url=http%3A%2F%2Fwww.magedu.com%2Fpython%3Fid%3D1%26name%3D%E5%BC%A0%E4%B8%89&url=http%3A%2F%2 Fwww.magedu.com%2Fpython
