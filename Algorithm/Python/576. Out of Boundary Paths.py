# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2017-07-21 23:54:13
# @Last modified by:   LC
# @Last Modified time: 2017-07-21 23:54:51
# @Email: liangchaowu5@gmail.com

# simple recursive, TLE
class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        if N < 0:
            return 0
        if i < 0 or i >= m or j < 0 or j >= n:
            return   1
        dirs = [[-1,0],[1,0],[0,-1],[0,1]]
        count = 0
        for d in dirs:
            count += self.findPaths(m, n, N-1, i+d[0], j+d[1])
        return count
            