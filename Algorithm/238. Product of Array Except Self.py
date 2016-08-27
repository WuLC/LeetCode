# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-27 20:24:48
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-27 20:40:07
# @Email: liangchaowu5@gmail.com

# O(n) time, O(n) space without division
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left, right, result = [], [], []
        tmp, n = 1, len(nums)
        for i in xrange(n - 1):
            tmp *= nums[i]
            left.append(tmp)
        tmp = 1
        for i in reversed(xrange(1, n)):
            tmp *= nums[i]
            right.append(tmp)
        for i in xrange(n):
            if i==0:
                result.append(right[-1])
            elif i==n-1:
                result.append(left[-1])
            else:
                result.append(left[i-1]*right[n-i-2])
        return result
 
                
# O(n) time, O(1) space without division
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result, n = [1], len(nums)
        for i in xrange(1, n):
            result.append(result[i-1]*nums[i-1])
        right = 1
        for i in reversed(xrange(n)):
            result[i] *=right
            right *= nums[i]
        return result    