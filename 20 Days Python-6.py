#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/25 20:54
# @Author  : Geng zhi
# @File    : 20 Days Python-6.py

# 列表：
l1 = ['哈登', '保罗', '库里']
print(l1)
l1.insert(0, '詹姆斯')
print(l1)
l1.append('乔治')
print(l1)

# 练习：过滤指定价格手机

def filterByPrice(data, price):
    res = []

    for phone in data.split(','):
        name, value = phone.split(':')
        # print(value)
        if int(value) > price:
            res.append(phone)
            # print(res)
    return res

phoneprice = '魅族x8:1798, 红米6:849, 荣耀8X:1399, 小米8:2499, 小米8SE:2099, 荣耀长完7A:699'

print(filterByPrice(phoneprice, 1500))

print('##############################')

def int2list1(value):
    result = []
    items = str(value)
    for item in items:
        result.append(int(item))

    return result
print(int2list1(123))

def int2list2(value):
    result = []
    while value:
        num = value % 10
        result.insert(0, num)
        value = value//10

    return result

print(int2list2(123))

print('################################')

# 练习：价格排序
def getprice(item):
    name, price = item.split(':')
    return int(price)
phoneprice = '魅族x8:1798, 红米6:849, 荣耀8X:1399, 小米8:2499, 小米8SE:2099, 荣耀长完7A:699'

items = phoneprice.split(',')
print(items)
items.sort(key=getprice)
print(items)

print('###########################')

# 其他
l1 = [1, 2, 3]
l2 = l1.copy()
print(id(l1), id(l2))