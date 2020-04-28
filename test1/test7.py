import os
from time import sleep
from selenium import webdriver
import json
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# 过滤出数据请求中的headers
def getHttpInfo(browser):
    for responseReceived in browser.get_log('performance'):
        try:
            response = json.loads(responseReceived[u'message'])[u'message'][u'params'][u'response']
            print(response)
            print(response['url'])
            print(response['headers'])
            print(response['headersText'])
        except:
            pass
    return None


# 请求页面 并设置headers到文件中
def setHeaders():
    d = DesiredCapabilities.CHROME
    d['loggingPrefs'] = {'performance': 'ALL'}
    options = webdriver.ChromeOptions()
    options.add_experimental_option('w3c', False)

    chromedriver = '/Users/quyixiao/chromedriver/chromedriver_mac64/chromedriver'
    os.environ["webdriver.chrome.driver"] = chromedriver

    driver = webdriver.Chrome(chromedriver, desired_capabilities=d, options=options)
    driver.get('http://www.baidu.com')
    sleep(5)
    headers = getHttpInfo(driver)
    driver.quit()
    # write header
    hand = open('header.txt', 'w')
    hand.write(json.dumps(headers))
    hand.close()


if __name__ == '__main__':
    setHeaders()
