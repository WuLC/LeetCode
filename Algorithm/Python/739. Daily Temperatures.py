# -*- coding: utf-8 -*-
# Created on Tue Dec 05 2017 11:45:40
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# stack, O(n) time
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while len(stack) > 0:
                if stack[-1][1] < temperatures[i]:
                    idx = stack.pop()[0]
                    result[idx] = i - idx
                else:
                    break
            stack.append((i, temperatures[i]))
        return result            