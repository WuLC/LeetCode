# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-09-27 10:10:55
# @Last Modified by:   WuLC
# @Last Modified time: 2017-09-30 15:31:08

# modify from the last digit to the first digit
# also remember to change all the digits after the modified digit to the possible smallest digit so as to get the smallest valid result

class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        raw_digits = [int(c) for c in time if c != ':']
        digits = sorted(set(raw_digits))
        for i in xrange(3, -1, -1):
            for d in digits:
                if d > raw_digits[i]:
                    if i == 3:
                        raw_digits[i] = d
                        return str(raw_digits[0]) + str(raw_digits[1]) + ':' + str(raw_digits[2]) + str(raw_digits[3])
                    elif i == 2 and d < 6:
                        raw_digits[i] = d
                        return str(raw_digits[0]) + str(raw_digits[1]) + ':' + str(raw_digits[2]) + str(digits[0])
                    elif i == 1 and (raw_digits[0] == 0 or raw_digits[0] == 1 or (raw_digits[0] == 2 and d < 4)):
                        raw_digits[i] = d
                        return str(raw_digits[0]) + str(raw_digits[1]) + ':' + str(digits[0]) + str(digits[0])
                    elif i == 0 and (d == 1 or (d == 2 and raw_digits[1] < 4)):
                        raw_digits[i] = d
                        return str(raw_digits[0]) + str(digits[0]) + ':' + str(digits[0]) + str(digits[0])
        if digits[0] == 0:
            return '00:0'+str(digits[1]) if len(digits) > 1 else '00:00'
        else:
            c = str(digits[0])
            return c + c + ':' + c + c