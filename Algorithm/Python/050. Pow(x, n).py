# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-01 11:11:40
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-01 11:12:01
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0 :
            return 1.0
        if x == 0:
            return 0
        if n<0:
            n = -1*n
            x = 1/x
        
        tmp = x
        result = 1
        while n>0:
            if n%2 == 1:
                result *= tmp
            tmp = tmp * tmp
            n = n/2
        return result 
        
        
        
        