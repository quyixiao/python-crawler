# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json


class BookPipeline(object):
    # spider实例创建时 可选 调用一次
    def __init__(self):  # 全局设置
        print('~~~~~~~~~~ init ~~~~~~~~~~~~')

    def open_spider(self, spider):  # 当某spider开启时调用
        print('{} ~~~~~~~~~~~~~~~~~~~~'.format(spider))
        print(spider.settings.get('filename'))

        self.file = open(spider.settings['filename'], 'w', encoding='utf-8')
        self.file.write('[\n')

    # item爬取的一个个数据
    # spider表示item的爬取者
    # 每一个item处理都调用
    # 返回一个Item对象，或抛出DropItem异常
    # 被丢弃的Item对象将不会被之后的pipeline组件处理
    def process_item(self, item, spider):
        # item 获取的item;spider 获取该item的spider
        self.file.write(json.dumps(dict(item)) + ',\n')
        return item

    def close_spider(self, spider):  # 当某spider关闭时调用
        self.file.write(']')
        self.file.close()

        print('{} ======================='.format(spider))
        print('-' * 30)