# 192.168.99.100:8050

# 大部分为Splash代码，仅用py文件存储代码

"""

# 渲染百度
function main(splash, args)
  assert(splash:go(args.url))
  assert(splash:wait(0.5))
  return {
    html = splash:html(),
    png = splash:png(),
    har = splash:har(),
  }
end

# 入口及返回值
function main(splash, args)
    splash:go("http://www.baidu.com")
    splash:wait(0.5)
    local title = splash:evaljs("document.title")
    return {title=title}
end

# 异步处理
function main(splash, args)
    local example_urls = {"www.baidu.com","www.taobao.com","www.zhihu.com"}
    local urls = args.urls or example_urls
    local results = {}
    for index,url in ipairs(urls) do
        local ok, reason = splash:go("http://" .. url)
        if ok then
            splash:wait(2)
            results[url] = splash:png()
        end
    end
    return results
end



### 对象属性

# args
function main(splash, args)
    local url = args.url
end
#等价于
function main(splash)
    local url = splash.args.url
end

# js_enabled 是Splash的JavaScript执行开关 默认为开即可，一般不用设置
# 关闭后会报错，如下
function main(splash, args)
    splash:go("https://www.baidu.com")
    splash.js_enabled = false
    local title =splash:evaljs("document.title")
    return {title=title}
end

# resource_timeout 设置加载超时时间 如0.1秒内没响应就报错，如下
function main(splash, args)
    splash.resource_timeout = 0.1
    assert(splash:go('https://www.taobao.com'))
    return splash:png()
end

# images_enabled 是否加载图片
function main(splash, args)
    splash.images_enabled = false
    assert(splash:go('https://www.taobao.com'))
    return {png=splash:png()}
end

# plugins_enabled 是否开启浏览器插件，列入Flash插件

# scroll_position 控制页面上下或者左右滚动
# y 上下 x 左右
function main(splash, args)
    splash:go("https://www.zhihu.com")
    splash.scroll_position = {y=400}
    return {png=splash:png()}
end



### Splash 对象的方法

# go   模拟请求
#ok, reason = splash:go{url, baseurl=nil, headers=nil, http_method="GET", body=nil, formdata=nil}
#ok 为空 则表示网页加载出现了错误 reason会给出错误原因 正确示例如下
function main(splash, args)
    local ok, reason = splash:go{"http://httpbin.org/post", http_method="POST", body="name_Germey"}
    if ok then
        return splash:html()
    end
end


# wait()  控制页面等待时间
ok,reason = splash:wait{time, cancel_on_redirect=false, cancel_on_error=true}


# jsfunc()
# 实现JavaScript方法到Lua脚本的转换，如下
function main(splash, args)
    local get_div_count = splash:jsfunc([[
    function(){
        var body = document.body;
        var divs = body.getElementsByTagName('div');
        return divs.length;
    }
    ]])
    splash:go("https://www.baidu.com")
    return("There are %s DIVs"):format(
        get_div_count())
end

# evaljs()  执行JavaScript代码并返回最后一条JavaScript语句的返回结果
result =splash:evaljs("xxx")

# runjs() 类似上一个 但是更偏向于执行某些动作或者声明某些方法
function main(splash, args)
    splash:go("https://www.baidu.com")
    splash:runjs("foo = function() { return 'bar'}")
    local result = splash:evaljs("foo()")
    return result
end


# autoload() 设置每个页面访问时自动加载的对象
ok, reason = splash:autoload{source_or_url, source=nil, url=nil}
# 只加载 不负责执行
# url可以是某些方法库


# call_later()  设置定时任务、延时时间来实现任务延时执行
# 并且可以在执行前通过cancel()方法重新执行定时任务
# 例如不同时间段进行截图 
function main(splash, args)
    local snapshots = {}
    local timer = splash:call_later(function()
        snapshots["a"] = splash:png()
        splash:wait(1.0)
        snapshots["b"] = splash:png()
    end, 0.2)
    splash:go("https://www.taobao.com")
    splash:wait(3.0)
    return snapshots
end



# http_get() 模拟HTTP的GET请求
response = splash:http_get{url, headers=nil, follow_redirects=true}

# http_post() 模拟HTTP的POST请求
response = splash:http_post{url, headers=nil, follow_redirects=true, body=nil}


# set_content() 设置页面的内容，如下
function main(splash, args)
    assert(splash:set_content("<html><body><h1>hello</h1></body></html>"))
    return splash:png()
end


# html() 获取网页源代码
function main(splash, args)
    splash:go("https://www.taobao.com")
    return splash:html()
end

# png() 获取截图
    return splash:png()

# jpeg() 同上；图片格式不同

# har() 获取页面加载过程描述
    return splash:har()

# url() 获取当前正在访问的URL

# get_cookies() 获取当前页面的Cookies
    return splash:get_cookies()


# add_cookies() 添加
cookies = splash:add_cookies{name, value, path=nil, domain=nil, expires=nil, httpOnly=nil, secure=nil}

# clear_cookies()
function main(splash, args)
    splash:go("https://www.taobao.com")
    splash:clear_cookies()
    return splash:get_cookies()
end



# get_viewport_size() 获取当前浏览页面大小，即高宽
    return splash:get_viewport_size()
# set_viewport_size(400， 700) 设置
# set_viewport_full() 全屏显示

# set_user_agent 设置代理
function main(splash, args)
    splash:go("https://www.taobao.com")
    splash:set_user_agent('Splash')
    splash:clear_cookies()
    return splash:html()
end

# set_custom_headers()
function main(splash, args)
    splash:go("https://www.taobao.com")
    splash:set_user_agent('Splash')
    splash:set_custom_headers({
        ["User-Agent"] = "Splash",
        ["Site"] = "splash",
        })
    splash:clear_cookies()
    return splash:html()
end



# select() 选中符合条件的第一个节点
# 参数为CSS选择器
function main(splash, args)
    splash:go("https://www.baidu.com")
    input = splash:select("#kw")
    input:send_text('Splash')
    splash:wait(3)
    return splash:png()
end

# select_all()
# 选择所有符合的节点，遍历后将其中文本获取下来，如下
function main(splash)
    local treat = require('treat')
    assert(splash:go("http://quotes.toscrape.com/"))
    assert(splash:wait(0.5))
    local texts = splash:select_all('.quote .text')
    local results = {}
    for index, text in ipairs(texts) do
        results[index] = text.node.innerHTML
    end
    return treat.as_array(results)
end



# mouse_click() 模拟鼠标点击
# 传入坐标值或者某个节点来定位
function main(splash)
    splash:go("https://www.baidu.com/")
    input = splash:select('#kw')
    input:send_text('Splash')
    submit = splash:select('#su')
    submit:mouse_click()
    splash:wait(3)
    return splash:png()
end

"""


