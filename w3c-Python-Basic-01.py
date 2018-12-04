#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/26 10:43
# @Author  : Geng zhi
# @File    : w3c-Python-Basic-01.py


dict1 = {'name':'geng', 'age':30}
print(dict1.keys())
print(dict1.values())
print(dict1.items())
print(list(dict1.items())) # [('name', 'geng'), ('age', 30)]
print(list(dict1.keys())) # ['name', 'age']

# 元祖：
# 元组也是允许重复的
t1 = (1, 2, 3)
t2 = (1, 1, 2, 3)
a, b, c = t1
print(a, b, c)
print(t2)
# 字典转化成元组，只会转key成元组
# 元组注意：充分利用元组解包和交叉赋值特性

# 集合：
# 舍弃了value的字典,无序并且唯一的
set_1 = set() # 不要直接加{}
print(type(set_1))
set_2 = {'a', 'b', 'c'}
print(type(set_2))
# 集合的转换
# 集合的操作, 交、并、差集
set_3 = {'b', 'c', 'd'}
print(set_2 & set_3)
print(set_2 | set_3)
print(set_2 - set_3)
print(set_3 - set_2)

# 方法：
set_2.update('e')
set_2.update(set_3)
print(set_2)

# python解释器注释：#和\，一行写不完，可以在结尾加\

# if else
# 如下的情况被判定为False：None，0， 0.0 '', [], (), {}, set()

# for循环
dict = {'geng':20, 'jean':20, 'jack':30}
for name in dict:
    print(name)
for value in dict.values():
    print(value)
for name, value in dict.items():
    print('name is {}, age is {}'.format(name, value))

# 打包zip
name = ['geng', 'jean', 'jack']
height = [180, 175, 170]
sex = ['male', 'female', 'male']
res = list(zip(name, height))
print(res) # [('geng', 180), ('jean', 175), ('jack', 170)]

# 注意：zip返回的是一个迭代器，并不会一次性生成，当每次迭代的时候才处理
for name, value in zip(name, height):
    print('name is {}, age is {}'.format(name, value))
# zip可以对三个列表进行并行迭代
for name, age, sex in zip(name, height, sex):
    print('name is {}. age is {}, and sex is {}'.format(name, age, sex))

# 注意：如果序列长度不一样，那么会按照最短的来处理
for i in range(5):
    print(i**2)

for i in range(1, 10, 2):
    print(i)

# 列表推导式
# for i in range(10):
#     print(i**2)
square = []
for i in range(4):
    square.append(i**2)
print(square)

tuidao01 = [i*i for i in range(10)]
tuidao02 = [i*i for i in range(10) if i % 2 == 0]
list1 = ['geng', 'jean', 'jackins', 'timyl']

tuidao03 = [word.title() for word in list1]
tuidao04 = [word.capitalize() for word in list1]
tuidao05 = [word for word in list1 if len(word) > 5]

print(tuidao01)
print(tuidao02)
print(tuidao03)
print(tuidao04)
print(tuidao05)

# 字典推导式
tuidao06 = {word: len(word) for word in list1}
tuidao07 = {word: len(word) for word in list1 if word.startswith('tim')}
print(tuidao06)
print(tuidao07)

# 集合推导式
tuidao08 = {word for word in list1 if len(word) > 5}
print(tuidao08)
print(type(tuidao08))

# 生成器：
gener = (i*i for i in range(5))
print(type(gener)) # <class 'generator'>
# 外边是()的时候，是生成器类型，可以使用list来转换查看,而且生成器只能运行一次
# print(list(gener)) # 结果 [0, 1, 4, 9, 16]
# print(list(gener)) # 空 []

# 所以它的好处就是处理大的数据量的时候，不会一次读取到内存，可以一次一次迭代
for res in gener:
    print(res)

print('###################################')
# 函数
def justprint():
    print('hello')
    return False
if justprint():
    print('result a')
else:
    print('result b')

def echo(string):
    return '{} ** {}'.format(string, string)
res = echo('hello')
print(res)

