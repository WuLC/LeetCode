# -*- coding: utf-8 -*-
# Created on Tue Dec 26 2017 16:18:55
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# naive solution
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx = nums.index(max(nums))
        for i in range(len(nums)):
            if nums[i] != nums[idx] and nums[i]*2 > nums[idx]:
                return -1
        return idx