#
# @lc app=leetcode id=674 lang=python
#
# [674] Longest Continuous Increasing Subsequence
#

# @lc code=start
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_len, result = 1, 1
        for i in range(1, len(nums)):
            curr_len = curr_len + 1 if nums[i] > nums[i-1] else 1
            result = max(curr_len, result)
        return result
            
# @lc code=end

