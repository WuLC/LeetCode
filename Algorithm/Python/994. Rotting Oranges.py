# -*- coding: utf-8 -*-
# Created on Sun Feb 17 2019 18:54:15
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# simple bfs, there may be multiple rotton oranges

from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        queue = deque()
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
        result = 0
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        while queue:
            curr = queue.popleft()
            result = max(result, curr[2])
            for d in dirs:
                ni, nj = curr[0]+d[0], curr[1]+d[1]
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    queue.append((ni, nj, curr[2]+1))
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    return -1
        return result
       