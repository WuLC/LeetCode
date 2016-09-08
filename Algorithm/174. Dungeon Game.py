# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-09-08 20:56:18
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-08 21:11:58
# @Email: liangchaowu5@gmail.com

# DP, from right-bottom to left-top
# dp[i][j] represent the minimum health at (i,j)

# DP with specifying special cases
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if len(dungeon) == 0:
            return 1
        m, n = len(dungeon), len(dungeon[0])
        dp = [[1]*(n) for i in xrange(m)]
        for i in reversed(xrange(m)):
            for j in reversed(xrange(n)):
                if i==m-1 and j == n-1:
                    dp[i][j] = dp[i][j] - dungeon[i][j] if dp[i][j] - dungeon[i][j] > 0 else 1
                elif i == m-1:
                    dp[i][j] = dp[i][j+1] - dungeon[i][j] if dp[i][j+1] - dungeon[i][j] > 0 else 1
                elif j == n-1:
                    dp[i][j] = dp[i+1][j] - dungeon[i][j] if dp[i+1][j] - dungeon[i][j] > 0 else 1
                else:
                    need = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
                    dp[i][j] = need if need > 0 else 1
        return dp[0][0]


# DP without specifying special cases but with extra space
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if len(dungeon) == 0:
            return 1
        INT_MAX = pow(2, 31) - 1
        m, n = len(dungeon), len(dungeon[0])
        dp = [[INT_MAX]*(n+1) for i in xrange(m+1)]
        dp[m][n-1], dp[m-1][n] = 1, 1
        for i in reversed(xrange(m)):
            for j in reversed(xrange(n)):
                need = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
                dp[i][j] = need if need > 0 else 1
        return dp[0][0]