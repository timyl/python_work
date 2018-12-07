#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 09:44
# @Author  : Geng zhi
# @File    : w3c-Python-Spider-01.py

# 网页下载库
# urllib, requests(第三方库)

# 网页解析库
# 正则表达式，Lxml库(xpath配合chrome浏览器)，Beautiful Soup库（解析速度稍慢）

# 爬虫框架
# scrapy，pyspider，cola

# HTTP 请求：
# 请求方法(get,post，head，put，delete等)、
# 请求头部（包含client端环境信息，user agent等信息）、
# 请求正文


import requests

# get()方法
response = requests.get('http://www.douban.com/')
response1 = requests.get('http://www.baidu.com/')

# 使用text文本方式查看
# print(response.text)

# 使用response.status_code来查看状态码
print(response.status_code)

# status_code: HTTP状态码：三位数字
# 200(或者2开头)：请求成功
# 301(或者3开头)：资源被转移
# 404(或者4开头): 请求资源不存在
# 500(或者5开头): 服务器内部错误

# requests.codes.ok 用来跟response.status_code进行对比，如果一致，则代表请求成功，至于为什么不直接跟200对比，是因为
# 有可能是202，203都代表成功，所以这里为了方便，就引入一个codes.ok代表成功

if response.status_code == requests.codes.ok:
    print('网站请求成功!')

# 查看网站编码
print(response.encoding) # utf-8
print(response1.encoding) # ISO-8859-1

# 手动更改为utf-8
# response1.encoding = 'utf-8'
# print(response1.encoding)
# print(response1.text)

# response对象查看二进制相应
# print(response.content) # 可以看到里边的字符集charset="utf-8"

# 下载网页中的图片和定制请求头---------------
# image_url = 'https://www.baidu.com/img/xinshouye_77c426fce3f7fd448db185a7975efae5.png'
# response2 = requests.get(image_url)
# with open('baidu_logo.png', 'wb') as f:
#     # 使用二进制方式下载和写入
#     f.write(response2.content)


# 自定义header, 伪装成chrome浏览器;这里只添加了user-agent字段，还可以添加其它的headers参数,例如：这里又添加了host
headers = {
            'Host':'www.baidu.com',
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
            }
# 在requests中添加headers
response3 = requests.get('http://www.baidu.com', headers=headers)

# response对象中有个request方法，用于查看对应的request中的header信息：
print(response3.request.headers)
# print(response.request.headers)

# 注意：不指定user-agent，那么默认是类似这中样式，User-Agent': 'python-requests/2.20.1'，服务器看到这个，就会呵呵了，直接封掉

# 重定向、超时与传递URL参数--------------------
# url方法用于查看实际访问的网页地址
print(response.url) # https://www.douban.com/

# history方法可以看到发生了一次重定向
print(response.history) # [<Response [301]>]

# 设定超时:
# response4 = requests.get('https://notepad-plus-plus.org/', timeout=0.01)
# print(response4.status_code)

# 传递URL参数
response5 = requests.get('https://www.douban.com/search', params={'q':'python', 'cat':'1001'})
print(response5.url) # https://www.douban.com/search?q=python&cat=1001






