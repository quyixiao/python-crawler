# -*- coding: utf-8 -*-
import scrapy

from scrapy.http.response.html import HtmlResponse

from book.items import BookItem


class DbbookSpider(scrapy.Spider):
    name = 'dbbook'  # 爬虫名
    allowed_domains = ['douban.com']  # 爬虫爬取范围
    url = 'https://book.douban.com/tag/%E7%BC%96%E7%A8%8B?start=0&type=T'
    start_urls = [url]  # 起始URL

    # spider上自定义配置信息
    custom_settings = {
        'filename': 'books.json'
    }


    # 下载器获取了WEB Server的response就行了，parse就是解析响应的内容,这个是如何解析HMTL内容
    # 下载器获取了WEB Server的response就行了，parse就是解析响应的内容
    def parse(self, response: HtmlResponse):
        items = []
        # xpath解析
        subjects = response.xpath('//li[@class="subject-item"]')
        for subject in subjects:
            title = subject.xpath('.//h2/a/text()').extract()
            rate = subject.xpath('.//span[@class="rating_nums"]/text()').extract_first()
            item = BookItem()
            item['title'] = title[0].strip()
            item['rate'] = rate.strip()

            #items.append(item)

            yield item

