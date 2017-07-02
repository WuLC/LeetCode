# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-07-02 16:33:28
# @Last Modified by:   WuLC
# @Last Modified time: 2017-07-02 16:34:38


# use set to store all possible candidates
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        candidate = set()
        i = 0
        while True:
            tmp = i**2
            if tmp > c:
                break
            else:
                candidate.add(tmp)
            i += 1
        for num in candidate:
            if c-num in candidate:
                return True
        return False