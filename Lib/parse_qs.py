#网页解析

#7.parse_qs

#反序列化

from urllib.parse import parse_qs as pq
query = 'name=getmey&age=22'
print(pq(query))


#讲GET请求转化为字典类型
