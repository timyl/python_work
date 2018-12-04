# /usr/bin/env python
# _author_: timyl
# date: 2018/3/29

import re

class Filter_usrStatus():
    '''
    RE variables for whole class
    '''
    msisdn = '861\d{6}?'
    usrStatus = '<name>usrStatus</name><value>2</value>'

    '''
    filtering where usrStatus=2 lines
    '''
    def __usrStatus_filter(self):
        with open('quanliang328.exml', 'r', encoding='utf8') as f:
            matched_usrStatus = []
            for line in f:
                target_line = re.findall(Filter_usrStatus.usrStatus, line)
                if target_line:
                    matched_usrStatus.append(line)
        # print(matched_usrStatus)
        return matched_usrStatus

    '''
    filtering where MSISDN belongs to LuoYang ranges
    '''
    def __Msisdn_filter(self, matched):
        f_read = open('ranges.txt', 'r', encoding='utf8')
        f_write = open('ranges_rest.txt', 'w', encoding='utf8')
        ranges = f_read.read()
            # print(numbers)

        matched_e164 = []
        for line in matched:
            # print(line)
            target_e164 = re.findall(Filter_usrStatus.msisdn, line)
            # print(target_e164[0])
            if target_e164[0] in ranges:
                matched_e164.append(line)
                print(line)
                f_write.write(line)
        print(len(matched_e164))
        return matched_e164

    def go(self):
        matched_usrStatus = self.__usrStatus_filter()
        matched_e164 = self.__Msisdn_filter(matched_usrStatus)

Filter_usrStatus = Filter_usrStatus()
Filter_usrStatus.go()



