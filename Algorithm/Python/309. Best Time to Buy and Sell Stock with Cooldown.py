# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-09-05 20:16:03
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-05 20:26:31
# @Email: liangchaowu5@gmail.com

# DP with O(n) space will lead to TLE 
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 2:
            return 0
        buy = [[0]*n for i in xrange(n)]
        buy[0], buy[1] = -prices[0], max(-prices[0], -prices[1])
        sell = [[0]*n for i in xrange(n)]
        sell[0], sell[1] = 0, max( prices[1] - prices[0], 0)
        result = max(buy[0], buy[1], sell[0], sell[1])
        for i in xrange(2,n):
            buy[i] = max(buy[i-1], sell[i-2]-prices[i])
            sell[i] = max(sell[i-1], buy[i-1]+prices[i])
            result = max(result, buy[i], sell[i])
        return result


# DP with constant space can ac
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 2:
            return 0
        b0, b1 = -prices[0], -prices[0]
        s2, s1, s0= 0, 0, 0
        for i in xrange(1, n):
            b0 = max(b1, s2 - prices[i])
            s0 = max(s1, b1 + prices[i])
            b1, s1, s2 = b0, s0, s1
        return s0