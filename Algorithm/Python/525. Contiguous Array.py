# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-03-09 23:47:18
# @Last modified by:   WuLC
# @Last Modified time: 2017-03-10 21:34:22
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
        

# dp, dp[i] represents the longest subarray the ends at i
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0 for _ in xrange(len(nums)+1)]
        
        for i in xrange(1, len(nums)):
            if nums[i] != nums[i-1]:
                dp[i+1] = dp[i-1] + 2
            elif i-1-dp[i] >=0 and nums[i] != nums[i-1-dp[i]]:
                dp[i+1] = dp[i-1-dp[i]] + dp[i] + 2
            else:
                dp[i+1] = 0
        return max(dp)