#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import re
import codecs
from StdSuites import lists

f = codecs.open('/Users/minghuichen/Desktop/full_export.exml', 'r', 'utf-8')
s = f.readlines()

f2 = codecs.open('/Users/minghuichen/Desktop/import_haoduan.txt', 'r')
lines = f2.readlines()

outfile = open("/Users/minghuichen/Desktop/export_range_number.txt", "w")


f.flush()
f.close()
f2.flush()
f2.close()

global export_lists
export_lists = []


for fileLine in lines:
    start_num = fileLine[2:9]
   # print start_num
    export_lists.append(start_num)



for fileLine in s:

    if u'<name>usrStatus</name><value>2</value>' in fileLine:
        line_pattern = r'\s*\d+\s?(.*)'


        def func(text):
            c = re.compile(line_pattern)
            lists = []
            lines = text.split('\n')
            for line in lines:
                r = c.findall(line)
                if r:
                    strtemp = r[0]
                    strmsisdn = strtemp[strtemp.rfind("861"):(strtemp.rfind("861"))+13]
                    strmsisdn_temp = strmsisdn[2:9]
                    #print strmsisdn_temp
                    #print export_lists
                    if strmsisdn_temp in export_lists:
                        print 'yes'
                        lists.append(strmsisdn)
                        outfile.writelines(strmsisdn + "\n")


            #print ", ".join(lists)
            return '\n'.join(lists)


        result = func(fileLine)


