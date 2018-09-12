from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener
from urllib import request
import socks
import socket
# urllib
'''
proxy = 'username:password@127.0.0.1:9743'
proxy_handler = ProxyHandler({
    'http':'http://' + proxy,
    'https':'https://' + proxy
    })
opener = build_opener(proxy_handler)
try:
    response = opener.open('http://httpbin.org/get')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)

'''
### SOCKS5类型
'''
socks.set_default_proxy(socks.SOCKS5,'61.135.217.7')#或者'127.0.0.1', 9742
socket.socket = socks.socksocket
try:
    response = request.urlopen('http://httpbin.org/get')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
'''



# 使用requests

import requests
'''
proxy = '61.135.217.7'
proxies ={
    'http':'http://' + proxy,
    'https':'https://' + proxy
    }
try:
    response = requests.get('http://httpbin.org/get',proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error',e.args)
'''
### SOCKS5类型
'''
proxy = '61.135.217.7'
proxies ={
    'http':'socks5://' + proxy,
    'https':'socks5://' + proxy
    }
try:
    response = requests.get('http://httpbin.org/get',proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error',e.args)
'''
###### 或者
'''
socks.set_default_proxy(socks.SOCKS5,'61.135.217.7')#或者'127.0.0.1', 9742
socket.socket = socks.socksocket
try:
    response = request.urlopen('http://httpbin.org/get')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
'''

# Selenium

### Chrome 无认证
'''
from selenium import webdriver

proxy = '61.135.217.7'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://' + proxy)
chrome = webdriver.Chrome(chrome_options=chrome_options)
chrome.get('http://httpbin.org/get')
'''
### Chrome 认证
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import zipfile

ip = '127.0.0.1'
port = 9743
username = 'foo'
password = 'bar'

manifest_json = """
{
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    }
}
"""

background_js = """
var config = {
        mode: "fixed_servers",
        rules: {
          singleProxy: {
            scheme: "http",
            host: "%(ip)s",
            port: %(port)s
          }
        }
      }
chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});
function callbackFn(details) {
    return {
        authCredentials: {
            username: "%(username)s",
            password: "%(password)s"
        }
    }
}
chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
)
""" % {'ip': ip, 'port': port, 'username': username, 'password': password}

plugin_file = 'proxy_auth_plugin.zip'
with zipfile.ZipFile(plugin_file, 'w') as zp:
    zp.writestr("manifest.json", manifest_json)
    zp.writestr("background.js", background_js)
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_extension(plugin_file)
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get('http://httpbin.org/get')
'''

###  PhantomJS
from selenium import webdriver

service_args = [
    '--proxy=125.112.196.164',
    '--proxy-type=http',
    '--proxy-auth=username:password'
    
]

browser = webdriver.PhantomJS(service_args=service_args)
browser.get('http://httpbin.org/get')
print(browser.page_source)
