#
# @lc app=leetcode id=309 lang=python
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [[0]*3 for _ in range(len(prices))]
        # 0: have stock
        # 1: have no stock and need to cool down
        # 2: have no stock and don't need to cool down
        for i in range(len(prices)):
            if i == 0:
                dp[i][0] = -prices[i]
            else:
                dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])
                dp[i][1] = dp[i-1][0] + prices[i]
                dp[i][2] = max(dp[i-1][2], dp[i-1][1])
        return max(dp[len(prices)-1][:])
        
# @lc code=end

