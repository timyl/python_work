#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/7 09:55
# @Author  : Geng zhi
# @File    : w3c-Python-Spider-07.py


# 常见的反爬虫策略以及应对技巧
'''
1：通过Headers识别反爬虫，或者Referre Policy等参数
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