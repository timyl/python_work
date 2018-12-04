#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 16:13
# @Author  : Geng zhi
# @File    : w3c-Python-Basic-02.py

# 异常
list1 = [1, 2, 3, 4]

position = 'a'

# 进化1:
# try:
#     print(list1[position])
# except Exception as e:
#     print('an error happened.\n', e)

# 进化2:
try:
    print(list1[position])
# 当知道大概错误是什么的时候，你可以指定错误类型
except IndexError as e:
    print('this is a bad index:', position)
# 当你无法判定会出现什么错误的时候，可以直接用Exception
except Exception as other:
    print('this is some other errors:', other)


# python 模块，包和程序
# 方法一：
import city
city.print_city()
# city.print_slow()

# 方法二：
import city as ct
ct.print_city()

# 方法三：
from city import print_city as pc
pc()
print('print city import finished')

# 模块搜索路径是sys.path
# python本身文件可以用sys.argv来获取，包括传入的参数，列表形式
import sys
# print(sys.path)
# print(sys.argv[1])

print('-----------------------------')
# 文件组织与包
# 包必须需要init.py文件存在
from coutry_test import print_country as pc
pc.print_c()

# 注意：print_country中引用print_city模块的话，按照当前运行目录来讲，不能直接引用
# 需要从上层包中逐层引用
# from coutry_test import print_city


# python标准库

print('------------------------------')
# 类和对象的创建
class Animal():
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def shout(self):
        print('wang,wang,wang...')

dogA = Animal(30, 10)
dogA.weight
dogA.shout()

# 类的继承
class Dog(Animal):
    # 添加Dog自己的方法
    def Run(self):
        print('Running...')

# 属性和方法都继承了
dogB = Dog(20, 10)
print(dogB.weight)
print(dogB.height)
dogB.shout()
dogB.Run()

# 方法的覆盖和重写
# 例如，猫不需要继承Animal中的shout方法
class Cat(Animal):
    def __init__(self, weight, height, eye_color):
        # 这里不需要重写weight,和hight属性，这里使用super来继承已有的属性，并加入新的特性
        super().__init__(weight, height)
        self.eye_color = eye_color

    # 重写父类的方法
    def shout(self):
        print('Miao, Miao....')

catA = Cat(20, 20, 'bule')
print(catA.weight)
print(catA.height)
print(catA.eye_color)
catA.shout()

# 对属性的访问
class Tiger():
    def __init__(self, weight, height):
        # 为了隐藏类的属性，安全性考虑,可以把属性改名字
        # self.hide_weight = weight
        self.__weight = weight
        self.__height = height

    # 这里使用装饰器来调用
    @property
    def weight(self):
        # return self.hide_weight
        return self.__weight

    @property
    def height(self):
        return self.__height

    @weight.setter
    def weight(self, input_weight):
        if input_weight < 0:
            print('weight must bigger than zero')
        else:
            self.__weight = input_weight

tiger1 = Tiger(30, 10)
print(tiger1.weight)

# 但是如果用户还是猜测到了属性名呢？那就需要使用self.__weight = weight这种私有方式了
# 这样的好处是使用户只能通过装饰器的方法来访问，而不能直接修改类的方法-------------
print(tiger1.weight)
print(tiger1.height)

# 如果还是想改属性呢？
# 使用weight.setter装饰器，如上
tiger1.weight = 100
print(tiger1.weight) # 100

# 类本身的方法和属性，这个是区别于上边的对象属性和方法了
import datetime
class People():
    # 类属性
    count = 0
    def __init__(self):
        # 类的属性调用，需要使用类名称
        People.count += 1
        # 实例调用静态方法，来返回people实例出生时间
        self.time = People.birthday()

    def shout(self):
        print('Fuck')

    # 类方法---使用类类调用
    @classmethod
    def peo_num(cls):
        print('we have {} people'.format(cls.count))

    # 静态方法--使用类来直接调用
    @staticmethod
    def birthday():
        return datetime.datetime.now()


