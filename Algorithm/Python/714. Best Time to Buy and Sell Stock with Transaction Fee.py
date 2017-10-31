# -*- coding: utf-8 -*-
# Created on Sun Oct 22 2017 16:50:12
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# Method 1
# dp, dp[i] represents the max profile up until the i-th day
# O(n^2) time complexity, TLE
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        profit = 0
        dp = [0] * len(prices)
        for i in xrange(1, len(prices)):
            pre_max = 0
            for j in xrange(i):
                pre_max = max(pre_max, dp[j])
                if prices[i] - prices[j] > fee:
                    dp[i] = max(dp[i], pre_max + prices[i] - prices[j] - fee)
                else:
                    dp[i] = max(dp[i], pre_max)
        return dp[-1]
        
# Method 2
# Also dp, but time complexity is O(n)
# use two arrays(buy and sell)  instead of one
# buy[i] represents the max profit up until i-th day while currently the stock were bought
# sell[i] represents the max profit up until i-th day while currenly the stock were sold
# so at each i, we update buy[i] with sell[i-1] and sell[i] with buy[i-1]
# because you may not buy more than 1 share of a stock at a time
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        n = len(prices)
        buy, sell = [0] * n, [0] * n
        buy[0], sell[0] = - prices[0] - fee, 0
        for i in xrange(1, len(prices)):
            buy[i] = max(buy[i-1], sell[i-1] - prices[i] - fee) # decide whether to buy stock on the i-th day
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])      # decide whether to sell stock on the i-th day
        return sell[n-1]

# Method3 
# same as method2, but change the space complexity from O(n^2) to O(n)
class Solution(object):
    def maxProfit(self, prices, fee):
        if len(prices) == 0:
            return 0
        n = len(prices)
        buy, sell = - prices[0] - fee, 0
        for i in xrange(1, len(prices)):
            pre_buy, pre_sell = buy, sell
            buy = max(pre_buy, pre_sell - prices[i] - fee) # decide whether to buy stock on the i-th day
            sell = max(pre_sell, pre_buy + prices[i])      # decide whether to sell stock on the i-th day
        return sell

# the above method assumes paying fee when buying
# the following method assumes paying fee when selling
class Solution(object):
    def maxProfit(self, prices, fee):
        sell, buy = 0, -prices[0]
        for i in xrange(1, len(prices)):
            pre_buy, pre_sell = buy, sell
            buy = max(pre_buy, pre_sell - prices[i])
            sell = max(pre_sell, pre_buy + prices[i] - fee)
        return sell