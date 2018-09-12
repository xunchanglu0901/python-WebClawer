import csv

# 1 写入
"""
with open('data.csv','w',encoding='utf-8') as csvfile:#防止中文乱码，加入encoding参数
    writer = csv.writer(csvfile)
    writer.writerow(['id','name','age'])
    writer.writerow(['10001','Mike',20])
    writer.writerow(['10002','Bob',21])
    writer.writerow(['10003','Jordan',22])
"""
# or writerows (write + row:行)
"""
with open('data1.csv','w') as csvfile:
    writer = csv.writer(csvfile,delimiter=' ')#修改分隔符后，由于本身是，分隔，所以[]的内容写入在了CSV中的同一个单元格
    writer.writerow(['id','name','age'])
    writer.writerows([['10001','Mike',20],['10002','Bob',21],['10003','Jordan',22],['10003','Jordan',22]])
"""

# 爬虫获取的数据，一般都是结构化数据，一般用字典表示，所以上述代码改写如下：
'''
with open('data2.csv','w') as csvfile:
    fieldnames = ['id','name','age']
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id':'1','name':'Mike','age':14})
    writer.writerow({'id':'2','name':'SIke','age':34})
    writer.writerow({'id':'3','name':'Dike','age':24})
'''

# 追加写入时需要把'w'换成'a'


# 2 读取

with open('data.csv','r',encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)


### 方法二
import pandas as pd
df = pd.read_csv('data2.csv')
print(df)
