# -*- coding: utf-8 -*-
# Created on Fri Nov 23 2018 20:50:28
# Author: WuLC
# EMail: liangchaowu5@gmail.com

class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        m, n = len(A), len(A[0])
        count = 0
        for i in xrange(n):
            for j in xrange(1, m):
                if A[j][i] < A[j-1][i]:
                    count += 1
                    break
        return count