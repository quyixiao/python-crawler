from bs4 import BeautifulSoup

# 文件对象
soup = BeautifulSoup(open("index.html"))  # 标记字符串
soup = BeautifulSoup("<html>data</html>")
