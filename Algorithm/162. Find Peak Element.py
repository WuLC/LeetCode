# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-08-03 15:41:54
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-03 15:42:02
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.helper(nums, 0, len(nums)-1)
    
    def helper(self, nums, left, right):
        if left == right:
            return left
        mid = (left+right)/2
        if nums[mid] > nums[mid+1]:
            return self.helper(nums, left, mid)
        else:
            return self.helper(nums, mid+1, right)