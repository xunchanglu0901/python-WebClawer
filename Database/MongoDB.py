######      第一个常用NoSql：MongoDB      ######

import pymongo

# 2 连接工作

client = pymongo.MongoClient(host='localhost',port=27017)

#or
#client = MongoClient('mongodb://localhost:27017/')

# 3 指定数据库
db = client.test
#or
#db = client['test']


# 4 指定集合
#字典形式表示
collection =db.students
#collection =db['students']


# 5 插入数据
'''
student1 = {
    'id':'1',
    'name':'Mike',
    'age':25,
    'gender':'male'
}
student2 = {
    'id':'1',
    'name':'Qac',
    'age':45,
    'gender':'female'
}
#result = db.collection.insert(student1)
result = collection.insert([student1,student2])
print(result)
#或者db.collection.insert_one()###_many([,])
'''

# 6 查询

#result = collection.find_one({'name':'Mike'})
#print(result,type(result))
#results = collection.find({'id':'1'})
#print(results)
#for result in results:
#    print(result)


# 7 计数
#count = collection.find({'id':'1'}).count()
#print(count)

# 8 排序
#results = collection.find().sort('name',pymongo.ASCENDING)
#for result in results:
#    print(result)



# 9 偏移
"""
results = collection.find().sort('name',pymongo.ASCENDING).skip(2).limit(2)
for result in results:
    print(result)
"""
#skip忽略2个
#limit只要2个数据



# 10 更新
'''
condition = {'name':'Qac'}
student = collection.find_one(condition)
student['age'] = 26
#result = collection.update(condition,student)
#print(result)
'''
#只更新student字典内的字段
#result = collection.update(condition,{'$set':student})

# 官方标准update用法如下
'''
condition = {'name': 'Qac'}
student = collection.find_one(condition)
student['age'] = 14
result = collection.update_one(condition, {'$set': student})
print(result)
print(result.matched_count, result.modified_count)
'''

# 查询年龄条件，并集体加一 /以下方法只能更改查询到的第一条
'''
condition = {'age': {'$gt': 20}}
result = collection.update_one(condition, {'$inc': {'age': 1}})
print(result)
print(result.matched_count, result.modified_count)
'''
# 以下方法可以更改查询到的所有数据
'''
condition = {'age': {'$gt': 20}}
result = collection.update_many(condition, {'$inc': {'age': 1}})
print(result)
print(result.matched_count, result.modified_count)
'''

# 11 删除
'''
#remove方法
result = collection.remove({'name':'Qac'})
print(result)
#delete方法
result = collection.delete_one({'name': 'Mac'})
print(result)
print(result.deleted_count)
result = collection.delete_many({'age': {'$lt': 15}})
print(result.deleted_count)#删除的数据个数
'''


