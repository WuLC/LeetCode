# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-12-19 17:24:08
# @Last modified by:   WuLC
# @Last Modified time: 2016-12-19 17:24:32
# @Email: liangchaowu5@gmail.com

# bit manipulation
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        distance = 0
        tmp = x ^ y
        for i in xrange(31):
            distance += (1&(tmp>>i))
        return distance
        