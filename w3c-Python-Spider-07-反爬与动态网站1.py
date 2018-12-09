#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/7 09:55
# @Author  : Geng zhi
# @File    : w3c-Python-Spider-07-反爬与动态网站1.py


# 常见的反爬虫策略以及应对技巧
'''
1：通过Headers识别反爬虫，或者Referer等参数
2：基于用户行为反爬虫,例如，短时间多次访问等行为
3：动态页面反爬虫，JavaScript、ajax等技术
4：其它，例如通过cookies进行反爬
'''

# 应对措施
'''
1: 添加Headers，例如：添加user-agent，或者referre policy等参数
2：使用IP代理或者加大请求间隔时间，但是代理IP需要自己去购买或者查找
3：使用selenium框架来爬取动态站点，这个框架可以模拟人工操作动作，缺点是速度是较慢的
'''

# 使用代理IP
# 代理IP：可以隐藏用户真实IP地址，突破IP访问限制，隐藏爬虫的真实IP

# 在Requests中使用代理IP
# 只需要加上proxies=proxies参数即可
'''
例如：设置代理ip字典
proxies = {"http": "http://10.10.1.10:3128", "https": "http://10.10.1.10:1080"}
requests.get("http://www.douban.com", proxies=proxies)
# 对于代理IP池，我们的处理办法是把每一个代理IP写成字典，然后都放入一个list中，最后调用的时候采用random方式去调用
'''

# 寻找代理IP
# 例如：西刺代理，www.xicidaili.com; 如下：
'''
Cn	139.129.207.72	808	北京	高匿	HTTPS	11天	不到1分钟
Cn	180.104.107.46	45700	江苏苏州	高匿	HTTPS	77天	不到1分钟
Cn	222.182.121.228	8118	重庆	高匿	HTTP	152天	不到1分钟
'''

import requests

proxies = {'https': 'https://101.132.142.124:8080'}
# response = requests.get('https://jsonip.com', proxies=proxies)

# if response.status_code == requests.codes.ok:
#     print('success!')

# 使用json()方法可以返回我们使用的IP地址，可以看到地址就是我们设置的代理
# print(response.json()) # {'ip': '101.132.142.124', 'about': '/about', 'Pro!': 'http://getjsonip.com', 'reject-fascism': 'Support the ACLU: https://action.aclu.org/secure/donate-to-aclu'}

# 注意：免费代理IP是很容易失效的

# 我们定义一个监测IP地址是否失效的函数
def check_ip(proxies):
    try:
        response = requests.get('https://jsonip.com', proxies=proxies)
    except:
        print('地址已经失效...')
    else:
        print('地址还可以用...')
        print(response.json())

# check_ip(proxies)


print('----------------------------------')
# 动态网页的爬取:-------------------
# 动态网页：一般使用ajax技术来实现网页异步更新;两条标准：1,是否在不刷新的情况下加载新信息，2,网页源代码结构与显示的不同
# 动态网页在后台进行大量的请求操作，我们可以利用这一点来爬取

# 动态网页爬取实例-微信文章的爬取
# 目标站点：https://weixin.sogou.com/
# 分析：例如"热门"标签下，没有分页，页面底部有"加载更多"按钮, 可以通过chrome来看，当点击后会向server发送什么？

# 结果：每当我们点击"加载更多"之后，都会发送相应的链接给server
'''
https://weixin.sogou.com/pcindex/pc/pc_0/2.html
https://weixin.sogou.com/pcindex/pc/pc_0/3.html
https://weixin.sogou.com/pcindex/pc/pc_0/4.html

'''
# 经过测试，以上这些链接我们可以单独在chrome中打开，说明是有效的链接；但是需要我们自己编码,因为他们脱离了主页，缺少了页面头部等信息

import requests
import re
from lxml import etree
import random
from string import punctuation  # 处理标点符号
import time

# 测试：
# url = 'https://weixin.sogou.com/pcindex/pc/pc_0/4.html'
# r = requests.get(url)
# r.encoding = 'utf-8'
# print(r.text)

# 完整代码：

# 1) 定义目标站点下载函数
def download(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

    # 定义代理池：
    proxies = [
        {'https': 'https://106.15.42.179:33543'},
        {'https': '115.148.173.121:808'},
        {'https': '183.63.123.3:56489'},
        {'https': '27.44.225.122:80'},
        {'https': '219.234.5.128:3128'}
    ]
    # response = requests.get(url, proxies=random.choice(proxies), headers=headers)
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    return etree.HTML(response.text)


# 2) 定义文章和保存函数
def article_detail(article_url):
    # 依然获取selector
    selector = download(article_url)
    title = selector.xpath('//h2[@class = "rich_media_title"]/text()')[0].strip()
    # 注意这里的content后边有个空格
    content = selector.xpath('string(//*[@class="rich_media_content "])').strip()
    # 调用保存函数
    data_writer(content, title)


def data_writer(content, title):
    # 标题中有标点符号竖线等符号替换为空，需要使用punctuation函数来处理一下;使用正则来处理，[]是或
    title = re.sub(r'[{}]+'.format(punctuation), '', title)
    # 写入：
    with open('./weixin_article/' + title + '.txt', 'wt', encoding='utf-8') as f:
        f.write(content)
        print('正在下载...', title)

# 3) 定义主函数
def spider(num):
    for i in range(1, num+1):
        url = 'http://weixin.sogou.com/pcindex/pc/pc_0/{}.html'.format(i)
        selector = download(url)
        all_article = selector.xpath('/html/body/li')
        for article in all_article:
            # 获取每篇文章的链接
            article_url = article.xpath('div[2]/h3/a/@href')[0]
            # 调用文章函数
            article_detail(article_url)


if __name__ == '__main__':
    spider(1)




