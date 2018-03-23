# -*- coding: utf-8 -*-
# Created on Fri Mar 23 2018 15:1:22
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# dp, O(n^2) time, O(n^2) space
# dp[i][j] represents the order of the largest plus sign while (i,j) is the center

class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        dp = [[N]*N for _ in xrange(N)]
        for mine in mines:
            dp[mine[0]][mine[1]] = 0
            
        for i in xrange(N):
            l, r, u, d = 0, 0, 0, 0
            for j in xrange(N):
                k = N - 1 - j
                
                l = l+1 if dp[i][j] != 0 else 0
                if dp[i][j] > l:
                    dp[i][j] = l
                
                r = r+1 if dp[i][k] != 0 else 0
                if dp[i][k] > r:
                    dp[i][k] = r
                
                u = u+1 if dp[j][i] != 0 else 0
                if dp[j][i] > u:
                    dp[j][i] = u
                
                d = d+1 if dp[k][i] != 0 else 0
                if dp[k][i] > d:
                    dp[k][i] = d
        
        result = 0
        for i in xrange(N):
            for j in xrange(N):
                result = max(result, dp[i][j])
        return result