# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-09 14:24:46
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-09 14:29:05
# @Email: liangchaowu5@gmail.com

# find the in intersect part of two rectangle

# method 1
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        length = self.intersect((A,C), (E, G))
        width = self.intersect((B,D), (F,H))
        return (C-A)*(D-B) + (G-E)*(H-F) - length*width
    
    def intersect(self, a, b):
        if a[0]>=b[1] or b[0] >= a[1]:
            return 0
        if a[0] > b[0]:
            if a[1] > b[1]:
                return b[1] - a[0]
            else:
                return a[1] - a[0]
        else:
            if b[1] > a[1]:
                return a[1] - b[0]
            else:
                return b[1] - b[0]


# similar solution ,but more concise code
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        overlap = max((min(C,G) - max(A,E)), 0) * max(min(D,H) - max(B,F), 0)
        return (C-A)*(D-B) + (G-E)*(H-F) -overlap 