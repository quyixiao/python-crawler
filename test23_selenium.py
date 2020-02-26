# 获取bing查询数据
from selenium import webdriver  # 核心对象
import datetime
import random
import time

# 指定PhantomJS的执行文件路径
from selenium.webdriver.chrome.options import Options
from selenium import webdriver  # 核心对象
import datetime
import random
from selenium.webdriver.support.ui import Select

driver = webdriver.PhantomJS(r'/Users/quyixiao/Documents/source/phantomjs-2.1.1-macosx/bin/phantomjs')
driver.set_window_size(1280, 2400)  # 设置窗口大小

# 打开网页GET方法，模拟浏览器地址栏输入网址
url = "https://www.oschina.net/search?scope=project&q=python"
driver.get(url)



# 保存图片
def save_pic():
    base_dir = 'tmp/'
    filename = "{}{:%Y%m%d%H%M%S}{:03}.png".format(base_dir, datetime.datetime.now(), random.randint(1,100))
    driver.save_screenshot(filename)


# 获取select
ele = driver.find_element_by_name('languageId')  # 获取元素
print(ele.tag_name)  # 标签名
print(ele)
print(driver.current_url)




save_pic()

s = Select(ele)
# 然后通过select选项的索引来定位选择对应选项（从0开始计数），如选择第三个选项:select_by_index(2)
s.select_by_index(1)  # web应用开发
print(driver.current_url)  # 新页面
save_pic()
driver.close()
