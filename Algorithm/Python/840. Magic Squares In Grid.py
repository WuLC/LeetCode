# -*- coding: utf-8 -*-
# Created on Mon May 28 2018 18:34:31
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# simple and ugly solution
class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        count = 0
        for i in xrange(m-2):
            for j in xrange(n-2):
                if self.is_magic(grid, i, j):
                    count += 1
        return count
    
    def is_magic(self, grid, i, j):
        tmp = set()
        row_sum = [0] * 3
        col_sum = [0] * 3
        left_diagonal, right_diagonal = 0 ,0 
        for di in xrange(3):
            for dj in xrange(3):
                if grid[i+di][j+dj]<=0 or grid[i+di][j+dj] > 9 or grid[i+di][j+dj] in tmp:
                    return False
                tmp.add(grid[i+di][j+dj])
                row_sum[di] += grid[i+di][j+dj]
                col_sum[dj] += grid[i+di][j+dj]
                if di == dj:
                    left_diagonal += grid[i+di][j+dj]
                if di+dj == 2:
                    right_diagonal += grid[i+di][j+dj]
        return all([e==15 for e in row_sum+col_sum]) and left_diagonal == 15 and right_diagonal == 15
        
                
                
                
        