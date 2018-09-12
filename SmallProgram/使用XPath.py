# 第四章解析库的使用

# 4.1 使用XPath

### 4 实例引入

#from lxml import etree
#text = '''
#<div>
#<ul>
#<li class='item-0><a href='link1.html'>first item</a></li>
#<li class='item-1><a href='link2.html'>second item</a></li>
#<li class='item-inactive'><a href='link3.html'>third item</a></li>
#<li class='item-1'><a href='link4.html'>forth item</a></li>
#<li class='item-0'><a href='link5.html'>fifth item</a>
#</ul>
#</div>
#'''
#html = etree.HTML(text)
#result = etree.tostring(html)
#print(result.decode('utf-8'))


# 也可以直接读取文本文件进行解析，如下：
'''
from lxml import etree
html = etree.parse('./test.html',etree.HTMLParser())
result = etree.tostring(html)
print(result.decode('utf-8'))
'''
### 5 所有节点
'''
from lxml import etree
html = etree.parse('./test.html',etree.HTMLParser())
result = html.xpath('//*')
print(result)
'''
'''
###### 指定节点
from lxml import etree
html = etree.parse('./test.html',etree.HTMLParser())
result = html.xpath('//li')
print(result)
#输出列表中的第一个
print(result[1])
'''


### 6 子节点
'''
from lxml import etree
html = etree.parse('./test.html',etree.HTMLParser())
result = html.xpath('//li/a')
print(result)
'''
###### 子孙节点
'''
from lxml import etree
html = etree.parse('./test.html',etree.HTMLParser())
result = html.xpath('//ul//a')
print(result)
'''

### 7 父节点
'''
from  lxml import etree
html = etree.parse('./test.html',etree.HTMLParser())
result = html.xpath('//a[@href="link4.html"]/../@class')
print(result)
'''

### 8 属性匹配
'''
from lxml import etree
html = etree.parse('./test.html',etree.HTMLParser())
result = html.xpath('//li[@class="item-1"]')
print(result)
'''

### 9 文本获取
'''
from lxml import etree
html = etree.parse('./test.html',etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]/text()')
print(result)
'''
###### 获取特定节点、内部文本内容
'''
from lxml import etree
html = etree.parse('./test.html',etree.HTMLParser())
#result = html.xpath('//li[@class="item-0"]/a/text()')
result = html.xpath('//li[@class="item-0"]//text()')
print(result)
'''

### 10 属性获取
'''
from lxml import etree
html = etree.parse('./test.html',etree.HTMLParser())
result = html.xpath('//li/a/@href')
print(result)
'''

### 11 属性多值匹配,
#某些节点的某个属性可能有多个值，如下，此时匹配就会失败，输出结果为[]
'''
from lxml import etree
text = '''
#<li class="li li-first"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[@class="li"]/a/text()')
print(result)
'''
#改写，使用contains()
'''
from lxml import etree
text = '''
#<li class="li li-first"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class,"li")]/a/text()')
print(result)
'''


### 12 多属性匹配，某个节点具有多个属性
'''
from lxml import etree
text = '''
#<li class="li li-first" name="item"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class,"li") and @name="item"]/a/text()')
print(result)
'''


### 13 按序选择
'''
from lxml import etree
text='''
#<div>
#<ul>
#<li class='item-0'><a href='link1.html'>first item</a></li>
#<li class='item-1'><a href='link2.html'>second item</a></li>
#<li class='item-inactive'><a href='link3.html'>third item</a></li>
#<li class='item-1'><a href='link4.html'>forth item</a></li>
#<li class='item-0'><a href='link5.html'>fifth item</a>
#</ul>
#</div>
'''
html = etree.HTML(text)
result1 = html.xpath('//li[1]/a/text()')
result2 = html.xpath('//li[last()]/a/text()')
result3 = html.xpath('//li[position()<3]/a/text()')
result4 = html.xpath('//li[last()-2]/a/text()')
print(result1,result2,result3,result4)
'''

### 14 节点轴选择

from lxml import etree
text='''
<div>
<ul>
<li class='item-0'><a href='link1.html'>first item</a></li>
<li class='item-1'><a href='link2.html'>second item</a></li>
<li class='item-inactive'><a href='link3.html'>third item</a></li>
<li class='item-1'><a href='link4.html'>forth item</a></li>
<li class='item-0'><a href='link5.html'>fifth item</a>
</ul>
</div>
'''
html = etree.HTML(text)
r1 = html.xpath('//li[1]/ancestor::*')
#print(r1)
r2 = html.xpath('//li[1]/ancestor::div')
#print(r2)
r3 = html.xpath('//li[1]/attribute::*')
#print(r3)
r4 = html.xpath('//li[1]/child::a[@href="link1.html"]')
#print(r4)
r5 = html.xpath('//li[1]/descendant::a')
#print(r5)
r6 = html.xpath('//li[1]/following::*[2]')
#print(r6)
r7 = html.xpath('//li[1]/following-sibling::*')
print(r7)
