# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-09-13 19:57:19
# @Last Modified by:   WuLC
# @Last Modified time: 2017-09-13 19:58:09

# be careful of the last element
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        result = 1
        count = 1
        for i in xrange(1, len(nums)):
            if nums[i] > nums[i-1]:
                count += 1
            else:
                count = 1
            result = max(result, count)
        return result
                    
                
                