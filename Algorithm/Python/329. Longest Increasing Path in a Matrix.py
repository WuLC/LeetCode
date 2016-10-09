# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-09-10 15:38:47
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-10 16:27:31
# @Email: liangchaowu5@gmail.com

# pure dfs, TLE
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        result = [0]
        if len(matrix) != 0:
            m, n = len(matrix), len(matrix[0])
            visited = set()
            for i in xrange(m):
                for j in xrange(n):
                    tmp = 1
                    if (i,j) not in visited:
                        self.dfs(matrix, i, j, m, n, visited, tmp, result)
        return result[0]
    
    def dfs(self, matrix, row, col, m, n, visited, tmp, result):
        visited.add((row, col))
        if row-1 >= 0 and matrix[row-1][col] > matrix[row][col]:
            self.dfs(matrix, row - 1, col, m, n, visited, tmp+1, result)
        if row+1 < m and matrix[row+1][col] > matrix[row][col]:
            self.dfs(matrix, row + 1, col, m, n, visited, tmp+1, result)
        if col-1 >= 0 and matrix[row][col-1] > matrix[row][col]:
            self.dfs(matrix, row, col-1, m, n, visited, tmp+1, result)
        if col+1 < n and matrix[row][col+1] > matrix[row][col]:
            self.dfs(matrix, row, col+1, m, n, visited, tmp+1, result)
        result[0] = max(result[0], tmp)



# dfs with dp
# dp[i][j] means the longest path that can get when starting from (i,j)
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        max_len = 0
        if len(matrix) != 0:
            m, n = len(matrix), len(matrix[0])
            dp = [[0 for j in xrange(n)] for i in xrange(m)]
            visited = set()
            for i in xrange(m):
                for j in xrange(n):
                    max_len = max(max_len, self.dfs(matrix, i, j, m, n, dp))  
        return max_len
    
    def dfs(self, matrix, row, col, m, n, dp):
        if dp[row][col] != 0:
            return dp[row][col]
        up, down, left, right = 0, 0, 0, 0
        if row-1 >= 0 and matrix[row-1][col] > matrix[row][col]:
            up = self.dfs(matrix, row - 1, col, m, n, dp)
        if row+1 < m and matrix[row+1][col] > matrix[row][col]:
            down = self.dfs(matrix, row + 1, col, m, n, dp)
        if col-1 >= 0 and matrix[row][col-1] > matrix[row][col]:
            left = self.dfs(matrix, row, col-1, m, n, dp)
        if col+1 < n and matrix[row][col+1] > matrix[row][col]:
            right = self.dfs(matrix, row, col+1, m, n, dp)
        dp[row][col] = max(left, right, up, down) + 1
        return dp[row][col]
        