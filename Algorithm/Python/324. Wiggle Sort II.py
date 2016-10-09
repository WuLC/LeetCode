# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-09-15 15:20:34
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-16 22:43:35
# @Email: liangchaowu5@gmail.com

# O(nlgn) time, O(n) space, AC
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]

# the same as the above solution
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        sorted_nums = sorted(nums)
        odd, even, idx =  (len(nums)-1)/2, len(nums)-1, 0
        while idx < len(nums):
            if idx % 2 == 0:
                nums[idx] = sorted_nums[odd]
                odd -= 1
            else:
                nums[idx] = sorted_nums[even]
                even -= 1
            idx += 1

# 