from selenium import webdriver
from browsermobproxy import Server
import os
import time
from selenium.webdriver.chrome.options import Options

server = Server(r'/Users/quyixiao/Downloads/browsermob-proxy-2.1.4/bin/browsermob-proxy')
server.start()

proxy = server.create_proxy()

chrome_options = Options()
print("=============================================",proxy.proxy)
chrome_options.add_argument('--proxy-server={0}'.format(proxy.proxy))


chromedriver = '/Users/quyixiao/chromedriver/chromedriver_mac64/chromedriver'
os.environ["webdriver.chrome.driver"] = chromedriver




driver = webdriver.Chrome(chromedriver,options=chrome_options)

print("=============================================")

base_url = "https://www.iesdouyin.com/share/user/63174596206"
proxy.new_har("douyin", options={'captureHeaders': True, 'captureContent': True})

driver.get(base_url)

time.sleep(5)

result = proxy.har



print("+++++++++++++++++++++++++" ,result)

for entry in result['log']['entries']:
    _url = entry['request']['url']
    # 根据URL找到数据接口
    if "/api/v2/aweme/post" in _url:
        _response = entry['response']
        _content = _response['content']['text']
        # 获取接口返回内容
        print(_content)

server.stop()
driver.quit()