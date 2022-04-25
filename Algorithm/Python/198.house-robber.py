#
# @lc app=leetcode id=198 lang=python
#
# [198] House Robber
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            if i == 0:
                dp[i+1] = nums[i]
            else:
                dp[i+1] = max(dp[i], dp[i-1] + nums[i])
        return dp[-1]
# @lc code=end

