# -*- coding: utf-8 -*-
# Created on Sun May 13 2018 11:28:6
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# simple solution
class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(A), len(A[0])
        odd = False
        if n&1 != 0:
            odd = True
            mid = n>>1
        for i in xrange(m):
            if odd:
                A[i][mid] ^= 1
            for j in xrange(n>>1):
                A[i][j], A[i][n-j-1] = A[i][n-j-1]^1, A[i][j]^1
        return A