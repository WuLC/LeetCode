# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-08-05 15:56:28
# @Last Modified by:   WuLC
# @Last Modified time: 2017-08-05 16:14:27


# dp
# dp[i+1][j] refers max profit up until prices[j] (Note: NOT ending with prices[ii]) using at most i transactions. 
# referer: https://discuss.leetcode.com/topic/4766/a-clean-dp-solution-which-generalizes-to-k-transactions

# time O(kn^2), TLE
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        m, n = 2, len(prices)
        dp = [[0 for i in xrange(n)] for j in xrange(m+1)]
        result = 0
        for i in xrange(m):
            for j in xrange(1, n):
                curr_max = max([dp[i][k] + prices[j] - prices[k] for k in xrange(j)])
                dp[i+1][j] = max(dp[i+1][j-1], curr_max)
                result = max(result, dp[i+1][j])
        return result
                
                    
                    
# time O(kn), AC
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        m, n = 2, len(prices)
        dp = [[0 for i in xrange(n)] for j in xrange(m+1)]
        result = 0
        for i in xrange(m):
            curr_max = dp[i][0] - prices[0]
            for j in xrange(1, n):
                dp[i+1][j] = max(dp[i+1][j-1], prices[j] + curr_max)
                curr_max = max(curr_max, dp[i][j] - prices[j])
                result = max(result, dp[i+1][j])
        return result              
                
        