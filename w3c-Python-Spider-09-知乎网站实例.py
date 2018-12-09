#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/8 22:38
# @Author  : Geng zhi
# @File    : w3c-Python-Spider-09-知乎网站实例.py


# 爬取知乎网站用户信息实例
# 对象：知乎网站用户的昵称、行业、关注人数、粉丝人数

# 1) 分析站点
# a.知乎没有直接的页面显示所有的用户，但是我们通过自己的主页，还有关注的人可以实现一个递归的查找，采用这种方式可以爬取全部用户
# b.知乎follow页面的关注人网页源代码显示是JSON数据格式

# 代码：
import requests
import re
from lxml import etree
import json
import time, random
# 使用队列
import collections
import hashlib
# 引入mongodb库
import pymongo
from pymongo import MongoClient

url = 'https://www.zhihu.com/people/timyl/following'
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

# 建立MongoClient
client = MongoClient('localhost', 27017)
db = client.zhihu_db
collection = db.user

# 构建知乎单用户爬虫函数
def Spider(user_url):
    # 获取页面，构建xpath-selector
    response = requests.get(user_url, headers=headers)
    time.sleep(random.randint(1, 4))
    sel = etree.HTML(response.text)

    '''1)爬取following信息：单用户页面最重要的是获取跟随者的用户信息，因为跟随者才是爬取全站用户的关键'''
    # 提取follow页面JSON数据：使用re, 中间的(.*)代表所有的JSON数据
    pat = re.compile('<script id="js-initialData" type="text/json">(.*)</script><script src="https://static.zhihu.com/heifetz/vendor.7c9abc3e398528f8abf1.js"></script>')
    # 结果是列表，切片取JSON即可
    json_res = re.findall(pat, response.text)[0]
    # print(json_res)
    # 层层薄茧，可以得到关注的人的名字；通过这些名字就可以构造他们的follow页面了
    # print(json.loads(json_res).get('initialState')['entities']['users'].keys())
    # 构建following人名列表：
    f_name_list = list(json.loads(json_res).get('initialState')['entities']['users'].keys())
    # 最终following人员URL列表如下
    f_url_list = ['https://www.zhihu.com/people/' + username + '/following/' for username in f_name_list]
    # print(f_url_list)

    '''2)爬取但页面用户自己的信息'''
    # 用户名字
    personal_title = sel.xpath('//*[@class="ProfileHeader-name"]/text()')[0]
    # 用户专业
    personal_profession = sel.xpath('//*[@class="ProfileHeader-infoItem"]/text()')[0]
    # following人数
    followings = sel.xpath('//*[@class="NumberBoard FollowshipCard-counts NumberBoard--divider"]/a[1]/div/strong/text()')[0]
    # 关注自己的人数
    followers = sel.xpath('//*[@class="NumberBoard FollowshipCard-counts NumberBoard--divider"]/a[2]/div/strong/text()')[0]
    print(personal_title, personal_profession, followings, followers)

    '''3)插入到MongoDB数据库'''
    collection.insert_one({'name':personal_title, 'profession': personal_profession, 'followings': followings, 'followers': followers})

    '''4)最后不要忘了返回url列表'''
    return f_url_list

# 构建待爬取队列,并加入一个初始URl
waited_urls_queue = collections.deque()
waited_urls_queue.append('https://www.zhihu.com/people/timyl/following')


# 构建已经爬取的队列
finished_urls_set = set()

# 写一个循环处理队列URLs
while True:
    # popleft()方法，可以把队列中最左侧的url提取，并删除
    pop_url = waited_urls_queue.popleft()
    #
    try:
        f_urls = Spider(pop_url)
        '''3)队列处理'''
        # 队列处理：
        # 把爬取完的url加入已经爬取队列(finished_urls_queue)
        finished_urls_set.add(pop_url)
        # 将上边f_url_list这个URL列表转换成集合，然后减去已经爬取的队列集合，这样就做到了不重复爬取
        waited_urls = set(f_urls) - finished_urls_set
        # 最后加入到waited_urls_queue队列中
        waited_urls_queue.extend(waited_urls)
    except:
        pass


