# -*- coding: utf-8 -*-
# Created on Wed Dec 26 2018 19:20:36
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# stack, O(n) time
# why left stack use >= when comparing while right stack do not, think about the case: [71,55,82,55]
# if both use >=, [55,82,55] will be duplicate, if both use >, [55,82,55] won't be considered
class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        s, left = [], []
        for i in xrange(n):
            while s and A[s[-1]] >= A[i]:
                s.pop()
            left.append(i - s[-1] if s else i + 1)
            s.append(i)
        
        s, right = [], []
        for i in xrange(n - 1, -1, -1):
            while s and A[s[-1]] > A[i]:
                s.pop()
            right.append(s[-1] - i if s else n - i)
            s.append(i)
        return sum(A[i] * left[i] * right[n-i-1] for i in xrange(n)) % (10**9 + 7) 