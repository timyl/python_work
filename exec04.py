#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/11 16:10
# @Author  : Geng zhi
# @File    : exec04.py

print(ord('A'))
print(ord('你'))
print(chr(100))
print(chr(25991))

# encode
print('ABC'.encode('ascii'))
print('ABC'.encode('utf-8'))
print('你好'.encode('utf-8'))

# decode
print(b'ABC'.decode('ascii'))
print(b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode('utf-8'))

s1 = 72
s2 = 85

r = 1 - s1 / s2
print(r)
print('his increase rate is %.1f%%' % r)

d1 = {'name':'geng', 'age':33, 'job':'engineer'}
print(d1.get('sex', 'male'))
print(d1.get('name'))

print(d1.pop('job'))

# set
s1 = set([1, 2, 3])
print(s1)

# bultin function


# self-defined func
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    if x < 0:
        return -x

# print(my_abs('A'))
print(my_abs(-10))
