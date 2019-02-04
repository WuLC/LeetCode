# -*- coding: utf-8 -*-
# Created on Mon Feb 04 2019 11:5:18
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# two pointers
class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[Interval]
        :type B: List[Interval]
        :rtype: List[Interval]
        """
        result = []
        p1, p2 = 0, 0
        while p1 < len(A) and p2 < len(B):
            if A[p1].start > B[p2].end:
                p2 += 1
            elif A[p1].end < B[p2].start:
                p1 += 1
            else:
                s, e = max(A[p1].start, B[p2].start), min(A[p1].end, B[p2].end)
                result.append(Interval(s, e))
                if A[p1].end > B[p2].end:
                    p2 += 1
                else:
                    p1 += 1
        return result



        