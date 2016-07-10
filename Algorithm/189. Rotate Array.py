# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-10 21:44:51
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-10 21:49:25
# @Email: liangchaowu5@gmail.com


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        for i in xrange(k):
            nums.insert(0, nums.pop())