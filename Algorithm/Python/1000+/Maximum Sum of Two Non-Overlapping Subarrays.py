# -*- coding: utf-8 -*-
# Created on Fri May 10 2019 9:22:54
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# dp,O(n) time
# for each split point, find the max L elements on the left + max M elements on the right
# or max M elements on the left + max L elements on the right

class Solution(object):
    def maxSumTwoNoOverlap(self, A, L, M):
        """
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        """
        return max(self.helper(A, L, M), self.helper(A, M, L))

    def helper(self, A, L, M):
        n = len(A)
        left, right = [0] * (n + 1), [0] * (n + 1)
        curr = 0
        for i in xrange(n):
            curr += A[i]
            if i >= L:
                curr -= A[i-L]
            left[i+1] = max(left[i], curr)
        curr = 0
        for i in xrange(n - 1, -1, -1):
            curr += A[i]
            if i <= n - M - 1:
                curr -= A[i+M]
            right[i] = max(right[i+1], curr)
        return max(max(left[i+1] + right[i+1], left[i] + right[i]) for i in xrange(n)) 
