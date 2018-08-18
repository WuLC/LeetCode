# -*- coding: utf-8 -*-
# Created on Tue Aug 14 2018 11:58:30
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# dfs
# imagine it as a graph, put the numbers into 1 group and -1 group
from collections import defaultdict
class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        edges = defaultdict(list)
        for d in dislikes:
            edges[d[0]].append(d[1])
            edges[d[1]].append(d[0])
        group = [0]*(N+1)
        for i in xrange(1, N+1):
            if group[i]==0 and (i in edges) and not self.dfs(i, edges, group, 1):
                return False
        return True

    def dfs(self, i, edges, group, g):
        """whether it is possible to put i in group g"""
        group[i] = g
        for neighbor in edges[i]:
            if group[neighbor] == group[i]:
                return False
            if group[neighbor]==0 and not self.dfs(neighbor, edges, group, -1*g): 
                return False
        return True