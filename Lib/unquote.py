#网页解析

#10.unquote

#URL解码

from urllib.parse import unquote

url = 'https://www.baidu.com/s?wd=%E4%BD%A0%E5%A5%BD'

print(unquote(url))
