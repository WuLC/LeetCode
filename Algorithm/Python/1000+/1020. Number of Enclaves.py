# -*- coding: utf-8 -*-
# Created on Mon Apr 01 2019 9:20:15
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# simple dfs
class Solution(object):
    def numEnclaves(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m, n = len(A), len(A[0])
        for i in xrange(m):
            if i == 0 or i == m - 1:
                for j in xrange(n):
                    if A[i][j] == 1:
                        self.dfs(A, i, j, m, n)
            else:
                if A[i][0] == 1:
                    self.dfs(A, i, 0, m, n)
                if A[i][n-1] == 1:
                    self.dfs(A, i, n - 1, m, n)
        
        return sum(A[i][j] for i in xrange(m) for j in xrange(n))
        
    
    def dfs(self, A, i, j, m, n):
        A[i][j] = 0
        if i - 1 >= 0 and A[i-1][j] == 1:
            self.dfs(A, i - 1, j, m, n)
        if i + 1 < m and A[i+1][j] == 1:
            self.dfs(A, i + 1, j, m, n)
        if j - 1 >= 0 and A[i][j-1] == 1:
            self.dfs(A, i, j - 1, m, n)
        if j + 1 < n and A[i][j+1] == 1:
            self.dfs(A, i, j + 1, m, n)
