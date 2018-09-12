 #3.2 使用requests

#3.2.1 基本用法

###### 2.实例引入
'''
import requests
r = requests.get('https://www.baidu.com/')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)
'''
###### 其他类型的方便实现
'''
import requests
a = requests.post('https://httpbin.org/post')
b = requests.put('https://httpbin.org/put')
c = requests.delete('https://httpbin.org/delete')
d = requests.head('http://httpbin.org/get')
e = requests.options('https://httpbin.org/get')
 '''

###### 3. GET请求
###### 基本实例
'''
import requests
r = requests.get('https://httpbin.org/get?name=ljw&age=22')
print(r.text)
'''
###### 信息数据用词典储存
'''
import requests
data = {
    'name':'ljw',
    'age':22
}
r = requests.get('http://httpbin.org/get',params=data)
print(r.text)
'''
###### 调用json()方法将JSON格式的字符串结果转化为字典
'''
import requests
r = requests.get('http://httpbin.org/get')
print(type(r.text))
print(r.json())
print(type(r.json()))
'''

###### 抓取知乎的问题标题  HTML文档
'''
import re,requests
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh;Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
r = requests.get('https://www.zhihu.com/explore',headers = headers)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
titles = re.findall(pattern,r.text)
print(titles)
'''

###### 抓取二进制数据  图片、视频、音乐
'''
import requests
r = requests.get('https://github.com/favicon.ico')#站点网页标签页小图标
print(r.text)#输出Unicode格式的编码，这里会把图片转化成字符串
print(r.content)#输出二进制的内容
'''
######### 保存上述图片
'''
import requests
r =requests.get('https://github.com/favicon.ico')
with open('favicon.ico','wb') as e:###open()方法，第一个参数是名称，第二是以二进制写的形式打开
    e.write(r.content)###对二进制内容进行写入
'''

###### 添加headers
########## 如果不传递headers则无法正常请求
'''
import requests
r = requests.get('https://www.zhihu.com/explore')
print(r.text)
'''
######### 添加后
'''
import requests
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh;Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
r = requests.get('https://www.zhihu.com/explore',headers = headers)
print(r.text)
'''

### 4 POST请求
'''
import requests
data = {'name':'ljw','age':'24'}
r = requests.post('https://httpbin.org/post',data=data)
print(r.text)
'\n'
'\n'
print(r)
'''


### 5 响应
###### 常用响应结果查询
'''
import requests
r =requests.get('http://www.jianshu.com')
print(type(r.status_code),r.status_code,type(r.headers),r.headers,type(r.cookies),r.cookies,type(r.url),r.url,type(r.history),r.history,sep='\n')
'''
######
import requests
r = requests.get('http://www.jianshu.com')
exit() if not r.status_code == requests.codes.ok else print('请求成功/Request Successfully')
