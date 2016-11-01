# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-11-01 21:35:10
# @Last modified by:   WuLC
# @Last Modified time: 2016-11-01 21:43:38
# @Email: liangchaowu5@gmail.com


# swap number to its right position continously,that is i+1 should be moved to nums[i]
# then those indices that don't have the right number is the missing number


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in xrange(len(nums)):
            idx = nums[i] - 1
            while i != nums[i]-1 and nums[idx] != idx+1:
                nums[i], nums[idx] = nums[idx], nums[i]
                idx = nums[i] - 1
        return [i+1 for i in xrange(len(nums)) if nums[i] != i+1]
        