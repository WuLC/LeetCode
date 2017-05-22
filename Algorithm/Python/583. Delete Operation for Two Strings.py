# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-05-22 09:38:47
# @Last modified by:   WuLC
# @Last Modified time: 2017-05-22 09:40:24
# @Email: liangchaowu5@gmail.com


# dp
# find the longest common subsequence of two strings with dp firstly
# then add the extra length of two strings

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        dp = [[0 for j in xrange(n+1)] for i in xrange(m+1)]
        for i in xrange(m):
            for j in xrange(n):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        return m + n - (dp[m][n] << 1)
        