#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/7 17:58
# @Author  : Geng zhi
# @File    : w3c-Python-Spider-07-反爬与动态网站2.py


# 综合实例---拉勾网站分析以及爬虫分析

# 目标网站：https://www.lagou.com/
# 目的：抓取"数据分析"职位全国的状况

# 1)分析过程：这里主要是分析拉钩网的反爬措施，以及如何应对
# 通过分析发现，例如我们搜索"数据分析"职位，而网站的搜索结果是500+，但是分页只到30页，一共才450个职位；我们可以查看拉钩网站的移动站点https://m.lagou.com
# 我们搜索数据分析；然后点击浏览更多，通过chrome可以得到如下的页面链接, 可以看到pageNO=4
# Request URL: http://m.lagou.com/search.json?city=%E5%85%A8%E5%9B%BD&positionName=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&pageNo=4&pageSize=15

# 问题：当我们把如上的链接输入到空白浏览器中却发现，站点返回如下错误：但是我们正常在m.lagou.com上的搜索页面点击"加载更多"就会正常显示
# {"success":false,"msg":"您操作太频繁,请稍后再访问","clientIp":"116.136.20.79"}

# 分析：通过chrome浏览器inspect的对比分析得知，我们单独访问这个分页链接headers中缺少了如下参数
# Referer: http://m.lagou.com/search.html

# 演示：
import requests
from lxml import etree
import time
import csv
import random


# # 这里pageNO=4
# url = 'http://m.lagou.com/search.json?city=%E5%85%A8%E5%9B%BD&positionName=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&pageNo=4&pageSize=15'
# # 定义headers：
# headers = {
#     # 添加referer
#     'Referer': 'http://m.lagou.com/search.html',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
# }
# # 获取页面
# response = requests.get(url, headers=headers)
# if response.status_code == requests.codes.ok:
#     print('success...')
#     # 获取文本：结果是JSON格式的数据
#     print(response.text)
#     # 还可以用json方法输出
#     print(response.json())

# 职位详情页的分析
# http://m.lagou.com/jobs/5359531.html
# 这里的5359531代表的是positionId，我们可以从搜索页面的结果中查到这个id，还有包括positionName，salary等

