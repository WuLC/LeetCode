# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-11-25 08:50:09
# @Last modified by:   WuLC
# @Last Modified time: 2016-11-25 08:52:08
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        perimeter = 0
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    if  i-1<0 or grid[i-1][j] == 0:  perimeter += 1
                    if  i+1==m or grid[i+1][j] == 0: perimeter += 1
                    if  j-1<0 or grid[i][j-1] == 0:  perimeter += 1
                    if  j+1==n or grid[i][j+1] == 0:  perimeter += 1
        return perimeter