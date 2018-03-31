# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-07 20:25:14
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-07 20:25:27
# @Email: liangchaowu5@gmail.com

# dp, O(1) space, O(n) time
# record the max number and min number at each position, cause a negative number may turn a min number to a max one
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, curr_max, curr_min = nums[0], nums[0], nums[0]
        for i in xrange(1, len(nums)):
            candidate = [nums[i], nums[i]*curr_max, nums[i]*curr_min]
            curr_max, curr_min = max(candidate), min(candidate)
            result = max(curr_max, result)
        return result
        