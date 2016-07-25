# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-25 12:15:11
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-25 12:15:24
# @Email: liangchaowu5@gmail.com


# DFS
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0: return 0
        m, n, result = len(grid), len(grid[0]), 0
        visited = [[0 for j in xrange(n)] for i in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    self.dfs(grid, visited, i, j)
                    result += 1
        return result
    
    def dfs(self, grid, visited, i, j):
        visited[i][j] = 1
        m, n = len(grid), len(grid[0])
        if 0<= i-1 <m and grid[i-1][j] == '1' and visited[i-1][j] == 0:
            self.dfs(grid, visited, i-1, j)
        if 0<= i+1 <m and grid[i+1][j] == '1' and visited[i+1][j] == 0:
            self.dfs(grid, visited, i+1, j)
        if 0<= j-1 <n and grid[i][j-1] == '1' and visited[i][j-1] == 0:
            self.dfs(grid, visited, i, j-1)
        if 0<= j+1 <n and grid[i][j+1] == '1' and visited[i][j+1] == 0:
            self.dfs(grid, visited, i, j+1)