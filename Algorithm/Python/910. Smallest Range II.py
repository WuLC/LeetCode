# -*- coding: utf-8 -*-
# Created on Sun Sep 23 2018 11:58:12
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# O(nlogn)
# sort, then add K for the smaller part and minus K for the larger part
class Solution(object):
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        result = A[-1] - A[0]
        for i in xrange(len(A)-1):
            tmp = max(A[i]+K, A[-1]-K) - min(A[0]+K, A[i+1]-K)
            result = min(result, tmp)
        return result