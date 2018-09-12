#!/usr/bin/env python
import re
import requests
import  lxml.html
url = 'https://movie.douban.com/top250?start={}&filter='
class DownloadUrl(object):
    def __init__(self,url):
        self.url = url
        self.head  = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36'}
        self.Alldata(self.url)

    def Alldata(self,url):
        content = requests.get(url,headers=self.head)
        content.encoding = 'utf-8'
        selector = lxml.html.fromstring(content.content)
        alldata = selector.xpath('//div[@class="info"]')
        self.Title(alldata)

    def Title(self,date):
        key = {}
        result = []
        for title in date:
            name = title.xpath('div[@class="hd"]/a/span[@class="title"]/text()')
            shortname = title.xpath('div[@class="hd"]/a/span[@class="other"]/text()')
            jianjie = title.xpath('div[@class="bd"]/p[@class=""]/text()')
            pingfen = title.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()')
            jingdian= title.xpath('div[@class="bd"]/p[@class="quote"]/span[@class="inq"]/text()')
            link = title.xpath('div[@class="hd"]/a/@href')
            key['title'] = ''.join(name + shortname)
            key['jianjie'] = ''.join(jianjie).strip()
            key['jingdian'] = ''.join(jingdian).strip()
            key['link'] = ''.join(link)
            result.append(''.join(key.values())+'\n')

        self.Writefile(result)

    def Writefile(self,file):
        text = open('DouBanUrl.txt','a+',encoding='utf-8')
        for f in file:
            text.write(f + '\n')
        text.close()

if __name__ =='__main__':
    for i in range(0,11):
        Douban = DownloadUrl(url.format(i * 25))
