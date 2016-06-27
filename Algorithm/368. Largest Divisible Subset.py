# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-06-27 21:34:45
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-27 21:35:03
# @Email: liangchaowu5@gmail.com


# method 1,TLE
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in xrange(len(nums)):
            tmp = [nums[i]]
            for j in xrange(len(nums)):
                if j != i and self.divisable(tmp, nums[j]):
                    tmp.append(nums[j])
            if len(tmp) > len(result):
                result = tmp[:]
        return result
    
    def divisable(self, nums, num):
        for i in xrange(len(nums)):
            if nums[i] % num == 0 or num % nums[i] == 0:
                continue
            else:
                return False
        return True
                