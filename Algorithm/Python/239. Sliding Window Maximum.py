# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-06-29 09:05:14
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-29 09:05:23
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result, index = [], []
        for i in xrange(len(nums)):
            if index and index[0]<i-k+1:
                index.remove(index[0])
            while index and nums[i] > nums[index[-1]]:
                index.pop()
            index.append(i)
            if i >= k-1:
                result.append(nums[index[0]])
        return result
                
            