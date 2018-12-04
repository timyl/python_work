#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/29 21:03
# @Author  : Geng zhi
# @File    : city.py

def print_city():
    print('this is beijing')

import time
def print_slow():
    for i in range(10):
        print(i)
        time.sleep(0.6)

# print_slow()