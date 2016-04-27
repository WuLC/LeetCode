# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-04-27 10:19:13
# @Last modified by:   WuLC
# @Last Modified time: 2016-04-27 10:19:27
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        b = []
        n = len(matrix)
        for i in xrange(n):
            tmp = matrix[i][:]
            b.append(tmp)
        
        for i in xrange(n):
            for j in xrange(n):
                matrix[j][n-1-i] = b[i][j]
        
        