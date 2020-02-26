from bs4 import BeautifulSoup

with open('test.html', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'lxml')
    # 元素选择器
    ele = soup.select('div')  # 所有的div标签
    print(ele[0].string,end='\n------------\n')  # 内容仅仅只能是文本类型，否则返回None
    print(list(ele[0].strings), end='\n------------\n')  # 迭代保留空白字符
    print(list(ele[0].stripped_strings), end='\n------------\n')  # 迭代不保留空白字符
    print(ele[0], end='\n------------\n')
    print(ele[0].text,  end='\n------------\n')  # 本质上就是get_text()，保留空白字符的strings
    print(ele[0].get_text(), end='\n------------\n')  # 迭代并join，保留空白字符，strip默认为False
    print(ele[0].get_text(strip=True))  # 迭代并join，不保留空白字符
