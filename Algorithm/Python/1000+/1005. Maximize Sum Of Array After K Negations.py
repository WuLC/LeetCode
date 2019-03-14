# -*- coding: utf-8 -*-
# Created on Mon Mar 11 2019 22:17:22
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# greedy, O(nlogn) time, O(1) space
# sort and turn negative numbers to positive numbers as many as possible

class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        idx = -1
        for i in xrange(len(A)):
            if A[i] >= 0:
                idx = i
                break
        result = 0
        if idx < 0 or idx >= K:
            for num in A:
                if K > 0:
                    num *= -1
                    K -= 1
                result += num
        else:
            left = (K - idx)&1
            for i in xrange(len(A)):
                if i == idx and left > 0:
                    if i > 0 and A[i-1]*-1 < A[i]:
                        result += 2*A[i-1]
                    else:
                        result += -2*A[i]
                    left -= 1
                result += -1*A[i] if A[i]<0 else A[i]
        return result

