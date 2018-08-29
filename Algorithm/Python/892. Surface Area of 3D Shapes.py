# -*- coding: utf-8 -*-
# Created on Tue Aug 28 2018 17:24:1
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# calculate surface at each point, then minus hidden area
# referer: https://leetcode.com/problems/surface-area-of-3d-shapes/discuss/163414/C++Java1-line-Python-Minus-Hidden-Area
class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        result = 0
        for i in xrange(n):
            for j in xrange(n):
                if grid[i][j]>0:
                    result += 2 + grid[i][j]*4
                if i != 0:
                    result -= min(grid[i][j], grid[i-1][j])*2
                if j != 0:
                    result -= min(grid[i][j], grid[i][j-1])*2
        return result