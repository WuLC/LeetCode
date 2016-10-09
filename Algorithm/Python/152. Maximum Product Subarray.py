# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-07 20:25:14
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-07 20:25:27
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pmax, nmax, result = nums[0], nums[0], nums[0]
        for i in xrange(1,len(nums)):
            if nums[i] < 0:
                pmax, nmax = nmax, pmax
            pmax = max(nums[i]*pmax, nums[i])
            nmax = min(nums[i]*nmax, nums[i])
            if result < pmax:
                result = pmax
        return result