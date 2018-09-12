#通过对象和数组的组合表示数据，轻量级

# 1 对象 和 数组
# 2 读取
import json
"""
str='''
[{
    "name":"Bob",
    "gender":"male",
    "birthday":"1994-09-09"
},{
    "name":"Selina",
    "gender":"female",
    "birthday":"1995-09-29"
}]
'''

"""
"""
print(type(str))
data = json.loads(str)
print(data,type(data))
print(data[0],data[0].get('name'),data[0].get('age',25))
"""
# 读取 转化 显示

with open('data.json','r') as file:
    sss = file.read()
    data = json.loads(sss)
    print(data)



# 输出JSON
"""
data='''
[{
    "name":"Bob",
    "gender":"male",
    "birthday":"1994-09-09"
},{
    "name":"Selina",
    "gender":"female",
    "birthday":"1995-09-29"
}]
'''
with open('data.json','w') as file:
    file.write(json.dumps(data,indent=2))#首行缩进2字符
    #如包含中文，会自动转化为Unicode字符格式
"""
