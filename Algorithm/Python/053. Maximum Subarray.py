# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-03 14:49:45
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-03 14:54:07
# @Email: liangchaowu5@gmail.com

"""
动态规划，因为只需要求大小，所以不用新开数组，直接在原数组操作
经过DP后nums[i]的大小为以原来nums[i]作为子串最后的一个元素的最大总和
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in xrange(1,n):
            if nums[i-1]>0:
                nums[i] = nums[i]+nums[i-1]
                
        max_num = nums[0]
        for i in xrange(1,n):
            if nums[i]>max_num:
                max_num = nums[i]
        
        return max_num
            