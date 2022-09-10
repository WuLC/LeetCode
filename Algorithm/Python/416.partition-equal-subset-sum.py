#
# @lc app=leetcode id=416 lang=python
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        if s&1:
            return False
        
        m, n = len(nums), s>>1
        dp = [[0]*(n+1) for _ in range(m+1)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n+1):
                dp[i+1][j] = dp[i][j]
                if j >= nums[i] and dp[i][j-nums[i]] > 0:
                    dp[i+1][j] += dp[i][j-nums[i]]
        return dp[m][n] > 0
        
# @lc code=end

