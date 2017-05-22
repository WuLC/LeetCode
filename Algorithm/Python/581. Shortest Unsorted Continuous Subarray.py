# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-05-22 10:03:34
# @Last modified by:   WuLC
# @Last Modified time: 2017-05-22 10:05:10
# @Email: liangchaowu5@gmail.com


# O(n) time
# find the part in the middle that must not follow the ascending rule
# then expand it in terms of the max and min value in it 
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        head = 0
        while head < len(nums)-1 and nums[head] <= nums[head+1]:
            head += 1
        if head == len(nums) - 1:
            return 0
        tail = len(nums) - 1
        while tail > 0 and nums[tail] >= nums[tail-1]:
            tail -= 1
        max_val, min_val = max(nums[head:tail+1]), min(nums[head:tail+1])
        
        while tail < len(nums) and  nums[tail] < max_val:
            tail += 1
        while head >= 0 and nums[head] > min_val:
            head -= 1
        return tail - head - 1