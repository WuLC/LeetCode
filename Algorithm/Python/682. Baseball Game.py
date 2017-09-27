# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-09-27 09:40:35
# @Last Modified by:   WuLC
# @Last Modified time: 2017-09-27 09:41:03

# stack
class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        for op in ops:
            if op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(stack[-1] * 2)
            elif op == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))
        return sum(stack)