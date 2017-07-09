# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-07-09 10:16:19
# @Last Modified by:   WuLC
# @Last Modified time: 2017-07-09 10:20:36


# split the equation into left part and right part
# deal with each part and return the coefficient of x and constant
class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        left, right = equation.split('=')
        left, right = self.helper(left), self.helper(right)
        if left == right:
            return 'Infinite solutions'
        elif left[0] == right[0] and left[1] != right[1]:
            return "No solution"
        else:
            return 'x={0}'.format((right[1] - left[1])/(left[0] - right[0]))
        
    
    def helper(self, s):
        nums = [0, 0]
        if len(s) == 0:
            return nums
        s += '+'
        pre = 0
        for i in xrange(1, len(s)):
            if s[i] in ['+', '-']:
                curr = s[pre:i]
                if curr[-1] == 'x':
                    left = curr[:-1]
                    if left in ['+', '-'] or len(left) == 0:
                        left += '1'
                    nums[0] += int(left)
                else:
                    nums[1] += int(curr)
                pre = i
        return nums
                    
                