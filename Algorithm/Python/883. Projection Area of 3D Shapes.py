# -*- coding: utf-8 -*-
# Created on Thu Aug 16 2018 18:22:33
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# simple solution
class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        xy, xz, yz = 0, [0]*n, [0]*n
        for i in xrange(n):
            for j in xrange(n):
                if grid[i][j]>0:
                    xy += 1
                xz[i] = max(xz[i], grid[i][j])
                yz[j] = max(yz[j], grid[i][j])
        return xy + sum(xz) + sum(yz)