# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-15 16:51:37
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-15 16:51:49
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tmp = reduce(lambda x,y: x^y, nums)
        for i in xrange(32):
            if tmp & (1<<i):
                index = i
                break
        nums1, nums2 = [], []
        for num in nums:
            if num & (1 << index):
                nums1.append(num)
            else:
                nums2.append(num)
        return [reduce(lambda x,y: x^y, n) for n in (nums1, nums2)]
                