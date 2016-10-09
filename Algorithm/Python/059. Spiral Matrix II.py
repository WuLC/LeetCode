# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-05 11:10:26
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-05 11:10:38
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result =[[0 for i in xrange(n)] for j in xrange(n)]
        self.helper(0,n-1,0,n-1,1,result)
        return result
        
    def helper(self,r1,r2,c1,c2,count,result):
        if r1>r2 or c1>c2:
            return 
        for i in xrange(c1,c2+1):
            result[r1][i] = count
            count += 1
        for i in xrange(r1+1,r2+1):
            result[i][c2]=count
            count+=1
        if r2>r1:
            for i in xrange(c2-1,c1-1,-1):
                result[r2][i] = count
                count+=1
        if c2>c1:
            for i in xrange(r2-1,r1,-1):
                result[i][c1] = count
                count += 1
        self.helper(r1+1,r2-1,c1+1,c2-1,count,result)
            
            
        