# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-06-27 21:34:45
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-28 19:57:18
# @Email: liangchaowu5@gmail.com


# method 1, judge diectly, O(n^3),TLE
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in xrange(len(nums)):
            tmp = [nums[i]]
            for j in xrange(len(nums)):
                if j != i and self.divisable(tmp, nums[j]):
                    tmp.append(nums[j])
            if len(tmp) > len(result):
                result = tmp[:]
        return result
    
    def divisable(self, nums, num):
        for i in xrange(len(nums)):
            if nums[i] % num == 0 or num % nums[i] == 0:
                continue
            else:
                return False
        return True

# method 2,DP, O(n^2), AC
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        dp = [1]*len(nums)
        record, index = [], 0
        for i in xrange(len(nums)):
            tmp = [nums[i]]
            for j in xrange(i):
                if nums[i] % nums[j] == 0:
                    if dp[j]+1 > dp[i]:
                        tmp = record[j] + [nums[i]]
                        dp[i] = dp[j] + 1
            if dp[i] > dp[index]:
                index = i
            record.append(tmp[:])
        return record[index] if record else record              