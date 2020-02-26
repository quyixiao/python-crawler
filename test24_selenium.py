# 模拟开源中国登陆

from selenium import webdriver  # 核心对象
import datetime
import random
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.PhantomJS(r'/Users/quyixiao/Documents/source/phantomjs-2.1.1-macosx/bin/phantomjs')

driver.set_window_size(1280, 2400)  # 设置窗口大小


# 保存图片
def save_pic():
    base_dir = '/tmp'
    filename = "{}{:%Y%m%d%H%M%S}{:03}.png".format(base_dir, datetime.datetime.now(), random.randint(1, 100))
    driver.save_screenshot(filename)


# 打开网页GET方法，模拟浏览器地址栏输入网址
url = "https://www.oschina.net/home/login"
driver.get(url)
save_pic()
# 模拟键盘输入
# 'userMail' 'userPassword'
username = driver.find_element_by_id('userMail')
username.send_keys('wei.xu@magedu.com')
pwd = driver.find_element_by_id('userPassword')
pwd.send_keys('magedu.com18')
save_pic()

# 模拟回车
pwd.send_keys(Keys.ENTER)
print('-' * 30)
print(driver.current_url)  # 当前url
while True:
    time.sleep(1)
    print(driver.current_url)
    try:
        userinfo = driver.find_element_by_class_name('user-info')
        print(userinfo.text)  # 打印文本
        save_pic()
        break
    except Exception as e:
        print(e)

cookies = driver.get_cookies()  # 获取长期登陆的cookie print(cookies)
driver.close()
