# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-25 14:37:53
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-25 14:39:28
# @Email: liangchaowu5@gmail.com

# execute the method in 083 row by row
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        max_re = 0
        heights = [0 for i in xrange(n)]
        for i in xrange(m):
            stack = []
            for j in xrange(n):
                heights[j] = heights[j]+1 if matrix[i][j]=='1' else 0
                while len(stack)!=0 and heights[j] < heights[stack[-1]]:
                    height = heights[stack.pop()]
                    width = j - stack[-1] - 1 if len(stack)>0 else j
                    max_re = max(max_re, width * height)
                stack.append(j)
            while len(stack) != 0:
                height = heights[stack.pop()]
                width = n - stack[-1] - 1 if len(stack)>0 else n
                max_re = max(max_re, width * height)
        return max_re
            
                
        