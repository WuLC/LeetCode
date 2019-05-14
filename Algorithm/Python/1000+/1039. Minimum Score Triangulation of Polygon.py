# -*- coding: utf-8 -*-
# Created on Tue May 14 2019 15:58:16
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# recursive
class Solution(object):
    def minScoreTriangulation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        self.dp = [[0]*n for _ in xrange(n)]
        return self.helper(A, 0, len(A)-1)
    
    def helper(self, A, i, j):
        if i + 1 >= j:
            return 0
        for k in xrange(i + 1, j):
            if self.dp[i][k] == 0:
                self.dp[i][k] = self.helper(A, i, k)
            if self.dp[k][j] == 0:
                self.dp[k][j] = self.helper(A, k, j)
            tmp = self.dp[i][k] + A[i]*A[k]*A[j] + self.dp[k][j]
            if self.dp[i][j] == 0:
                self.dp[i][j] = tmp
            else:
                self.dp[i][j] = min(self.dp[i][j], tmp)
        return self.dp[i][j]

