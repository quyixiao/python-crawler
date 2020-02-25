from lxml import etree

# 使用etree构建HTML
root = etree.Element('html')

print(type(root))
print(root.tag)

body = etree.Element('body')
root.append(body)
print(etree.tostring(root))
sub = etree.SubElement(body, 'child1')  # 增加子节点
print(type(sub))
sub = etree.SubElement(body, 'child2').append(etree.Element('child21'))
print('--------------------------')
print(etree.tostring(root, pretty_print=True).decode())
