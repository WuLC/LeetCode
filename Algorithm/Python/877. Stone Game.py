# -*- coding: utf-8 -*-
# Created on Tue Jul 31 2018 9:55:39
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# 2D-DP
# dp[i][j] represents how many stones the person who takes first finally get more than the other in piles[i] to piles[j]
class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        dp = [[0]*n for _ in xrange(n)]
        for i in reversed(xrange(n)):
            for j in xrange(i, n):
                if i==j:
                    dp[i][j] = piles[i]
                else:
                    dp[i][j] = max(piles[i]-dp[i+1][j], piles[j]-dp[i][j-1])
        return dp[0][n-1]>0