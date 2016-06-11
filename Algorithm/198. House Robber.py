# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-06-11 13:19:29
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-11 13:19:45
# @Email: liangchaowu5@gmail.com


# DP
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.insert(0, 0)
        for i in xrange(3, len(nums)):
            nums[i] = max(nums[i]+nums[i-2], nums[i]+nums[i-3])
        return max(nums)
