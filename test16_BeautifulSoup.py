from bs4 import BeautifulSoup

# 如果使用以上过滤器还不能提取出想要的节点，可以使用函数，此函数仅只能接收一个参数。 如果这个函数返回True，
# 表示当前节点匹配;返回False则是不匹配。
# 例如，找出所有有class属性且有多个值的节点，符合这个要求只有h3标签
def many_class(tag):
    # print(type(tag))
    # print(tag.attrs)
    return len(tag.attrs.get('class', [])) > 1


with open('test.html', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'lxml')
    print(soup.find_all(many_class))
