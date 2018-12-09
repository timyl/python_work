#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/26 10:40
# @Author  : Geng zhi
# @File    : w3c-Python-Basic-03.py


# 爬虫
# requests库,第三方库
import requests
from lxml import etree
import csv
import time, random

response = requests.get('http://www.daqianduan.com/')
print(response) # <Response [200]>
# print(response.text)

# 使用etree来构造选择器，然后使用xpath来选择元素就可以了
selector = etree.HTML(response.text)
# 在chrome浏览器中右键选择要查找的内容，然后copy到xpath，最后复制到这里，注意：xpath路径最后要加/text()
res = selector.xpath('/html/body/section/div[1]/div/article[1]/header/h2/a/text()')
print(res) # ['BAT究竟需要的是怎样的工程师？']
print(type(res)) # <class 'list'> 列表形式，所以后边用到的时候，需要使用分片来提取需要的元素

# 目标：爬取大前端前5页的文章题目和发布时间
# 分析：每页中题目和发布时间这个操作是一个循环，后4页的操作又是一个大循环
# 即：对网页做循环，然后对每一篇文章左循环，然后提取每一篇文章的题目和时间

# step1:
# article_first = selector.xpath('/html/body/section/div[1]/div/article[1]')
# article_last = selector.xpath('/html/body/section/div[1]/div/article[11]')


# step2:
# for i in range(1, 11):
    # article, article_title, article_time 注意：结果都是列表，需要取第一个元素
    # article = selector.xpath('/html/body/section/div[1]/div/article[{}]'.format(i))[0]
    # 注意：这里header前边不能加/
    # article_title = article.xpath('header/h2/a/text()')[0]
    # article_time = article.xpath('p[1]/time/text()')[0]
    # print('文章标题: {:-<55} 创建时间 {}'.format(article_title, article_time))

# 爬虫函数
def spider(url):
    response = requests.get(url)
    # time.sleep(random.randrange(1, 2))
    time.sleep(2)
    selector = etree.HTML(response.text)
    for i in range(1, 12):
        article = selector.xpath('/html/body/section/div[1]/div/article[{}]'.format(i))[0]
        article_title = article.xpath('header/h2/a/text()')[0]
        article_time = article.xpath('p[1]/time/text()')[0]
        item = [article_title, article_time]

        # 调用保存函数
        csv_writer(item)

# 写入文件
def csv_writer(item):
    # 这里注意如果用excel打开csv会乱码，所以这里使用gbk来编码
    with open('daqianduan.csv', 'at', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(item)
        print('正在下载.....', item)

# 爬取1-4页新闻
for page_n in range(1, 5):
    url = 'http://www.daqianduan.com/page/{}'.format(str(page_n))
    spider(url)


# random 模块
'''
print( random.randint(1,10) )        # 产生 1 到 10 的一个整数型随机数  
print( random.random() )             # 产生 0 到 1 之间的随机浮点数
print( random.uniform(1.1,5.4) )     # 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数
print( random.choice('tomorrow') )   # 从序列中随机选取一个元素
print( random.randrange(1,100,2) )   # 生成从1到100的间隔为2的随机整数

a=[1,3,5,6,7]                # 将序列a中的元素顺序打乱
random.shuffle(a)
print(a)
'''