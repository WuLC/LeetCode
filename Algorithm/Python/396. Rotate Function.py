# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-09-12 12:20:14
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-12 12:21:43
# @Email: liangchaowu5@gmail.com

# O(n^2) time, TLE
class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        result, n  = None, len(A)
        for move in xrange(n):
            tmp = 0
            for i in xrange(n):
                tmp += A[i] * ((i+move)%n)
            result = max(tmp, result) if result else tmp
        return result if result else 0

# O(n) time, O(1) space, AC
# class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        result, n  = None, len(A)
        total = sum(A)
        previous = 0
        for i in xrange(n):
            previous += i*A[i]
        result = previous
        for move in xrange(1,n):
            previous = previous - total + n*A[move-1]
            result = max(previous, result)
        return result