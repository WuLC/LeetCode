# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-05-10 09:06:36
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-10 09:06:56
# @Email: liangchaowu5@gmail.com

# DP
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        for i in xrange(m):
            for j in xrange(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0 :
                    grid[i][j] += grid[i][j-1]
                elif j == 0 :
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] = min(grid[i][j]+grid[i][j-1],grid[i][j]+grid[i-1][j])
        return grid[m-1][n-1]
        