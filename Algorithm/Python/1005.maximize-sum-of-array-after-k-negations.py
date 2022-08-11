#
# @lc app=leetcode id=1005 lang=python
#
# [1005] Maximize Sum Of Array After K Negations
#

# @lc code=start
class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] *= -1
                k -= 1
        
        if k%2 > 0:
            nums.sort()
            nums[0] *= -1
        
        return sum(nums)

# @lc code=end

