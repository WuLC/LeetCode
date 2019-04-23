# -*- coding: utf-8 -*-
# Created on Sun Apr 21 2019 11:22:7
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# simple bfs
from collections import deque

class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        result, queue = [], deque()
        queue.append((r0, c0))
        visited = [[0 for j in xrange(C)] for i in xrange(R)]
        visited[r0][c0] = 1
        while len(queue) > 0:
            r, c = queue.popleft()
            result.append([r, c])
            if r - 1 >= 0 and not visited[r - 1][c]:
                queue.append((r - 1, c))
                visited[r - 1][c] = 1
            if r + 1 < R and not visited[r + 1][c]:
                queue.append((r + 1, c))
                visited[r + 1][c] = 1
            if c - 1 >= 0 and not visited[r][c - 1]:
                queue.append((r, c - 1))
                visited[r][c - 1] = 1
            if c + 1 < C and not visited[r][c + 1]:
                queue.append((r, c + 1))
                visited[r][c + 1] = 1
        return result
