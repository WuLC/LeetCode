# -*- coding: utf-8 -*-
# Created on Mon Mar 05 2018 20:40:56
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# dp O(n) space
class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        dp = [0 for _ in xrange(len(A)+1)]
        pre = -1
        for i in xrange(len(A)):
            if A[i] > R:
                pre = i
                dp[i+1] = 0
            elif A[i] < L:
                dp[i+1] = dp[i]
            else:
                dp[i+1] = i - pre
        return sum(dp)


# dp O(1) space
class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        idx = -1
        pre, curr = 0, 0
        count = 0
        for i in xrange(len(A)):
            pre = curr
            curr = 0
            if A[i] > R:
                idx = i
            elif A[i] < L:
                curr = pre 
            else:
                curr = i - idx
            count += curr
        return count