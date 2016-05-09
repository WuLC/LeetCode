# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-09 15:58:11
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-09 15:58:26
# @Email: liangchaowu5@gmail.com

#DP
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for i in xrange(n)] for j in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if i==0 or j==0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]