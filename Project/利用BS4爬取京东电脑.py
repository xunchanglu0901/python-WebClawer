import requests
from bs4 import BeautifulSoup

# 获取网页信息
def getHtmlText(url):
    try:
        r =requests.get(url)

        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print('success')
        return r.text
    except:
        print('false')
        return 'false'

# 解析网页数据， 获取有用信息
def parseHtml(goods_data, html):
    soup = BeautifulSoup(html, 'lxml')
    lis = soup.find_all('li', class_="gl-item")
    print(len(lis))
    for i in range(len(lis)):
        try:
            # 获取商品信息 div 中的第一个 a 标签， 获取 title 属性值
            title = lis[i].a['title']
            # print(title)
            # 获取商品的价格信息
            price = lis[i].find('div', class_='p-price').i.string
            # print(price)
            goods_data.append([title, price])
        except:
            print('')

# 显示数据
def displayHtmlGoods(goods_data):
    std = r'{0:^100}{1:^8}'
    print(std.format('商品名称', '价格'))
    for i in range(len(goods_data)):
        print(std.format(goods_data[i][0], goods_data[i][0]))

def main():
    url_basic = 'https://search.jd.com/Search?keyword='
    total_pages = 3 # 需要爬取的总页数
    keyword = '电脑' # 关键字

    goods_data = []
    for i in range(total_pages):
        page = 1 + i * 2 
        url = url_basic + keyword + '&enc=utf-8&wq=' + keyword + '&page=' + str(page)
        print(url)
        html = getHtmlText(url)
        parseHtml(goods_data, html)

    displayHtmlGoods(goods_data)

if __name__ == '__main__':
    main()
