# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-15 14:39:42
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-15 14:39:50
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in xrange(32):
            bit = 0
            for num in nums:
                bit += num & (1 << i)
            bit %= 3
            if bit:
                if i == 31:  # if the highest bit is 1,it is negative 
                    result -= pow(2,31)
                else:
                    result += pow(2, i)
        return result