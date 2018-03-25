# -*- coding: utf-8 -*-
# Created on Wed Mar 21 2018 14:47:25
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# dp with two arrays
# dp1[i] represents the minimum swaps of A[:i] and B[:i] with swaping at i
# dp2[i] represents the minimum swaps of A[:i] and B[:i] without swaping at i 

class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n = len(A)
        dp1 = [n for _ in xrange(n)] # not swap 
        dp2 = [n for _ in xrange(n)] # swao 
        for i in xrange(n):
            if i == 0:
                dp1[i] = 0
                dp2[i] = 1
                continue
            if A[i] > A[i-1] and B[i] > B[i-1]:
                dp1[i] = min(dp1[i], dp1[i-1])
                dp2[i] = min(dp2[i], dp2[i-1]+1)
            if A[i] > B[i-1] and B[i] > A[i-1]:
                dp1[i] = min(dp1[i], dp2[i-1])
                dp2[i] = min(dp2[i], dp1[i-1]+1)
        return min(dp1[n-1], dp2[n-1])