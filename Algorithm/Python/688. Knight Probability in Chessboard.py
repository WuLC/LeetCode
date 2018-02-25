# -*- coding: utf-8 -*-
# Created on Sun Feb 25 2018 22:40:45
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# dfs, TLE
class Solution(object):
    def __init__(self):
        self.count = 0
        self.moves = [[-2, -1], [-1, -2], [1, -2], [2, -1], [-2, 1], [-1, 2], [2, 1], [1, 2]]
        
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        self.count = 0
        self.helper(N, K, r, c)
        return self.count*1.0/(8**K)
    
    def helper(self, N, K, r, c):
        if not (0<=r<N and 0<=c<N):
            return 
        if K == 0:
            if 0<=r<N and 0<=c<N:
                self.count += 1
            return
        for m in self.moves:
            self.helper(N, K-1, r+m[0], c+m[1])