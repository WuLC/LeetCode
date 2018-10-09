# -*- coding: utf-8 -*-
# Created on Sun Oct 07 2018 20:47:50
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# dp, O(n) time
# brilliant solution: https://leetcode.com/problems/maximum-sum-circular-subarray/discuss/178422/C++JavaPython-One-Pass
class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        max_sub, min_sub = A[0], A[0]
        curr_max, curr_min = A[0], A[0]
        total = A[0]
        for i in xrange(1, len(A)):
            total += A[i]
            curr_max = max(curr_max + A[i], A[i])
            curr_min = min(A[i], curr_min + A[i])
            max_sub = max(max_sub, curr_max)
            min_sub = min(min_sub, curr_min)
        return max(max_sub, max(A) if total == min_sub else total - min_sub)