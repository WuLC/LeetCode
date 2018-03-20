# -*- coding: utf-8 -*-
# Created on Tue Mar 20 2018 14:54:47
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# dfs, TLE
# check whether loop exists when starting from a node, if exists it will not succeed
class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        result = []
        visited = [0 for i in xrange(len(graph))]
        for i in xrange(len(graph)):
            if self.isSafe(i, visited, graph):
                result.append(i)
        return result
    
    def isSafe(self, curr, visited, graph):
        if len(graph[curr])==0:
            return True
        visited[curr] = 1
        for node in graph[curr]:
            if visited[node] == 1 or not self.isSafe(node, visited, graph):
                return False
        visited[curr] = 0
        return True
                        

# bfs-like
# store the nodes with 0 out_degree in the queue, keep removing from the queue's head and add new nodes with 0 out_degree
from collections import deque, defaultdict
class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        n = len(graph)
        out_degree = {}
        source = defaultdict(list)
        for i in xrange(n):
            for num in graph[i]:
                out_degree[i] = len(graph[i])
                source[num].append(i)
        
        result = []
        queue = deque([i for i in xrange(n) if i not in out_degree])      
        while len(queue) > 0:
            curr = queue.popleft()
            result.append(curr)
            for s in source[curr]:
                out_degree[s] -= 1
                if out_degree[s] == 0:
                    queue.append(s)
        return sorted(result)