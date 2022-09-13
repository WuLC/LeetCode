#
# @lc app=leetcode id=714 lang=python
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        dp = [[0]*2 for _ in range(len(prices))]
        # 0: hold the stock; 1: hold no stock
        for i in range(len(prices)):
            if i == 0:
                dp[i][0] = -prices[i]
            else:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
                dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i] - fee)
        return max(dp[len(prices)-1][:])
        
# @lc code=end

