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
            <li class='item-0'><a href='cctv.com'>fourth item</a></li>
            <li class='else-0'>else item</li>
        </ul>
    </div>
"""

# 获取网页
response = requests.get('https://www.douban.com/')

# 构造选择器对象selector
selector = etree.HTML(htm)

# 1）通过路径查找元素-----------------------------------------
# title = selector.xpath(htm)

# 定位所有li
all_li = selector.xpath('//div/ul/li')
print(all_li) # [<Element li at 0x102cb5848>, <Element li at 0x102cb5808>, <Element li at 0x102cb57c8>]

# 定位第一个li
# 注意：在xpath中分片是从1开始的
first_li = selector.xpath('//div/ul/li[1]')
print(first_li) # [<Element li at 0x102cb5848>]

# 取文本：使用text()方法
# text_li = selector.xpath('//div/ul/li[1]/a/text()')
# 对于这种唯一的标签，我们可以直接从根节点定位，例如ul标签是唯一的，所以可以不加div
text_li = selector.xpath('//ul/li[1]/a/text()')
print(text_li) # ['first item']

# 举例说明这个//取值的原理：例如北京首都体育学院，我们一般不说北京市海淀区北三环100号首体，我们一般直接说首体
# 所以这种方式依然可以取出我们想要的值,//就是从根节点直接定位元素
li1 = selector.xpath('//li[1]/a/text()')
print(li1) # first item


# 2）通过属性查找元素--------------------------------------
# 例如：找li3，注意：class写法
# li3 = selector.xpath('//li[@class="item-inactive"]/a/text()')

# 还可以如下方式：用*号代替li
# li3 = selector.xpath('//*[@class="item-inactive"]/a/text()')

# 再简单一步，还可以,因为href的值是唯一的
li3 = selector.xpath('//*[@href="sougou.com"]/text()')
print(li3)


# 3）获取属性值----------------------
class_a = selector.xpath('//li[2]/a/@href')
print(class_a) # ['google.com']

class_li = selector.xpath('//li/@class')
print(class_li) # ['item-0', 'item-1', 'item-inactive', 'item-0', 'else-0']

text_all = selector.xpath('//li/a/text()')
print(text_all) # ['item-0', 'item-1', 'item-inactive', 'item-0', 'else-0']

# 注意：可以在一个元素中持续使用xpath，但是这里提示：后边需要加[0]先把element从list中拿出来再继续使用
li4 = selector.xpath('//li[4]')[0]
print(li4)
# 继续使用xpath
text_li4 = li4.xpath('a/text()')
print(text_li4) # ['fourth item']











