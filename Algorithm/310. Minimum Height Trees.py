# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-09-04 23:13:39
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-04 23:14:06
# @Email: liangchaowu5@gmail.com

# DFS, TLE
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

# BFS, 