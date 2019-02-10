# -*- coding: utf-8 -*-
# Created on Sun Feb 10 2019 10:50:7
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# union find set
class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        ufs = UnionFindSet()
        for e in equations:
            if e[1] == '=':
                ufs.union(ord(e[0]) - 97, ord(e[3]) - 97)
        for e in equations:
            if e[1] == '!' and ufs.find(ord(e[0]) - 97) == ufs.find(ord(e[3]) - 97):
                return False
        return True
    

class UnionFindSet(object):
    def __init__(self):
        self.parent = range(26)
        self.rank = [0] * 26
    
    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
    
    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1