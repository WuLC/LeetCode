# -*- coding: utf-8 -*-
# Created on Sun Mar 25 2018 11:9:43
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# simple solution
class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        left_right = [max(row) for row in grid]
        bottom_up = [0]*n
        for i in xrange(m):
            for j in xrange(n):
                bottom_up[j] = max(bottom_up[j], grid[i][j])
        
        count = 0
        for i in xrange(m):
            for j in xrange(n):
                count += min(left_right[i], bottom_up[j]) - grid[i][j]
        return count  