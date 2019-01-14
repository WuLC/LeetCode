# -*- coding: utf-8 -*-
# Created on Mon Jan 14 2019 19:25:29
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# O(n) time
# a triangle with edges a, b, c is legal only when 
# a+b > c
# a+c > b
# b+c > a
class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        result = 0
        A.sort()
        for i in xrange(len(A) - 1, 1, -1):
            if A[i] < A[i-1] + A[i-2]:
                result = A[i] + A[i-1] + A[i-2]
                break
        return result