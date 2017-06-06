# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-06-06 21:47:07
# @Last modified by:   WuLC
# @Last Modified time: 2017-06-06 21:47:32
# @Email: liangchaowu5@gmail.com


# naive O(n^2), TLE
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in xrange(1, len(nums)):
            nums[i] += nums[i-1]
        count = 0
        nums = [0] + nums
        for i in xrange(len(nums)-1):
            for j in xrange(i+1, len(nums)):
                if nums[j] - nums[i] == k:
                    count += 1
        return count


# 