#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/5 22:17
# @Author  : Geng zhi
# @File    : w3c-Python-Spider-05.py

# 爬取网站

# 目标网站:大前端

import requests
from lxml import etree
import csv
import re

'''
base_url = 'http://www.daqianduan.com/page/'
# 构建整个72页的URL列表
whole_url = [base_url + str(x) for x in range(1, 2)]
# print(whole_url)

# 构建headers
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
# 注意：有的site还会检查其它头部的参数，这里值添加了一个user-agent的参数


# 主框架
# 1) 下载文章列表和时间

for url in whole_url:
    # 页码：
    page_num = re.search('\d+', url).group()
    # 获取网页
    response = requests.get(url, headers=headers)
    # 解析网页text源码，构建selector
    selector = etree.HTML(response.text)
    # 通过分析网页源码，发现每篇文章的属性class都是唯一标示，例如：excerpt excerpt-1，所以我们可以用//*的形式直接定位
    articles = selector.xpath('//*[starts-with(@class,"excerpt excerpt-")]')

    # 这里可以继续遍历每篇文章，注意这里没有用range()遍历，因为我们不知道最后一页有几篇
    for article in articles:
        # 接下来我们需要编写每一篇文章标题的xpath，注意：是相对的xpath；先用chrome复制一下实际的xpath
        # 这里有个技巧：先复制上一层article的xpath然后再复制标题的xpath，然后对比一下，看看相对路径是什么; 例如：
        # article_xpath = '/html/body/section/div[1]/div/article[1]'
        # title_xpath = '/html/body/section/div[1]/div/article[1]/header/h2/a'
        # time_xpath = '/html/body/section/div[1]/div/article[1]/p[1]/time'
        title = article.xpath('header/h2/a/text()')[0]
        time = article.xpath('p[1]/time/text()')[0]
        article_list = [title, time]
        # 注意：使用chrome直接复制的缺点：chrome复制的是从根目录一层一层复制的，不动态，一旦网站有变更，那么这个路径就会出错
        # 所以，我们自己写的例如 starts-with形式就一般不会出错

        # # 写入csv
        # with open('qianduan.csv', 'a') as csvfile:
        #     writer = csv.writer(csvfile)
        #     writer.writerow(article_list)
        #     print('正在爬取....', title)
'''


# 2) 下载文章内容和文章logo图片
# 我们需要对代码进行重构；例如：下载图片和内容分别用单独的函数来处理

# 全局参数：
base_url = 'http://www.daqianduan.com/page/'
# 构建整个72页的URL列表
whole_url = [base_url + str(x) for x in range(1, 5)]
# print(whole_url)

# 构建headers
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
# 注意：有的site还会检查其它头部的参数，这里值添加了一个user-agent的参数


# 保存函数
def csv_writer(article_list):
    # 指定编码，设定newline=''代表不要插入空格
    with open('qianduan.csv', 'a', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # 这里加入捕捉异常
        try:
            writer.writerow(article_list)
        except Exception as e:
            print('发生了错误', e)
        print('正在爬取....', article_list[0])

# 爬取网页的函数
def spider(url):
    # headers 我们在外边全局定义
    response = requests.get(url, headers=headers)
    # 直接就返回selector了
    return etree.HTML(response.text)

# 处理文章正文函数
def parse_article(article_url):
    # 再次调用spider函数处理页面
    selector = spider(article_url)
    # 获取文本内容，并返回
    return selector.xpath('string(//*[@class="article-content"])')

# 爬取文章logo图片函数:
def download_img(img_url, title):
    # 用二进制保存
    img = requests.get(img_url, headers=headers).content
    with open('./daqianduan_pic/' + title + ".jpg", 'wb') as f:
        f.write(img)

# 主函数
def parse(each_page_url):
    selector = spider(each_page_url)
    articles = selector.xpath('//*[starts-with(@class,"excerpt excerpt-")]')

    for article in articles:
        title = article.xpath('header/h2/a/text()')[0]
        time = article.xpath('p[1]/time/text()')[0]
        # 获得文章href地址
        article_url = article.xpath('header/h2/a/@href')[0]

        # 对文章详情用单独函数处理
        content = parse_article(article_url)
        # 调用保存函数
        csv_writer([title, time, content])
        # ------------
        # 图片的处理,img是article的xpath下边的，而且是唯一的;这里注意，用article继续解析，所以这里a前边不要加/，加了就是从根匹配了
        img_url = article.xpath('a/img/@src')[0]
        # 用单独函数处理图片,而且使用文章title来命名图片
        # download_img(img_url, title)

# 测试函数
if __name__ == '__main__':
    for url in whole_url:
        # 用正则截取页码:
        page_num = re.search('\d+', url).group()
        print('正在爬取第{}页-------'.format(page_num))
        parse(url)

