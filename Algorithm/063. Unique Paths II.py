# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-09 16:12:04
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-09 16:13:03
# @Email: liangchaowu5@gmail.com

# DP
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for i in xrange(n)] for j in xrange(m)]
        rb,cb=False,False # check if the first row or column is blocked or not
        for i in xrange(m):
            for j in xrange(n):
                if obstacleGrid[i][j] == 1:
                    if i==0:
                        rb = True
                    if j==0:
                        cb = True
                    continue
                elif i==0 or j==0:
                    if (i==0 and rb) or (j==0 and cb):
                        continue
                    else:
                        dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]
        