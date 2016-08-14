# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-08-13 21:10:12
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-14 23:39:41
# @Email: liangchaowu5@gmail.com


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        """since python will automatically transfer int to long when overflow, the following code won't work, but it work for Java, C++
        if a&b:
            return self.getSum(a^b, (a&b) << 1)
        else:
            return a^b
       """
        MAX_INT = 0x7FFFFFFF
        MIN_INT = 0x80000000
        MASK = 0x100000000
        while b:
            a, b = (a ^ b) % MASK, ((a & b) << 1) % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)