#实力化对象
people1 = People()
print(people1.time)
people2 = People()
print(people2.time)
people3 = People()
print(people3.time)
People.peo_num() # we have 3 people, 每实例话一个对象，count就会+1

# 静态方法
People.birthday()


# 特殊方法------------------
# __str__方法
class Dog():
    def __init__(self, name):
        self.name = name

    # 魔术方法一：可以在print中人性化显示结果
    def __str__(self):
        return self.name

    # 魔术方法二：可以在解释器中直接人性化显示对象的结果，不是内存地址，而直接是对象名字
    def __repr__(self):
        return 'Dog {}'.format(self.name)

    # 魔术方法三：equal方法: 可以使两个name进行对比
    # def equal(self, dogx):
    def __eq__(self, dogx):
        return self.name.lower() == dogx.name.lower()

dog1 = Dog('ahuang')
# 不加__str__方法，显示不是很人性化：<__main__.Dog object at 0x106817630>
print(dog1) # ahuang
dog2 = Dog('Ahuang')
# res = dog1.equal(dog2)
# print(res) # True

# 上边equal方法加上__之后就可以直接"对象对比了",例如
print(dog1 == dog2)


print('---------------------------------------')
# python字符串的编码于解码
# 编码：文本编码成二进制  把str类型编码成bytes，python使用unicode编码，而utf-8就是它的一种实现方式，可变长的编码方式，1-4字节来表示一个字符
# 解码：二进制解码成文本 把bytes转化成str

# utf-8是python，linux，html标准文本编码格式，编解码一般都建议使用
# 例如：
s = '你howareyou'
b_s = s.encode()  # 默认就是utf-8编码，如果认为定制，那解码也要一致
print(b_s) # b'\xe4\xbd\xa0howareyou', 字母编码完是不变的，中文会变成二进制形式
s_s = b_s.decode()
print(s_s)  # 你howareyou

# 文本格式化
# 方式一：%s 字符串， %d 十进制整数，%f浮点数
name_list = ['Jean', 'Geng', 'Frank', 'Markies']
for name in name_list:
    print('the students %s have good life, earned %dk per year, about %.2f wan per month' % (name, 300, 2.889))

# 方式二：
# 括号中还可以添加format中元素的序号，来改变顺序，例如{2} {1} {0}
# 另外还能支持关键形式，例如'{n} {f} {s}'.format(n=30, f=2.88, s='name')
# 这种情况也能控制域宽, >右对其，<左对其，^中间，其它都跟方式一差不多
for name in name_list:
    # print('the students {} have good name, earned {}k per year, about {} wan per month'.format(name, 300, 2.88))
    print('I have {0: >10.2f}k money, earn {1: >4d}k dollars per year'.format(35.345, 300))


# 文件读写--------------------------
# 首先需要打开一个文件
poem = 'you are my sunshine, my only sunshine...'
# 写入，wt和rt是写入和读取文本格式，wb和rb是二进制文件; 默认就是t格式文本格式
f = open('poem.txt', 'wt')
f.write(poem)
f.close()

# 读取
f = open('poem.txt', 'rt')
print(f.read()) # 一次性读取所有
f.close()

# 二进制文件制作
b_poem = poem.encode()
f = open('b_poem', 'wb')
f.write(b_poem)
f.close()
# 读取二进制
f = open('b_poem', 'rb')
print(f.read())  # b'you are my sunshine, my only sunshine...'
f.close()

# 使用上下文管理器来读写文件,无需手动关闭了
with open('poem.txt', 'rt') as f:
    res = f.read()
    print(res)

# 追加
poem2 = '\nyou make me happy...'
with open('poem.txt', 'at') as f:
    f.write(poem2)

