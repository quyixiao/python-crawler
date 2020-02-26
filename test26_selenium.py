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
# 打开URL,可以跟踪跳转，可以返回当前页面的实际URL
# 获取页面的title
# 处理cookie
# 控制浏览器操作，例如前进，后退，刷新，关闭，最大化等
# 执行js脚本
# 在DOM 中搜索页面元素WEb Elment，指定或者一批，find系方法
# 操作网页元素
# 模似下拉框

# 页面隐式等待
driver = webdriver.PhantomJS(
    r'/Users/quyixiao/Documents/source/phantomjs-2.1.1-macosx/bin/phantomjs')  # driver.implicitly_wait(10) # 增加这一句，全局设置，会导致下面找元素等待10秒
url = "https://movie.douban.com/"
driver.get(url)
try:
    print('begin-------')
    ele = driver.find_element_by_id('abcde')
except Exception as e:
    print(type(e))  # <class 'selenium.common.exceptions.NoSuchElementException'> print(e, '~~~~~~~~~~')
finally:
    driver.quit()
