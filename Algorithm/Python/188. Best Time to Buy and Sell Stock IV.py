# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-30 21:58:01
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-30 21:58:06
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0: return 0
        # add this to avoid the condition that k is very large thus lead to TLE
        if k >= len(prices)-1:
            max_profit = 0
            for i in xrange(len(prices)-1):
                if prices[i] < prices[i+1]:
                    max_profit += (prices[i+1] - prices[i])
            return max_profit
            
        dp = [[0 for j in xrange(len(prices))] for i in xrange(k+1)]
        for i in xrange(1,k+1):
            tmp_max = dp[i-1][0] - prices[0]
            for j in xrange(1, len(prices)):
                dp[i][j] = max(tmp_max + prices[j], dp[i][j-1])
                tmp_max = max(tmp_max, dp[i-1][j-1] - prices[j])
        return dp[k][len(prices)-1]