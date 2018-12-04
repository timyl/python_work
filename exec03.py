#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/9 15:31
# @Author  : Geng zhi
# @File    : exec03.py

print(abs(-10))
print(abs)

def add(x, y , f):
    return f(x) + f(y)

res = add (5, -6, abs)
print(res)

def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5])
print(r)
print(list(r))


from functools import reduce

def add(x, y):
    return x + y

res1 = reduce(add, [1, 2, 3, 4, 5])
print(res1)

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5}[s]

# print(char2num('2'))

res2 = map(char2num, '12345')
print(list(res2))

def fn(x, y):
    return x * 10 + y

res3 = reduce(fn, map(char2num, '12345'))
print(res3)

print('#########################')
def normalize(name):
    pass

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def is_odd(n):
    return n % 2 == 1

res4 = list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7]))
print(res4)

print(sorted([36, 12, 0, -1, 8, 5, 3]))
print(sorted([36, 12, 0, -1, 8, 5, 3], key=abs))

res5 = list(map(lambda x: x * x, [1, 2, 3, 4]))
print(res5)

from collections import Iterable
print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))

for i, value in enumerate(['1', 'a', 'c']):
    print(i, value)

list1 = [x * x for x in range(1, 11)]
print(list1)

list2 = [x * x for x in range(1, 11) if x % 2 == 0]
print(list2)

list3 = [m + n for m in 'ABC' for n in 'XYZ']
print(list3)

import os
list4 = [d for d in os.listdir('.')]
print(list4)