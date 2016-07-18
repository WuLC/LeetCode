# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-11 20:37:19
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-18 08:42:24
# @Email: liangchaowu5@gmail.com

# method 1, find maximal square in histogram level by level, O(mn)
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0]) if m>0 else 0
        result = 0
        height = [0 for i in xrange(n)]
        for i in xrange(m):
            stack = []
            for j in xrange(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
                while len(stack)>0 and height[j] < height[stack[-1]]:
                    heigh = height[stack.pop()]
                    width = j if len(stack) == 0 else j-stack[-1]-1
                    result = max(result, pow(min(width,heigh),2))
                stack.append(j)
            while len(stack) > 0:
                heigh = height[stack.pop()]
                width = n if len(stack) == 0 else n-stack[-1]-1
                result = max(result, pow(min(width,heigh),2))
        return result


# method 2, DP
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        dp = [[int(matrix[i][j]) for j in xrange(n)] for i in xrange(m)]
        max_len = 0
        for i in xrange(m):
            for j in xrange(n):
                if i==0 or j==0:
                    max_len = max(max_len, dp[i][j])
                elif matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_len = max(max_len, dp[i][j])
        return pow(max_len, 2)