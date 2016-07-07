# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-07 20:34:36
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-07 20:34:46
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            if n % 2 ==1:
                count += 1
            n >>= 1
        return count