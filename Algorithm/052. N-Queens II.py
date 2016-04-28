# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-04-28 23:10:30
# @Last modified by:   WuLC
# @Last Modified time: 2016-04-28 23:10:48
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        matrix  = [['.' for i in xrange(n)] for j in xrange(n)]
        result = [0]
        self.helper(matrix,0,result)
        return result[0]
    
    def helper(self,matrix,row,result):
        n = len(matrix)
        if row == n:
            result[0] += 1
            return 
        for i in xrange(n):
            if self.is_valid(matrix,row,i):
                matrix[row][i] = 'Q'
                self.helper(matrix,row+1,result)
                matrix[row][i] = '.'
        
                
    def is_valid(self,matrix,i,j):
        n = len(matrix)
    
        for k in xrange(n):
            if matrix[k][j] == 'Q':
                return False
        
        ti,tj=i,j
        # left
        while ti>=0 and tj>=0:
            if matrix[ti][tj] == 'Q':
                return False
            ti -= 1
            tj -= 1
        # right
        while 0<=i<n and 0<=j<n:
            if matrix[i][j]=='Q':
                return False
            i -= 1
            j += 1
        
        return True