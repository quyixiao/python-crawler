# 爬虫，应该称为网络爬虫，也叫网页蜘蛛，网络机器人，网络蚂蚁，
# 搜索引擎，就是网络爬虫的应用者
# 为什么到了今天，反而这个词汇被频繁的提起呢？有搜索引擎不就够了吗？
# 实际上，大数据时代的到来，所有的企业都希望通过海量的数据
# 觉就是搜索引擎，无差别的收集数据，存储，提取关键字，构建索引库，给用户提供搜索接口
# 爬取一般的流程
# 初始化一批URL,将这些URL放入到待爬取队列
# 从队列取出这些URL,通过DNS解析DNSIP，对IP对应的站点下载HTML 页面，保存到本地服务器中，爬取完成URL放到已经爬取的队列
# 分析这些网页内容，找出网页里面的其他关心的URL链接，继续执行第二步，直到爬取条件结束
# 搜索引擎如何获取一个新网站的URL
# 新的网站的主动提交给搜索引擎
# 通过其它的网站页面中设置了外链
# 搜索引擎和DNS服务器合作，获取新收录的网站
# 聚集爬虫
# 有针对性的编写特定领域的数据爬取程序，针对某些类别的数据采集爬虫，面向主题的爬虫
# Robots协义
# 指定一个robots.txt文件，告诉爬虫引擎什么时候可以爬取
# 其它爬虫，不允许爬取
# 这是一个君子协定，爬亦有道
# 这个协义为了搜索引擎更加效率搜索自己的内容，提供了Sitemap这样的文件
# 这个文件禁止抓取的往往以是可以我们感兴趣的内容，它揉面泄露了这些地址
# urllib包
# urllib是标准库，它是一个工具包的模块，包含下面的模块来处理url
# urllib.request 用于打开和读写url
# urllib.error 包含了由于urllib.request引起异常
# urllib.parse 用于解析url
# url.robotparser分析robots.txt文件
# Python2中提供了urllib和urllib2，urllib提供了较为底层的接口，urllib2和urllib进行了进一步的封装，Python3中将urllib合并到了
# urllib2中，并只提供了标准库urllib包
# urllib.request模块
# 模块定义了基本和摘要式的身份证，重定向，cookies等应用中打开Url(主要HTTP)的函数和类
# urlopen方法
# urlopen(url,data=None)
# url是链接地址字符串，或者请求对象
# data提交数据，如果data为None发起的请求，否则发起了Post请求，见urllib.request.Request#get_method返回http.client.HTTPResponse
# 类的响应的对象，这是一个类文件对象
#


from urllib.request import urlopen

# 打开一个url返回一个响应对象，类文件对象
# 下面的链接访问后会有跳转
response = urlopen('http://www.bing.com')  # GET方法 print(response.closed)
with response:
    print(1, type(response))  # http.client.HTTPResponse 类文件对象
    print(2, response.status, response.reason) # 状态
    print(3, response.geturl())  # 返回真正的URL
    print(4, response.info())  # headers
    print(5, response.read())  # 读取返回的内容 print(response.closed)