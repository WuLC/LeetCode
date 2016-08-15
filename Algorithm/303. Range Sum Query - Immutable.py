# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-15 22:29:39
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-15 22:29:46
# @Email: liangchaowu5@gmail.com

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        for i in xrange(1, len(nums)):
            nums[i] += nums[i-1]
        self.nums = nums
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.nums[j]
        else:
            return self.nums[j] - self.nums[i-1]
        


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)