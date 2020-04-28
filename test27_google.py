import os
import sys

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()



chromedriver = '/Users/quyixiao/chromedriver/chromedriver_mac64/chromedriver'
os.environ["webdriver.chrome.driver"] = chromedriver



driver = webdriver.Chrome(chromedriver,options=chrome_options)

# 定义要访问的页面
url = "http://www.python.org"
# 打开
driver.get(url)
# 打开页面后停止3秒
time.sleep(3)
# 关闭页面
driver.quit()