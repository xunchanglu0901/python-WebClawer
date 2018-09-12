# 4.2 使用Beautiful Soup
### 简单高效

#from bs4 import BeautifulSoup
#soup = BeautifulSoup('<p>Hello</p>','lxml')





# 4.基本用法
#p代表段落
#html ="""
#<html><head><title>The Dirmouse's story</title></head>
#<body>
#<p class="title" name="dormouse"><b>Dormouse's story</b></p>
#<p class="story">Once upon a time there were three littles sisters; and their names were
#<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
#<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
#<a href="http://example.com/tillie" class="sister" id"link3">Tillie</a>;
#and they lived at the bottom of a well.</p>
#<p class="story">...</p>
#"""

#from bs4 import BeautifulSoup
#soup = BeautifulSoup(html,'lxml')
#print(soup.prettify())
#print(soup.title.string)


# 5 节点选择器
### 选择元素

#from bs4 import BeautifulSoup
#soup = BeautifulSoup(html,'lxml')
#print(soup.title)
#print(type(soup.title))
#print(soup.title.string)
#print(soup.head)
#print(soup.p)

### 提取信息
###### 提取节点名称
#print(soup.title.name)
###### 获取节点属性
#print(soup.p.attrs)#<class>类别
#print(soup.p.attrs['name'])
#print(soup.p['name'])
#print(soup.p['class'])
###### 获取内容
#print(soup.p)
#print(soup.p.string)

### 嵌套选择
#from bs4 import BeautifulSoup
#soup = BeautifulSoup(html,'lxml')
#print(soup.head.title)
#print(type(soup.head.title))
#print(soup.head.title.string)

### 关联选择
######子节点和子孙节点
#html = '''
#<html>
#<head>
#<title>The Dormouse's story</title>
#</head>
#<body>
#<p class='story'>
#    Once upon a time there were three little sisters;and their names were
#    <a href='http://example.com/elsie' class='sister' id='link1'>
#<span>Elsie</span>
#</a>
#<a href='http://example.com/lacit' class='sister' id='link2'>Lacie</a>
#and
#<a href='http://example.com/tittle' class='sister' id='link3'>Tittle</a>
#and they lived at the bottom of a well.
#</p>
#<p class='story'>...</p>
#'''

#from bs4 import BeautifulSoup
#soup = BeautifulSoup(html,'lxml')
#print(soup.p.contents)
#print(soup.p.children)
#for i, child in enumerate(soup.body.children):
#    print(i, child)
#for i, child in enumerate(soup.body.descendants):
#    print(i, child)



######  父节点和祖先节点
#from bs4 import BeautifulSoup
#soup = BeautifulSoup(html,'lxml')
#print(soup.a.parent)
#print(type(soup.a.parents))
#print(list(enumerate(soup.a.parents)))#列举#

###### 兄弟节点
#print('Next Sibling',soup.a.next_sibling)
#print('Prev Sibling',soup.a.previous_sibling)
#print('Next Siblings',list(enumerate(soup.a.next_sibling)))
#print('Prev Siblings',list(enumerate(soup.a.previous_sibling)))

###### 提取信息
#from bs4 import BeautifulSoup
#soup = BeautifulSoup(html,'lxml')
#print(soup.a.next_sibling.string)
#print(list(soup.a.parents)[0])

### 6 方法选择器
#from bs4 import BeautifulSoup
#soup = BeautifulSoup(html,'lxml')
#print(soup.find_all(name='a'))
#print(type(soup.find_all(name='a')[1]))#从0开始 1代表的其实是第二个
#for p in soup.find_all(name='p'):
#    print(p.find_all(name='p'))

html = '''
<div class="panel">
<div class="panel-heading">
<h4>Hello</h4>
</div>
<div class="panel-body">
<a>Hello,this is a link</a>
<a>Hello,this is a link too</a>
<ul class="list" id="list-1" name='elements'>
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<ul class="list list-small" id=list-2">
<li class="element">Foo</li>
<li class="element">Bar</li>
</ul>
</div>
</div>
'''
#(1)name
'''
from bs4 import BeautifulSoup
soup=BeautifulSoup(html,'lxml')
for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))
    for li in ul.find_all(name='li'):
        print(li.string)
'''
#(2)attrs
import re
from bs4 import BeautifulSoup
soup=BeautifulSoup(html,'lxml')
#print(soup.find_all(attrs={'id':"list-1"}))
#print(soup.find_all(attrs={'class':'element'}))
#print(soup.find_all(attrs={'name':'elements'}))
#print(soup.find_all(text=re.compile('link')))
#(3)

###### find()
#print(soup.find(name='ul'))
#print(soup.find_all(name='ul'))


### 7 CSS选择器
#print(soup.select('.panel .panel-heading'))#注意空格
#print(soup.select('ul li'))
#print(soup.select('#list-1 .element'))#元素属性之类的需要加.但web标签开头不需要
#print(type(soup.select('ul')[0]))

###### 嵌套选择
#for ul in soup.select('ul'):
#    print(ul.select('li'))
###### 获取属性
     #print(ul['id'])
#或者使用attrs
     #print(ul.attrs['id'])

###### 获取文本
for li in soup.select('li'):
    print('get text:',li.get_text())
    print('string:',li.string)
