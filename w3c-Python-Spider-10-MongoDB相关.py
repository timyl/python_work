#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/9 11:31
# @Author  : Geng zhi
# @File    : w3c-Python-Spider-10-MongoDB相关.py


# 之前使用集合去重，但是有缺点的，一旦断电队列就不存在了
# MongoDB：非关系行数据库，key/value形式

# 安装：macOS可以直接使用brew install mongodb
# 参考链接：https://www.jianshu.com/p/7241f7c83f4a
# 安装完成之后：直接mongod命令就可以启动了；也可以加参数 --dbpath=,例如：
# mongod --dbpath=/Users/timyl_geng/PycharmProjects/python_work/data/db
# mongodb监听端口为27017

# python环境需要安装pymongo库，用来驱动mongodb数据库
import pymongo
from pymongo import MongoClient

# 连接数据库
client = MongoClient()
# 可以看到log已经连接：type: "Darwin", name: "Darwin", architecture: "x86_64", version: "10.13.6" }, platform: "CPython 3.7.0.final.0" }

# 还可以详细指定：
# client = MongoClient('localhost', 27017)

# MongoDB可视化软件
# https://www.robomongo.org/download

# 代码创建数据库
db = client.zhihu_db
# 注意1：mongodb属于惰性数据库，只有在当插入数据的时候，数据库才被创建
# 注意2：在MongoDB中，你也不需要创建集合。当你插入一些文档时，MongoDB会自动创建集合

# 指定一个知乎user的集合（注意：暂时不被创建，只有当插入文档的时候才会被创建）
collection = db.user
# 创建用户，和插入单条数据
# student1 = {'name': 'Jean', 'age': '30'}
# collection.insert_one(student1)

# student2 = {'name': 'Geng', 'age': '32', 'height': 180}
# collection.insert_one(student2)

# mongodb命令行查看：
# 具体参考：http://www.runoob.com/mongodb/mongodb-tutorial.html
'''
> show dbs
admin     0.000GB
config    0.000GB
local     0.000GB
zhihu_db  0.000GB
> use zhihu_db
switched to db zhihu_db
> show collections
user

> db.user.find()
{ "_id" : ObjectId("5c0cb8cf9dcb98345e466d2a"), "name" : "Jean", "age" : "30" }
{ "_id" : ObjectId("5c0cb9809dcb9834929fea68"), "name" : "Jean", "age" : "30" }
{ "_id" : ObjectId("5c0cb9809dcb9834929fea69"), "name" : "Geng", "age" : "32", "height" : 180 }
>
'''

# 其它方法
student3 = {'name': 'Frank'}
student4 = {'name': 'Markies'}
# 一次插入多条数据，放到一个列表中
# collection.insert_many([student3, student4])

# 查询用户：
print(collection.find_one({'name': 'Geng'}))
# {'_id': ObjectId('5c0cb9809dcb9834929fea69'), 'name': 'Geng', 'age': '32', 'height': 180}

# 改写知乎爬虫，保存用户信息到mongodb


