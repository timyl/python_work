#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/9 15:12
# @Author  : Geng zhi
# @File    : exec02.py

from prettytable import PrettyTable
table = PrettyTable(["animal", "ferocity"])
table.add_row(["wolverine", 100])
table.add_row(["grizzly", 87])
table.add_row(["Rabbit of Caerbannog", 110])
table.add_row(["cat", -1])
table.add_row(["platypus", 23])
table.add_row(["dolphin", 63])
table.add_row(["albatross", 44])
table.sort_key("ferocity")
table.reversesort = True

print(table)


