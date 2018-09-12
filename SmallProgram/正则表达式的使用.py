#3.3 正则表达式

### 1 实例引入
'''
http://tool.oschina.net/regex

'''

### 2 match() 常用匹配方法之一
'''
import re
content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}',content)
print(result)
print(result.group())
print(result.span())
'''

###### 匹配目标 提取内容
'''
import re
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^Hello\s(\d+)\sWorld',content)
print(result)
print(result.group())
print(result.group(1))
print(result.span())
'''

###### 通用匹配
'''
import re
content = 'Hello 123 4567 World_This is a Regex Demo'
result = re.match('^Hello.*Demo$',content)#其中$可以不加
print(result)
print(result.group())
print(result.span())
'''

###### 贪婪与非贪婪
'''
import re
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*(\d+).*Demo',content)
print(result)
print(result.group(1))
'''
'''
import re
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*?(\d+).*Demo',content)
print(result)
print(result.group(1))
'''
'''
import re
content = 'Hello 1234567 World_This is a Regex Demo'
result1 = re.match('^He.*?(\d+)(.*)',content)
result2 = re.match('^He.*?(\d+)(.*?)',content)
print('result1:')
'\n'
print(result1.group(2))
'\n'
print('result2:')
'\n'
print(result2.group(2))
'''

###### 修饰符
#
#import re
#content = '''Hello 1234567 World_This
#is a Regex Demo
#'''
#result = re.match('^He.*?(\d+).*?Demo$',content,re.S)
#print(result.group(1))
#


###### 转义匹配
'''
import re
content = '(百度)www.baidu.com'
result = re.match('\(百度\)www\.baidu\.com',content)
print(result)
'''


### 3 search()
# match一旦开头不匹配，那个整个匹配就会失败
# 例如：
'''
import re
content = 'Exrat stings Hello 1234567 World_This is Regex Demo Extra stings'
result = re.match('^Hello.*?(\d+).*?Demo',content)#开头^可以不加
print(result)
'''
'''
import re
content = 'Exrat stings Hello 1234567 World_This is Regex Demo Extra stings'
result = re.search('^Hello.*?(\d+).*?Demo',content)#开头^可以不加
print(result,result.group(1))
'''
### 4 finall()
#获取所有的

### 5 sub()
#去掉所有数字，本质上还是替换，但比replace()方法简洁很多
'''
import re
content = 'k35jjh34k5h3k4f4fjk4h5k4j45464jhje'
content = re.sub('\d+','',content)
print(content)
'''


### 6 compile()
#将正则字符串保存、编译成正则表达式对象，方便以后的复用
import re
c1 = '2017-12-15 12:00'
c2 = '2018-4-7 12:34'
c3 ='2018-7-22 13:38'
pattern = re.compile('\d{2}:\d{2}')
r1 = re.sub(pattern,'',c1)
r2 = re.sub(pattern,'',c2)
r3 = re.sub(pattern,'',c3)
print(r1,r2,r3,sep='\n')
