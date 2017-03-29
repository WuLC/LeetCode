# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-03-28 20:46:11
# @Last modified by:   WuLC
# @Last Modified time: 2017-03-29 12:57:29
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
# push reachable nodes into queue
# then update the distance of other nodes when there are shorter paths
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