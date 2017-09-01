# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-09-01 20:26:40
# @Last Modified by:   WuLC
# @Last Modified time: 2017-09-01 20:28:52

# dp, time complexity: O(n^3)
# dp[i][j] represents the minimum number of turns for s[i:j+1]
# pay attention to the order of traverse

class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: 
            return 0
        n = len(s)
        dp = [[0 for i in xrange(n)] for j in xrange(n)]
        for i in reversed(xrange(len(s))):
            dp[i][i] = 1
            for j in xrange(i+1, len(s)):
                temp = dp[i][j-1] + 1
                for k in xrange(i, j):
                    if s[k] == s[j]:
                        temp = min(temp, dp[i][k-1] + dp[k][j-1])
                dp[i][j] = temp
        return dp[0][n-1]