def isOdd(num):
    if num %2 == 0:
        print('this is a even number')
    else:
        print('this is a odd number')
isOdd(111)

# 韩素参数
def sum(arg1, arg2, arg3):
    return arg1 + arg2 + arg3
sum(1, 2, 4)

# 基于位置的参数
def printHeight(name1, name2):
    print('{} height is 180'.format(name1))
    print('{} height is 185'.format(name2))

printHeight('Geng', 'Jean')
printHeight('Jean', 'Geng')

# 关键字参数
# 注意：以下是默认值，如果不传入就按照默认，传入了就按照传入的值
def printHeight(name1='geng', name2='jean'):
    print('{} height is 180'.format(name1))
    print('{} height is 185'.format(name2))

# 不定长参数
def myprint(*args):
    for item in args:
        print(item)
myprint('hello', 'world', [1, 2, 3])
# 不定长关键字参数
def myprint01(**kwargs):
    print(kwargs)
myprint01(a=1, b=2, c=3) # {'a': 1, 'b': 2, 'c': 3}

# 参数顺序(前后顺序)
# 位置参数>默认参数>args<kwargs


print('------------------------')
# 定义函数的文档字符串

def func_doc():
    '''文档字符串描述'''
    return True
print(help(func_doc))  # 文档字符串描述
print(func_doc.__doc__) # 文档字符串描述

# 函数本身当成参数
def isodd(num):
    if num % 2 == 0:
        print('{}是偶数'.format(num))
    else:
        print('{}是奇数'.format(num))

def outer_func(func, *args):
    for num in args:
        func(num)
outer_func(isodd, 2, 3, 4, 5)

# 嵌套函数
def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)
outer(2, 3)

# 闭包
# 一个可以由另一个函数动态生成的函数
def exp(x):
    def inner(num):
        return num**x
    return inner
exp1 = exp(2)
print(exp1(4))

# 匿名函数，生成器函数，和装饰器
# lambda函数
list1 = ['geng', 'tom', 'mike']
# 这时想要处理每个字符串，首字母大写，正常思路是写个函数
def changeit(a):
    return a.title()
# 然后在使用列表推导式
list2 = [changeit(x) for x in list1]
print(list2) # ['Geng', 'Tom', 'Mike']

# 使用匿名函数
# 第一步进化：
step1 = list(map(changeit, list1))
print(step1)
# 第二部进化:直接使用匿名函数
step2 = list(map(lambda x:x.title(), list1))
print(step2)


# 生成器函数：
def string_reg(lis):
    for item in lis:
        yield item.title()  # 在循环中加yield
print(type(string_reg(list1))) # <class 'generator'> 生成器函数
# for item in string_reg(list1):
#     print(item)
a = string_reg(list1)
print(list(a)) # ['Geng', 'Tom', 'Mike']
print(list(a)) # []

# 函数大的命名空间和作用域
s = 10
def sum():
    # s = 0
    global s
    for i in range(10):
        s += i
    return s
print(sum())
# 引用外部变量 使用global关键字
# print(globals())
# print(locals())

# 装饰器函数
def my_sum(a, b):
    '''
    result is the sum of a and b
    '''
    return a + b
# 增加功能，打印函数名称，文档描述等信息
# 注意：装饰器函数的输入是一个函数，输出也是函数
def doc_func(func):
    def new_func(*args, **kwargs):
        print('the func name is:', func.__name__)
        print('the func doc is:', func.__doc__)
        return func(*args, **kwargs)
    return new_func
# 现在就不一样了，既可以返回原函数的结果，也可以返回装饰器函数增加的内容

# new_sum = doc_func(my_sum)
# new_sum(3, 4)
# print(new_sum(3, 4))

# 装饰器的使用，直接在目标函数上使用
@doc_func
def my_sum(a, b):
    '''
    result is the sum of a and b
    '''
    return a + b

print(my_sum(3, 4))
# 结果：
'''
the func name is: my_sum
the func doc is: 
    result is the sum of a and b
    
7
'''