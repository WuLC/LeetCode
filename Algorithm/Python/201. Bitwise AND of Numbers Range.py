# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-07-20 15:41:02
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-20 15:41:42
# @Email: liangchaowu5@gmail.com

# find the common prefix of the two numbers
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        count = 0
        while m != n:
            m >>= 1
            n >>= 1
            count += 1
        for i in xrange(count):
            m <<= 1
        return m