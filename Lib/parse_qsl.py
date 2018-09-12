#网页解析

#8.parse_qsl

#将参数转化为元组组成的列表

#元组 类似于 数对

from urllib.parse import parse_qsl

query = 'name=germey&age=22'

print(parse_qsl(query))
