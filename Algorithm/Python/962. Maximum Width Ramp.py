# -*- coding: utf-8 -*-
# Created on Mon Dec 24 2018 14:5:43
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# stack, O(n) time
# reference: https://leetcode.com/problems/maximum-width-ramp/discuss/208348/JavaC++Python-O(N)-Using-Stack
class Solution(object):
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        stack = [0]
        for i in xrange(1, len(A)):
            if A[i] < A[stack[-1]]:
                stack.append(i)
        result = 0
        for i in xrange(len(A) - 1, -1, -1):
            while stack and A[i] >= A[stack[-1]]:
                result = max(result, i - stack.pop())
            if len(stack) == 0:
                break
        return result        