# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-10-08 22:37:53
# @Last Modified by:   WuLC
# @Last Modified time: 2017-10-08 22:38:12

# bit manipulation
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num = n^(n >> 1) 
        while num != 0:
            if (num & 1) == 0:
                return False
            num >>= 1
        return True   