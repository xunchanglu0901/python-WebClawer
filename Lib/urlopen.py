#1
#import urllib.request
#response = urllib.request.urlopen('https://www.baidu.com/')
#print(response.read().decode('utf-8'))
#print(type(response))
#print(response.status)
#print(response.getheader('server'))
#print(response.read())
#print(response.msg)


#2 data参数
#import urllib.parse
#import urllib.request

#data=bytes(urllib.parse.urlencode({"word":"hello"}),encoding='utf8')
#response = urllib.request.urlopen('https://httpbin.org/post',data=data)
#print(response.read())


#3 timeout参数+跳过抓取并输出超时
#import urllib.request
#response = urllib.request.urlopen('https://httpbin.org/get',timeout=0.1)
#print(response.read())
import socket
import urllib.request
import urllib.error
try:
    respense = urllib.request.urlopen('https://httpbin.org/get',timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('超时')
