# 定位搜索框，搜索电影
from selenium import webdriver  # 核心对象
import datetime
import random
# 键盘操作
from selenium.webdriver.common.keys import Keys
# WebDriverWait 负责循环等待
from selenium.webdriver.support.wait import WebDriverWait
# expected_conditions条件，负责条件触发
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

driver = webdriver.PhantomJS(r'/Users/quyixiao/Documents/source/phantomjs-2.1.1-macosx/bin/phantomjs')

driver.set_window_size(1280, 2400)  # 设置窗口大小

# 打开网页GET方法，模拟浏览器地址栏输入网址
url = "https://movie.douban.com/"  # 豆瓣电影
driver.get(url)


# 保存图片
def save_pic():
    base_dir = 'tmp/'
    filename = "{}{:%Y%m%d%H%M%S}{:03}.png".format(base_dir, datetime.datetime.now(), random.randint(1, 100))
    driver.save_screenshot(filename)


try:
    ele = WebDriverWait(driver, 20).until(
        ec.presence_of_element_located((By.XPATH, '//input[@id="inp-query"]'))  # 元素是否已经加载 到了dom树中
    )  # 使用哪个driver，等到什么条件ok，ec就是等待的条件
    ele.send_keys('TRON')
    ele.send_keys(Keys.ENTER)
    save_pic()
finally:
    driver.quit()
