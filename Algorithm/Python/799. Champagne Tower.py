# -*- coding: utf-8 -*-
# Created on Mon Mar 12 2018 11:6:22
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# dp
class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        dp = [[0 for _ in xrange(i+1)] for i in xrange(query_row+1)]
        dp[0][0] = poured
        for i in xrange(1, query_row+1):
            for j in xrange(i+1):
                if j < i and dp[i-1][j] > 1:
                    dp[i][j] += (dp[i-1][j]-1)/2.0
                if j > 0 and dp[i-1][j-1] > 1:
                    dp[i][j] += (dp[i-1][j-1]-1)/2.0
        return dp[query_row][query_glass] if dp[query_row][query_glass] < 1 else 1
            
        