# -*- coding: utf-8 -*-
# Created on Mon Jul 09 2018 0:3:21
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# simple solution
class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(A), len(A[0])
        result = [[] for _ in xrange(n)]
        for i in xrange(m):
            for j in xrange(n):
                result[j].append(A[i][j])
        return result