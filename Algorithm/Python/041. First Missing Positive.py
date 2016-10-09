# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-04-17 11:08:24
# @Last modified by:   WuLC
# @Last Modified time: 2016-04-17 11:08:36
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        for i in xrange(n):
            while 0<nums[i]<=n and (not nums[nums[i]-1]==nums[i]):
                    tmp = nums[i]
                    nums[i] = nums[tmp-1]
                    nums[tmp-1] = tmp
                    # nums[i],nums[nums[i]-1] = nums[nums[i]-1],nums[i]错误
            
        for i in xrange(n):
            if nums[i] == i+1:
                continue
            else:
                return i+1
        
        return n+1 # all match
        