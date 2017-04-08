# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2017-04-08 22:41:48
# @Last modified by:   WuLC
# @Last Modified time: 2017-04-08 22:42:12
# @Email: liangchaowu5@gmail.com

# binary search
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + ((right - left)>>1);
            if mid-1 >= 0 and nums[mid] == nums[mid-1]:
                if mid-1 > 0 and ((mid - 1) & 1):
                    right = mid - 2
                else:
                    left = mid + 1
            elif mid+1 < len(nums) and nums[mid+1] == nums[mid]:
                if mid > 0 and (mid & 1):
                    right = mid - 1
                else:
                    left = mid + 2
            else:
                return nums[mid]