print('--------------------------------')
# 三种读取文本的方法-------
# 1. readline,迭代器，每次读取一行，对于大量的数据有好处
poemlist = ''
with open('poem.txt', 'r') as f:
    # print(f.readline())
    # print(f.readline())
    while True:
        line = f.readline()
        if not line:
            break
        poemlist += line
print(poemlist)

# 2.readlines(), 读取所有，放到一个列表
with open('poem.txt', 'r') as f:
    line = f.readlines()
    print(line) # ['you are my sunshine, my only sunshine...\n', 'you make me happy...']

# 3.使用迭代器方式
with open('poem.txt', 'r') as f:
    for line in f:
        print(line.upper())


print('---------------------------')
# 结构化格式文件读取，csv，json，pickle
# csv，逗号分隔符,除了逗号，也会有制表符，|等分割
import csv
student = [['jack', 'jean'], ['geng', 'frank'], ['mike', 'markies']]
# 保存为csv，写多行（二维）, 这里newline=''是为了避免出现读取的时候出现空字符串情况，正常情况下没有出现
with open('student.csv', 'w', newline='') as f:
    # 首先简历一个csv writer类,然后使用这个类来调用writerow方法
    csv_writer = csv.writer(f)
    # print(type(csv_writer))
    # writerows是一个二维形式
    csv_writer.writerows(student)

# 写一行（一维）
with open('student.csv', 'a') as f:
    # 首先简历一个csv writer类,然后使用这个类来调用writerow方法
    csv_writer = csv.writer(f)
    # writerow是一维
    csv_writer.writerow(['zhang', 'jin', 'lili'])

# 读取csv
with open('student.csv', 'r') as f:
    csv_reader = csv.reader(f)
    # 这里使用列表推导公
    stu = [row for row in csv_reader]
    print(stu) # [['jack', 'jean'], ['geng', 'frank'], ['mike', 'markies'], ['zhang', 'jin', 'lili']]


# json, 源于js,用于数据交换
import json
student_dic = {'class':
                    {'group1':
                        {'Mike': 170, 'Markies': 180},
                    'group2':
                        {'Jean': 160, 'Geng': 180},
                    'group3':
                        {'Frank': 175, 'Dalton':176}
                    }}

# 转化成json
stu_json = json.dumps(student_dic)
print(stu_json)
# {"class": {"group1": {"Mike": 170, "Markies": 180}, "group2": {"Jean": 160, "Geng": 180}, "group3": {"Frank": 175, "Dalton": 176}}}

# 读取json
stu = json.loads(stu_json)
print(stu)
# {'class': {'group1': {'Mike': 170, 'Markies': 180}, 'group2': {'Jean': 160, 'Geng': 180}, 'group3': {'Frank': 175, 'Dalton': 176}}}

# json缺点：并不能支持所有的数据类型转化成json
import datetime
time_now = datetime.datetime.now()
print(time_now) # 2018-11-30 18:59:20.328063
# 把时间转化成json, 会报错
# time_json = json.dumps(time_now) # Object of type datetime is not JSON serializable

# 为了解决如上问题，可以使用pickle, 但是它是python独有的序列化格式，使用纯python环境没问题，但是有其它语言环境就会出错
import pickle
pickle_time = pickle.dumps(time_now)
print(pickle_time)
# b'\x80\x03cdatetime\ndatetime\nq\x00C\n\x07\xe2\x0b\x1e\x13\x02\x11\x08\xc50q\x01\x85q\x02Rq\x03.'

# 读取pickle
reverse_pickle = pickle.loads(pickle_time)
print(reverse_pickle) # 2018-11-30 19:03:10.782620

list1 = ['geng', 1, 2.8, 'hello']
pickle_list = pickle.dumps(list1)
with open('pickle_save', 'wb') as f:
    f.write(pickle_list)

with open('pickle_save', 'rb') as f:
    read_pickle = pickle.loads(f.readline())
    print(read_pickle) # ['geng', 1, 2.8, 'hello']


