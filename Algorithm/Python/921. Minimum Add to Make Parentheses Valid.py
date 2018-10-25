# -*- coding: utf-8 -*-
# Created on Tue Oct 23 2018 20:28:25
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# greedy, think with stack
class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        left, right, result = 0, 0, 0
        for c in S:
            if c == '(':
                left += 1
            else:
                if left == 0:
                    result += 1
                else:
                    left -= 1
            result += left
        return result
