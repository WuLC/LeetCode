# -*- coding: utf-8 -*-
# Created on Thu Aug 23 2018 8:56:21
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# greedy
class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m, n = len(A), len(A[0])
        # flip row
        for i in xrange(m):
            if A[i][0]==0:
                self.flip(A, i, 1)
        
        # flip col
        count = [0]*n
        for i in xrange(m):
            for j in xrange(n):
                count[j] += (1&A[i][j])
        for j in xrange(n):
            if count[j] <= (m>>1):
                self.flip(A, j, -1)
                count[j] = m-count[j]
        return sum(count[j]*(2**(n-j-1)) for j in xrange(n))
            

    def flip(self, A, index, flag):
        if flag==1: # flip row
            for j in xrange(len(A[0])):
                A[index][j] ^= 1
        elif flag==-1: # flip col
            for i in xrange(len(A)):
                A[i][index] ^= 1