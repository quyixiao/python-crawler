from bs4 import BeautifulSoup

from bs4 import BeautifulSoup

with open('test.html', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'lxml')
    print(soup.builder)
    print(0, soup)  # 输出整个解析的文档对象
    print(1, soup.prettify()) # 格式输出
    print('-'*30)
    print(2, soup.div, type(soup.div))  # bs4.element.Tag, Tag对象
    print(3, soup.div.name, soup.div.attrs)
    # print(3, soup.div['class']) # KeyError，div没有class属性 print(3, soup.div.get('class'))
    print(4, soup.h3['class'])  # 多值属性
    print(4, soup.h3.get('class'))  # 多值属性
    print(4, soup.h3.attrs.get('class'))  # 多值属性
    print(5, soup.img.get('src'))
    soup.img['src'] = 'http://www.python.org/'  # 修改属性
    print(5, soup.img['src'])
    print(6, soup.a)  # 找不到返回None
    del soup.h3['class'] # 删除属性
    print(4, soup.h3.get('class'))