# 码代码
# 1) 保存函数
def csv_write(item, companyName):
    with open('lagou.csv', 'at', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        try:
            writer.writerow(item)
            print('正在爬取...', companyName)
        except Exception as e:
            print('写入错误:', e)

# 2) spider爬取函数
def spider(url):
    # 定义headers
    headers = {
        # 添加referer
        'Referer': 'http://m.lagou.com/search.html',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    # 定义cookies：这个cookies是根据网站策略，从消息中copy处理后拿到
    cookies = {
        '_ga': 'GA1.3.1578062898.1544176791',
        '_gid': 'GA1.2.1945854850.1544176791',
        'user_trace_token': '20181207175950-d6577d21-fa06-11e8-8daa-525400f775ce',
        'LGUID': '20181207175950-d6578243-fa06-11e8-8daa-525400f775ce',
        'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1544176791',
        'index_location_city': '%E5%85%A8%E5%9B%BD',
        'JSESSIONID': 'ABAAABAAAFDABFGE6E23D8D7A77D41CA27D12802253F34D',
        'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1544234700',
        '_gat': '1',
        'LGSID': '20181208100459-aabec6fd-fa8d-11e8-8dec-525400f775ce',
        'PRE_UTM': '',
        'PRE_HOST': '',
        'PRE_SITE': 'http%3A%2F%2Fm.lagou.com%2Fjobs%2F4512248.html',
        'PRE_LAND': 'http%3A%2F%2Fm.lagou.com%2Fsearch.html',
        'LGRID': '20181208100511-b1b0e8be-fa8d-11e8-8ce7-5254005c3644'
    }

    r = requests.get(url, headers=headers, cookies=cookies)
    # 加个random值
    time.sleep(random.randint(1, 3))
    # 返回页面
    return r

# 3) 搜索结果列表函数-主函数
def spider_list(list_url):
    # 调用spider下载搜索列表页面
    res = spider(list_url)
    res1 = res.json()
    print(res1)
    # 使用for循环来迭代JSON结果中的职位信息，并取出相应的职位详情关键字，例如地点、工资、职位ID等
    for comp in res1['content']['data']['page']['result']:
        city = comp.get('city')
        companyName = comp.get('companyName')
        createTime = comp.get('createTime')
        salary = comp.get('salary')
        positionId = comp.get('positionId')
        positionName = comp.get('positionName')

        # 关键步骤：构建职位详细的URL------------------------------
        position_url = 'http://m.lagou.com/jobs/' + str(positionId) + '.html'
        # print(position_url)
        # 再次调用spider爬取职位详情页面
        response = spider(position_url)
        # 构建selector
        selector = etree.HTML(response.text)
        # 例如chrome和xpath来查找一些关键职位信息：
        '''这里爆出了一个问题，就是在爬取这些workyear等信息时，出现为[]的情况，我们先用try，except来忽略
        这其实是网站反爬的策略之一，当检测到有爬虫行为的时候，会禁止一段时间，然后再放开，然后监测到再禁止
        网站是如何检测的呢？排除了headers和访问频率等原因，分析得知有可能是cookies原因，但是不确定，我们把
        拉钩网的cookies截取在下边
        '''
        try:
            workyear = selector.xpath('//span[@class="item workyear"]/span/text()')[0].strip()
        except:
            workyear = ''
        try:
            education = selector.xpath('//span[@class="item education"]/span/text()')[0].strip()
        except:
            education = ''
        # # 最后使用string()方法取出职位描述，使用string()就不需要切片了，但可以使用strip()去空
        try:
            jd = selector.xpath('string(//div[@class="content"])').strip()
        except:
            jd = ''
        # # 构建职位列表-------
        item = [positionId, positionName, companyName, city, salary, workyear, education, jd]

        # 调用写入函数
        csv_write(item, companyName)

# 4) 构建一个list_url列表
for i in range(1, 2):
    # 后边使用format
    url = 'http://m.lagou.com/search.json?city=%E5%85%A8%E5%9B%BD&positionName=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&pageNo={}&pageSize=15'.format(i)
    # 调用列表函数
    spider_list(url)

# cookies反爬分析：---------------------------
# 我们将chrome浏览器的历史浏览记录和cookies都清空，然后访问m.lagou.com，模拟第一次，然后抓取到response-header消息中，server端
# 会设置Set-Cookie:JSESSIONID=, 还有Set-Cookie:user_trace_token等参数，所以可以得知，这个站点正式用了cookies进行反爬虫
# 如下：使用firefox测试
# Set-Cookie: user_trace_token=2018120810151…Dec-2019 02:15:17 GMT; Path=/
# Set-Cookie: JSESSIONID=ABAAABAAAFDABFGA8DB…B76C280C36E; Path=/; HttpOnly


# cookies反爬中解决: -------------------------
# 采用复制cookies中的关键信息，首先我们使用函数来处理一个cookies
# def cookie_break(cookie):
#     coo = {}
#     for kv in cookie.split(';'):
#         # 有可能在value中还有=，这里我们就设定分割第一个等号即可
#         k, v = kv.split('=', 1)
#         coo[k.strip()] = v.replace('"', '')
#     return coo
#
# cookie = '_ga=GA1.2.1578062898.1544176791; _gid=GA1.2.1945854850.1544176791; user_trace_token=20181207175950-d6577d21-fa06-11e8-8daa-525400f775ce; LGUID=20181207175950-d6578243-fa06-11e8-8daa-525400f775ce; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1544176791; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAAAFDABFGE6E23D8D7A77D41CA27D12802253F34D; _ga=GA1.3.1578062898.1544176791; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1544234700; _gat=1; LGSID=20181208100459-aabec6fd-fa8d-11e8-8dec-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=http%3A%2F%2Fm.lagou.com%2Fjobs%2F4512248.html; PRE_LAND=http%3A%2F%2Fm.lagou.com%2Fsearch.html; LGRID=20181208100511-b1b0e8be-fa8d-11e8-8ce7-5254005c3644'
#
# cookies = cookie_break(cookie)
# 处理后结果：
'''
{'_ga': 'GA1.3.1578062898.1544176791',
 '_gid': 'GA1.2.1945854850.1544176791',
 'user_trace_token': '20181207175950-d6577d21-fa06-11e8-8daa-525400f775ce',
 'LGUID': '20181207175950-d6578243-fa06-11e8-8daa-525400f775ce',
 'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1544176791',
 'index_location_city': '%E5%85%A8%E5%9B%BD',
 'JSESSIONID': 'ABAAABAAAFDABFGE6E23D8D7A77D41CA27D12802253F34D',
 'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1544234700',
 '_gat': '1',
 'LGSID': '20181208100459-aabec6fd-fa8d-11e8-8dec-525400f775ce',
 'PRE_UTM': '',
 'PRE_HOST': '',
 'PRE_SITE': 'http%3A%2F%2Fm.lagou.com%2Fjobs%2F4512248.html',
 'PRE_LAND': 'http%3A%2F%2Fm.lagou.com%2Fsearch.html',
 'LGRID': '20181208100511-b1b0e8be-fa8d-11e8-8ce7-5254005c3644'}
'''
# 注意1：拿到这个cookies之后就可以在request中直接调用了；但是这个方式有缺点的，因为cookies中会有失效时间(叫max-age)，所以不能长时间运行
# 注意2：requests库一般是处理字典形式的参数，例如headers，所以cookies我们一般也要处理成字典，才能被调用


# 小结：目前为止关于反爬有以下几种方式
# 1) headers的添加(user-agent, referer等),cookies的处理和添加
# 2) 动态的IP代理池的使用
# 3) 爬取时间的控制(time.sleep(random.randint(2, 4)))

