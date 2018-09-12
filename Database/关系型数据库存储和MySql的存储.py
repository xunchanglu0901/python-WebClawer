# 2 连接数据库

import pymysql
#记得在cmd启动mysql 代码net start mysql
'''
db=pymysql.connect(host='localhost',user='root',password='123234',port=3306)
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('Database version:',data)
#cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
db.close()
'''
# 3 创建表格
'''
db=pymysql.connect(host='localhost',user='root',password='123234',port=3306,db='spiders')
cursor = db.cursor()
sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
cursor.execute(sql)
db.close()
'''

# 4 添加数据
"""
id = '2018001'
user = 'Bob'
age =20
db = pymysql.connect(host='localhost',user='root',password='123234',port=3306,db='spiders')
cursor = db.cursor()
sql = 'INSERT INTO students(id.name,age) values(%s,%s,%s,)'
try:
    cursor.execute(sql,(id,user,age))
    db.commit()
except:
    db.rollback()
db.close()
"""

### 动态改写
"""
db = pymysql.connect(host='localhost',user='root',password='123234',port=3306,db='spiders')
data = {
    'id':'2018001',
    'name':'Bob',
    'age':20
    }
table = 'students'
keys = ', '.join(data.keys())
values= ', '.join(['%s'] * len(data))
sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
try:
    if cursor.execute(sql,tuple(data.values())):
        print('成功')
        db.commit()
except:
    print('失败')
    db.rollback()
db.close()
"""


# 5 更新数据
db = pymysql.connect(host='localhost',user='root',password='123234',port=3306,db='spiders')
"""
data = {
    'id':'2018001',
    'name':'Bob',
    'age':24
    }
table = 'students'
keys = ', '.join(data.keys())
values= ', '.join(['%s'] * len(data))

sql = ' INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table,keys=keys,values=values)
updata = ','.join([" {key} = %s".format(key=key) for key in data])
sql += updata
try:
    if cursor.execute(sql,tuple(data.values())*2):
        print('成功')
        db.commit()
except:
    print('失败')
    db.rollback()
db.close()
"""

# 6 删除数据
"""
table = 'students'
condition = 'age > 10 '
sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table, condition=condition)
try:
    if cursor.execute(sql):
        print('成功')
        db.commit()
except:
    print('失败')
    db.rollback()
db.close()
"""

# 7 查询数据
sql = 'SELECT * FROM students WHERE age >= 15'
"""
try:
    cursor.execute(sql)
    print('Count:',cursor.rowcount)
    one = cursor.fetchall()
    print('One:',one)
    results = cursor.fetchall()
    print('Results:',results)
    print('Results Type:',type(results))
    for row in results:
        print(row)
        #由于一开始的指针偏移一次的原因，只显示第二条到最后一条的数据
except:
    print('Error')
"""
### 获取所有数据 通过while循环可以获取从第一条到最后一条的所有数据 随用随取 简单高效
try:
    cursor.execute(sql)
    print('Count:',cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print('Row:',row)
        row = cursor.fetchone()
except:
    print('Error')
