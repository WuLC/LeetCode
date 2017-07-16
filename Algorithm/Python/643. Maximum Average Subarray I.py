# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-07-16 16:23:38
# @Last Modified by:   WuLC
# @Last Modified time: 2017-07-16 16:23:45


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        start, end = 0, k
        count = sum(nums[0:k])
        result = 1.0*count/k
        while end < len(nums):
            count -= nums[start]
            start += 1
            count += nums[end]
            end += 1
            result = max(result, 1.0*count/k)
        return result
            
        