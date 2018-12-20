# -*- coding: utf-8 -*-
# Created on Thu Dec 20 2018 16:12:37
# Author: WuLC
# EMail: liangchaowu5@gmail.com

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + ((right-left)>>1)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left if nums[left] == target else -1