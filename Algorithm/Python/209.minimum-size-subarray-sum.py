#
# @lc app=leetcode id=209 lang=python
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        result, left, right, curr_sum = 0, 0, 0, 0
        while right <= len(nums):
            while curr_sum >= target:
                if result == 0:
                    result = right - left
                else:
                    result = min(result, right - left)
                curr_sum -= nums[left]
                left += 1
            if right < len(nums):
                curr_sum += nums[right]
            right += 1
        return result

        
        
# @lc code=end

