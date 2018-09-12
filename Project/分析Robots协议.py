#网页解析
#爬虫解析robots.txt
#是否可以爬去某网站

from urllib.robotparser import RobotFileParser

rp = RobotFileParser()


rp.set_url('http://www.jianshu.com/robots.txt')
rp.read()
#或者使用如下表达式
'''
from urllib.request import urlopen
rp.parse(urlopen('http://www.jianshu.com/robots.txt').read().decode('utf-8').split('\n'))
'''


print(rp.can_fetch('*','https://www.jianshu.com/'))
print(rp.can_fetch('*',"https://www.jd.com/"))
print(rp.can_fetch('Googlebot','https://www.jianshu.com/b73423e34'))
