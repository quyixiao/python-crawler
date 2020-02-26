# 返回json的解析和处理
from jsonpath import jsonpath
import requests
import json

ua = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36"
url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=10&page_start=0'
with requests.get(url, headers={'User-agent': ua}) as response:
    text = response.text
    print(1, text)  # str类型的json数据
    js = json.loads(text)
    print(2, js)  # Json转为Python数据结构
    # 找到所有电影的名称
    rs1 = jsonpath(js, '$..title')
    print(3, rs1)
    # 找打所有得分高于8分的电影名称
    # 根下任意层的subjects的子节点rate大于字符串8
    rs2 = jsonpath(js, '$..subjects[?(@.rate > "8")]')
    print(4, rs2)
    # 根下任意层的subjects的子节点rate大于字符串8的节点的子节点title
    rs3 = jsonpath(js, '$..subjects[?(@.rate > "8")].title')
    print(5, rs3)
