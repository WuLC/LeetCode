#
# @lc app=leetcode id=977 lang=python
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0] * len(nums)
        left, right = 0, len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            l, r = nums[left]**2, nums[right]**2
            if l > r:
                result[i] = l
                left += 1
            else:
                result[i] = r
                right -= 1
        return result
        
# @lc code=end

