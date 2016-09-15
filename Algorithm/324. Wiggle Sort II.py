# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-09-15 15:20:34
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-15 15:20:47
# @Email: liangchaowu5@gmail.com


class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]