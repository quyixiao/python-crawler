from concurrent.futures import ThreadPoolExecutor
import requests
import logging
from queue import Queue
import threading
from bs4 import BeautifulSoup
import time

FORMAT = '%(asctime)s 【%(levelname)s】 [%(filename)s:%(lineno)d] %(message)s'

logging.basicConfig(format=FORMAT, level=logging.INFO)
BASE_URL = 'https://news.cnblogs.com'
NEWS_PAGE = '/n/page/'
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/5.0 Chrome/55.0.2883.75 Safari/537.36",
}
# 使用池，以后可以使用第三方消息队列完成
urls = Queue()  # url的队列
htmls = Queue()  # 响应数据队列
outputs = Queue()  # 结果输出队列
event = threading.Event()


# 创建博客园的新闻urls，每页30条新闻
def create_urls(start, end, step=1):
    for i in range(start, end + 1, step):
        url = '{}{}{}/'.format(BASE_URL, NEWS_PAGE, i)
        print("创建完毕url：", url)
        urls.put(url)
    print('url创建完毕')  # 爬取页面线程函数


def crawler():
    while not event.is_set():
        try:
            url = urls.get(True, 1)
            with requests.get(url, headers=headers) as response:
                html = response.text
                htmls.put(html)
                print("爬取完成的url：", url)
        except:
            pass


# 解析线程函数
def parser():
    while not event.is_set():
        try:
            html = htmls.get(True, 1)
            soup = BeautifulSoup(html, 'lxml')
            titles = soup.select('h2.news_entry a')
            for title in titles:
                # <a href="/n/602987/" target="_blank">特斯拉推最新生活方式产品:1500美元冲浪板</a>
                val = title.text, BASE_URL + title.get('href')
                outputs.put(val)
                print('生产: ',val)
        except:
            pass


# 持久化线程函数
def save(path):
    with open(path, 'a+') as f:
        while not event.is_set():
            try:
                text, url = outputs.get(True, 1)
                print('消费 标题：',text,"链接地址：", url, '~~~~~~~~')
                f.write('{} {}\n'.format(text, url))
                f.flush()
            except:
                pass


# 线程池
executor = ThreadPoolExecutor(10)
executor.submit(create_urls, 1, 10)
executor.submit(parser)
executor.submit(save, 'news.txt')


for i in range(7):
    executor.submit(crawler)

while True:
    inp = input('>>>')
    if inp.strip() == 'quit':
        event.set()
        print('closing ......')
        time.sleep(4)
        break
