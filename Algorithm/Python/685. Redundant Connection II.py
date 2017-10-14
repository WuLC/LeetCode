# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-10-14 19:39:39
# @Last Modified by:   WuLC
# @Last Modified time: 2017-10-14 19:42:16

# check whether a node has multiple parents firstly
# if yes, then the edge that needs to be removed must be connected to this node
# if no, then check whether there is a cycle with union-find set
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
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        redundant_edges = None
        count = {}
        for e in edges:
            if e[1] not in count:
                count[e[1]] = []
            count[e[1]].append(e)
            if len(count[e[1]]) == 2:
                redundant_edges = count[e[1]]
                break
            
        if redundant_edges:
            ufs = UnionFindSet()
            for edge in edges:
                if edge == redundant_edges[1]:
                    continue
                if ufs.union(edge[0], edge[1]):
                    return redundant_edges[0]
            return redundant_edges[1]
        else:
            ufs = UnionFindSet()
            for edge in edges:
                if ufs.union(edge[0], edge[1]):
                    return edge