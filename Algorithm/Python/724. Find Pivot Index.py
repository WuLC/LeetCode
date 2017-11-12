# -*- coding: utf-8 -*-
# Created on Sun Nov 12 2017 11:15:47
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# simple solution
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        curr_sum = 0
        for i in xrange(len(nums)):
            if (curr_sum << 1) == total - nums[i]:
                return i
            curr_sum += nums[i]
        return -1
                
        