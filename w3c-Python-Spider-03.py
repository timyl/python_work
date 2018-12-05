#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 20:13
# @Author  : Geng zhi
# @File    : w3c-Python-Spider-03.py


# 常用网页解析工具
# Lxml(xpath), Beautfulsoup, 正则表达式

# lxml是一个网页解析库，xpath是一种在xml文档中查找信息的语言，在xml中对元素进行遍历

# xpath路径表达式：
'''
/ 从根节点选取，类似于绝对路径
// 从根节点开始匹配，而不考虑他们的位置
/text() 选取文本
@ 选取属性
'''

import requests
from lxml import etree

# html例子：
htm = """
    <div>
        <ul>
            <li class='item-0'><a href='baidu.com'>first item</a></li>
            <li class='item-1'><a href='google.com'>second item</a></li>
            <li class='item-inactive'><a href='sougou.com'>third item</a></li>
            <li class='else-0'>else item</li>
        </ul>
    </div>
"""

# 获取网页
response = requests.get('https://www.douban.com/')

# 构造选择器对象selector
selector = etree.HTML(htm)

# 通过路径查找元素
# title = selector.xpath(htm)

# 定位所有li
all_li = selector.xpath('//div/ul/li')
print(all_li) # [<Element li at 0x102cb5848>, <Element li at 0x102cb5808>, <Element li at 0x102cb57c8>]

# 定位第一个li
first_li = selector.xpath('//div/ul/li[1]')
print(first_li) # [<Element li at 0x102cb5848>]

# 取文本
text_li = selector.xpath('//div/ul/li[1]/a/text()')
print(text_li) # ['first item']



