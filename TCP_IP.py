#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 18:34
# @Author  : Geng zhi
# @File    : TCP_IP.py


from scapy.all import *

p = IP(dst='github.com')/TCP()

# data = 'welcome to the jungle'
# pkt=IP(src='192.168.1.2', dst='192.168.1.3', ttl=1, id=168)/ICMP(id=188, seq=1)/data
#
# send(pkt, inter=1, count=5, iface="en0")


# IpScan = '192.168.1.0/24'
# try:
#     ans,unans = srp(Ether(dst="FF:FF:FF:FF:FF:FF")/ARP(pdst=IpScan), timeout=2)
# except Exception as e:
#     print(e)
# else:
#     for send, rcv in ans:
#         ListMACAddr = rcv.sprintf("%Ether.src%---%ARP.psrc%")
#         print(ListMACAddr)
