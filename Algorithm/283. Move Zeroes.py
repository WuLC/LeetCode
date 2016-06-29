# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-06-29 09:39:50
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-29 09:40:07
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, count = 0, 0
        while i < len(nums):
            while i < len(nums) and nums[i] == 0:
                nums.remove(nums[i])
                count += 1
            i += 1
        for i in xrange(count):
            nums.append(0)