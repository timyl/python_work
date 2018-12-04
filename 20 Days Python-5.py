#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/25 17:10
# @Author  : Geng zhi
# @File    : 20 Days Python-5.py

# 练习1：查找置顶字符串位置，返回索引值

s = 'c++pythonjava'
substr = 'python'

index = 3
lens = len(substr)

tmp = s[index:index + lens]

print('tmp = {}, substr = {}, index = {}'.format(tmp, substr, index))
if tmp == substr:
    print('find {} in {} index={}'.format(substr, s, index))
else:
    print('not found')

def myfind(data, substr):
    index = 0

    datalens = len(data)
    lens = len(substr)

    while True:
        if datalens-index < lens:
            return -1

        tmp = data[index:index + lens]
        print('tmp = {}, substr = {}, index = {}'.format(tmp, substr, index))
        if tmp == substr:
            print('find {} in {} index = {}'.format(substr, data, index))
            return index
        else:
            print('not found')
        index += 1

source = 'c++pythonjava'
substr = 'python'
index = myfind(source, substr)

print(index)


print('###########################################')

# 练习2：计算器小工具
def rtoarea(r):
    pi = 3.14
    return pow(r, 2)*pi

def dollartormb(dollar):
    rate = 6.9367
    return dollar * rate

def kmtomile(km):
    ratio = 0.6213712
    return km * ratio

def main():
    while True:
        tips = '1:输入半径输出面积\n2:输入美元输出RMB\n3:输入公里输出英里\nq:退出\n'
        cmd = input(tips)

        if cmd == '1':
            r = input('输入半径：')
            print(rtoarea(float(r)))
        elif cmd == '2':
            dollar = input('输入美金：')
            print(dollartormb(float(dollar)))
        elif cmd == '3':
            km = input('输入公里：')
            print(kmtomile(float(km)))
        elif cmd == 'q':
            print('推出')
            break
        else:
            print('请按照提示输入！')

#if __name__ == '__main__':
#    main()

print('##########################################')

# 练习3：统计词频
# s = ''
# for val in range(ord('a'), ord('z')+1):
#     s += chr(val)
# print(s)

def countmax(data):
    lastchar = ''
    lastnum = 0

    if len(data) == 0:
        return lastchar

    for val in range(ord('a'), ord('z')+1):
        char = chr(val)
        n = data.count(char)

        if n > lastnum:
            lastnum = n
            lastchar = char

    return lastchar

if __name__ == '__main__':
    for data in ['aabbcc', 'abbccdddeeee', '']:
        print('{} maximum: {}'.format(data, countmax(data)))


print('############################################')

# 练习4：99乘法表
def lines(num):
    f = '{}x{}={}'
    for n in range(1, num + 1):
        print(f.format(n, num, n * num), end=' ')
    print()
# lines(3)
# lines(4)
if __name__ == '__main__':
    for n in range(1, 10):
        lines(n)

print('#############################')

# 练习5：抽检数字，计算总价
s = '上衣:300 , 鞋子:230 , 手机:1499 , 裤子:199'
# items = s.split(',')
# print(items)
# item = items[0]
# print(item)
# vals = item.split(':')
# print(vals[1].strip())

def sumconsume(data):
    money = 0

    for item in data.split(','):
        vals = item.split(':')
        price = vals[1]
        price = price.strip()
        money += int(price)

    return money

print('{} 一共消费金额：{} RMB'.format(s, sumconsume(s)))