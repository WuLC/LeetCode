#
# @lc app=leetcode id=343 lang=python
#
# [343] Integer Break
#

# @lc code=start
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        dp[1], dp[2] = 1, 1
        for i in range(3, n+1):
            for j in range(1, i-1):
                dp[i] = max(dp[i], max(j * (i-j), j * dp[i-j]))
        return dp[n]
        
# @lc code=end

