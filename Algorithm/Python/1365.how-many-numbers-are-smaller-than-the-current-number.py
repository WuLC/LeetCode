#
# @lc app=leetcode id=1365 lang=python
#
# [1365] How Many Numbers Are Smaller Than the Current Number
#

# @lc code=start
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        idx = dict()
        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in idx:
                idx[sorted_nums[i]] = i
        return [idx[num] for num in nums]
                  
# @lc code=end

