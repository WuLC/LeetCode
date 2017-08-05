# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-03-09 23:47:18
# @Last modified by:   WuLC
# @Last Modified time: 2017-08-05 12:28:05
# @Email: liangchaowu5@gmail.com

# change 0 to -1
# similar to the problem to find subsequence whose sum is n*k 
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in xrange(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
        
        mapping = {0:-1}
        curr_sum = 0
        result = 0
        for i in xrange(len(nums)):
            curr_sum += nums[i]
            if curr_sum in mapping:
                result = max(result, i-mapping[curr_sum])
            else:
                mapping[curr_sum] = i
        return result