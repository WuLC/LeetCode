# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-05-18 08:21:00
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-18 08:21:10
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = [[]]
        tmp = []
        for i in xrange(1,len(nums)+1):
            self.helper(nums,i,0,result,tmp)
        return result
        
    def helper(self,nums,k,begin,result,tmp):
        if len(tmp) == k:
            result.append(tmp[:])
        for i in xrange(begin,len(nums)):
            tmp.append(nums[i])
            self.helper(nums,k,i+1,result,tmp)
            tmp.remove(nums[i])
        
        