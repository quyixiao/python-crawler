# 获取bing查询数据
from selenium import webdriver  # 核心对象
import datetime
import random
import time

# 指定PhantomJS的执行文件路径
from selenium.webdriver.chrome.options import Options

driver = webdriver.PhantomJS(r'/Users/quyixiao/Documents/source/phantomjs-2.1.1-macosx/bin/phantomjs')
driver.set_window_size(1280, 2400)  # 设置窗口大小


# 打开网页GET方法，模拟浏览器地址栏输入网址
url = 'https://www.taobao.com/'

#url = "https://www.baidu.com/"

driver.get(url)

time.sleep(4)


# 保存图片
def save_pic():
    base_dir = 'tmp/'
    filename = "{}{:%Y%m%d%H%M%S}{:03}.png".format(base_dir, datetime.datetime.now(), random.randint(1, 100))
    driver.save_screenshot(filename)


save_pic()  # 是否看到查询结果?

MAXRETRIES = 5  # 最大重试次数
for i in range(MAXRETRIES):  # 循环测试
    time.sleep(1)
    try:
        ele = driver.find_element_by_id('b_content')  # 如果查询结果来了，就会有这个id的标签
        print('ok')
        save_pic()
        break
    except Exception as e:
        print(e)



driver.close()
