# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-19 17:56:52
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-21 08:03:13
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

# method 2, DP and binary search， O(n*logn)
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []
        for num in nums:
            if len(dp) == 0 or len(dp) > 0 and num > dp[-1]:
                dp.append(num)
            else:
                self.binary_search(dp, num)
        return len(dp)
    
    
    def binary_search(self, dp, num):
        left, right = 0, len(dp)-1
        while left < right:
            mid = left + (right - left)/2
            if dp[mid] == num:
                return
            elif dp[mid] > num:
                right = mid 
            else:
                left = mid + 1
        if dp[left] > num:
            dp[left] = num