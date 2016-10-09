# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-06-30 19:06:48
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-30 19:06:55
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        num, count = 5, 0
        while num <= n:
            count += n/num
            num *= 5
        return count