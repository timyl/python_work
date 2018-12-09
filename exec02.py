#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/9 15:12
# @Author  : Geng zhi
# @File    : exec02.py

from prettytable import PrettyTable
table = PrettyTable(["animal", "ferocity"])
table.add_row(["wolverine", 100])
table.add_row(["grizzly", 87])
table.add_row(["Rabbit of Caerbannog", 110])
table.add_row(["cat", -1])
table.add_row(["platypus", 23])
table.add_row(["dolphin", 63])
table.add_row(["albatross", 44])
table.sort_key("ferocity")
table.reversesort = True

print(table)


# 集合练习：
urls =['https://www.zhihu.com/people/Germey/following/', 'https://www.zhihu.com/people/bei-jing-qian-feng-hu-lian-ke-ji-you-xian-gong-si/following/', 'https://www.zhihu.com/people/aws-54/following/', 'https://www.zhihu.com/people/mingxinglai/following/', 'https://www.zhihu.com/people/xiao-hong-hui-15/following/', 'https://www.zhihu.com/people/crossin/following/', 'https://www.zhihu.com/people/timyl/following/']
s1 = set(urls)
print(s1)

s2 = set()
s2.add('https://www.zhihu.com/people/Germey/following/')
print(s2)

print(list(s1 - s2))





