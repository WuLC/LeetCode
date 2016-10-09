# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-14 12:56:12
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-14 12:56:23
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        if m > 0:
            n = len(matrix[0])
        else:
            return 
        
        rows, cols = set(), set()
        for i in xrange(m):
            for j in xrange(n):
               if matrix[i][j] == 0:
                   rows.add(i)
                   cols.add(j)
                   
        for i in rows:
            for j in xrange(n):
                matrix[i][j] = 0
                
        for j in cols:
            for i in xrange(m):
                matrix[i][j] = 0
        
        