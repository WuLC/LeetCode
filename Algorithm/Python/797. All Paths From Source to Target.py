# -*- coding: utf-8 -*-
# Created on Sun Mar 11 2018 11:34:6
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# dfs or bfs
class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        self.result = []
        self.dfs(graph, [0], 0)
        return self.result
    
    def dfs(self, graph, tmp, curr):
        if curr == len(graph)-1:
            self.result.append(tmp[:])
            return
        
        for nex in graph[curr]:
            tmp.append(nex)
            self.dfs(graph, tmp, nex)
            tmp.pop()
