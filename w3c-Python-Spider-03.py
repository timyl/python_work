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



# 练习-爬取360搜索导航栏
print('-----------------------------------------')

# 目标URL
# www.so.com

import requests
from lxml import etree

url = 'https://www.so.com'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
response = requests.get(url, headers=headers)

if response.status_code == requests.codes.ok:
    print('请求成功')

# 定义selector
selector = etree.HTML(response.text)
# 取元素
# 1) 使用我们上边传统的方式xpath路径来取,结果是没问题的
tra_path = selector.xpath('//body/div[2]/header/section/nav/a[1]/text()')[0]
tra_path_href = selector.xpath('//body/div[2]/header/section/nav/a[1]/@href')[0]
print(tra_path) # 360导航
print(tra_path_href) # http://www.so.com/link?m=aQlkv%2BrmCbRODu%2BgRHnyuqF50H9Vyumk%2FW16hnzpUezyJrLA%2FgiDy0kYO9xZTQs3e

# 还可以简洁：因为nav是唯一的（我们可以通过查看网页源代码搜索得知）
tra_path_1 = selector.xpath('//*[@class="skin-text skin-text-tab"]/a[1]/text()')[0]
print(tra_path_1) # 360导航


# 2) 结合chrome浏览器的工具来取路径
# 具体做法，就是找到具体地方，右键copy->到xpath即可
chrome_xpath = selector.xpath('//*[@id="bd_tabnav"]/nav/a[2]/text()')[0]
print(chrome_xpath) # 资讯

chrome_xpath_nav = selector.xpath('//*[@id="bd_tabnav"]/nav/a/text()')
print(chrome_xpath_nav) # ['360导航', '资讯', '视频', '图片', '良医', '地图', '百科', '英文', '更多']

chrome_xpath_nav_href = selector.xpath('//*[@id="bd_tabnav"]/nav/a/@href')

# 可以使用for循环来遍历
for title, url in zip(chrome_xpath_nav, chrome_xpath_nav_href):
    print(title, url)


# 注意：以上的方式爬取不是万能的，因为对于一些动态生成的内容，例如JS生成的东西是不起作用的
# 例如：上边的结果中，'更多 javascript:void(0)'


print('--------------------------------')
# xpath高级用法-----------------------------
# 模糊匹配,以上边的htm为例
selector01 = etree.HTML(htm)
lis = selector01.xpath('//li[starts-with(@class, "item-")]/a/text()')
print(lis) # ['first item', 'second item', 'third item', 'fourth item']

str = selector01.xpath('string(//ul)')

# 找到所有string之后，可以继续用遍历方法处理
for item in str.split('\n'):
    if item.strip():
        print(item.strip())


# 列表推导式:
print([item.strip() for item in str.split('\n') if item.strip()])











