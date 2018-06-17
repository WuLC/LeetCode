# -*- coding: utf-8 -*-
# Created on Sun Jun 17 2018 12:40:42
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# simple solution
class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        idx = 0
        for i in xrange(1, len(A)):
            if A[i] > A[idx]:
                idx = i
        return idx