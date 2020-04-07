# -*- coding: utf-8 -*-
# Created on Mon Apr 06 2020 22:19:19
# Author: WuLC
# EMail: liangchaowu5@gmail.com

class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        conn = {
            1: [0, 2],
            2: [1, 3],
            3: [0, 3],
            4: [2, 3],
            5: [0, 1],
            6: [1, 2]
        }
        mapping = {0:2, 1:3, 2:0, 3:1}
        m, n = len(grid), len(grid[0])
        direction = ((0, -1), (-1, 0), (0, 1), (1, 0))
        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return True
            for k in conn[grid[i][j]]:
                ni, nj = i + direction[k][0], j + direction[k][1]
                if not (0 <= ni < m and 0 <= nj < n and grid[ni][nj] > 0):
                    continue
                if mapping[k] in conn[grid[ni][nj]]:
                    grid[i][j] = -1i
                    # do not return dfs(ni, nj) directly for the case like [[4,1],[6,1]]
                    if dfs(ni, nj):
                        return True
            return False
        return dfs(0, 0)
