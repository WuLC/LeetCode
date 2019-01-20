# -*- coding: utf-8 -*-
# Created on Sun Jan 20 2019 10:48:33
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# O(n) time, O(n) space
class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        idx = len(A)
        for i in xrange(len(A)):
            if A[i] >= 0:
                idx = i
                break
        result = []
        left, right = idx - 1, idx
        while left >= 0 and right < len(A):
            if abs(A[left]) > abs(A[right]):
                result.append(A[right]**2)
                right += 1
            else:
                result.append(A[left]**2)
                left -= 1
        while left >= 0:
            result.append(A[left]**2)
            left -= 1
        while right < len(A):
            result.append(A[right]**2)
            right += 1
        return result