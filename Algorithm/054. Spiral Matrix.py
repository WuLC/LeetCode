# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-05-05 10:27:01
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-05 10:33:57
# @Email: liangchaowu5@gmail.com

# 递归，每次解决最外一圈
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        result = []
        if m ==0:
            return result
            
        n = len(matrix[0])
        self.helper(matrix,0,m-1,0,n-1,result)
        return result
        
    def helper(self,matrix,r1,r2,c1,c2,result):
        if r1>r2 or c1>c2:
            return
        for i in xrange(c1,c2+1):
            result.append(matrix[r1][i])
        for i in xrange(r1+1,r2+1):
            result.append(matrix[i][c2])
        if r2>r1:  # 需要判断，否则同一行会重复
            for i in xrange(c2-1,c1-1,-1):
                result.append(matrix[r2][i])
        if c2>c1:  # 需要判断，否则同一列会重复
            for i in xrange(r2-1,r1,-1):
                result.append(matrix[i][c1])
        
        self.helper(matrix,r1+1,r2-1,c1+1,c2-1,result)
        