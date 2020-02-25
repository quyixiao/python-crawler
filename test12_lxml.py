from lxml import etree

from lxml import etree
import requests

url = 'https://movie.douban.com/'
ua = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36"

with requests.get(url, headers={'User-agent': ua}) as response:
    content = response.text  # HTML内容
    html = etree.HTML(content)  # 分析HTML，返回DOM根节点
    titles = html.xpath("//div[@class='billboard-bd']//tr/td/a/text()")  # 返回文本列表
    for t in titles: # 豆瓣电影之 本周口碑榜
        print(t)
