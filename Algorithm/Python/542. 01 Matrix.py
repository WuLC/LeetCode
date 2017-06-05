# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-03-28 20:46:11
# @Last modified by:   WuLC
# @Last Modified time: 2017-06-05 21:17:31
# @Email: liangchaowu5@gmail.com


# bfs, TLE
# perform bfs for each cell that is not 0
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(matrix) == 0: 
            return None
        m, n = len(matrix), len(matrix[0])
        result = [[0]*n for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == 0:
                    continue
                result[i][j] = self.bfs(matrix, m, n, i, j)
        return result
    
    def bfs(self, matrix, m, n, i, j):
        queue = [(i,j,0)]
        visited = [[0]*n for _ in xrange(m)]
        visited[i][j] = 1
        direction = [(-1,0), (1,0), (0,1), (0,-1)]
        while queue:
            curr = queue.pop(0)
            distance = curr[2] + 1
            for dir in direction:
                ni, nj = curr[0]+dir[0], curr[1]+dir[1]
                if 0 <= ni < m and 0 <= nj < n and visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    if matrix[ni][nj] == 0:
                        return distance
                    else:
                        queue.append((ni, nj, distance))


# bfs, AC
# start bfs from nodes that are 0, and reach as many nodes as possible
# update the distance of other nodes when the current distance is shorter than the distance of other nodes
# then push reachable nodes into queue
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(matrix) == 0: 
            return None
        m, n = len(matrix), len(matrix[0])
        queue = []
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == 0:
                    queue.append((i,j,0))
                else:
                    matrix[i][j] = -1
        direction = [(-1,0), (1,0), (0,1), (0,-1)]
        while queue:
            curr = queue.pop(0)
            distance = curr[2] + 1
            for dir in direction:
                ni, nj = curr[0]+dir[0], curr[1]+dir[1]
                if 0 <= ni < m and 0 <= nj < n and (matrix[ni][nj] == -1 or matrix[ni][nj] > distance):
                    matrix[ni][nj] = distance
                    queue.append((ni, nj, distance))
        return matrix



# bfs, similar to the above solution, but don't store the distance in the queue
from collections import deque
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        queue = deque()
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == 0:
                    queue.append((i, j))
                else:
                    matrix[i][j] = -1
        
        distance = 1
        directions = [[-1,0], [1, 0], [0, -1], [0, 1]]
        while len(queue) != 0:
            next = deque()
            while len(queue) != 0:
                cx, cy = queue.popleft()
                for dx, dy in directions:
                    x = cx + dx
                    y = cy + dy
                    if 0 <= x < m and 0 <= y < n and (matrix[x][y] == -1 or matrix[x][y] > distance):
                        matrix[x][y] = distance
                        next.append((x, y))
            queue = next
            distance += 1
        return matrix