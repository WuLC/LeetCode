# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2017-07-21 23:54:13
# @Last modified by:   WuLC
# @Last Modified time: 2017-07-22 15:02:57
# @Email: liangchaowu5@gmail.com

# recursive, TLE
# time complexity: O(4^n)
class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        if N < 0:
            return 0
        if i < 0 or i >= m or j < 0 or j >= n:
            return   1
        dirs = [[-1,0],[1,0],[0,-1],[0,1]]
        count = 0
        for d in dirs:
            count += self.findPaths(m, n, N-1, i+d[0], j+d[1])
        return count


# dp, AC
# time complexity: O(m * n * N)
# referer: https://leetcode.com/problems/out-of-boundary-paths/#/solution
class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        dp = [[0 for u in xrange(n)] for v in xrange(m)]
        dp[i][j] = 1
        M = 1000000007
        result = 0
        for _ in xrange(N):
            tmp = [[0 for u in xrange(n)] for v in xrange(m)]
            for i in xrange(m):
                for j in xrange(n):
                    if i == 0: result += dp[i][j]
                    if i == m-1: result += dp[i][j]
                    if j == 0: result += dp[i][j]
                    if j == n-1: result += dp[i][j]
                    # update dp for next step    
                    if i > 0: tmp[i][j] += dp[i-1][j]
                    if i < m-1: tmp[i][j] += dp[i+1][j]
                    if j > 0: tmp[i][j] += dp[i][j-1]
                    if j < n-1: tmp[i][j] += dp[i][j+1]
                    tmp[i][j] %= M
            dp = tmp
        return result