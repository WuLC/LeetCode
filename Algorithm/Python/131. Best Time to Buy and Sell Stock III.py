# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-22 07:52:19
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-22 19:45:12
# @Email: liangchaowu5@gmail.com

# DP1, TLE, O(n^4)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        t = 2 # number of transaction
        n = len(prices)
        dp = [[0 for j in xrange(n+1)] for i in xrange(t+1)]
        for i in xrange(1,t+1):
            for j in xrange(n):
                for k in xrange(j+1):
                    dp[i][j+1] = max(dp[i][j+1], prices[j]-min(prices[k:j+1])+dp[i-1][k+1])
                    if dp[i][j+1] > result:
                        result = dp[i][j+1]
        return result

# DP2, TLE, O(n^3)
# class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result, n = 0, len(prices)
        k = 2
        dp = [[0 for i in xrange(n)] for j in xrange(k+1)]
        for i in xrange(1, k+1):
            for j in xrange(1,n):
                for m in xrange(j):
                    dp[i][j] = max(dp[i][j], dp[i-1][m] + prices[j] - prices[m])
                dp[i][j] = max(dp[i][j], dp[i][j-1])
                result = max(result, dp[i][j])
        return result


# DP3, AC, O(n^2)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        result = 0
        t = 2 # number of transaction
        n = len(prices)
        dp = [[0 for j in xrange(n)] for i in xrange(t+1)]
        for i in xrange(1,t+1):
            tmp = dp[i-1][0] - prices[0]
            for j in xrange(1,n):
               dp[i][j] = max(tmp + prices[j], dp[i][j-1])
               tmp = max(tmp, dp[i-1][j]-prices[j])
               result = max(result, dp[i][j])
        return result