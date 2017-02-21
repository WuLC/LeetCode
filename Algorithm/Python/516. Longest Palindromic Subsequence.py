# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-02-14 11:30:37
# @Last modified by:   WuLC
# @Last Modified time: 2017-02-21 22:02:25
# @Email: liangchaowu5@gmail.com


# two dimentional dp, time O(n^2), space O(n^2)
# Java can AC , but Python get TLE
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: return 0
        n = len(s)
        dp = [[0 for i in xrange(n)] for j in xrange(n)]
        for i in reversed(xrange(n)):
            for j in xrange(i, n):
                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]

# improve upon the above dp solution, time O(n^2), space O(n)
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[1]*2 for _ in xrange(n)]
        for j in xrange(n):
            for i in reversed(xrange(j)):
                if s[i] == s[j]:
                    dp[i][j&1] = 2+dp[i+1][(j-1)&1] if j-1>=i+1 else 2
                else:
                    dp[i][j&1] = max(dp[i+1][j&1], dp[i][(j-1)&1])
        return dp[0][(n-1)&1]