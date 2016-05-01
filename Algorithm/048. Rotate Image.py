# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-04-27 10:19:13
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-01 08:56:01
# @Email: liangchaowu5@gmail.com

# method 1,space complexity O(n)
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
        
# method 2，space complexity O(1)
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in xrange(n/2):
            matrix[i], matrix[n-1-i] = matrix[n-1-i], matrix[i]

        for i in xrange(n):
            for j in xrange(i+1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

"""
clockwise rotate
first reverse up to down, then swap the symmetry 
1 2 3     7 8 9     7 4 1
4 5 6  => 4 5 6  => 8 5 2
7 8 9     1 2 3     9 6 3

anticlockwise rotate
first reverse left to right, then swap the symmetry
1 2 3     3 2 1     3 6 9
4 5 6  => 6 5 4  => 2 5 8
7 8 9     9 8 7     1 4 7
"""
