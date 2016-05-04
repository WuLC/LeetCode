# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-04 14:48:52
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-04 14:49:06
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.helper(nums,0,result)
        return result
        
    def helper(self, nums, begin, result):
        n = len(nums)
        if begin == n:
            tmp = nums[:]
            result.append(tmp)
            return
        
        for i in xrange(begin,n):
            nums[begin],nums[i] = nums[i], nums[begin]
            self.helper(nums,begin+1,result)
            nums[begin],nums[i] = nums[i], nums[begin]
        