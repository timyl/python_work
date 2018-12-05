#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 19:13
# @Author  : Geng zhi
# @File    : w3c-Python-Spider-02.py


# Urllib库

# urllib库四个模块：
# urllib.request,打开和读取URL
# urllib.error包含urllib.request各种错误模块
# urllib.parse 解析URL
# urllib.robotparse，解析网站的robots.txt文件，这个文件定义了哪些内容允许被爬取

# urllib库的使用-----------------------
from urllib.request import urlopen

html = urlopen('https://www.douban.com')
response = html.read() # 返回二进制内容响应
print(response)

# 解码：
# print(response.decode('utf-8'))

# 传递URL参数---------------------------
import urllib.request
import urllib.parse

# parse用于解析网址
payload = {'q':'python', 'cat':'1001'}
request_url = 'https://www.douban.com/search'

# 先进行编码
payload_encode = urllib.parse.urlencode(payload)
real_url = request_url + '?' + payload_encode

response1 = urllib.request.urlopen(real_url)
# 查看我们构造的url
print(response1.url) # https://www.douban.com/search?q=python&cat=1001

# 最后读取response并解码
# print(response1.read().decode('utf-8'))

# 查看状态码：
print(response1.getcode()) # 200


# urllib库添加自定义headers---------------------------
# 依然以chrome为例:
import urllib.request
import urllib.parse

url = 'https://www.douban.com'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

# 构造请求头：创建一个request对象res，包含网址和头
res = urllib.request.Request(url, headers=headers)

# 使用urlopen来打开网址，并读取
response2 = urllib.request.urlopen(res).read()


# 向一个网站POST数据-------------------------
from urllib import request, parse
# 构造POST数据
post_data = parse.urlencode([('key1', 'val1'), ('key2', 'val2')])
# 构造请求对象
base_url = urllib.request.Request('https://httpbin.org/post', post_data)
# 添加头信息
base_url.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36')
# print(base_url)

# 向网站发起请求，并返回response
response3 = urllib.request.urlopen(base_url, data=post_data.encode('utf-8')).read()

# 最后解码打印
print(response3.decode('utf-8'))

# urljoin函数用于拼接URL
from urllib.parse import urljoin
