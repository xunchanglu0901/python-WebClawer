#网页解析

#5.urljoin

#合并

#后面的新链接代替原有旧链接

from urllib.parse import urljoin

print(urljoin('http://www.baidu.com','FAQ.html'))
print(urljoin('http://www.baidu.com','https://liujiwei.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html','https://liujiwei.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html','https://liujiwei.com/FAQ.html?question=2'))
print(urljoin('http://www.baidu.com?wd=abd','https://liujiwei.com/index.php'))
print(urljoin('http://www,baidu.com','?category=2#comment'))
print(urljoin('www.baidu.com','?category=2#comment'))
print(urljoin('www.baidu.com#comment','?category=2'))
