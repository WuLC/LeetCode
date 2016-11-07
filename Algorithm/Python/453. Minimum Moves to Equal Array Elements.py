# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-11-07 11:11:17
# @Last modified by:   WuLC
# @Last Modified time: 2016-11-07 11:29:32
# @Email: liangchaowu5@gmail.com


# suppose n is the length of nums, m is the number of minimun moves, k is the equal elements
# sum(nums) + (n-1)*m = k*n  -->  m = sum(nums) - (k-m)*n
# (k-m)*n refers to the current largest equal sum

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 0 if len(nums) == 0 else sum(nums) - min(nums)*len(nums)
