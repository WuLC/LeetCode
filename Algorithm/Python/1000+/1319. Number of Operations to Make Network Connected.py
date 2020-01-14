# -*- coding: utf-8 -*-
# Created on Sun Jan 12 2020 15:31:42
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# count the connecte network

# solution 1 union find set
class UnionFindSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.depth = [0] * n
        
    def find(self, val):
        if self.parent[val] != val:
            self.parent[val] = self.find(self.parent[val])
        return self.parent[val]
        
    def union(self, val1, val2):
        p1, p2 = self.find(val1), self.find(val2)
        if p1 != p2:
            if self.depth[p1] > self.depth[p2]:
                self.parent[p2] = p1
            elif self.depth[p1] < self.depth[p2]:
                self.parent[p1] = p2
            else:
                self.parent[p2] = p1
                self.depth[p2] += 1
        

class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        if len(connections) < n-1:
            return -1
        ufs = UnionFindSet(n)
        for edge in connections:
            ufs.union(edge[0], edge[1])
        unique_parents = {ufs.find(ufs.parent[i]) for i in range(n)}
        return len(unique_parents) - 1

# solution 2, dfs
class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        if len(connections) < n - 1:
            return -1
        g = [[] for _ in range(n)]
        for n1, n2 in connections:
            g[n1].append(n2)
            g[n2].append(n1)
        visited = [0] * n
        def dfs(i):
            if visited[i]:
                return 0
            visited[i] = 1
            for j in g[i]:
                if visited[j]:
                    continue
                dfs(j)
            return 1
        return sum(dfs(i) for i in range(n)) - 1
                