# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-09-10 16:54:55
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-10 21:03:20
# @Email: liangchaowu5@gmail.com

# O(mn) time, O(mn) space
import collections
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return 
        m, n = len(board), len(board[0])
        copy = collections.deque()
        for i in xrange(m):
            copy.append([0]+board[i][:]+[0])
        copy.appendleft([0]*(n+2))
        copy.append([0]*(n+2))
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                count = sum(copy[i-1][j-1:j+2])+sum(copy[i+1][j-1:j+2])+copy[i][j-1]+copy[i][j+1]
                if board[i-1][j-1] == 1:
                    board[i-1][j-1] = 1 if 2<=count<=3 else 0
                else:
                    board[i-1][j-1] = 1 if count==3 else 0
                    

# O(mn) time, O(1) space
# use the lowest bit to represent the initial state 
# the second lowest bit to represent the next state

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return 
        m, n = len(board), len(board[0])
        for i in xrange(m):
            for j in xrange(n):
                lived = 0
                for r in xrange(i-1, i+2):
                    for c in xrange(j-1, j+2):
                        if 0 <= r < m and 0 <= c < n and (i != r or j != c):
                            lived += (board[r][c] & 1)
                if (board[i][j] == 1 and 2 <= lived <= 3) or (board[i][j] == 0 and lived==3):
                        board[i][j] ^= 2
        for i in xrange(m):
            for j in xrange(n):
                board[i][j] >>= 1
                    