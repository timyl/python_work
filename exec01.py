#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/9 14:47
# @Author  : Geng zhi
# @File    : exec01.py

x = [True, True, False]
if any(x):
    print("at lease one True")

if all(x):
    print("Not one False")

if any(x) and not all(x):
    print("At least one True and one False")

