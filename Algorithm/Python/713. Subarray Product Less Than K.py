# -*- coding: utf-8 -*-
# Created on Sun Oct 22 2017 20:33:35
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# two pointers
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        left, right = 0, 0
        product = 1
        while right < len(nums):
            product *= nums[right]
            while left <= right and product >= k:
                product /= nums[left]
                left += 1
            count += right - left + 1
            right += 1
        return count