### 7 Splash-API 调用

# render.html 获取JavaScript渲染的页面HTML代码 可以用python实现
"""
import requests
url = 'http://192.168.99.100:8050/render.html?url=https://www.baidu.com&wait=5'#等待五秒再开始获取
response = requests.get(url)
print(response)
print(response.text)
"""
# render.png 截图
"""
import requests
url = 'http://192.168.99.100:8050/render.png?url=https://www.baidu.com&wait=5&width=1000&height=700'
response = requests.get(url)
with open('png.png','wb') as f:
    f.write(response.content)
"""
# render.jpeg 同上，仅多了设置图片质量的参数，quality

# render.har 获取HAR数据
'''
import requests
url = 'http://192.168.99.100:8050/render.har?url=https://www.baidu.com'
response = requests.get(url)
print(response.text)
'''
# render.json 同上，不过是JSON格式
"""
import requests
url = 'http://192.168.99.100:8050/render.json?url=https://www.baidu.com&html=1'
response = requests.get(url)
print(response.text)
"""

# execute 交互操作；与Lua脚本对接
# 例如
"""
import requests
from urllib.parse import quote

lua = '''
function main(splash)
    return 'hello'
end
'''
url = 'http://192.168.99.100:8050/execute?lua_source=' + quote(lua)
response = requests.get(url)
print(response.text)
print(response)
"""

import requests
from urllib.parse import quote
lua = '''
function main(splash, args)
    local treat = require("treat")
    local response = splash:http_get("http://httpbin.org/get")
        return {
            html=treat.as_string(response.body),
            url=response.url,
            status=response.status
            }
end
'''
url = 'http://192.168.99.100:8050/execute?lua_source=' + quote(lua)
response = requests.get(url)
print(response.text)

