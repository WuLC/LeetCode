#
# @lc app=leetcode id=322 lang=python
#
# [322] Coin Change
#

# @lc code=start
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [-1] * (amount+1)
        dp[0] = 0
        for c in coins:
            for i in range(c, amount+1):
                if dp[i-c] >= 0:
                    dp[i] = dp[i-c]+1 if dp[i] < 0 else min(dp[i], dp[i-c]+1)
        return dp[amount]
        
# @lc code=end

