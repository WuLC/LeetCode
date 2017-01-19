# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2017-01-19 12:53:09
# @Last modified by:   WuLC
# @Last Modified time: 2017-01-19 12:53:28
# @Email: liangchaowu5@gmail.com


# constanct space dynamic programming

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        previous = 0
        result = 0
        for i in xrange(len(nums)):
            if nums[i] == 0:
                result = max(previous, result)
                previous = 0
            else:
                previous += 1
        result = max(result, previous)
        return result