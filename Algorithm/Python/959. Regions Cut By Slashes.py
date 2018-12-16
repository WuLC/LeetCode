# -*- coding: utf-8 -*-
# Created on Sun Dec 16 2018 20:0:17
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# dfs
# reference: https://leetcode.com/problems/regions-cut-by-slashes/discuss/205674/C++-with-picture-DFS-on-upscaled-grid
class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        n = 3*len(grid)
        mapping = [[0 for i in xrange(n)] for j in xrange(n)]
        for i in xrange(len(grid)):
            for j in xrange(len(grid)):
                if grid[i][j] == '/':
                    mapping[i*3][j*3+2] = 1
                    mapping[i*3+1][j*3+1] = 1
                    mapping[i*3+2][j*3] = 1
                elif grid[i][j] == '\\':
                    mapping[i*3][j*3] = 1
                    mapping[i*3+1][j*3+1] = 1
                    mapping[i*3+2][j*3+2] = 1
        count = 0
        for i in xrange(n):
            for j in xrange(n):
                if mapping[i][j] == 0:
                    self.dfs(mapping, n, i, j)
                    count += 1
        return count
        
    def dfs(self, mapping, n, i, j):
        if 0 <= i < n and 0 <= j < n and mapping[i][j] == 0:
            mapping[i][j] = -1
            self.dfs(mapping, n, i-1, j)
            self.dfs(mapping, n, i+1, j)
            self.dfs(mapping, n, i, j-1)
            self.dfs(mapping, n, i, j+1)