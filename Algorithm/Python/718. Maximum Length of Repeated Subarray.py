# -*- coding: utf-8 -*-
# Created on Tue Oct 31 2017 21:7:54
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# dp
# dp[i][j] represents the maximum length of repeated subarray between A[:i] and B[:j]
# while A ends at index i and B ends at index j
# time complexity: O(mn), m is the length of A while n is the length of B, yet TLE
class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        result = 0
        m, n = len(A), len(B)
        dp = [[0 for j in xrange(n+1) ] for i in xrange(m+1)]
        for i in xrange(m):
            for j in xrange(n):
                if A[i] == B[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                result = max(result, dp[i+1][j+1])
        return result