# -*- coding: utf-8 -*-
import scrapy


class DbbookSpider(scrapy.Spider):
    name = 'dbbook'  # 爬虫名
    allowed_domains = ['douban.com']  # 爬虫爬取范围
    url = 'https://book.douban.com/tag/%E7%BC%96%E7%A8%8B?start=0&type=T'
    start_urls = [url]  # 起始URL

    # 下载器获取了WEB Server的response就行了，parse就是解析响应的内容
    def parse(self, response):
        print(type(response))  # scrapy.http.response.html.HtmlResponse print('-'*30)
        print(response)
