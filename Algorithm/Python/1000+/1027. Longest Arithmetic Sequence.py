# -*- coding: utf-8 -*-
# Created on Sun Apr 14 2019 15:51:22
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# two dimensional dp, O(n^2) time
# dp[i][j] represents the result ending at index i with diff j

from collections import defaultdict

class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        result = 0
        dp = {}
        for i in xrange(len(A)):
            dp[i] = defaultdict(int)
            for j in xrange(i):
                diff = A[i] - A[j]
                dp[i][diff] = max(dp[i][diff], dp[j][diff] + 1)
                result = max(dp[i][diff], result)
        return result + 1
