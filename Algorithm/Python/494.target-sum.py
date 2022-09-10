#
# @lc app=leetcode id=494 lang=python
#
# [494] Target Sum
#

# @lc code=start
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # x - (sum-x) = target -> x = (sum+target)/2
        total = sum(nums) + target
        if (total&1) > 0 or (total>>1) < 0:
            return 0
        
        m, n = len(nums), total>>1
        dp = [[0] * (n+1) for _ in range(m+1)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n+1):
                dp[i+1][j] = dp[i][j]
                if j >= nums[i] and dp[i][j-nums[i]]:
                    dp[i+1][j] += dp[i][j-nums[i]]

        return dp[m][n]
        
# @lc code=end

