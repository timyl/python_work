#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/5 14:48
# @Author  : Geng zhi
# @File    : w3c-Python-Spider-04.py


# Beautifulsoup
# 特点：python编写，但是运行速度稍慢

from bs4 import BeautifulSoup

# 举例：
htm = """
    <div>
        <ul>
            <li class='item-0'><a href='baidu.com'>first item</a></li>
            <li class='item-1'><a href='google.com'>second item</a></li>
            <li class='item-inactive'><a href='sougou.com'>third item</a></li>
            <li class='item-0'><a href='cctv.com'>fourth item</a></li>
            <li class='item-1'><a href='sina.com'>fifth item</a></li>
            <li class='else-0'>else item</li>
        </ul>
    </div>
"""

# 创建选择器，类似selector; 参数需要传入解析库，支持lxml, html等解析库,默认是html
soup = BeautifulSoup(htm, 'lxml')

# 选择元素方式,这里根xpath的区别就是，使用soup选择器，直接就能返回html元素代码，而xpath是返回元素对象
# 1)使用"点"来选取--------
print(soup.ul)
# 如果有多个标签，默认返回第一个li标签
print(soup.li)
# 以此类推，取文本
print(soup.li.a.string)
# 查属性
print(soup.a['href']) # baidu.com
print(soup.a.get('href')) # baidu.com

# 2)使用find_all()方法,注意：finall_all结果的切片是从0开始的，这个根xpath不同
print(soup.find_all('a')[0])
print(soup.find_all('a')[0].string)

# fina_all简写方式,直接省略
print(soup('a'))
print(soup('a')[0].string)

# 3)通过属性查找
print('---------------------------')
# 注意：这里为了根python中类的关键字相区别，使用class_来替代
print(soup(class_='else-0'))
print(soup(href='sina.com')[0].string)

# 4)正则表达式方式查找
import re
res = soup(class_=re.compile('item-'))
print(res[0])

# 5)get_text()方法取文本
res1 = soup.ul.get_text()
print([x.strip() for x in res1.split('\n') if x.strip()])

# 注意：其实点这种方法就是find的含义


# 正则表达式--------------------------------------------------------
print('-------------------------------------------------------')

import re

text = 'Beautiful is better than ugly/, Explicit is better than implicit, double click 666'

# 1) match()方法,注意：match()方法只能匹配开头,而且需要使用group()方法来取出内容
print(re.match('Beautiful', text).group())  # Beautiful
# 根据自己写的模式来匹配
print(re.match('\w+ is \w+', text).group())  # Beautiful is better
# 分组匹配，0代表全部结果
print(re.match('(\w+) is (\w+)', text).group(0)) # Beautiful is better
print(re.match('(\w+) is (\w+)', text).group(1)) # Beautiful
print(re.match('(\w+) is (\w+)', text).group(2)) # better

# 2) search()方法，会遍历整个字符串，返回第一个匹配的内容
# span()取范围
print(re.search('ugly', text).span())  # (25, 29)
# group()取内容
print(re.search('ugly', text).group()) # ugly
# 再练习下分组匹配
print(re.search('is (\w+)', text).group(0)) # is better
print(re.search('is (\w+)', text).group(1)) # better

# 3) sub()替换方法, 默认替换全部，可以通过count参数控制
print(re.sub('better', 'greater', text, count=1))
print(re.sub(', double.*', '', text)) # Beautiful is better than ugly, Explicit is better than implicit

# 4) split()方法，分割,根据自己编写的模式来匹配
print(re.split(',', text)) # ['Beautiful is better than ugly', ' Explicit is better than implicit', ' double click 666']

# 5）findall()方法，最重要的方法，找到所有匹配的结果;返回的是可迭代对象 list形式
print(re.findall('than \w+', text))  # ['than ugly', 'than implicit']

# compile()方法，函数
# 用于编译一个模式，然后再调用; 这样做的好处是如果匹配任务比较多，这样做会增速
self_pattern = re.compile('than \w+')
print(re.findall(self_pattern, text)) # ['than ugly', 'than implicit']
# 也可以：总之很灵活
print(re.compile('than \w+').findall(text)) # ['than ugly', 'than implicit']

# 正则表达式模式参考
# http://www.runoob.com/python/python-reg-expressions.html

# 例如查找/前边的字符
print(re.compile(r'(\w+)\/').findall(text)) # ['ugly']


# 正则表达式-提取网页源代码-------------------------------------
# 网页源码
html = '''
<html>
    <head>
        <base href='http://www.baidu.com/' />
        <title>testing website</title>
    </head>
    <body>
        <div id='images'>
            <a href='image1.html'>Name: My image 1 <br /><img src='image1_thumb.jpg' /></a>
            <a href='image2.html'>Name: My image 2 <br /><img src='image2_thumb.jpg' /></a>
            <a href='image3.html'>Name: My image 3 <br /><img src='image3_thumb.jpg' /></a>
            <a href='image4.html'>Name: My image 4 <br /><img src='image4_thumb.jpg' /></a>
            <a href='image5.html'>Name: My image 5 <br /><img src='image5_thumb.jpg' /></a>
        </div>
    </body>
</html>
'''

# 提取目标：
# 1)提取文本
# 这里使用正则 .*
res = re.compile("'image1.html'>(.*)<br /><img src='image1_thumb.jpg' />").findall(html)
print(res) # ['Name: My image 1 ']
# 改良
res1 = re.compile("'image1.html'>Name:(.*)<br />").findall(html)
print(res1) # [' My image 1 ']

res2 = re.compile(".html'>Name:(.*)<br />").findall(html)
print(res2) # [' My image 1 ', ' My image 2 ', ' My image 3 ', ' My image 4 ', ' My image 5 ']

# 2)提取属性：
res3 = re.compile("a href='(\w+.\w+)").findall(html)
print(res3) # ['image1.html', 'image2.html', 'image3.html', 'image4.html', 'image5.html']







