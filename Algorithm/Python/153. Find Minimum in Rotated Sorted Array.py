# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-03 16:23:35
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-03 16:23:47
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return None
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right)/2
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid
        return nums[left]