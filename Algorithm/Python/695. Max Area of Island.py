# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-10-08 21:59:05
# @Last Modified by:   WuLC
# @Last Modified time: 2017-10-08 21:59:19

# dfs
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        result = 0
        m, n = len(grid), len(grid[0])
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    result = max(result, self.dfs(grid, i, j))
        return result
    
    
    def dfs(self, grid, i, j):
        count = 1
        grid[i][j] = 0
        for di in [-1, 1]:   
            if 0 <= i + di < len(grid) and grid[i+di][j] == 1:
                count += self.dfs(grid, i + di, j)
        for dj in [-1, 1]:   
            if 0 <= j + dj < len(grid[0]) and grid[i][j+dj] == 1:
                count += self.dfs(grid, i , j + dj)
        return count
        
        
        