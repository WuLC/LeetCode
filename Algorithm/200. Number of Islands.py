# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-25 12:15:11
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-09 10:05:12
# @Email: liangchaowu5@gmail.com


# method 1, DFS
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

# method 2, BFS
from collections import deque
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        count = 0
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == '1':
                    self.bfs(i, j, grid)
                    count += 1
        return count
    def bfs(self, row, col, grid):
        m, n = len(grid), len(grid[0])
        que = deque()
        que.append((row, col))
        grid[row][col] = '2'
        while que:
            row, col = que.popleft()
            if row>0 and grid[row-1][col]=='1':
                que.append((row-1, col))
                grid[row-1][col] = '2'
            if row<m-1 and grid[row+1][col] == '1':
                que.append((row+1, col))
                grid[row+1][col] = '2'
            if col>0 and grid[row][col-1]=='1':
                que.append((row, col-1))
                grid[row][col-1] = '2'
            if col<n-1 and grid[row][col+1] == '1':
                que.append((row, col+1))
                grid[row][col+1] = '2'