from bs4 import BeautifulSoup

from bs4 import BeautifulSoup

from bs4.element import Tag

with open('test.html', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'lxml')
    values = [True, None, False]
    for value in values:
        all = soup.find_all(value)
        print(len(all))
    print('-' * 30)
    count = 0

    for i, t in enumerate(soup.descendants):
        print(i, type(t), t.name)
        if isinstance(t, Tag):
            count += 1
            print(count)
    # 数目一致，所以返回的是Tag类型的节点，源码中确实返回的Tag类型
