# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-04-01 13:54:25
# @Last modified by:   WuLC
# @Last Modified time: 2016-11-03 16:23:43
# @Email: liangchaowu5@gmail.com


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = pow(2,31)-1  
        if divisor == 0:
            return MAX_INT
    
        flag = 1
        if (dividend > 0 and divisor<0 ) or (dividend<0 and divisor >0):
            flag = -1
        a = abs(dividend)
        b = abs(divisor)
        res = 0
        while a >= b :
            sum = b
            count =1 
            while a >= sum+sum:
                sum += sum
                count += count
            a-=sum
            res+=count

        # overflow
        return MAX_INT if res*flag > MAX_INT else res*flag