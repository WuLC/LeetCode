# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-11-30 11:44:28
# @Last modified by:   WuLC
# @Last Modified time: 2016-11-30 11:46:09
# @Email: liangchaowu5@gmail.com

# naivve solution, O(n^2), TLE
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        curr_min = nums[0]
        for i in xrange(1, len(nums)-1):
            if curr_min < nums[i]:
                for j in xrange(i+1, len(nums)):
                    if curr_min < nums[j] < nums[i]:
                        return True
            else:
                curr_min = nums[i]
        return False

# 