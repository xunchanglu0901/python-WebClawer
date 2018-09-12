html="""
<div class='wrap'>
<div id='container'>
<ul class='list'>
<li class='item-0'>first item</li>
<li class='tiem-1'><a href='link2.html'>second item</a></li>
<li class='item-0 active'><a href='link3.html'><span class='bold'>third item</span></a></li>
<li class='item-1 active'><a href='link4.html'>fourth item</a></li>
<li class='item-0'<a href='link5.html'>fifth item</a></li>
</ul>
</div>
</div>
"""
from pyquery import PyQuery as pq
doc = pq(html)

# 2 初始化
### 字符串初始化
#from pyquery import PyQuery as pq
#doc = pq(html)
#print(doc('li'))

### URL初始化
#from pyquery import PyQuery as pq
#doc = pq(url='https://www.baidu.com')
#print(doc('title'))
#import requests
#doc =pq(requests.get('http://www.baidu.com').text)
#print(doc('title'))

### 文件初始化
#from pyquery import PyQuery as pq
#doc = pq(filename='hhh.html')
#print(doc('li'))


# 3 基本CSS选择器
#from pyquery import PyQuery as pq
#doc = pq(html)
#print(doc('#container li'))
#print(type(doc('#container li')))

# 4 查找节点
### 子节点
#items = doc('.list')
#print(items)
#print(type(items))
#lis =items.find('li')
#print(lis)

#lis = items.children()
#print(lis)
#lis=items.children('.active')
#print(lis)


### 父节点
#container = items.parent()
#print(type(container))
#print(container)

### 祖父节点
#items = doc('.list')
#container = items.parents()
#print(type(container))
#print(container)
#print(items.parents('.wrap'))

### 兄弟节点
#li = doc('.list .item-0.active')
#print(li.siblings())
#print(li.siblings('.active'))

# 5 遍历
#li = doc('.item-0.active')
#print(li)
#print(str(li))
#lis = doc('li').items()
#print(type(lis))
#for li in lis:
#    print(li,type(li))


# 6 获取信息
###获取属性
#a1h = doc('.item-0.active a')
#print(a1h,type(a1h))
#print(a1h.attr('href'))
#hhh = doc('a')
#print(hhh,type(hhh))
#print(hhh.attr('href'))
#print(hhh.attr.href)
#for item in hhh.items():
#    print(item.attr.href)
###获取文本
#h = doc('.item-0.active a')
#print(h)
#print(h.text())
#li = doc('.item-0.active a')
#print(li)
#print(li.html())


# 7 节点操作
### 添加和移除某个节点
'''
li = doc('.item-0.active')
print(li)
li.removeClass('active')
print(li)
li.addClass('active')
print(li)
'''

### attr & text & html
#li = doc('.item-0.active')
#print(li)
#li.attr('name','link')
#print(li)
#li.text('changed item"')
#print(li)
#li.html('<span>changed item</span>')
#print(li)


### remove()
html2 = '''
<div class="wrap">
    Hello,World
<p>This is a paragraph.</p>
</div>
'''
#doc2 =pq(html2)
#wrap = doc2('.wrap')
#print(wrap.text())
#wrap.find('p').remove()
#print(wrap.text())


# 8 伪类选择器
li = doc('li:first-child')
print(li)
li = doc('li:last-child')
print(li)
li = doc('li:nth-child(2)')
print(li)
li = doc('li:gt(2)')
print(li)
li = doc('li:nth-child(2n)')
print(li)
li = doc('li:contains(second)')
print(li)
