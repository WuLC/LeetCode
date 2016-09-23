# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-09-23 23:59:07
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-24 00:02:47
# @Email: liangchaowu5@gmail.com

# use stack
# extract i digits from nums1 and (k-i) digits from nums2 and merge them to the largest number
# thus the problem is to  extract i digits from a numbers array to form the largest number

class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        return max(self.merge(self.single_max(nums1, i), self.single_max(nums2, k-i)) for i in xrange(k+1) if i <= len(nums1) and (k-i) <= len(nums2))
    
    
    def single_max(self, nums, k):
        drop = len(nums) - k
        stack = []
        for digit in nums:
            while drop and stack and stack[-1] < digit:
                stack.pop()
                drop -= 1
            stack.append(digit)
        return stack[:k]
    
    def merge(self, nums1, nums2):
        return [max(nums1,nums2).pop(0) for _ in xrange(len(nums1)+len(nums2))]
    
    
        