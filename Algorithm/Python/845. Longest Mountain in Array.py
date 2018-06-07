# -*- coding: utf-8 -*-
# Created on Thu Jun 07 2018 20:49:29
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# two pointers
class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        result = 0
        p1 = 0
        while p1 < len(A)-1:
            if A[p1] < A[p1+1]:
                p2 = p1 + 1
                down = False
                while p2 + 1 < len(A) and A[p2] < A[p2+1]:
                    p2 += 1
                while p2 + 1 < len(A) and A[p2] > A[p2+1]:
                    down = True
                    p2 += 1
                if down:
                    result = max(result, p2 - p1 + 1)
                p1 = p2
            else:
                p1 += 1
        return result