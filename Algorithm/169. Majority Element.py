# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-06-28 21:03:20
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-28 22:14:39
# @Email: liangchaowu5@gmail.com

# method 1, extra space
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

# method 2, Boyer-Moore Majority Vote algorithm 
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate, count = nums[0], 1
        for i in xrange(1, len(nums)):
            if nums[i] == candidate:
                count += 1
            else:
                count -= 1
            if count == 0:
                candidate, count = nums[i], 1
        return candidate