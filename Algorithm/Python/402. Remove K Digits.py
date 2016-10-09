# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-09-23 23:36:46
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-23 23:38:44
# @Email: liangchaowu5@gmail.com

# stack
# go through the digits of the number and pop when the current element smaller than the top elements of the stack
# pay attention that the redundant 0 before the number and there may be an empty string after removing
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        remain = len(num) - k
        for dig in num:
            while k and stack and stack[-1] > dig:
                stack.pop()
                k -= 1
            stack.append(dig)
        return ''.join(stack[:remain]).lstrip('0') or '0'

