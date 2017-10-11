# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-10-09 09:38:37
# @Last Modified by:   WuLC
# @Last Modified time: 2017-10-11 19:09:06


# union-find set


# simple union-find set
# time complexity: O(mn)
# m is the number of edges while n is the number of possible integers
class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parents = [i for i in xrange(1001)]
        for edge in edges:
            v1, v2 = edge[0], edge[1]
            if parents[v1] == parents[v2]:
                return edge
            tmp = parents[v2]
            for i in xrange(len(parents)):
                if parents[i] == tmp:
                    parents[i] = parents[v1]
        return None


# with path compression and union join by rank
# time complexity: O(mlogn)
class UnionFindSet(object):
    def __init__(self):
        self.parents = range(1001)
        self.rank = [0] * 1001
        
    def find(self, val):
        """find with path compression"""
        if self.parents[val] != val:
            self.parents[val] = self.find(self.parents[val])
        return self.parents[val]

    def union(self, v1, v2):
        """union by rank, check whether union two vertics will lead to a cycle"""
        p1, p2 = self.find(v1), self.find(v2)
        if p1 == p2:
            return True
        elif self.rank[p1] > self.rank[p2]:
            self.parents[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parents[p1] = p2
        else:
            self.rank[p2] += 1
            self.parents[p1] = p2
        return False
            
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        ufs = UnionFindSet()
        for edge in edges:
            if ufs.union(edge[0], edge[1]):
                return edge
