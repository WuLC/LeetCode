#
# @lc app=leetcode id=188 lang=python
#
# [188] Best Time to Buy and Sell Stock IV
#

# @lc code=start

# variant of problem 188
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        dp = [[0]*(2*k+1) for _ in range(len(prices))]
        for i in range(len(prices)):
            if i == 0:
                for j in range(1, 2*k+1, 2):
                    dp[i][j] = -prices[i] # buy on the first day
            else:
                for j in range(1, 2*k+1):
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + (-1)**j * prices[i])
        return max(dp[len(prices)-1][:])
        
# @lc code=end

