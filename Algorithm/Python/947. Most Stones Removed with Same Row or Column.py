# -*- coding: utf-8 -*-
# Created on Sat Dec 08 2018 20:28:36
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# union find set
# stones at the same row or col connect to each other
from collections import defaultdict

class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        row_index, col_index = defaultdict(list), defaultdict(list)
        for i in range(len(stones)):
            row_index[stones[i][0]].append(i)
            col_index[stones[i][1]].append(i)
        
        edges = []
        for _, v in row_index.items():
            for i in range(len(v)):
                for j in range(i + 1, len(v)):
                    edges.append((v[i], v[j]))

        for _, v in col_index.items():
            for i in range(len(v)):
                for j in range(i + 1, len(v)):
                    edges.append((v[i], v[j]))
        
        # union find set
        n = len(stones)
        self.parents = [i for i in range(n)]
        self.rank = [0] * n
        for v1, v2 in edges:
            self.union(v1, v2)
        unique_parents = {self.find(i) for i in range(n)}
        return n - len(unique_parents)


    def find(self, val):
        if self.parents[val] != val:
            self.parents[val] = self.find(self.parents[val])
        return self.parents[val]
        

    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)
        if p1 == p2:
            return
        elif self.rank[p1] > self.rank[p2]:
            self.parents[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parents[p1] = p2
        else:
            self.parents[p2] = p1
            self.rank[p1] += 1  