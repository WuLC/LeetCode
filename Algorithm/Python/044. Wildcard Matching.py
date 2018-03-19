# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-03-12 10:40:35
# @Last modified by:   LC
# @Last Modified time: 2016-04-10 16:24:46
# @Email: liangchaowu5@gmail.com


# dp, dp[i][j] represents whether p[:i] matches s[:j]
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(p), len(s)
        dp = [[False for j in xrange(n+1)] for i in xrange(m+1)]
        dp[0][0] = True
        for i in xrange(1, m+1):
            for j in xrange(n+1):
                if j == 0:
                    if p[i-1] == '*':
                        dp[i][j] = dp[i-1][j]
                elif p[i-1] == s[j-1] or p[i-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[i-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
        return dp[m][n]