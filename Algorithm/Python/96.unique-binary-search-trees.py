#
# @lc app=leetcode id=96 lang=python
#
# [96] Unique Binary Search Trees
#

# @lc code=start
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            for j in range(i):
                dp[i] += dp[j]*dp[i-j-1]
        return dp[n]
        
# @lc code=end

