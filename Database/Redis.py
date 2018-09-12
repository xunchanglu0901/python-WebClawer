######      第二个常用NoSql：Redis      ######

# 3 连接Redis库
from redis import StrictRedis

redis = StrictRedis(host='localhost',port=6379 ,db=0)
#redis.set=('name','Bob')
#print(redis.get('name'))


#可以使用ConnectionPool连接


# 操作内容
'''
键操作
字符串操作
列表操作
集合操作
有序集合操作
散列操作
'''

# 10 RedisDump
###redis-dump
###redis-load
