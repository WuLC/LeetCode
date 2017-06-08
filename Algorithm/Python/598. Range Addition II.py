# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-06-08 19:59:17
# @Last modified by:   WuLC
# @Last Modified time: 2017-06-08 20:09:51
# @Email: liangchaowu5@gmail.com


# find the common area
class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        x, y =  m, n
        for op in ops:
            x = min(op[0], x)
            y = min(op[1], y)
        return x * y