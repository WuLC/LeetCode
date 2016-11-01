# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-11-01 21:31:30
# @Last modified by:   WuLC
# @Last Modified time: 2016-11-01 21:40:09
# @Email: liangchaowu5@gmail.com

# due to the characteristic of the range of the numbers
# swap the number to its right position, that is to move i+1 to nums[i]
# finally those number with value that don't match its index is the duplicate number

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in xrange(len(nums)):
            idx = nums[i] - 1
            while nums[i] != i+1 and nums[idx] != idx+1:
                nums[i], nums[idx] = nums[idx], nums[i]
                idx = nums[i] - 1
        return [nums[i] for i in xrange(len(nums)) if nums[i] != i+1]
            
        