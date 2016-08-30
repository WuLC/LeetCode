# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-30 12:02:38
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-30 12:25:01
# @Email: liangchaowu5@gmail.com

# backtracking, TLE
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        result = [0]
        self.helper(s, t, 0, 0, result)
        return result[0]
        
    def helper(self, s, t, si, ti, result):
        if ti == len(t):
            result[0] += 1
            return 
        if si == len(s):
            return 
        while si < len(s):
            if s[si] == t[ti]:
                self.helper(s, t, si+1, ti+1, result)
            si += 1

# DP, AC
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s)+1, len(t)+1
        dp = [[0 for i in xrange(n)] for j in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = 0
                else:
                    if s[i-1] != t[j-1]:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
        return dp[m-1][n-1]
