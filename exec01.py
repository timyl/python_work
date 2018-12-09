#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/9 14:47
# @Author  : Geng zhi
# @File    : exec01.py

x = [True, True, False]
if any(x):
    print("at lease one True")

if all(x):
    print("Not one False")

if any(x) and not all(x):
    print("At least one True and one False")

import hashlib

s1 = set()

l1 = ['jack', 'jean', 'jack', 'frank']
l2 = []

for item in l1:
    m = hashlib.md5()
    m.update(item.encode('utf-8'))
    name = m.hexdigest()
    l2.append(name)
    s1.add(name)

print(l2)
print(s1)


