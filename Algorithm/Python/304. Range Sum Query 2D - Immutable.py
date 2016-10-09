# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-16 10:25:33
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-16 14:21:51
# @Email: liangchaowu5@gmail.com

# method 1,O(mn) time complexity to initialize, O(n) time complexity for each query, O(1) space complexity
class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if len(matrix) == 0: return
        m, n = len(matrix), len(matrix[0])
        for i in xrange(m):
            for j in xrange(1, n):
                matrix[i][j] += matrix[i][j-1]
        self.matrix = matrix
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        result = 0
        for i in xrange(row1, row2+1):
            result += self.matrix[i][col2] - self.matrix[i][col1-1] if col1 != 0 else self.matrix[i][col2]
        return result


# method 2,O(mn) time complexity to initialize, O(1) for each query, O(mn) space
class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if len(matrix) == 0: return
        m, n = len(matrix), len(matrix[0])
        for i in xrange(m):
            for j in xrange(1, n):
                matrix[i][j] += matrix[i][j-1]
        for j in xrange(n):
            for i in xrange(1, m):
                matrix[i][j] += matrix[i-1][j]
        self.matrix = matrix
                
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1==0 and col1==0:
            return self.matrix[row2][col2]
        elif row1 == 0:
            return self.matrix[row2][col2] - self.matrix[row2][col1-1]
        elif col1 == 0:
            return self.matrix[row2][col2] - self.matrix[row1-1][col2]
        else:
            return self.matrix[row2][col2] - self.matrix[row1-1][col2] - self.matrix[row2][col1-1]+self.matrix[row1-1][col1-1]
            