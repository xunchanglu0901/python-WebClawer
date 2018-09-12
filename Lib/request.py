#1
#import urllib.request
#request = urllib.request.Request('https://python.org')
#response = urllib.request.urlopen(request)
#print(response.read().decode('utf-8'))



#2 附加Headers
#from urllib import request,parse
#url='http://httpbin.org/post'
#headers={
#    'User-Agent':'Mozilla/4.0 (compatible;MSIE 5.5;Windows NT)',
#    'Host':'httpbin.org'
#}
#dict={
#    'name':'Germey'
#}
#data = bytes(parse.urlencode(dict),encoding='utf8')
#req = request.Request(url=url,data=data,headers=headers,method='POST')
#response = request.urlopen(req)
#print(response.read().decode('utf-8'))
#或者使用add_headers()方法添加请求头
#req = request.Request(url=url,data=data,method='POST')
#req.add_headers('User-Agent','MOzilla/4.0 (compatible;MSIE 5.5;Windows NT)')



#3 高级用法
#3-1验证并返回错误原因
#from urllib.request import HTTPPasswordMgrWithDefaultRealm,HTTPBasicAuthHandler,build_opener
#from urllib.error import URLError
#username = 'username'
#password = 'password'
#url = 'http://localhost:5000/' #cmd启动pyspider all,而且本机没有设密码
#p = HTTPPasswordMgrWithDefaultRealm()
#p.add_password(None,url,username,password)
#auth_handler = HTTPBasicAuthHandler(p)
#opener = build_opener(auth_handler)
#try:
#    result = opener.open(url)
#    html =result.read().decode('utf-8')
#    print(html)
#except URLError as e:
#    print(e.reason)
#3-2添加代理 需要防火墙开端口(目前系统有问题）
#from urllib.error import URLError
#from urllib.request import ProxyHandler,build_opener
#proxy_handler=ProxyHandler({
#    'http':'http://127.0.0.1:9743',
#    'https':'https://127.0.0.1:9743'
#})
#opener = build_opener(proxy_handler)
#try:
#    response = opener.open('https://www.baidu.com')
#    print(response.read().decode('utf-8'))
#except URLError as e:
#    print(e.reason)
#3-3 Cookies的相关处理,输出成文件格式，再输出网页源代码
#import http.cookiejar,urllib.request
#cookie = http.cookiejar.CookieJar()
#handler = urllib.request.HTTPCookieProcessor(cookie)
#opener =urllib.request.build_opener(handler)
#response = opener.open('http://www.baidu.com')
#for item in cookie:
#    print(item.name+'='+item.value)
#filename = 'cookies.txt'
###cookie = http.cookiejar.MozillaCookieJar(filename)
#cookie = http.cookiejar.LWPCookieJar(filename)
#handler = urllib.request.HTTPCookieProcessor(cookie)
#opener = urllib.request.build_opener(handler)
#response=opener.open('http://www.baidu.com')
#cookie.save(ignore_discard=True,ignore_expires=True)
#cookie = http.cookiejar.LWPCookieJar()
#cookie.load('cookies.txt',ignore_discard=True)
#handler = urllib.request.HTTPCookieProcessor(cookie)
#opener = urllib.request.build_opener(handler)
#response = opener.open('http://www.baidu.com')
#print(response.read().decode('utf-8'))



#3.1.2异常处理
#URLError
#from urllib import request,error
#try:
#    response = request.urlopen('https://cuiqingcai.com/index.htm')
#except error.URLError as e:
#    print(e.reason)

#HTTPError
#from urllib import request,error
#try:
#    response = request.urlopen('https://cuiqingcai.com/index.htm')
#except error.HTTPError as e:
#   print(e.reason,'\n',e.code,'\n',e.headers,)
##except error.URLError as e:
##    print(e.reason)
###优化，先捕获子类错误，再捕获父类错误，其中URLError是HTTPError的父类
#from urllib import request,error
#try:
#    response = request.urlopen('https://cuiqingcai.com/index.htm')
#except error.HTTPError as e:
#    print(e.reason,e.code,e.headers,'HTTP错误',sep='\n')
#except error.URLError as e:
#    print(e.reason,'URLE错误',sep='\n')
#else:
#    print('Request Successfully')

#错误类型不是字符串，而是对象的情况
#import socket
#import urllib.request
#import urllib.error
#try:
#    response =urllib.request.urlopen('https://www.baidu.com',timeout=0.01)
#except urllib.error.URLError as e:
#    print(type(e.reason))
#    if isinstance(e.reason,socket.timeout):
#        print('time out')
