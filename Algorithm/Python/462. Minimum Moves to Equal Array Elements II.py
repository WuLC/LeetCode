# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-11-25 09:42:17
# @Last modified by:   WuLC
# @Last Modified time: 2016-11-25 09:42:35
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        target = (nums[n/2]+nums[n/2-1])/2 if n % 2 == 0 else nums[n/2]
        return sum([abs(num - target) for num in nums])