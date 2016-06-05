# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-06-05 11:37:16
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-05 11:38:07
# @Email: liangchaowu5@gmail.com

# method 1,divide and conquer
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        if n<=1:
            return 1
        for i in xrange(n/2):
            left = self.numTrees(i)
            right = self.numTrees(n-i-1)
            result += left * right
        result *= 2
        if n%2 == 1:
            result += pow(self.numTrees(n/2),2)
        return result


# method 2,DP