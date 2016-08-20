# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-19 17:56:52
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-19 21:11:59
# @Email: liangchaowu5@gmail.com

# method 1,dynamic programming , O(n^2)
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 0
        dp, result = [1]*n, 1
        for i in xrange(1,n):
            for j in xrange(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            result = max(result, dp[i])
        return result

# method 2, 