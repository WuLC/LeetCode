#
# @lc app=leetcode id=122 lang=python
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [[0]*2 for _ in range(len(prices))]
        # dp[i][0]: have stock, dp[i][1]: have no stock
        for i in range(len(prices)):
            if i == 0:
                dp[i][0] = -prices[i]
            else:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
                dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        return dp[len(prices)-1][1]
        
# @lc code=end

