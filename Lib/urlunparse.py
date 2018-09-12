#网页解析2.urlunparse 将各个部分组合成URL
from urllib.parse import urlunparse
data=['hhtps','www.liujiwei.com','index.html','user','h=6','comment']
print(urlunparse(data))
