#
# @lc app=leetcode id=300 lang=python
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, dp = 0, [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i-1, -1, -1):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
            result = max(dp[i], result)
        return result
        
# @lc code=end

