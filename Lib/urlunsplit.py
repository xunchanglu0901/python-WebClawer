#网页解析 4.urlunsplit

#合并

from urllib.parse import urlunsplit
data=['https','www.baidu.com','index.html','a=6','comment']
print(urlunsplit(data))
