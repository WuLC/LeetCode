# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-05-22 10:29:29
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-22 11:30:59
# @Email: liangchaowu5@gmail.com

# method 1, stack
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_re, n = 0, len(heights)
        stack = []
        for i in xrange(n):
            while len(stack)>0 and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if len(stack) == 0 else i-stack[-1]-1
                max_re = max(max_re, height * width)
            stack.append(i)
        while len(stack)>0:
            height = heights[stack.pop()]
            width = n if len(stack) == 0 else n-stack[-1]-1
            max_re = max(max_re, height * width)
        return max_re

