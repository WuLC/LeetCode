# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-06-28 21:03:20
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-28 21:03:28
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, n = {}, len(nums)
        for i in xrange(n):
            if nums[i] not in count:
                count[nums[i]] = 0
            count[nums[i]] += 1
            if count[nums[i]] > n/2:
                return nums[i]