# -*- coding: utf-8 -*-
# Created on Sun Oct 22 2017 17:40:14
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# dp, dp[i][j] represents the minimum ascii delete sum for s1[:i] ans s2[:j]
# TLE, time complexity O(mn), m = len(s1), n = len(s2)
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        m, n = len(s1) + 1, len(s2) + 1
        dp = [[0] * n for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    dp[i][j] = dp[i][j-1] + ord(s2[j-1])
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + ord(s1[i-1])
                elif s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min([dp[i-1][j-1] + ord(s2[j-1]) + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1]), dp[i-1][j] + ord(s1[i-1])])
        return dp[m-1][n-1]

# 