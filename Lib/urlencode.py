#网页解析

#6.urlencode

from urllib.parse import urlencode

params = {
    'name':'germey',
    'age':22
}
base_url = 'https://www.baidu.com?'
url = base_url + urlencode(params)
print(url)


#params 用于GET请求
#data   用于POST请求
