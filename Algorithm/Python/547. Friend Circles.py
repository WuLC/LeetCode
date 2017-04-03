# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2017-04-03 15:24:22
# @Last modified by:   WuLC
# @Last Modified time: 2017-04-03 15:30:11
# @Email: liangchaowu5@gmail.com

# bfs, 115ms
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        circles = 0
        visited = [0] * n
        for i in xrange(n):
            if visited[i] == 0:
                self.bfs(i, M, visited)
                circles += 1
        return circles
    
    
    def bfs(self,idx, M, visited):
        n = len(M)
        visited[idx] = 1
        queue = [idx]
        while queue:
            curr = queue.pop(0)
            for j in xrange(n):
                if M[curr][j] == 1 and visited[j] == 0:
                    queue.append(j)
                    visited[j] = 1


# dfs, 75ms
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        circles = 0
        visited = [0] * n
        for i in xrange(n):
            if visited[i] == 0:
                self.dfs(i, M, visited)
                circles += 1
        return circles
    
    
    def dfs(self,idx, M, visited):
        visited[idx] = 1
        for j in xrange(len(M)):
            if M[idx][j] == 1 and visited[j] == 0:
                self.dfs(j, M, visited)