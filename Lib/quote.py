#网页解析

#9.quote

#quote = 引用、引述

#将内容转化为URL编码格式

#URL含有中文参数时，可能会导致乱码问题

from urllib.parse import quote

keyword = '你好'
url = 'https://www.baidu.com/s?wd='+quote(keyword)
print(url)
