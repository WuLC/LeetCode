# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-10-23 15:35:39
# @Last modified by:   WuLC
# @Last Modified time: 2016-10-23 17:12:03
# @Email: liangchaowu5@gmail.com

# method1, use a set to store candidate sum
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total>>1
        candidates = {0}
        for num in nums:
            tmp = set()
            for can in candidates:
                t = can + num 
                if t == target:
                    return True
                if t < target:
                    tmp.add(t)
            candidates |= tmp
        return False



# method 2, DP, dp[i] represents whether i can be sum up from nums
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total>>1
        dp = [False for i in xrange(target+1)]
        dp[0] = True
        for num in nums:
            if num > target:
                continue
            for i in reversed(xrange(num, target+1)): # indices from larger to smaller, otherwise some elements can be caculated repeatedly
                dp[i] = dp[i] or dp[i-num]
            if dp[target]:
                return True
        return False


# method 3, 