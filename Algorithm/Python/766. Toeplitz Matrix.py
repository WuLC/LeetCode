# -*- coding: utf-8 -*-
# Created on Tue Jan 23 2018 21:16:26
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# compare with top-left element
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])
        for i in xrange(1, m):
            for j in xrange(1, n):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True

# group by indices (row-col)
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        record = {}
        m, n = len(matrix), len(matrix[0])
        for i in xrange(m):
            for j in xrange(n):
                if i-j not in record:
                    record[i-j] = matrix[i][j]
                elif record[i-j] != matrix[i][j]:
                    return False
        return True