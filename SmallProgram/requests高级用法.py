###3.2.2requests高级用法

###### 1 文件上传
'''
import requests
file = {'file':open('favicon.ico','rb')}
r = requests.post('https://httpbin.org/post',files=file)
print(r.text)
'''

###### 2 Cookies
########## 获取与设置
'''
import requests
r =requests.get('https://www.baidu.com')
print(r.cookies)
for key ,value in r.cookies.items():
    print(key+'='+value)
'''
######### 维持登录
'''
import requests
headers = {
    'Cookie':'zap=2a7d3b98-c9b9-4afd-8f16-fe7e3116ac18; capsion_ticket="2|1:0|10:1532185555|14:capsion_ticket|44:YjZjM2I0YjkzYzQ3NDQwYmIxNGNiNTIzN2M1OTQzNDI=|15598a5ef7d120327b82440686e7d177b7a4f55d74c0da20f4d3b9a542a46ed4"; _xsrf=8e6946d9-0acd-4df9-a1bb-210b6792cd4c; d_c0="AOBmKLBr7w2PThzsOnOiGMkUfFhpv0L8xqg=|1532185547"; q_c1=1e352c2fa1634d3ebb25d2114c13188a|1532185547000|1532185547000; z_c0="2|1:0|10:1532185566|4:z_c0|92:Mi4xQUF1YkJnQUFBQUFBNEdZb3NHdnZEU1lBQUFCZ0FsVk4zcGxBWEFBVy12YnpTM1MwOXFQNVE2YnpvU3FNN0I1R0hR|ff41d0aa9f9b5c8170506e6b65aebf5a4a309b6465c268eb63a5c62e35860eab"',
    'Host':'www.zhihu.com',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4)'
}
r = requests.get('https://www.zhihu.com',headers=headers)
print(r.text)
'''
###### 3 会话维持
'''
import requests
requests.get('https://httpbin.org/cookies/set/number/123456789')
r = requests.get('https://httpbin.org/cookies')
print(r.text)
'''#这样无法获取到我们设置的cookies(number=123456789)
'''
import requests
s = requests.Session()
s.get('https://httpbin.org/cookies/set/number/123456789')
r = s.get('https://httpbin.org/cookies')
print(r.text)
'''

###### 4 SSL证书验证
'''
import requests
r = requests.get('https://www.12306.cn')
print(r.status_code)
'''#出现SSLError
'''
import requests
r = requests.get('https://www.12306.cn',verify=False)
print(r.text)
'''#不验证，但依然出线了警告，我们接下来忽略给他指定证书，即忽略警告
'''
import requests
from requests.packages import urllib3
urllib3.disable_warnings()
r = requests.get('https://www.12306.cn',verify=False)
print(r.status_code)
'''
#我们也可以指定本地证书
'''
r = requests.get('https://www.12306.cn',cert=('/path/server.crt','/path/key'))
'''



###### 5 代理设置
'''
import requests
proxies = {
    'http':'http://110.73.4.114:8123',#注意逗号
    'https':'http://101.236.21.22:8866',#最后一行的逗号可以不加
    }
requests.get('https://www.taobao.com',proxies=proxies)
'''
######### HTTP Basic Auth
'''
import requests
proxies = {
     'http':'http://user:password@110.73.4.114:8123'
    }
requests.get('https://www.taobao.com',proxies=proxies)
'''
######### SOCK协议的使用
'''
import requests
proxies = {
    'http':'sock5://user:password@host:port'
    }
requests.get('https://www.taobao.com',proxies=proxies)
'''


###### 6 超时设置
#########  防止等待过久，设置等待最长时间界限
'''
import requests
#r = requests.get('https://www.taobao.com',timeout=1)
#r = requests.get('https://www.taobao.com',timeout=None)
r = requests.get('https://www.taobao.com',timeout=(5,11))
print(r.status_code)
'''

###### 7 身份认证

#以下几个例子需要在cmd中运行pyspider all命令
#由于本机5000端口没有设置账户密码，所以用username和password代替
'''
import requests
from requests.auth import HTTPBasicAuth
r = requests.get('http://localhost:5000',auth=HTTPBasicAuth('username','password'))
print(r.status_code)
'''
######### 使用元组简化上述方法
'''
import requests
r = requests.get('https://localhost:5000',auth=('username','password'))
print(r.status_code)
'''
######### 使用OAuth1认证的方法如下：
'''
import requests
from requests_oauthlib import OAuth1
url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1('YOUR_APP_KEY','YOUR_APP_SECRET',
              'USER_OAUTH_TOKEN','USER_OAUTH_TOKEN_SECRET')
requests.get(url,auth=auth)
'''

###### 8 Prepared Request
######### 构造request对象，方便以后的调用
from requests import Request,Session
url = 'http://httpbin.org/post'
data = {
    'name':'germey'
}
headers = {
    'User-Agent': 'AppleWebKit/537.36 (KHTML, like Gecko)'
    }
req = Request('POST',url,data=data,headers=headers)
prepped = Session().prepare_request(req)
r = Session().send(prepped)
print(r.text)

#其中prepped就是PreparedRequest所构建的可调用对象
