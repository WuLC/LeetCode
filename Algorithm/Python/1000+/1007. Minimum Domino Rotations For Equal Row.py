# -*- coding: utf-8 -*-
# Created on Fri Mar 15 2019 17:5:55
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# simple solution


# two traversal
class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        c1, c2 = self.minSwap(A[0], A, B), self.minSwap(B[0], A, B)
        if c1 == -1:
            return c2
        elif c2 == -1:
            return c1
        else:
            return min(c1, c2)


    def minSwap(self, target, A, B):
        num_A, num_B = 0, 0
        for i in xrange(len(A)):
            if A[i] != target and B[i] != target:
                return -1
            if A[i] != target:
                num_A += 1
            if B[i] != target:
                num_B += 1
        return min(num_A, num_B)


# one traversal
class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        c1, c2 = 0, 0
        t1, t2 = A[0], B[0]
        t1_A, t1_B = 0, 0
        t2_A, t2_B = 0, 0
        for i in xrange(len(A)):
            if c1 != -1:
                if A[i] != t1 and B[i] != t1:
                    c1 = -1
                if A[i] != t1:
                    t1_A += 1
                if B[i] != t1:
                    t1_B += 1
            if c2 != -1:
                if A[i] != t2 and B[i] != t2:
                    c2 = -1
                if A[i] != t1:
                    t2_A += 1
                if B[i] != t1:
                    t2_B += 1
            if c1 == -1 and c2 == -1:
                return -1
        if c1 == -1:
            return min(t2_A, t2_B)
        elif c2 == -1:
            return min(t1_A, t1_B)
        else:
            return min([t1_A, t1_B, t2_A, t2_B])
