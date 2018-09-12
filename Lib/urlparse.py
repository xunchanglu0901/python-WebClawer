#3.1.3解析连接
#urlparse 实现url的识别和分段

#from urllib.parse import urlparse
#result=urlparse('http://www.baidu.com/index.html;user?id=5#comment')
#print(type(result),result)

#API用法
#from urllib.parse import urlparse
#result = urlparse('www.baidu.com/index.html;user?id=5#comment',scheme='http')
#print(result)

#是否忽略fragment
'''
from urllib.parse import urlparse
result = urlparse('https://www.baidu.com/index.html#comment',allow_fragments=False)
print(result)
'''
#分别用索引顺序和属性名获取对应信息
'''
from urllib.parse import urlparse
result = urlparse('https://www.baidu.com/index.html#comment',allow_fragments=False)
print(result.scheme,result[0],result.netloc,result[1],sep='\n')
'''
