# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-07-20 10:11:00
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-20 10:13:11
# @Email: liangchaowu5@gmail.com

# If this function is called many times, we can store pow(2,i) (0<=i<=31) in a list to optmize it
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        for i in xrange(32):
            if n&(1<<i):
                result += pow(2, 32-i-1) 
        return result