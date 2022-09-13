#
# @lc app=leetcode id=123 lang=python
#
# [123] Best Time to Buy and Sell Stock III
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [[0]*5 for _ in range(len(prices))]
        # do nothing, first buy, first sell, second buy, second sell
        for i in range(len(prices)):
            if i == 0:
                dp[i][1], dp[i][3] = -prices[i], -prices[i]
            else:
                # dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
                # dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i])
                # dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i])
                # dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i])

                # use more concise code
                for j in range(1, 5):
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + (-1)**j * prices[i])
        return max(dp[len(prices)-1][:])

        
# @lc code=end

