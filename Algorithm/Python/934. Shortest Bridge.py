# -*- coding: utf-8 -*-
# Created on Fri Nov 09 2018 20:21:25
# Author: WuLC
# EMail: liangchaowu5@gmail.com


# bfs
# referer: https://leetcode.com/problems/shortest-bridge/discuss/189293/C++-BFS-Island-Expansion-+-UF-Bonus
from collections import deque
class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        self.queue = deque()
        painted = False
        for i in xrange(len(A)):
            for j in xrange(len(A)):
                if A[i][j] == 1:
                    self.paint(A, i, j)
                    painted = True
                    break
            if painted:
                break

        # bfs
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        while self.queue:
            i, j = self.queue.popleft()
            for d in directions:
                if 0 <= i + d[0] < len(A) and 0 <= j + d[1] < len(A):
                    if A[i+d[0]][j+d[1]] == 0:
                        A[i+d[0]][j+d[1]] = A[i][j] + 1
                        self.queue.append((i + d[0], j + d[1]))
                    elif A[i+d[0]][j+d[1]] == 1:
                        return A[i][j] - 2
    
    def paint(self, A, i, j):
        if i < 0 or i >= len(A) or j < 0 or j >= len(A) or A[i][j] != 1:
            return
        A[i][j] = 2
        if (i - 1 >= 0 and A[i-1][j] == 0) or (i + 1 < len(A) and A[i+1][j] == 0) or (j - 1 >= 0 and A[i][j-1] == 0) or (j + 1 < len(A) and A[i][j+1] == 0):
           self.queue.append((i, j))            
        self.paint(A, i - 1, j)
        self.paint(A, i + 1, j)
        self.paint(A, i, j - 1)
        self.paint(A, i, j + 1)


