# -*- coding: utf-8 -*-
# Created on Tue Dec 18 2018 21:10:57
# Author: WuLC
# EMail: liangchaowu5@gmail.com


# greedy, O(mn)
# reference: https://leetcode.com/problems/delete-columns-to-make-sorted-ii/discuss/203182/JavaC++Python-Greedy-Solution-O(MN)
class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        m, n = len(A), len(A[0])
        sorted = [False] * (m - 1)
        count = 0
        for i in xrange(n):
            legal = True
            for j in xrange(m-1):
                if not sorted[j] and A[j][i] > A[j+1][i]:
                    count += 1
                    legal = False
                    break
            if legal:
                for j in xrange(m-1):
                    if A[j][i] < A[j+1][i]:
                        sorted[j] = True
        return count