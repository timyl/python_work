#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/8 11:28
# @Author  : Geng zhi
# @File    : w3c-Python-Spider-08-Selenium.py

# 练习：登陆新浪微博
# 1.登陆
# 2.解析当前页面
# 3.刷新页面提取新的内容
# 4.保存内容到csv


from selenium import webdriver
import csv
import time
import random
import hashlib


# 驱动设定
driver = webdriver.Chrome('./chromedriver/chromedriver')

# 定义一个微博的集合
weibo_set = set()

# 定义保存函数
def weibo_writer(item):
    # 去重代码：注意：
    md5 = hashlib.md5()
    md5.update(item.encode('utf-8'))
    # 计算哈希值
    weibo_md5 = md5.hexdigest()
    if weibo_md5 not in weibo_set:
        with open('webo.txt', 'at', encoding='utf-8', newline='') as f:
            f.write(item + '\n')
        # 最后保存新的哈希值到weibo_set，注意这里要用add()方法!!!
        weibo_set.add(weibo_md5)
        print(weibo_set)



# 定义登陆函数
# 注意：任何遇到浏览器需要加载的地方，最好都插入time等待代码片段
def login():
    driver.get('https://weibo.com/')
    # 这个sleep很重要！,selenium支持显式和隐式的等待，进官方文档，这里用的sleep()是最原始的方法
    time.sleep(6)
    # 定位登录框
    username = driver.find_element_by_id('loginname')
    username.send_keys('gongtixinyi@163.com')
    pass_word = driver.find_element_by_name('password')
    pass_word.send_keys('cisco123---')
    login_button = driver.find_element_by_xpath('//*[@class="W_btn_a btn_32px"]')
    login_button.click()
    time.sleep(random.randint(2, 4))


# if __name__ == '__main__':
#     driver = webdriver.Chrome('./chromedriver/chromedriver')
#     login('https://weibo.com/')


# 继续抓取微博文章
# 首先进入weibo，然后找到每篇文章对应的xpath，通过分析发现，文章对应的class="WB_text W_f14"，这样我们就可以利用find_elements_by_xpath
# 来返回一个文章的列表，然后写一个专门的函数来爬取

def spider():
    # 首先刷新一下微博首页，使用driver.get()即可
    driver.get('https://weibo.com/')
    time.sleep(5)
    all_weibo = driver.find_elements_by_xpath('//*[@class="WB_text W_f14"]')
    # 迭代文章
    for weibo in all_weibo:
        # 提取文本
        each_weibo = weibo.text

        # 调用weibo_writer函数
        weibo_writer(each_weibo)


if __name__ == '__main__':
    driver = webdriver.Chrome('./chromedriver/chromedriver')
    login()
    # 循环执行spider爬取微博
    while True:
        spider()
        time.sleep(30)

