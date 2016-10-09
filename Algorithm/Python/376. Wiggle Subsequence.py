# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-09-04 09:43:45
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-04 09:49:44
# @Email: liangchaowu5@gmail.com

# DP, O(n) time, O(1) space
# 32 ms, first time to beat 100.00% of pythonsubmissions, ^_^
class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        pos, neg = 0, 0 # pos is the max length so far ended with a positive difference ,while neg is the the max length so far ended with a negative difference
        diff = []
        for i in xrange(1, len(nums)):
            tmp =  nums[i] - nums[i-1]
            if tmp != 0:
                diff.append(tmp)
        for i in xrange(len(diff)):
            if diff[i] > 0:
                pos = max(neg+1, pos)
            else:
                neg = max(pos+1, neg)
        return max(pos, neg)+1
            
            
            
            
        