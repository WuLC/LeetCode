# -*- coding: utf-8 -*-
# Created on Tue Apr 10 2018 8:17:31
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# dp, time complexity O(kn^2)
# dp[k][j] represents the largest sum of averages while dividing k groups with nums[:j]
class Solution(object):
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        n = len(A)
        result = 0
        dp = [[0]*(n+1) for _ in xrange(K+1)]
        for i in xrange(K):
            for j in xrange(i, n):
                curr_sum, count = 0, 0
                for k in reversed(xrange(i, j+1)):
                    curr_sum += A[k]
                    count += 1
                    if i==0:
                        dp[i][j+1] = curr_sum*1.0/count
                    else:
                        dp[i][j+1] = max(dp[i][j+1], dp[i-1][k] + curr_sum*1.0/count)
                if j == n-1:
                    result = max(result, dp[i][j+1])
        return result