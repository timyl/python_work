#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/1 09:58
# @Author  : Geng zhi
# @File    : 20 Days Python-7.py

import psutil

print(psutil.version_info)

print(psutil.cpu_times())
# print('CPU执行用户进程时间：', psutil.cpu_times().user)
# print('CPU执行系统调用时间：', psutil.cpu_times().system)
# print('CPU空闲等待时间:', psutil.cpu_times().idle)
# # print('CPU相应中断时间:', psutil.cpu_times().interrupt)
#
# print('CPU使用率:', psutil.cpu_percent())
# print('CPU 3秒内的使用率:', psutil.cpu_percent(interval=3))
# print('每个逻辑CPU使用率:', psutil.cpu_percent(percpu=True))
# print('CPU各个状态使用情况:', psutil.cpu_times_percent())
# cpuinfos = psutil.cpu_times_percent(percpu = True)
# for info in cpuinfos:
#     print(info)


# 内存
mem = psutil.virtual_memory()
print('系统内存:', mem)
print('总内存:', mem.total)
print('空闲内存:', mem.available)
print('使用内存:', mem.used)
print('未使用内存:', mem.free)
print('内存使用率: {} %'.format(mem.percent)) # 21.3
print('swap内存:', psutil.swap_memory())

# human read
M = 1024 * 1024
G = M * 1024
mem = psutil.virtual_memory()
print('系统内存:', mem)
print('总内存: {}M {}G'.format(mem.total//M, mem.total/G))

# 磁盘使用率
print('-----------------------------')
devs = psutil.disk_partitions()
print(devs)
for dev in devs:
    print('硬盘名: {}, 挂载点: {}, 文件类型: {}'.format(dev.device, dev.mountpoint, dev.fstype))

# 函数
def showdiskinfo(path):
    G = 1024 * 1024 * 1024
    diskinfo = psutil.disk_usage(path)
    print(path, diskinfo)
    print('{}大小:{}G, 已经使用:{}G, 未使用:{}G, 使用百分比:{}%'.format(path, \
        diskinfo.total//G, diskinfo.used//G, diskinfo.free//G, diskinfo.percent))

showdiskinfo('/')

print('--------------')
# 磁盘读写情况
diskrw = psutil.disk_io_counters()
print(diskrw)
diskrw1 = psutil.disk_io_counters(perdisk=True)
print(diskrw1)


# 进程信息
print('----------------')
pids = psutil.pids()
print(pids)
process = psutil.Process(pids[0])
print(process) # psutil.Process(pid=2605, name='Python', started='09:16:35')

p = psutil.Process(0)
print('进程名称:', p.name())
print('运行状态:', p.status())
# print('内存信息:', p.memory_info())
# print('线程数:', p.num_threads())

# 练习：
def getPidByName(name):
    listp = []
    for pid in psutil.pids():
        p = psutil.Process(pid)

        if name in p.name():
            listp.append(pid)
    return listp
name = 'firefox'
result = getPidByName(name)
print(result) # [2875]




