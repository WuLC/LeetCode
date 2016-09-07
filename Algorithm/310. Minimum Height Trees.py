# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-09-04 23:13:39
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-07 22:39:48
# @Email: liangchaowu5@gmail.com

# DFS, O(n^2) time, TLE
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph, height = {i:[] for i in xrange(n)}, {}
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        result, mini = [], n
        for root in xrange(n):
            height[root] = self.dfs(root, graph, set())
            mini = min(height[root], mini)
        for k,v in height.items():
            if v==mini:
                result.append(k)
        return result
        
    def dfs(self, root, graph, visited):
        if root in visited:
            return 0
        tmp = 0
        visited.add(root)
        for node in graph[root]:
            tmp = max(tmp, self.dfs(node, graph, visited))
        return tmp + 1

# BFS, O(n) time and O(n) space
# to find the middle nodes of the graph ,remove leaves level by level
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        if n == 1: 
            return [0] 
        adj = [set() for _ in xrange(n)]
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)
    
        leaves = [i for i in xrange(n) if len(adj[i]) == 1]
    
        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for i in leaves:
                j = adj[i].pop()
                adj[j].remove(i)
                if len(adj[j]) == 1: newLeaves.append(j)
            leaves = newLeaves
        return leaves
            