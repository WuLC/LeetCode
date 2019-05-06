# -*- coding: utf-8 -*-
# Created on Sun May 05 2019 10:27:22
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# bfs, record borders of connected component

from collections import deque

class Solution(object):
    def colorBorder(self, grid, r0, c0, color):
        """
        :type grid: List[List[int]]
        :type r0: int
        :type c0: int
        :type color: int
        :rtype: List[List[int]]
        """
        queue, borders = deque(), []
        m, n = len(grid), len(grid[0])
        visited = [[0] * n for _ in xrange(m)]
        queue.append((r0, c0))
        visited[r0][c0] = 1
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        while queue:
            r, c = queue.popleft()
            if r == 0 or r == m - 1 or c == 0 or c == n - 1:
                borders.append((r, c))
            for d in directions:
                nr, nc = r + d[0], c + d[1]
                if 0 <= nr < m and  0 <= nc < n:
                    if grid[nr][nc] == grid[r0][c0]:
                        if visited[nr][nc] == 0:
                            queue.append((nr, nc))
                    else:
                        borders.append((r, c))
                    visited[nr][nc] = 1
        for r, c in borders:
            grid[r][c] = color
        return grid
    